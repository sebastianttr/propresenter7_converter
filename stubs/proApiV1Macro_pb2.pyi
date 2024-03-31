import proApiV1Color_pb2 as _proApiV1Color_pb2
import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Macro(_message.Message):
    __slots__ = ("id", "color", "image_type")
    ID_FIELD_NUMBER: _ClassVar[int]
    COLOR_FIELD_NUMBER: _ClassVar[int]
    IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    color: _proApiV1Color_pb2.API_v1_Color
    image_type: str
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., color: _Optional[_Union[_proApiV1Color_pb2.API_v1_Color, _Mapping]] = ..., image_type: _Optional[str] = ...) -> None: ...

class API_v1_Macro_Collection(_message.Message):
    __slots__ = ("id", "macros")
    ID_FIELD_NUMBER: _ClassVar[int]
    MACROS_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    macros: _containers.RepeatedCompositeFieldContainer[API_v1_Macro]
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., macros: _Optional[_Iterable[_Union[API_v1_Macro, _Mapping]]] = ...) -> None: ...

class API_v1_Macro_Request(_message.Message):
    __slots__ = ("macros", "get_macro", "put_macro", "delete_macro", "trigger_macro", "macro_collections", "get_macro_collection", "post_macro_collections", "put_macro_collection", "delete_macro_collection", "macro_icon", "put_macro_icon")
    class Macros(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetMacro(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PutMacro(_message.Message):
        __slots__ = ("id", "name_change", "color_change", "image_type_change")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_CHANGE_FIELD_NUMBER: _ClassVar[int]
        COLOR_CHANGE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_TYPE_CHANGE_FIELD_NUMBER: _ClassVar[int]
        id: str
        name_change: str
        color_change: _proApiV1Color_pb2.API_v1_Color
        image_type_change: str
        def __init__(self, id: _Optional[str] = ..., name_change: _Optional[str] = ..., color_change: _Optional[_Union[_proApiV1Color_pb2.API_v1_Color, _Mapping]] = ..., image_type_change: _Optional[str] = ...) -> None: ...
    class DeleteMacro(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class TriggerMacro(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class MacroCollections(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetMacroCollection(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PostMacroCollections(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class PutMacroCollection(_message.Message):
        __slots__ = ("id", "changes")
        ID_FIELD_NUMBER: _ClassVar[int]
        CHANGES_FIELD_NUMBER: _ClassVar[int]
        id: str
        changes: API_v1_Macro_Collection
        def __init__(self, id: _Optional[str] = ..., changes: _Optional[_Union[API_v1_Macro_Collection, _Mapping]] = ...) -> None: ...
    class DeleteMacroCollection(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class MacroIcon(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PutMacroIcon(_message.Message):
        __slots__ = ("id", "content_type", "icon")
        ID_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        id: str
        content_type: str
        icon: bytes
        def __init__(self, id: _Optional[str] = ..., content_type: _Optional[str] = ..., icon: _Optional[bytes] = ...) -> None: ...
    MACROS_FIELD_NUMBER: _ClassVar[int]
    GET_MACRO_FIELD_NUMBER: _ClassVar[int]
    PUT_MACRO_FIELD_NUMBER: _ClassVar[int]
    DELETE_MACRO_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_MACRO_FIELD_NUMBER: _ClassVar[int]
    MACRO_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    GET_MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    POST_MACRO_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    PUT_MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DELETE_MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    MACRO_ICON_FIELD_NUMBER: _ClassVar[int]
    PUT_MACRO_ICON_FIELD_NUMBER: _ClassVar[int]
    macros: API_v1_Macro_Request.Macros
    get_macro: API_v1_Macro_Request.GetMacro
    put_macro: API_v1_Macro_Request.PutMacro
    delete_macro: API_v1_Macro_Request.DeleteMacro
    trigger_macro: API_v1_Macro_Request.TriggerMacro
    macro_collections: API_v1_Macro_Request.MacroCollections
    get_macro_collection: API_v1_Macro_Request.GetMacroCollection
    post_macro_collections: API_v1_Macro_Request.PostMacroCollections
    put_macro_collection: API_v1_Macro_Request.PutMacroCollection
    delete_macro_collection: API_v1_Macro_Request.DeleteMacroCollection
    macro_icon: API_v1_Macro_Request.MacroIcon
    put_macro_icon: API_v1_Macro_Request.PutMacroIcon
    def __init__(self, macros: _Optional[_Union[API_v1_Macro_Request.Macros, _Mapping]] = ..., get_macro: _Optional[_Union[API_v1_Macro_Request.GetMacro, _Mapping]] = ..., put_macro: _Optional[_Union[API_v1_Macro_Request.PutMacro, _Mapping]] = ..., delete_macro: _Optional[_Union[API_v1_Macro_Request.DeleteMacro, _Mapping]] = ..., trigger_macro: _Optional[_Union[API_v1_Macro_Request.TriggerMacro, _Mapping]] = ..., macro_collections: _Optional[_Union[API_v1_Macro_Request.MacroCollections, _Mapping]] = ..., get_macro_collection: _Optional[_Union[API_v1_Macro_Request.GetMacroCollection, _Mapping]] = ..., post_macro_collections: _Optional[_Union[API_v1_Macro_Request.PostMacroCollections, _Mapping]] = ..., put_macro_collection: _Optional[_Union[API_v1_Macro_Request.PutMacroCollection, _Mapping]] = ..., delete_macro_collection: _Optional[_Union[API_v1_Macro_Request.DeleteMacroCollection, _Mapping]] = ..., macro_icon: _Optional[_Union[API_v1_Macro_Request.MacroIcon, _Mapping]] = ..., put_macro_icon: _Optional[_Union[API_v1_Macro_Request.PutMacroIcon, _Mapping]] = ...) -> None: ...

class API_v1_Macro_Response(_message.Message):
    __slots__ = ("macros", "get_macro", "put_macro", "delete_macro", "trigger_macro", "macro_collections", "get_macro_collection", "post_macro_collections", "put_macro_collection", "delete_macro_collection", "macro_icon", "put_macro_icon")
    class Macros(_message.Message):
        __slots__ = ("macros",)
        MACROS_FIELD_NUMBER: _ClassVar[int]
        macros: _containers.RepeatedCompositeFieldContainer[API_v1_Macro]
        def __init__(self, macros: _Optional[_Iterable[_Union[API_v1_Macro, _Mapping]]] = ...) -> None: ...
    class GetMacro(_message.Message):
        __slots__ = ("macro",)
        MACRO_FIELD_NUMBER: _ClassVar[int]
        macro: API_v1_Macro
        def __init__(self, macro: _Optional[_Union[API_v1_Macro, _Mapping]] = ...) -> None: ...
    class PutMacro(_message.Message):
        __slots__ = ("macro",)
        MACRO_FIELD_NUMBER: _ClassVar[int]
        macro: API_v1_Macro
        def __init__(self, macro: _Optional[_Union[API_v1_Macro, _Mapping]] = ...) -> None: ...
    class DeleteMacro(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TriggerMacro(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MacroCollections(_message.Message):
        __slots__ = ("macro_collections",)
        class Collections(_message.Message):
            __slots__ = ("collections",)
            COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
            collections: _containers.RepeatedCompositeFieldContainer[API_v1_Macro_Collection]
            def __init__(self, collections: _Optional[_Iterable[_Union[API_v1_Macro_Collection, _Mapping]]] = ...) -> None: ...
        MACRO_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
        macro_collections: API_v1_Macro_Response.MacroCollections.Collections
        def __init__(self, macro_collections: _Optional[_Union[API_v1_Macro_Response.MacroCollections.Collections, _Mapping]] = ...) -> None: ...
    class GetMacroCollection(_message.Message):
        __slots__ = ("macro_collection",)
        MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
        macro_collection: API_v1_Macro_Collection
        def __init__(self, macro_collection: _Optional[_Union[API_v1_Macro_Collection, _Mapping]] = ...) -> None: ...
    class PostMacroCollections(_message.Message):
        __slots__ = ("macro_collection",)
        MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
        macro_collection: API_v1_Macro_Collection
        def __init__(self, macro_collection: _Optional[_Union[API_v1_Macro_Collection, _Mapping]] = ...) -> None: ...
    class PutMacroCollection(_message.Message):
        __slots__ = ("macro_collection",)
        MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
        macro_collection: API_v1_Macro_Collection
        def __init__(self, macro_collection: _Optional[_Union[API_v1_Macro_Collection, _Mapping]] = ...) -> None: ...
    class DeleteMacroCollection(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MacroIcon(_message.Message):
        __slots__ = ("content_type", "icon")
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        content_type: str
        icon: bytes
        def __init__(self, content_type: _Optional[str] = ..., icon: _Optional[bytes] = ...) -> None: ...
    class PutMacroIcon(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    MACROS_FIELD_NUMBER: _ClassVar[int]
    GET_MACRO_FIELD_NUMBER: _ClassVar[int]
    PUT_MACRO_FIELD_NUMBER: _ClassVar[int]
    DELETE_MACRO_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_MACRO_FIELD_NUMBER: _ClassVar[int]
    MACRO_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    GET_MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    POST_MACRO_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    PUT_MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    DELETE_MACRO_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    MACRO_ICON_FIELD_NUMBER: _ClassVar[int]
    PUT_MACRO_ICON_FIELD_NUMBER: _ClassVar[int]
    macros: API_v1_Macro_Response.Macros
    get_macro: API_v1_Macro_Response.GetMacro
    put_macro: API_v1_Macro_Response.PutMacro
    delete_macro: API_v1_Macro_Response.DeleteMacro
    trigger_macro: API_v1_Macro_Response.TriggerMacro
    macro_collections: API_v1_Macro_Response.MacroCollections
    get_macro_collection: API_v1_Macro_Response.GetMacroCollection
    post_macro_collections: API_v1_Macro_Response.PostMacroCollections
    put_macro_collection: API_v1_Macro_Response.PutMacroCollection
    delete_macro_collection: API_v1_Macro_Response.DeleteMacroCollection
    macro_icon: API_v1_Macro_Response.MacroIcon
    put_macro_icon: API_v1_Macro_Response.PutMacroIcon
    def __init__(self, macros: _Optional[_Union[API_v1_Macro_Response.Macros, _Mapping]] = ..., get_macro: _Optional[_Union[API_v1_Macro_Response.GetMacro, _Mapping]] = ..., put_macro: _Optional[_Union[API_v1_Macro_Response.PutMacro, _Mapping]] = ..., delete_macro: _Optional[_Union[API_v1_Macro_Response.DeleteMacro, _Mapping]] = ..., trigger_macro: _Optional[_Union[API_v1_Macro_Response.TriggerMacro, _Mapping]] = ..., macro_collections: _Optional[_Union[API_v1_Macro_Response.MacroCollections, _Mapping]] = ..., get_macro_collection: _Optional[_Union[API_v1_Macro_Response.GetMacroCollection, _Mapping]] = ..., post_macro_collections: _Optional[_Union[API_v1_Macro_Response.PostMacroCollections, _Mapping]] = ..., put_macro_collection: _Optional[_Union[API_v1_Macro_Response.PutMacroCollection, _Mapping]] = ..., delete_macro_collection: _Optional[_Union[API_v1_Macro_Response.DeleteMacroCollection, _Mapping]] = ..., macro_icon: _Optional[_Union[API_v1_Macro_Response.MacroIcon, _Mapping]] = ..., put_macro_icon: _Optional[_Union[API_v1_Macro_Response.PutMacroIcon, _Mapping]] = ...) -> None: ...
