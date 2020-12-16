#-------------------------------------------------------------------------------
#
# Project: EOxServer <http://eoxserver.org>
# Authors: Fabian Schindler <fabian.schindler@eox.at>
#
#-------------------------------------------------------------------------------
# Copyright (C) 2013 EOX IT Services GmbH
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies of this Software or works derived from this Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#-------------------------------------------------------------------------------


class OWS20ExceptionHandler(object):
    """ A Fallback exception handler. This class does on purpose not implement
        the ExceptionHandlerInterface and must be instantiated manually.
    """

    def handle_exception(self, request, exception):
        message = str(exception)
        version = "2.0.0"
        # NOTE: An existing 'code' attribute can be set to None value!!!
        code = getattr(exception, "code", None) or "NoApplicableCode"
        locator = getattr(exception, "locator", None)
        status_code = 400

        from eoxserver.services.ows.common.v20.encoders import (
            OWS20ExceptionXMLEncoder
        )
        encoder = OWS20ExceptionXMLEncoder()

        return (
            encoder.serialize(
                encoder.encode_exception(message, version, code, locator)
            ),
            encoder.content_type,
            status_code
        )
