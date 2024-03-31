from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_PlaylistPresentationItem(_message.Message):
    __slots__ = ("presentation_uuid",)
    PRESENTATION_UUID_FIELD_NUMBER: _ClassVar[int]
    presentation_uuid: str
    def __init__(self, presentation_uuid: _Optional[str] = ...) -> None: ...
