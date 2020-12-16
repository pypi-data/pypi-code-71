"""Declares low-level functions and classes for request handling."""
import functools
import inspect
import logging
import re
from collections import OrderedDict
from inspect import Parameter

from ioc.exc import UnsatisfiedDependency
from fastapi import APIRouter
from fastapi import HTTPException
from fastapi import Request
from fastapi import Path
from fastapi.responses import JSONResponse
from unimatrix.ext.model.exc import CanonicalException
from unimatrix.ext.model.exc import FeatureNotSupported

from frf import exceptions


class ResourceMetaclass(type):
    """Constructs a :class:`APIView` class."""

    def __new__(cls, name, bases, attrs):
        super_new = super().__new__
        if name in ('APIView', 'Resource'):
            return super_new(cls, name, bases, attrs)
        attrs['router'] = APIRouter()
        return super_new(cls, name, bases, attrs)


class Resource(metaclass=ResourceMetaclass):
    """The base class for all API views (request handlers)."""

    #: The default logger for endpoints
    logger = logging.getLogger('endpoints')

    #: The human-readable resource name.
    resource_name = None

    #: The list of allowed HTTP methods.
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head',
        'options', 'trace']

    @classmethod
    def get_resource_name(cls):
        """Return the name that will be used in constructing the
        URL paths for this :class:`Resource`.
        """
        # Some naieve pluralizing
        name = str.lower(cls.__name__)
        if not str.endswith(name, 's'):
            name = name + 's'
        return re.sub('(Resource|View|ViewSet)$', '', name)

    @classmethod
    def as_method_handler(cls, app, path, method, handler, **initkwargs):
        """Main entry point for a request-response process for the given request
        method.
        """
        method = str.lower(method)
        if not hasattr(app, method) or not hasattr(cls, handler):
            raise ValueError(f"Unsupported request method: {method}")
        for key in initkwargs:
            if key in cls.http_method_names:
                raise TypeError(
                    'The method name %s is not accepted as a keyword argument '
                    'to %s().' % (key, cls.__name__)
                )
            if not hasattr(cls, key):
                raise TypeError("%s() received an invalid keyword %r. as_view "
                                "only accepts arguments that are already "
                                "attributes of the class." % (cls.__name__, key))


        # Instantiate the view class so we can use the signature of the
        # request handler, which is used by FastAPI to generated the API
        # interface.
        view = cls(**initkwargs)
        register_endpoint = getattr(cls.router, method)
        f = getattr(view, handler)
        response_model = getattr(f, 'response_model', None)

        # Do some black magic here to trick FastAPI to inject the request
        # and response.
        signature = inspect.signature(f)
        call_args = OrderedDict()

        # Add the Request object as the first argument if it is not provided.
        inject_request = 'request' in signature.parameters
        inject_id = handler in ['retrieve', 'update', 'delete', 'replace']
        call_args['request'] = inspect.Parameter(
            'request',
            Parameter.POSITIONAL_OR_KEYWORD,
            annotation=Request
        )
        if inject_id:
            p = signature.parameters.get('resource_id')
            call_args['resource_id'] = inspect.Parameter(
                'resource_id',
                Parameter.POSITIONAL_OR_KEYWORD,
                default=Path(...,
                    title="Identifies the {cls.get_resource_name()} object."
                ),
                annotation=p.annotation\
                    if (p and p.annotation != inspect._empty) else str
            )

        # Update the call_args dictionary with the remaining parameters
        # and create a new call signature.
        call_args.update({x: y for x, y in list(signature.parameters.items())
            if x not in call_args})
        signature = signature.replace(
            parameters=list(call_args.values()))

        @register_endpoint(path, response_model=response_model)
        @functools.wraps(f)
        async def request_handler(request: Request, **kwargs):
            view = cls(**initkwargs)
            view.cls = cls
            view.initkwargs = initkwargs
            view.funckwargs = dict(kwargs)
            if inject_request:
                view.funckwargs['request'] = request
            return await view.dispatch(f, request, **kwargs)

        request_handler.__signature__ = signature
        request_handler.__annotations__ = call_args

        return request_handler

    async def dispatch(self, handler, request, *args, **kwargs):
        """`.dispatch()` is pretty much the same as Django's regular dispatch,
        but with extra hooks for startup, finalize, and exception handling.
        """
        self.args = args
        self.kwargs = kwargs
        request = await self.initialize_request(request, *args, **kwargs)
        self.request = request
        try:
            await self.initial(request, *args, **kwargs)
            response = await handler(**dict(self.funckwargs))
        except Exception as exc:
            response = await self.handle_exception(exc)

        self.response = await self.finalize_response(request, response)
        return response

    async def finalize_response(self, request, response):
        """Returns the final response object."""
        return response

    async def initial(self, request, *args, **kwargs):
        """Runs anything that needs to occur prior to calling the method
        handler.
        """
        pass

    async def handle_exception(self, exc):
        """Handle any exception that occurs, by returning an appropriate
        response, or re-raising the error.
        """
        if isinstance(exc, HTTPException):
            raise exc

        if isinstance(exc, CanonicalException):
            if exc.http_status_code >= 500:
                exc.log(self.logger.exception)
            return JSONResponse(
                status_code=exc.http_status_code,
                content=exc.as_dict()
            )

        if isinstance(exc, UnsatisfiedDependency):
            return await self.handle_exception(FeatureNotSupported())

        self.raise_uncaught_exception(exc)

    async def http_method_not_allowed(self, request, *args, **kwargs):
        """If `request.method` does not correspond to a handler method,
        determine what kind of exception to raise.
        """
        raise exceptions.MethodNotAllowed(request.method)

    async def initialize_request(self, request, *args, **kwargs):
        """Returns the initial request object."""
        return request

    def raise_uncaught_exception(self, exc):
        """Raise an exception that is not caught by a handler."""
        raise exc


class APIView(Resource):
    pass
