import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_StageLayoutMap(_message.Message):
    __slots__ = ("entries",)
    class Entry(_message.Message):
        __slots__ = ("screen", "layout")
        SCREEN_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_FIELD_NUMBER: _ClassVar[int]
        screen: _proApiV1Identifier_pb2.API_v1_Identifier
        layout: _proApiV1Identifier_pb2.API_v1_Identifier
        def __init__(self, screen: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., layout: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    entries: _containers.RepeatedCompositeFieldContainer[API_v1_StageLayoutMap.Entry]
    def __init__(self, entries: _Optional[_Iterable[_Union[API_v1_StageLayoutMap.Entry, _Mapping]]] = ...) -> None: ...

class API_v1_Stage_Request(_message.Message):
    __slots__ = ("get_layout_map", "set_layout_map", "get_message", "put_message", "delete_message", "get_screens", "get_screen_layout", "set_screen_layout", "get_layouts", "delete_layout", "get_layout_thumbnail")
    class GetLayoutMap(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SetLayoutMap(_message.Message):
        __slots__ = ("map",)
        MAP_FIELD_NUMBER: _ClassVar[int]
        map: API_v1_StageLayoutMap
        def __init__(self, map: _Optional[_Union[API_v1_StageLayoutMap, _Mapping]] = ...) -> None: ...
    class GetMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PutMessage(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class DeleteMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetScreens(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetScreenLayout(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class SetScreenLayout(_message.Message):
        __slots__ = ("id", "layout")
        ID_FIELD_NUMBER: _ClassVar[int]
        LAYOUT_FIELD_NUMBER: _ClassVar[int]
        id: str
        layout: str
        def __init__(self, id: _Optional[str] = ..., layout: _Optional[str] = ...) -> None: ...
    class GetLayouts(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class DeleteLayout(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class GetLayoutThumbnail(_message.Message):
        __slots__ = ("id", "quality")
        ID_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        id: str
        quality: int
        def __init__(self, id: _Optional[str] = ..., quality: _Optional[int] = ...) -> None: ...
    GET_LAYOUT_MAP_FIELD_NUMBER: _ClassVar[int]
    SET_LAYOUT_MAP_FIELD_NUMBER: _ClassVar[int]
    GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_SCREENS_FIELD_NUMBER: _ClassVar[int]
    GET_SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    SET_SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    GET_LAYOUTS_FIELD_NUMBER: _ClassVar[int]
    DELETE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    GET_LAYOUT_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    get_layout_map: API_v1_Stage_Request.GetLayoutMap
    set_layout_map: API_v1_Stage_Request.SetLayoutMap
    get_message: API_v1_Stage_Request.GetMessage
    put_message: API_v1_Stage_Request.PutMessage
    delete_message: API_v1_Stage_Request.DeleteMessage
    get_screens: API_v1_Stage_Request.GetScreens
    get_screen_layout: API_v1_Stage_Request.GetScreenLayout
    set_screen_layout: API_v1_Stage_Request.SetScreenLayout
    get_layouts: API_v1_Stage_Request.GetLayouts
    delete_layout: API_v1_Stage_Request.DeleteLayout
    get_layout_thumbnail: API_v1_Stage_Request.GetLayoutThumbnail
    def __init__(self, get_layout_map: _Optional[_Union[API_v1_Stage_Request.GetLayoutMap, _Mapping]] = ..., set_layout_map: _Optional[_Union[API_v1_Stage_Request.SetLayoutMap, _Mapping]] = ..., get_message: _Optional[_Union[API_v1_Stage_Request.GetMessage, _Mapping]] = ..., put_message: _Optional[_Union[API_v1_Stage_Request.PutMessage, _Mapping]] = ..., delete_message: _Optional[_Union[API_v1_Stage_Request.DeleteMessage, _Mapping]] = ..., get_screens: _Optional[_Union[API_v1_Stage_Request.GetScreens, _Mapping]] = ..., get_screen_layout: _Optional[_Union[API_v1_Stage_Request.GetScreenLayout, _Mapping]] = ..., set_screen_layout: _Optional[_Union[API_v1_Stage_Request.SetScreenLayout, _Mapping]] = ..., get_layouts: _Optional[_Union[API_v1_Stage_Request.GetLayouts, _Mapping]] = ..., delete_layout: _Optional[_Union[API_v1_Stage_Request.DeleteLayout, _Mapping]] = ..., get_layout_thumbnail: _Optional[_Union[API_v1_Stage_Request.GetLayoutThumbnail, _Mapping]] = ...) -> None: ...

class API_v1_Stage_Response(_message.Message):
    __slots__ = ("get_layout_map", "set_layout_map", "get_message", "put_message", "delete_message", "get_screens", "get_screen_layout", "set_screen_layout", "get_layouts", "delete_layout", "get_layout_thumbnail")
    class GetLayoutMap(_message.Message):
        __slots__ = ("map",)
        MAP_FIELD_NUMBER: _ClassVar[int]
        map: API_v1_StageLayoutMap
        def __init__(self, map: _Optional[_Union[API_v1_StageLayoutMap, _Mapping]] = ...) -> None: ...
    class SetLayoutMap(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetMessage(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: str
        def __init__(self, message: _Optional[str] = ...) -> None: ...
    class PutMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class DeleteMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetScreens(_message.Message):
        __slots__ = ("screens",)
        SCREENS_FIELD_NUMBER: _ClassVar[int]
        screens: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        def __init__(self, screens: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
    class GetScreenLayout(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: _proApiV1Identifier_pb2.API_v1_Identifier
        def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
    class SetScreenLayout(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetLayouts(_message.Message):
        __slots__ = ("layouts",)
        class Layout(_message.Message):
            __slots__ = ("id",)
            ID_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1Identifier_pb2.API_v1_Identifier
            def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ...) -> None: ...
        LAYOUTS_FIELD_NUMBER: _ClassVar[int]
        layouts: _containers.RepeatedCompositeFieldContainer[API_v1_Stage_Response.GetLayouts.Layout]
        def __init__(self, layouts: _Optional[_Iterable[_Union[API_v1_Stage_Response.GetLayouts.Layout, _Mapping]]] = ...) -> None: ...
    class DeleteLayout(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetLayoutThumbnail(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: _Optional[bytes] = ...) -> None: ...
    GET_LAYOUT_MAP_FIELD_NUMBER: _ClassVar[int]
    SET_LAYOUT_MAP_FIELD_NUMBER: _ClassVar[int]
    GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_SCREENS_FIELD_NUMBER: _ClassVar[int]
    GET_SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    SET_SCREEN_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    GET_LAYOUTS_FIELD_NUMBER: _ClassVar[int]
    DELETE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    GET_LAYOUT_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    get_layout_map: API_v1_Stage_Response.GetLayoutMap
    set_layout_map: API_v1_Stage_Response.SetLayoutMap
    get_message: API_v1_Stage_Response.GetMessage
    put_message: API_v1_Stage_Response.PutMessage
    delete_message: API_v1_Stage_Response.DeleteMessage
    get_screens: API_v1_Stage_Response.GetScreens
    get_screen_layout: API_v1_Stage_Response.GetScreenLayout
    set_screen_layout: API_v1_Stage_Response.SetScreenLayout
    get_layouts: API_v1_Stage_Response.GetLayouts
    delete_layout: API_v1_Stage_Response.DeleteLayout
    get_layout_thumbnail: API_v1_Stage_Response.GetLayoutThumbnail
    def __init__(self, get_layout_map: _Optional[_Union[API_v1_Stage_Response.GetLayoutMap, _Mapping]] = ..., set_layout_map: _Optional[_Union[API_v1_Stage_Response.SetLayoutMap, _Mapping]] = ..., get_message: _Optional[_Union[API_v1_Stage_Response.GetMessage, _Mapping]] = ..., put_message: _Optional[_Union[API_v1_Stage_Response.PutMessage, _Mapping]] = ..., delete_message: _Optional[_Union[API_v1_Stage_Response.DeleteMessage, _Mapping]] = ..., get_screens: _Optional[_Union[API_v1_Stage_Response.GetScreens, _Mapping]] = ..., get_screen_layout: _Optional[_Union[API_v1_Stage_Response.GetScreenLayout, _Mapping]] = ..., set_screen_layout: _Optional[_Union[API_v1_Stage_Response.SetScreenLayout, _Mapping]] = ..., get_layouts: _Optional[_Union[API_v1_Stage_Response.GetLayouts, _Mapping]] = ..., delete_layout: _Optional[_Union[API_v1_Stage_Response.DeleteLayout, _Mapping]] = ..., get_layout_thumbnail: _Optional[_Union[API_v1_Stage_Response.GetLayoutThumbnail, _Mapping]] = ...) -> None: ...
