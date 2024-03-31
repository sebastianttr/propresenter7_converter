import uuid_pb2 as _uuid_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TimecodeSettings(_message.Message):
    __slots__ = ("device_identifier", "channel", "format", "offset", "playlist_identifier", "is_active")
    class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        FORMAT_24_FPS: _ClassVar[TimecodeSettings.Format]
        FORMAT_25_FPS: _ClassVar[TimecodeSettings.Format]
        FORMAT_29_97_FPS: _ClassVar[TimecodeSettings.Format]
        FORMAT_30_FPS: _ClassVar[TimecodeSettings.Format]
    FORMAT_24_FPS: TimecodeSettings.Format
    FORMAT_25_FPS: TimecodeSettings.Format
    FORMAT_29_97_FPS: TimecodeSettings.Format
    FORMAT_30_FPS: TimecodeSettings.Format
    DEVICE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    CHANNEL_FIELD_NUMBER: _ClassVar[int]
    FORMAT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    device_identifier: str
    channel: int
    format: TimecodeSettings.Format
    offset: float
    playlist_identifier: _uuid_pb2.UUID
    is_active: bool
    def __init__(self, device_identifier: _Optional[str] = ..., channel: _Optional[int] = ..., format: _Optional[_Union[TimecodeSettings.Format, str]] = ..., offset: _Optional[float] = ..., playlist_identifier: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., is_active: bool = ...) -> None: ...
