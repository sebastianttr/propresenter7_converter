from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProClockSource(_message.Message):
    __slots__ = ("uuid", "name", "connected", "active", "type")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKOWN: _ClassVar[ProClockSource.Type]
        TYPE_INPUT: _ClassVar[ProClockSource.Type]
        TYPE_OUTPUT: _ClassVar[ProClockSource.Type]
    TYPE_UNKOWN: ProClockSource.Type
    TYPE_INPUT: ProClockSource.Type
    TYPE_OUTPUT: ProClockSource.Type
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    CONNECTED_FIELD_NUMBER: _ClassVar[int]
    ACTIVE_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    connected: bool
    active: bool
    type: ProClockSource.Type
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., connected: bool = ..., active: bool = ..., type: _Optional[_Union[ProClockSource.Type, str]] = ...) -> None: ...
