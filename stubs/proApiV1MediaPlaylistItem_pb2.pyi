import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_MediaPlaylistItem(_message.Message):
    __slots__ = ("id", "type", "artist", "duration")
    class API_v1_MediaPlaylistItemType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        audio: _ClassVar[API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType]
        image: _ClassVar[API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType]
        video: _ClassVar[API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType]
    audio: API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType
    image: API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType
    video: API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType
    ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ARTIST_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    type: API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType
    artist: str
    duration: int
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., type: _Optional[_Union[API_v1_MediaPlaylistItem.API_v1_MediaPlaylistItemType, str]] = ..., artist: _Optional[str] = ..., duration: _Optional[int] = ...) -> None: ...
