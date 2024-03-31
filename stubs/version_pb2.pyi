from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Version(_message.Message):
    __slots__ = ("major_version", "minor_version", "patch_version", "build")
    MAJOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    MINOR_VERSION_FIELD_NUMBER: _ClassVar[int]
    PATCH_VERSION_FIELD_NUMBER: _ClassVar[int]
    BUILD_FIELD_NUMBER: _ClassVar[int]
    major_version: int
    minor_version: int
    patch_version: int
    build: str
    def __init__(self, major_version: _Optional[int] = ..., minor_version: _Optional[int] = ..., patch_version: _Optional[int] = ..., build: _Optional[str] = ...) -> None: ...
