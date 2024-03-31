from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Identifier(_message.Message):
    __slots__ = ("uuid", "name", "index")
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    name: str
    index: int
    def __init__(self, uuid: _Optional[str] = ..., name: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...
