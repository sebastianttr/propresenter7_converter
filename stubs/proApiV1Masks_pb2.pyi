import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Masks_Request(_message.Message):
    __slots__ = ("masks", "get_mask", "get_thumbnail")
    class Masks(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetMask(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class GetThumbnail(_message.Message):
        __slots__ = ("id", "quality")
        ID_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        id: str
        quality: int
        def __init__(self, id: _Optional[str] = ..., quality: _Optional[int] = ...) -> None: ...
    MASKS_FIELD_NUMBER: _ClassVar[int]
    GET_MASK_FIELD_NUMBER: _ClassVar[int]
    GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    masks: API_v1_Masks_Request.Masks
    get_mask: API_v1_Masks_Request.GetMask
    get_thumbnail: API_v1_Masks_Request.GetThumbnail
    def __init__(self, masks: _Optional[_Union[API_v1_Masks_Request.Masks, _Mapping]] = ..., get_mask: _Optional[_Union[API_v1_Masks_Request.GetMask, _Mapping]] = ..., get_thumbnail: _Optional[_Union[API_v1_Masks_Request.GetThumbnail, _Mapping]] = ...) -> None: ...

class API_v1_Masks_Response(_message.Message):
    __slots__ = ("masks", "get_mask", "get_thumbnail")
    class Masks(_message.Message):
        __slots__ = ("masks",)
        MASKS_FIELD_NUMBER: _ClassVar[int]
        masks: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        def __init__(self, masks: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
    class GetMask(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _proApiV1Identifier_pb2.API_v1_Identifier
        def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
    class GetThumbnail(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: _Optional[bytes] = ...) -> None: ...
    MASKS_FIELD_NUMBER: _ClassVar[int]
    GET_MASK_FIELD_NUMBER: _ClassVar[int]
    GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    masks: API_v1_Masks_Response.Masks
    get_mask: API_v1_Masks_Response.GetMask
    get_thumbnail: API_v1_Masks_Response.GetThumbnail
    def __init__(self, masks: _Optional[_Union[API_v1_Masks_Response.Masks, _Mapping]] = ..., get_mask: _Optional[_Union[API_v1_Masks_Response.GetMask, _Mapping]] = ..., get_thumbnail: _Optional[_Union[API_v1_Masks_Response.GetThumbnail, _Mapping]] = ...) -> None: ...
