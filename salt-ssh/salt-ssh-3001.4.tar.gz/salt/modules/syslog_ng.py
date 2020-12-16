# -*- coding: utf-8 -*-
"""
Module for getting information about syslog-ng

:maintainer:    Tibor Benke <btibi@sch.bme.hu>
:maturity:      new
:depends:       cmd
:platform:      all

This module is capable of managing syslog-ng instances which were installed
via a package manager or from source. Users can use a directory as a parameter
in the case of most functions, which contains the syslog-ng and syslog-ng-ctl
binaries.

Syslog-ng can be installed via a package manager or from source. In the
latter case, the syslog-ng and syslog-ng-ctl binaries are not available
from the PATH, so users should set location of the sbin directory with
:mod:`syslog_ng.set_binary_path <salt.modules.syslog_ng.set_binary_path>`.

Similarly, users can specify the location of the configuration file with
:mod:`syslog_ng.set_config_file <salt.modules.syslog_ng.set_config_file>`, then
the module will use it. If it is not set, syslog-ng uses the default
configuration file.


"""

# Import Python libs
from __future__ import (
    absolute_import,
    generators,
    print_function,
    unicode_literals,
    with_statement,
)

import logging
import os
import os.path
import time

import salt

# Import Salt libs
import salt.utils.files
import salt.utils.path
from salt.exceptions import CommandExecutionError

# Import 3rd-party libs
from salt.ext import six
from salt.ext.six.moves import range

__SYSLOG_NG_BINARY_PATH = None
__SYSLOG_NG_CONFIG_FILE = "/etc/syslog-ng.conf"
__SALT_GENERATED_CONFIG_HEADER = """#Generated by Salt on {0}"""


class SyslogNgError(Exception):
    pass


log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

# Don't shadow built-in's.
__func_alias__ = {"reload_": "reload"}

_INDENT = ""
_INDENT_STEP = "    "

# These are needed during building of the configuration tree
_current_statement = None
_current_option = None
_current_parameter = None
_current_parameter_value = None


def _increase_indent():
    """
    Increases the indentation level.
    """
    global _INDENT
    _INDENT += _INDENT_STEP


def _decrease_indent():
    """
    Decreases the indentation level.
    """
    global _INDENT
    _INDENT = _INDENT[4:]


def _indent(value):
    """
    Returns the indented parameter.
    """
    return "{0}{1}".format(_INDENT, value)


def _indentln(string):
    """
    Return the indented parameter with newline.
    """
    return _indent(string + "\n")


class Buildable(object):
    """
    Base class of most classes, which have a build method.

    It contains a common build function.

    Does not need examples.
    """

    def __init__(self, iterable, join_body_on="", append_extra_newline=True):
        self.iterable = iterable
        self.join_body_on = join_body_on
        self.append_extra_newline = append_extra_newline

    def build_header(self):
        """
        Builds the header of a syslog-ng configuration object.
        """
        return ""

    def build_tail(self):
        """
        Builds the tail of a syslog-ng configuration object.
        """
        return ""

    def build_body(self):
        """
        Builds the body of a syslog-ng configuration object.
        """
        _increase_indent()
        body_array = [x.build() for x in self.iterable]

        nl = "\n" if self.append_extra_newline else ""

        if len(self.iterable) >= 1:
            body = self.join_body_on.join(body_array) + nl
        else:
            body = ""

        _decrease_indent()
        return body

    def build(self):
        """
        Builds the textual representation of the whole configuration object
        with its children.
        """
        header = self.build_header()
        body = self.build_body()
        tail = self.build_tail()
        return header + body + tail


class Statement(Buildable):
    """
    It represents a syslog-ng configuration statement, e.g. source, destination,
    filter.

    Does not need examples.
    """

    def __init__(self, type, id="", options=None, has_name=True):
        super(Statement, self).__init__(
            options, join_body_on="", append_extra_newline=False
        )
        self.type = type
        self.id = id
        self.options = options if options else []
        self.iterable = self.options
        self.has_name = has_name

    def build_header(self):
        if self.has_name:
            return _indentln("{0} {1} {{".format(self.type, self.id))
        else:
            return _indentln("{0} {{".format(self.type))

    def build_tail(self):
        return _indentln("};")

    def add_child(self, option):
        self.options.append(option)


