import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_PropData(_message.Message):
    __slots__ = ("id", "is_active")
    ID_FIELD_NUMBER: _ClassVar[int]
    IS_ACTIVE_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    is_active: bool
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., is_active: bool = ...) -> None: ...

class API_v1_Prop_Request(_message.Message):
    __slots__ = ("props", "get_prop", "delete_prop", "trigger_prop", "clear_prop", "get_thumbnail")
    class Props(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetProp(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class DeleteProp(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class TriggerProp(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class ClearProp(_message.Message):
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
    PROPS_FIELD_NUMBER: _ClassVar[int]
    GET_PROP_FIELD_NUMBER: _ClassVar[int]
    DELETE_PROP_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PROP_FIELD_NUMBER: _ClassVar[int]
    CLEAR_PROP_FIELD_NUMBER: _ClassVar[int]
    GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    props: API_v1_Prop_Request.Props
    get_prop: API_v1_Prop_Request.GetProp
    delete_prop: API_v1_Prop_Request.DeleteProp
    trigger_prop: API_v1_Prop_Request.TriggerProp
    clear_prop: API_v1_Prop_Request.ClearProp
    get_thumbnail: API_v1_Prop_Request.GetThumbnail
    def __init__(self, props: _Optional[_Union[API_v1_Prop_Request.Props, _Mapping]] = ..., get_prop: _Optional[_Union[API_v1_Prop_Request.GetProp, _Mapping]] = ..., delete_prop: _Optional[_Union[API_v1_Prop_Request.DeleteProp, _Mapping]] = ..., trigger_prop: _Optional[_Union[API_v1_Prop_Request.TriggerProp, _Mapping]] = ..., clear_prop: _Optional[_Union[API_v1_Prop_Request.ClearProp, _Mapping]] = ..., get_thumbnail: _Optional[_Union[API_v1_Prop_Request.GetThumbnail, _Mapping]] = ...) -> None: ...

class API_v1_Prop_Response(_message.Message):
    __slots__ = ("props", "get_prop", "delete_prop", "trigger_prop", "clear_prop", "get_thumbnail")
    class Props(_message.Message):
        __slots__ = ("props",)
        PROPS_FIELD_NUMBER: _ClassVar[int]
        props: _containers.RepeatedCompositeFieldContainer[API_v1_PropData]
        def __init__(self, props: _Optional[_Iterable[_Union[API_v1_PropData, _Mapping]]] = ...) -> None: ...
    class GetProp(_message.Message):
        __slots__ = ("prop",)
        PROP_FIELD_NUMBER: _ClassVar[int]
        prop: API_v1_PropData
        def __init__(self, prop: _Optional[_Union[API_v1_PropData, _Mapping]] = ...) -> None: ...
    class DeleteProp(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TriggerProp(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ClearProp(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetThumbnail(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: _Optional[bytes] = ...) -> None: ...
    PROPS_FIELD_NUMBER: _ClassVar[int]
    GET_PROP_FIELD_NUMBER: _ClassVar[int]
    DELETE_PROP_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_PROP_FIELD_NUMBER: _ClassVar[int]
    CLEAR_PROP_FIELD_NUMBER: _ClassVar[int]
    GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    props: API_v1_Prop_Response.Props
    get_prop: API_v1_Prop_Response.GetProp
    delete_prop: API_v1_Prop_Response.DeleteProp
    trigger_prop: API_v1_Prop_Response.TriggerProp
    clear_prop: API_v1_Prop_Response.ClearProp
    get_thumbnail: API_v1_Prop_Response.GetThumbnail
    def __init__(self, props: _Optional[_Union[API_v1_Prop_Response.Props, _Mapping]] = ..., get_prop: _Optional[_Union[API_v1_Prop_Response.GetProp, _Mapping]] = ..., delete_prop: _Optional[_Union[API_v1_Prop_Response.DeleteProp, _Mapping]] = ..., trigger_prop: _Optional[_Union[API_v1_Prop_Response.TriggerProp, _Mapping]] = ..., clear_prop: _Optional[_Union[API_v1_Prop_Response.ClearProp, _Mapping]] = ..., get_thumbnail: _Optional[_Union[API_v1_Prop_Response.GetThumbnail, _Mapping]] = ...) -> None: ...
