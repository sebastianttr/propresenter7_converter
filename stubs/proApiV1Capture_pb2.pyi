import proApiV1Size_pb2 as _proApiV1Size_pb2
import uuid_pb2 as _uuid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_CaptureSettings(_message.Message):
    __slots__ = ("source", "audio_routing", "disk", "rtmp", "resi")
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_ROUTING_FIELD_NUMBER: _ClassVar[int]
    DISK_FIELD_NUMBER: _ClassVar[int]
    RTMP_FIELD_NUMBER: _ClassVar[int]
    RESI_FIELD_NUMBER: _ClassVar[int]
    source: _uuid_pb2.UUID
    audio_routing: _containers.RepeatedCompositeFieldContainer[API_v1_AudioRouting]
    disk: API_v1_DiskCapture
    rtmp: API_v1_RTMPCapture
    resi: API_v1_ResiCapture
    def __init__(self, source: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., audio_routing: _Optional[_Iterable[_Union[API_v1_AudioRouting, _Mapping]]] = ..., disk: _Optional[_Union[API_v1_DiskCapture, _Mapping]] = ..., rtmp: _Optional[_Union[API_v1_RTMPCapture, _Mapping]] = ..., resi: _Optional[_Union[API_v1_ResiCapture, _Mapping]] = ...) -> None: ...

class API_v1_AudioRouting(_message.Message):
    __slots__ = ("map",)
    MAP_FIELD_NUMBER: _ClassVar[int]
    map: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, map: _Optional[_Iterable[int]] = ...) -> None: ...

class API_v1_DiskCapture(_message.Message):
    __slots__ = ("file_location", "codec", "resolution", "frame_rate")
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    CODEC_FIELD_NUMBER: _ClassVar[int]
    RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
    file_location: str
    codec: str
    resolution: _proApiV1Size_pb2.API_v1_Size
    frame_rate: float
    def __init__(self, file_location: _Optional[str] = ..., codec: _Optional[str] = ..., resolution: _Optional[_Union[_proApiV1Size_pb2.API_v1_Size, _Mapping]] = ..., frame_rate: _Optional[float] = ...) -> None: ...

class API_v1_RTMPCapture(_message.Message):
    __slots__ = ("server", "key", "encoding", "save_local", "file_location")
    SERVER_FIELD_NUMBER: _ClassVar[int]
    KEY_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    SAVE_LOCAL_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    server: str
    key: str
    encoding: str
    save_local: bool
    file_location: str
    def __init__(self, server: _Optional[str] = ..., key: _Optional[str] = ..., encoding: _Optional[str] = ..., save_local: bool = ..., file_location: _Optional[str] = ...) -> None: ...

class API_v1_ResiCapture(_message.Message):
    __slots__ = ("event_name", "event_description", "destination_group", "encoding")
    EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
    EVENT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    DESTINATION_GROUP_FIELD_NUMBER: _ClassVar[int]
    ENCODING_FIELD_NUMBER: _ClassVar[int]
    event_name: str
    event_description: str
    destination_group: str
    encoding: str
    def __init__(self, event_name: _Optional[str] = ..., event_description: _Optional[str] = ..., destination_group: _Optional[str] = ..., encoding: _Optional[str] = ...) -> None: ...