class NamedStatement(Statement):
    """
    It represents a configuration statement, which has a name, e.g. a source.

    Does not need examples.
    """

    def __init__(self, type, id="", options=None):
        super(NamedStatement, self).__init__(type, id, options, has_name=True)


class UnnamedStatement(Statement):
    """
    It represents a configuration statement, which doesn't have a name, e.g. a
    log path.

    Does not need examples.
    """

    def __init__(self, type, options=None):
        super(UnnamedStatement, self).__init__(
            type, id="", options=options, has_name=False
        )


class GivenStatement(Buildable):
    """
    This statement returns a string without modification. It can be used to
     use existing configuration snippets.

    Does not need examples.
    """

    def __init__(self, value, add_newline=True):
        super(GivenStatement, self).__init__(iterable=None)
        self.value = value
        self.add_newline = add_newline

    def build(self):
        if self.add_newline:
            return self.value + "\n"
        else:
            return self.value


class Option(Buildable):
    """
    A Statement class contains Option instances.

    An instance of Option can represent a file(), tcp(), udp(), etc.  option.

    Does not need examples.
    """

    def __init__(self, type="", params=None):
        super(Option, self).__init__(params, ",\n")
        self.type = type
        self.params = params if params else []
        self.iterable = self.params

    def build(self):
        header = _indentln("{0}(".format(self.type))
        tail = _indentln(");")
        body = self.build_body()

        return header + body + tail

    def add_parameter(self, param):
        self.params.append(param)


class Parameter(Buildable):
    """
    An Option has one or more Parameter instances.

    Does not need examples.
    """

    def __init__(self, iterable=None, join_body_on=""):
        super(Parameter, self).__init__(iterable, join_body_on)


class SimpleParameter(Parameter):
    """
    A Parameter is a SimpleParameter, if it's just a simple type, like a
    string.

    For example:

    .. code-block:: text

        destination d_file {
            file(
                '/var/log/messages'
            );
        };

    ``/var/log/messages`` is a SimpleParameter.

    Does not need examples.
    """

    def __init__(self, value=""):
        super(SimpleParameter, self).__init__()
        self.value = value

    def build(self):
        return _indent(self.value)


class TypedParameter(Parameter):
    """
    A Parameter, which has a type:

    .. code-block:: text

        destination d_tcp {
            tcp(
                ip(127.0.0.1)
            );
        };

    ``ip(127.0.0.1)`` is a TypedParameter.

    Does not need examples.
    """

    def __init__(self, type="", values=None):
        super(TypedParameter, self).__init__(values, ",\n")
        self.type = type
        self.values = values if values else []
        self.iterable = self.values

    def build(self):
        header = _indentln("{0}(".format(self.type))
        tail = _indent(")")
        body = self.build_body()

        return header + body + tail

    def add_value(self, value):
        self.values.append(value)


class ParameterValue(Buildable):
    """
    A TypedParameter can have one or more values.

    Does not need examples.
    """

    def __init__(self, iterable=None, join_body_on=""):
        super(ParameterValue, self).__init__(iterable, join_body_on)


class SimpleParameterValue(ParameterValue):
    """
    A ParameterValuem which holds a simple type, like a string or a number.

    For example in ip(127.0.0.1) 127.0.0.1 is a SimpleParameterValue.

    Does not need examples.
    """

    def __init__(self, value=""):
        super(SimpleParameterValue, self).__init__()
        self.value = value

    def build(self):
        return _indent(self.value)


class TypedParameterValue(ParameterValue):
    """
    We have to go deeper...

    A TypedParameter can have a 'parameter', which also have a type. For example
    key_file and cert_file:

    .. code-block:: text

        source demo_tls_source {
            tcp(
                ip(0.0.0.0)
                port(1999)
                tls(
                    key_file('/opt/syslog-ng/etc/syslog-ng/key.d/syslog-ng.key')
                    cert_file('/opt/syslog-ng/etc/syslog-ng/cert.d/syslog-ng.cert')
                )
            );
        };

    Does not need examples.
    """

    def __init__(self, type="", arguments=None):
        super(TypedParameterValue, self).__init__(arguments, "\n")
        self.type = type
        self.arguments = arguments if arguments else []
        self.iterable = self.arguments

    def build(self):
        header = _indentln("{0}(".format(self.type))
        tail = _indent(")")
        body = self.build_body()

        return header + body + tail

    def add_argument(self, arg):
        self.arguments.append(arg)


