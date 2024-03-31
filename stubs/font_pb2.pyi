from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Font(_message.Message):
    __slots__ = ("name", "size", "italic", "bold", "family", "face")
    NAME_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ITALIC_FIELD_NUMBER: _ClassVar[int]
    BOLD_FIELD_NUMBER: _ClassVar[int]
    FAMILY_FIELD_NUMBER: _ClassVar[int]
    FACE_FIELD_NUMBER: _ClassVar[int]
    name: str
    size: float
    italic: bool
    bold: bool
    family: str
    face: str
    def __init__(self, name: _Optional[str] = ..., size: _Optional[float] = ..., italic: bool = ..., bold: bool = ..., family: _Optional[str] = ..., face: _Optional[str] = ...) -> None: ...