class API_v1_Capture_Request(_message.Message):
    __slots__ = ("get_status", "operation", "get_settings", "set_settings", "get_encodings")
    class Status(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Operation(_message.Message):
        __slots__ = ("operation",)
        class CaptureOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            start: _ClassVar[API_v1_Capture_Request.Operation.CaptureOperation]
            stop: _ClassVar[API_v1_Capture_Request.Operation.CaptureOperation]
        start: API_v1_Capture_Request.Operation.CaptureOperation
        stop: API_v1_Capture_Request.Operation.CaptureOperation
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        operation: API_v1_Capture_Request.Operation.CaptureOperation
        def __init__(self, operation: _Optional[_Union[API_v1_Capture_Request.Operation.CaptureOperation, str]] = ...) -> None: ...
    class GetSettings(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SetSettings(_message.Message):
        __slots__ = ("settings",)
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        settings: API_v1_CaptureSettings
        def __init__(self, settings: _Optional[_Union[API_v1_CaptureSettings, _Mapping]] = ...) -> None: ...
    class Encodings(_message.Message):
        __slots__ = ("type",)
        class API_v1_CaptureDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            disk: _ClassVar[API_v1_Capture_Request.Encodings.API_v1_CaptureDestination]
            rtmp: _ClassVar[API_v1_Capture_Request.Encodings.API_v1_CaptureDestination]
            resi: _ClassVar[API_v1_Capture_Request.Encodings.API_v1_CaptureDestination]
        disk: API_v1_Capture_Request.Encodings.API_v1_CaptureDestination
        rtmp: API_v1_Capture_Request.Encodings.API_v1_CaptureDestination
        resi: API_v1_Capture_Request.Encodings.API_v1_CaptureDestination
        TYPE_FIELD_NUMBER: _ClassVar[int]
        type: API_v1_Capture_Request.Encodings.API_v1_CaptureDestination
        def __init__(self, type: _Optional[_Union[API_v1_Capture_Request.Encodings.API_v1_CaptureDestination, str]] = ...) -> None: ...
    GET_STATUS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    GET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GET_ENCODINGS_FIELD_NUMBER: _ClassVar[int]
    get_status: API_v1_Capture_Request.Status
    operation: API_v1_Capture_Request.Operation
    get_settings: API_v1_Capture_Request.GetSettings
    set_settings: API_v1_Capture_Request.SetSettings
    get_encodings: API_v1_Capture_Request.Encodings
    def __init__(self, get_status: _Optional[_Union[API_v1_Capture_Request.Status, _Mapping]] = ..., operation: _Optional[_Union[API_v1_Capture_Request.Operation, _Mapping]] = ..., get_settings: _Optional[_Union[API_v1_Capture_Request.GetSettings, _Mapping]] = ..., set_settings: _Optional[_Union[API_v1_Capture_Request.SetSettings, _Mapping]] = ..., get_encodings: _Optional[_Union[API_v1_Capture_Request.Encodings, _Mapping]] = ...) -> None: ...

class API_v1_Capture_Response(_message.Message):
    __slots__ = ("get_status", "operation", "get_settings", "set_settings", "get_encodings")
    class GetStatus(_message.Message):
        __slots__ = ("status", "capture_time", "status_text")
        class API_v1_CaptureStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            active: _ClassVar[API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus]
            inactive: _ClassVar[API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus]
            caution: _ClassVar[API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus]
            error: _ClassVar[API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus]
        active: API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
        inactive: API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
        caution: API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
        error: API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
        STATUS_FIELD_NUMBER: _ClassVar[int]
        CAPTURE_TIME_FIELD_NUMBER: _ClassVar[int]
        STATUS_TEXT_FIELD_NUMBER: _ClassVar[int]
        status: API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus
        capture_time: str
        status_text: str
        def __init__(self, status: _Optional[_Union[API_v1_Capture_Response.GetStatus.API_v1_CaptureStatus, str]] = ..., capture_time: _Optional[str] = ..., status_text: _Optional[str] = ...) -> None: ...
    class Operation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetSettings(_message.Message):
        __slots__ = ("settings",)
        SETTINGS_FIELD_NUMBER: _ClassVar[int]
        settings: API_v1_CaptureSettings
        def __init__(self, settings: _Optional[_Union[API_v1_CaptureSettings, _Mapping]] = ...) -> None: ...
    class SetSettings(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Encodings(_message.Message):
        __slots__ = ("encodings",)
        ENCODINGS_FIELD_NUMBER: _ClassVar[int]
        encodings: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, encodings: _Optional[_Iterable[str]] = ...) -> None: ...
    GET_STATUS_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    GET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    SET_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    GET_ENCODINGS_FIELD_NUMBER: _ClassVar[int]
    get_status: API_v1_Capture_Response.GetStatus
    operation: API_v1_Capture_Response.Operation
    get_settings: API_v1_Capture_Response.GetSettings
    set_settings: API_v1_Capture_Response.SetSettings
    get_encodings: API_v1_Capture_Response.Encodings
    def __init__(self, get_status: _Optional[_Union[API_v1_Capture_Response.GetStatus, _Mapping]] = ..., operation: _Optional[_Union[API_v1_Capture_Response.Operation, _Mapping]] = ..., get_settings: _Optional[_Union[API_v1_Capture_Response.GetSettings, _Mapping]] = ..., set_settings: _Optional[_Union[API_v1_Capture_Response.SetSettings, _Mapping]] = ..., get_encodings: _Optional[_Union[API_v1_Capture_Response.Encodings, _Mapping]] = ...) -> None: ...