class Argument(object):
    """
    A TypedParameterValue has one or more Arguments. For example this can be
    the value of key_file.

    Does not need examples.
    """

    def __init__(self, value=""):
        self.value = value

    def build(self):
        return _indent(self.value)


def _is_statement_unnamed(statement):
    """
    Returns True, if the given statement is an unnamed statement, like log or
    junction.

    """
    return statement in ("log", "channel", "junction", "options")


def _is_simple_type(value):
    """
    Returns True, if the given parameter value is an instance of either
    int, str, float or bool.
    """
    return (
        isinstance(value, six.string_types)
        or isinstance(value, int)
        or isinstance(value, float)
        or isinstance(value, bool)
    )


def _get_type_id_options(name, configuration):
    """
    Returns the type, id and option of a configuration object.
    """
    # it's in a form of source.name
    if "." in name:
        type_, sep, id_ = name.partition(".")
        options = configuration
    else:
        type_ = next(six.iterkeys(configuration))
        id_ = name
        options = configuration[type_]

    return type_, id_, options


def _expand_one_key_dictionary(_dict):
    """
    Returns the only one key and its value from a dictionary.
    """
    key = next(six.iterkeys(_dict))
    value = _dict[key]
    return key, value


def _parse_typed_parameter_typed_value(values):
    """
    Creates Arguments in a TypedParametervalue.
    """
    type_, value = _expand_one_key_dictionary(values)

    _current_parameter_value.type = type_
    if _is_simple_type(value):
        arg = Argument(value)
        _current_parameter_value.add_argument(arg)
    elif isinstance(value, list):
        for idx in value:
            arg = Argument(idx)
            _current_parameter_value.add_argument(arg)


def _parse_typed_parameter(param):
    """
    Parses a TypedParameter and fills it with values.
    """
    global _current_parameter_value
    type_, value = _expand_one_key_dictionary(param)
    _current_parameter.type = type_

    if _is_simple_type(value) and value != "":
        _current_parameter_value = SimpleParameterValue(value)
        _current_parameter.add_value(_current_parameter_value)
    elif isinstance(value, list):
        for i in value:
            if _is_simple_type(i):
                _current_parameter_value = SimpleParameterValue(i)
                _current_parameter.add_value(_current_parameter_value)
            elif isinstance(i, dict):
                _current_parameter_value = TypedParameterValue()
                _parse_typed_parameter_typed_value(i)
                _current_parameter.add_value(_current_parameter_value)


def _create_and_add_parameters(params):
    """
    Parses the configuration and creates Parameter instances.
    """
    global _current_parameter
    if _is_simple_type(params):
        _current_parameter = SimpleParameter(params)
        _current_option.add_parameter(_current_parameter)
    else:
        # must be a list
        for i in params:
            if _is_simple_type(i):
                _current_parameter = SimpleParameter(i)
            else:
                _current_parameter = TypedParameter()
                _parse_typed_parameter(i)
            _current_option.add_parameter(_current_parameter)


def _create_and_add_option(option):
    """
    Parses the configuration and creates an Option instance.
    """
    global _current_option

    _current_option = Option()
    type_, params = _expand_one_key_dictionary(option)
    _current_option.type = type_
    _create_and_add_parameters(params)
    _current_statement.add_child(_current_option)


def _parse_statement(options):
    """
    Parses the configuration and creates options the statement.
    """
    for option in options:
        _create_and_add_option(option)


def _is_reference(arg):
    """
    Return True, if arg is a reference to a previously defined statement.
    """
    return (
        isinstance(arg, dict)
        and len(arg) == 1
        and isinstance(next(six.itervalues(arg)), six.string_types)
    )


def _is_junction(arg):
    """
    Return True, if arg is a junction statement.
    """
    return (
        isinstance(arg, dict)
        and len(arg) == 1
        and next(six.iterkeys(arg)) == "junction"
    )


def _add_reference(reference, statement):
    """
    Adds a reference to statement.
    """
    type_, value = _expand_one_key_dictionary(reference)
    opt = Option(type_)
    param = SimpleParameter(value)
    opt.add_parameter(param)
    statement.add_child(opt)


