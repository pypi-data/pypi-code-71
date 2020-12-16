# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AuthenticationMode',
    'CompatibilityLevel',
    'ContentStoragePolicy',
    'Encoding',
    'EventSerializationType',
    'EventsOutOfOrderPolicy',
    'JobType',
    'JsonOutputSerializationFormat',
    'OutputErrorPolicy',
    'OutputStartMode',
    'StreamingJobSkuName',
]


class AuthenticationMode(str, Enum):
    """
    Authentication Mode.
    """
    MSI = "Msi"
    USER_TOKEN = "UserToken"
    CONNECTION_STRING = "ConnectionString"


class CompatibilityLevel(str, Enum):
    """
    Controls certain runtime behaviors of the streaming job.
    """
    _1_0 = "1.0"


class ContentStoragePolicy(str, Enum):
    """
    Valid values are JobStorageAccount and SystemAccount. If set to JobStorageAccount, this requires the user to also specify jobStorageAccount property. .
    """
    SYSTEM_ACCOUNT = "SystemAccount"
    JOB_STORAGE_ACCOUNT = "JobStorageAccount"


class Encoding(str, Enum):
    """
    Specifies the encoding of the incoming data in the case of input and the encoding of outgoing data in the case of output. Required on PUT (CreateOrReplace) requests.
    """
    UTF8 = "UTF8"


class EventSerializationType(str, Enum):
    """
    Indicates the type of serialization that the input or output uses. Required on PUT (CreateOrReplace) requests.
    """
    CSV = "Csv"
    AVRO = "Avro"
    JSON = "Json"
    CUSTOM_CLR = "CustomClr"
    PARQUET = "Parquet"


class EventsOutOfOrderPolicy(str, Enum):
    """
    Indicates the policy to apply to events that arrive out of order in the input event stream.
    """
    ADJUST = "Adjust"
    DROP = "Drop"


class JobType(str, Enum):
    """
    Describes the type of the job. Valid modes are `Cloud` and 'Edge'.
    """
    CLOUD = "Cloud"
    EDGE = "Edge"


class JsonOutputSerializationFormat(str, Enum):
    """
    This property only applies to JSON serialization of outputs only. It is not applicable to inputs. This property specifies the format of the JSON the output will be written in. The currently supported values are 'lineSeparated' indicating the output will be formatted by having each JSON object separated by a new line and 'array' indicating the output will be formatted as an array of JSON objects. Default value is 'lineSeparated' if left null.
    """
    LINE_SEPARATED = "LineSeparated"
    ARRAY = "Array"


class OutputErrorPolicy(str, Enum):
    """
    Indicates the policy to apply to events that arrive at the output and cannot be written to the external storage due to being malformed (missing column values, column values of wrong type or size).
    """
    STOP = "Stop"
    DROP = "Drop"


class OutputStartMode(str, Enum):
    """
    This property should only be utilized when it is desired that the job be started immediately upon creation. Value may be JobStartTime, CustomTime, or LastOutputEventTime to indicate whether the starting point of the output event stream should start whenever the job is started, start at a custom user time stamp specified via the outputStartTime property, or start from the last event output time.
    """
    JOB_START_TIME = "JobStartTime"
    CUSTOM_TIME = "CustomTime"
    LAST_OUTPUT_EVENT_TIME = "LastOutputEventTime"


class StreamingJobSkuName(str, Enum):
    """
    The name of the SKU. Required on PUT (CreateOrReplace) requests.
    """
    STANDARD = "Standard"
