#
# Autogenerated by Thrift Compiler (0.11.0)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py
#

from thrift.Thrift import TType, TMessageType, TFrozenDict, TException, TApplicationException
from thrift.protocol.TProtocol import TProtocolException
from thrift.TRecursive import fix_spec

import sys

from thrift.transport import TTransport
all_structs = []


class ErrorCode(object):
    DATABASE = 0
    IOERROR = 1
    GENERAL = 2
    AUTH_DENIED = 3
    UNAUTHORIZED = 4
    API_MISMATCH = 5
    SOURCE_FILE = 6

    _VALUES_TO_NAMES = {
        0: "DATABASE",
        1: "IOERROR",
        2: "GENERAL",
        3: "AUTH_DENIED",
        4: "UNAUTHORIZED",
        5: "API_MISMATCH",
        6: "SOURCE_FILE",
    }

    _NAMES_TO_VALUES = {
        "DATABASE": 0,
        "IOERROR": 1,
        "GENERAL": 2,
        "AUTH_DENIED": 3,
        "UNAUTHORIZED": 4,
        "API_MISMATCH": 5,
        "SOURCE_FILE": 6,
    }


class Permission(object):
    """
    The following permission scopes exist.

    SYSTEM: These permissions are global to the running CodeChecker server.
      In this case, the 'extraParams' field is empty.

    PRODUCT: These permissions are configured per-product.
      The extra data field looks like the following object:
        { i64 productID }
    """
    SUPERUSER = 1
    PRODUCT_ADMIN = 16
    PRODUCT_ACCESS = 17
    PRODUCT_STORE = 18

    _VALUES_TO_NAMES = {
        1: "SUPERUSER",
        16: "PRODUCT_ADMIN",
        17: "PRODUCT_ACCESS",
        18: "PRODUCT_STORE",
    }

    _NAMES_TO_VALUES = {
        "SUPERUSER": 1,
        "PRODUCT_ADMIN": 16,
        "PRODUCT_ACCESS": 17,
        "PRODUCT_STORE": 18,
    }


class DBStatus(object):
    """
    Status information about the database backend.
    """
    OK = 0
    MISSING = 1
    FAILED_TO_CONNECT = 2
    SCHEMA_MISMATCH_OK = 3
    SCHEMA_MISMATCH_NO = 4
    SCHEMA_MISSING = 5
    SCHEMA_INIT_ERROR = 6
    SCHEMA_UPGRADE_FAILED = 7

    _VALUES_TO_NAMES = {
        0: "OK",
        1: "MISSING",
        2: "FAILED_TO_CONNECT",
        3: "SCHEMA_MISMATCH_OK",
        4: "SCHEMA_MISMATCH_NO",
        5: "SCHEMA_MISSING",
        6: "SCHEMA_INIT_ERROR",
        7: "SCHEMA_UPGRADE_FAILED",
    }

    _NAMES_TO_VALUES = {
        "OK": 0,
        "MISSING": 1,
        "FAILED_TO_CONNECT": 2,
        "SCHEMA_MISMATCH_OK": 3,
        "SCHEMA_MISMATCH_NO": 4,
        "SCHEMA_MISSING": 5,
        "SCHEMA_INIT_ERROR": 6,
        "SCHEMA_UPGRADE_FAILED": 7,
    }


class RequestFailed(TException):
    """
    Attributes:
     - errorCode
     - message
     - extraInfo
    """


    def __init__(self, errorCode=None, message=None, extraInfo=None,):
        self.errorCode = errorCode
        self.message = message
        self.extraInfo = extraInfo

    def read(self, iprot):
        if iprot._fast_decode is not None and isinstance(iprot.trans, TTransport.CReadableTransport) and self.thrift_spec is not None:
            iprot._fast_decode(self, iprot, [self.__class__, self.thrift_spec])
            return
        iprot.readStructBegin()
        while True:
            (fname, ftype, fid) = iprot.readFieldBegin()
            if ftype == TType.STOP:
                break
            if fid == 1:
                if ftype == TType.I32:
                    self.errorCode = iprot.readI32()
                else:
                    iprot.skip(ftype)
            elif fid == 2:
                if ftype == TType.STRING:
                    self.message = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                else:
                    iprot.skip(ftype)
            elif fid == 3:
                if ftype == TType.LIST:
                    self.extraInfo = []
                    (_etype3, _size0) = iprot.readListBegin()
                    for _i4 in range(_size0):
                        _elem5 = iprot.readString().decode('utf-8') if sys.version_info[0] == 2 else iprot.readString()
                        self.extraInfo.append(_elem5)
                    iprot.readListEnd()
                else:
                    iprot.skip(ftype)
            else:
                iprot.skip(ftype)
            iprot.readFieldEnd()
        iprot.readStructEnd()

    def write(self, oprot):
        if oprot._fast_encode is not None and self.thrift_spec is not None:
            oprot.trans.write(oprot._fast_encode(self, [self.__class__, self.thrift_spec]))
            return
        oprot.writeStructBegin('RequestFailed')
        if self.errorCode is not None:
            oprot.writeFieldBegin('errorCode', TType.I32, 1)
            oprot.writeI32(self.errorCode)
            oprot.writeFieldEnd()
        if self.message is not None:
            oprot.writeFieldBegin('message', TType.STRING, 2)
            oprot.writeString(self.message.encode('utf-8') if sys.version_info[0] == 2 else self.message)
            oprot.writeFieldEnd()
        if self.extraInfo is not None:
            oprot.writeFieldBegin('extraInfo', TType.LIST, 3)
            oprot.writeListBegin(TType.STRING, len(self.extraInfo))
            for iter6 in self.extraInfo:
                oprot.writeString(iter6.encode('utf-8') if sys.version_info[0] == 2 else iter6)
            oprot.writeListEnd()
            oprot.writeFieldEnd()
        oprot.writeFieldStop()
        oprot.writeStructEnd()

    def validate(self):
        return

    def __str__(self):
        return repr(self)

    def __repr__(self):
        L = ['%s=%r' % (key, value)
             for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not (self == other)
all_structs.append(RequestFailed)
RequestFailed.thrift_spec = (
    None,  # 0
    (1, TType.I32, 'errorCode', None, None, ),  # 1
    (2, TType.STRING, 'message', 'UTF8', None, ),  # 2
    (3, TType.LIST, 'extraInfo', (TType.STRING, 'UTF8', False), None, ),  # 3
)
fix_spec(all_structs)
del all_structs