def _is_inline_definition(arg):
    """
    Returns True, if arg is an inline definition of a statement.
    """
    return (
        isinstance(arg, dict)
        and len(arg) == 1
        and isinstance(next(six.itervalues(arg)), list)
    )


def _add_inline_definition(item, statement):
    """
    Adds an inline definition to statement.
    """
    global _current_statement
    backup = _current_statement

    type_, options = _expand_one_key_dictionary(item)
    _current_statement = UnnamedStatement(type=type_)
    _parse_statement(options)
    statement.add_child(_current_statement)

    _current_statement = backup


def _add_junction(item):
    """
    Adds a junction to the _current_statement.
    """
    type_, channels = _expand_one_key_dictionary(item)
    junction = UnnamedStatement(type="junction")
    for item in channels:
        type_, value = _expand_one_key_dictionary(item)
        channel = UnnamedStatement(type="channel")
        for val in value:
            if _is_reference(val):
                _add_reference(val, channel)
            elif _is_inline_definition(val):
                _add_inline_definition(val, channel)
        junction.add_child(channel)
    _current_statement.add_child(junction)


def _parse_log_statement(options):
    """
    Parses a log path.
    """
    for i in options:
        if _is_reference(i):
            _add_reference(i, _current_statement)
        elif _is_junction(i):
            _add_junction(i)
        elif _is_inline_definition(i):
            _add_inline_definition(i, _current_statement)


def _build_config_tree(name, configuration):
    """
    Build the configuration tree.

    The root object is _current_statement.
    """
    type_, id_, options = _get_type_id_options(name, configuration)
    global _INDENT, _current_statement
    _INDENT = ""
    if type_ == "config":
        _current_statement = GivenStatement(options)
    elif type_ == "log":
        _current_statement = UnnamedStatement(type="log")
        _parse_log_statement(options)
    else:
        if _is_statement_unnamed(type_):
            _current_statement = UnnamedStatement(type=type_)
        else:
            _current_statement = NamedStatement(type=type_, id=id_)
        _parse_statement(options)


def _render_configuration():
    """
    Renders the configuration tree into syslog-ng's configuration syntax.
    """
    text_repr = _current_statement.build()
    _INDENT = ""
    return text_repr


def config(name, config, write=True):
    """
    Builds syslog-ng configuration. This function is intended to be used from
    the state module, users should not use it directly!

    name : the id of the Salt document or it is the format of <statement name>.id
    config : the parsed YAML code
    write : if True, it writes  the config into the configuration file,
    otherwise just returns it

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.config name='s_local' config="[{'tcp':[{'ip':'127.0.0.1'},{'port':1233}]}]"

    """

    _build_config_tree(name, config)
    configs = _render_configuration()

    if __opts__.get("test", False):
        comment = "State syslog_ng will write '{0}' into {1}".format(
            configs, __SYSLOG_NG_CONFIG_FILE
        )
        return _format_state_result(name, result=None, comment=comment)

    succ = write
    if write:
        succ = _write_config(config=configs)

    return _format_state_result(name, result=succ, changes={"new": configs, "old": ""})


def set_binary_path(name):
    """
    Sets the path, where the syslog-ng binary can be found. This function is
    intended to be used from states.

    If syslog-ng is installed via a package manager, users don't need to use
    this function.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.set_binary_path name=/usr/sbin

    """
    global __SYSLOG_NG_BINARY_PATH
    old = __SYSLOG_NG_BINARY_PATH
    __SYSLOG_NG_BINARY_PATH = name
    changes = _format_changes(old, name)
    return _format_state_result(name, result=True, changes=changes)


def set_config_file(name):
    """
    Sets the configuration's name. This function is intended to be used from
    states.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.set_config_file name=/etc/syslog-ng

    """
    global __SYSLOG_NG_CONFIG_FILE
    old = __SYSLOG_NG_CONFIG_FILE
    __SYSLOG_NG_CONFIG_FILE = name
    changes = _format_changes(old, name)
    return _format_state_result(name, result=True, changes=changes)


def get_config_file():
    """
    Returns the configuration directory, which contains syslog-ng.conf.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.get_config_file

    """
    return __SYSLOG_NG_CONFIG_FILE


def _run_command(cmd, options=(), env=None):
    """
    Runs the command cmd with options as its CLI parameters and returns the
    result as a dictionary.
    """
    params = [cmd]
    params.extend(options)
    return __salt__["cmd.run_all"](params, env=env, python_shell=False)


def _determine_config_version(syslog_ng_sbin_dir):
    ret = version(syslog_ng_sbin_dir)
    full_version = ret["stdout"]
    dot_count = 0
    for idx, part in enumerate(full_version):
        if part == ".":
            dot_count = dot_count + 1
        if dot_count == 2:
            return full_version[0:idx]
    # return first 3 characters
    return full_version[:3]


def set_parameters(version=None, binary_path=None, config_file=None, *args, **kwargs):
    """
    Sets variables.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.set_parameters version='3.6'
        salt '*' syslog_ng.set_parameters  binary_path=/home/user/install/syslog-ng/sbin config_file=/home/user/install/syslog-ng/etc/syslog-ng.conf

    """
    if binary_path:
        set_binary_path(binary_path)
    if config_file:
        set_config_file(config_file)
    if version:
        version = _determine_config_version(__SYSLOG_NG_BINARY_PATH)
        write_version(version)

    return _format_return_data(0)


def _run_command_in_extended_path(syslog_ng_sbin_dir, command, params):
    """
    Runs the specified command with the syslog_ng_sbin_dir in the PATH
    """
    orig_path = os.environ.get("PATH", "")
    env = None
    if syslog_ng_sbin_dir:
        # Custom environment variables should be str types. This code
        # normalizes the paths to unicode to join them together, and then
        # converts back to a str type.
        env = {
            str(
                "PATH"
            ): salt.utils.stringutils.to_str(  # future lint: disable=blacklisted-function
                os.pathsep.join(salt.utils.data.decode((orig_path, syslog_ng_sbin_dir)))
            )
        }
    return _run_command(command, options=params, env=env)


def _format_return_data(retcode, stdout=None, stderr=None):
    """
    Creates a dictionary from the parameters, which can be used to return data
    to Salt.
    """
    ret = {"retcode": retcode}
    if stdout is not None:
        ret["stdout"] = stdout
    if stderr is not None:
        ret["stderr"] = stderr
    return ret


def config_test(syslog_ng_sbin_dir=None, cfgfile=None):
    """
    Runs syntax check against cfgfile. If syslog_ng_sbin_dir is specified, it
    is added to the PATH during the test.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.config_test
        salt '*' syslog_ng.config_test /home/user/install/syslog-ng/sbin
        salt '*' syslog_ng.config_test /home/user/install/syslog-ng/sbin /etc/syslog-ng/syslog-ng.conf
    """
    params = ["--syntax-only"]
    if cfgfile:
        params.append("--cfgfile={0}".format(cfgfile))

    try:
        ret = _run_command_in_extended_path(syslog_ng_sbin_dir, "syslog-ng", params)
    except CommandExecutionError as err:
        return _format_return_data(retcode=-1, stderr=six.text_type(err))

    retcode = ret.get("retcode", -1)
    stderr = ret.get("stderr", None)
    stdout = ret.get("stdout", None)
    return _format_return_data(retcode, stdout, stderr)


def version(syslog_ng_sbin_dir=None):
    """
    Returns the version of the installed syslog-ng. If syslog_ng_sbin_dir is
    specified, it is added to the PATH during the execution of the command
    syslog-ng.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.version
        salt '*' syslog_ng.version /home/user/install/syslog-ng/sbin
    """
    try:
        ret = _run_command_in_extended_path(syslog_ng_sbin_dir, "syslog-ng", ("-V",))
    except CommandExecutionError as err:
        return _format_return_data(retcode=-1, stderr=six.text_type(err))

    if ret["retcode"] != 0:
        return _format_return_data(
            ret["retcode"], stderr=ret["stderr"], stdout=ret["stdout"]
        )

    lines = ret["stdout"].split("\n")
    # The format of the first line in the output is:
    # syslog-ng 3.6.0alpha0
    version_line_index = 0
    version_column_index = 1
    line = lines[version_line_index].split()[version_column_index]
    return _format_return_data(0, stdout=line)


def modules(syslog_ng_sbin_dir=None):
    """
    Returns the available modules. If syslog_ng_sbin_dir is specified, it
    is added to the PATH during the execution of the command syslog-ng.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.modules
        salt '*' syslog_ng.modules /home/user/install/syslog-ng/sbin
    """
    try:
        ret = _run_command_in_extended_path(syslog_ng_sbin_dir, "syslog-ng", ("-V",))
    except CommandExecutionError as err:
        return _format_return_data(retcode=-1, stderr=six.text_type(err))

    if ret["retcode"] != 0:
        return _format_return_data(ret["retcode"], ret.get("stdout"), ret.get("stderr"))

    lines = ret["stdout"].split("\n")
    for line in lines:
        if line.startswith("Available-Modules"):
            label, installed_modules = line.split()
            return _format_return_data(ret["retcode"], stdout=installed_modules)
    return _format_return_data(-1, stderr="Unable to find the modules.")


def stats(syslog_ng_sbin_dir=None):
    """
    Returns statistics from the running syslog-ng instance. If
    syslog_ng_sbin_dir is specified, it is added to the PATH during the
    execution of the command syslog-ng-ctl.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.stats
        salt '*' syslog_ng.stats /home/user/install/syslog-ng/sbin
    """
    try:
        ret = _run_command_in_extended_path(
            syslog_ng_sbin_dir, "syslog-ng-ctl", ("stats",)
        )
    except CommandExecutionError as err:
        return _format_return_data(retcode=-1, stderr=six.text_type(err))

    return _format_return_data(ret["retcode"], ret.get("stdout"), ret.get("stderr"))


def _format_changes(old="", new=""):
    return {"old": old, "new": new}


def _format_state_result(name, result, changes=None, comment=""):
    """
    Creates the state result dictionary.
    """
    if changes is None:
        changes = {"old": "", "new": ""}
    return {"name": name, "result": result, "changes": changes, "comment": comment}


def _add_cli_param(params, key, value):
    """
    Adds key and value as a command line parameter to params.
    """
    if value is not None:
        params.append("--{0}={1}".format(key, value))


def _add_boolean_cli_param(params, key, value):
    """
    Adds key as a command line parameter to params.
    """
    if value is True:
        params.append("--{0}".format(key))


def stop(name=None):
    """
    Kills syslog-ng. This function is intended to be used from the state module.

    Users shouldn't use this function, if the service module is available on
    their system.  If :mod:`syslog_ng.set_config_file
    <salt.modules.syslog_ng.set_binary_path>` is called before, this function
    will use the set binary path.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.stop

    """
    pids = __salt__["ps.pgrep"](pattern="syslog-ng")

    if pids is None or len(pids) == 0:
        return _format_state_result(
            name, result=False, comment="Syslog-ng is not running"
        )

    if __opts__.get("test", False):
        comment = "Syslog_ng state module will kill {0} pids"
        return _format_state_result(name, result=None, comment=comment)

    res = __salt__["ps.pkill"]("syslog-ng")
    killed_pids = res["killed"]

    if killed_pids == pids:
        changes = {"old": killed_pids, "new": []}
        return _format_state_result(name, result=True, changes=changes)
    else:
        return _format_state_result(name, result=False)


def start(
    name=None,
    user=None,
    group=None,
    chroot=None,
    caps=None,
    no_caps=False,
    pidfile=None,
    enable_core=False,
    fd_limit=None,
    verbose=False,
    debug=False,
    trace=False,
    yydebug=False,
    persist_file=None,
    control=None,
    worker_threads=None,
):
    """
    Ensures, that syslog-ng is started via the given parameters. This function
    is intended to be used from the state module.

    Users shouldn't use this function, if the service module is available on
    their system. If :mod:`syslog_ng.set_config_file
    <salt.modules.syslog_ng.set_binary_path>`, is called before, this function
    will use the set binary path.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.start

    """
    params = []
    _add_cli_param(params, "user", user)
    _add_cli_param(params, "group", group)
    _add_cli_param(params, "chroot", chroot)
    _add_cli_param(params, "caps", caps)
    _add_boolean_cli_param(params, "no-capse", no_caps)
    _add_cli_param(params, "pidfile", pidfile)
    _add_boolean_cli_param(params, "enable-core", enable_core)
    _add_cli_param(params, "fd-limit", fd_limit)
    _add_boolean_cli_param(params, "verbose", verbose)
    _add_boolean_cli_param(params, "debug", debug)
    _add_boolean_cli_param(params, "trace", trace)
    _add_boolean_cli_param(params, "yydebug", yydebug)
    _add_cli_param(params, "cfgfile", __SYSLOG_NG_CONFIG_FILE)
    _add_boolean_cli_param(params, "persist-file", persist_file)
    _add_cli_param(params, "control", control)
    _add_cli_param(params, "worker-threads", worker_threads)
    if __SYSLOG_NG_BINARY_PATH:
        syslog_ng_binary = os.path.join(__SYSLOG_NG_BINARY_PATH, "syslog-ng")
        command = [syslog_ng_binary] + params

        if __opts__.get("test", False):
            comment = "Syslog_ng state module will start {0}".format(command)
            return _format_state_result(name, result=None, comment=comment)

        result = __salt__["cmd.run_all"](command, python_shell=False)
    else:
        command = ["syslog-ng"] + params

        if __opts__.get("test", False):
            comment = "Syslog_ng state module will start {0}".format(command)
            return _format_state_result(name, result=None, comment=comment)

        result = __salt__["cmd.run_all"](command, python_shell=False)

    if result["pid"] > 0:
        succ = True
    else:
        succ = False

    return _format_state_result(
        name, result=succ, changes={"new": " ".join(command), "old": ""}
    )


def reload_(name):
    """
    Reloads syslog-ng. This function is intended to be used from states.

    If :mod:`syslog_ng.set_config_file
    <salt.modules.syslog_ng.set_binary_path>`, is called before, this function
    will use the set binary path.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.reload

    """
    if __SYSLOG_NG_BINARY_PATH:
        syslog_ng_ctl_binary = os.path.join(__SYSLOG_NG_BINARY_PATH, "syslog-ng-ctl")
        command = [syslog_ng_ctl_binary, "reload"]
        result = __salt__["cmd.run_all"](command, python_shell=False)
    else:
        command = ["syslog-ng-ctl", "reload"]
        result = __salt__["cmd.run_all"](command, python_shell=False)

    succ = True if result["retcode"] == 0 else False
    return _format_state_result(name, result=succ, comment=result["stdout"])


def _format_generated_config_header():
    """
    Formats a header, which is prepended to all appended config.
    """
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    return __SALT_GENERATED_CONFIG_HEADER.format(now)


def write_config(config, newlines=2):
    """
    Writes the given parameter config into the config file. This function is
    intended to be used from states.

    If :mod:`syslog_ng.set_config_file
    <salt.modules.syslog_ng.set_config_file>`, is called before, this function
    will use the set config file.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.write_config config='# comment'

    """
    succ = _write_config(config, newlines)
    changes = _format_changes(new=config)
    return _format_state_result(name="", result=succ, changes=changes)


def _write_config(config, newlines=2):
    """
    Writes the given parameter config into the config file.
    """
    text = config
    if isinstance(config, dict) and len(list(list(config.keys()))) == 1:
        key = next(six.iterkeys(config))
        text = config[key]

    try:
        with salt.utils.files.fopen(__SYSLOG_NG_CONFIG_FILE, "a") as fha:
            fha.write(salt.utils.stringutils.to_str(text))

            for _ in range(0, newlines):
                fha.write(salt.utils.stringutils.to_str(os.linesep))
        return True
    except Exception as err:  # pylint: disable=broad-except
        log.error(six.text_type(err))
        return False


def write_version(name):
    """
    Removes the previous configuration file, then creates a new one and writes
    the name line. This function is intended to be used from states.

    If :mod:`syslog_ng.set_config_file
    <salt.modules.syslog_ng.set_config_file>`, is called before, this function
    will use the set config file.

    CLI Example:

    .. code-block:: bash

        salt '*' syslog_ng.write_version name="3.6"

    """
    line = "@version: {0}".format(name)
    try:
        if os.path.exists(__SYSLOG_NG_CONFIG_FILE):
            log.debug(
                "Removing previous configuration file: %s", __SYSLOG_NG_CONFIG_FILE
            )
            os.remove(__SYSLOG_NG_CONFIG_FILE)
            log.debug("Configuration file successfully removed")

        header = _format_generated_config_header()
        _write_config(config=header, newlines=1)
        _write_config(config=line, newlines=2)

        return _format_state_result(name, result=True)
    except OSError as err:
        log.error(
            "Failed to remove previous configuration file '%s': %s",
            __SYSLOG_NG_CONFIG_FILE,
            err,
        )
        return _format_state_result(name, result=False)
