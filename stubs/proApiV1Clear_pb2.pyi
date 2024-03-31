import proApiV1Color_pb2 as _proApiV1Color_pb2
import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
import proApiV1LayerType_pb2 as _proApiV1LayerType_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_ClearGroup(_message.Message):
    __slots__ = ("id", "icon", "tint", "layers", "stop_timeline_announcements", "stop_timeline_presentation", "clear_next_presentation")
    class API_v1_ClearGroupLayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        music: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        audio_effects: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        props: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        messages: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        announcements: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        presentation: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        presentation_media: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
        video_input: _ClassVar[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
    music: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    audio_effects: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    props: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    messages: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    announcements: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    presentation: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    presentation_media: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    video_input: API_v1_ClearGroup.API_v1_ClearGroupLayerType
    ID_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    TINT_FIELD_NUMBER: _ClassVar[int]
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    STOP_TIMELINE_ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    STOP_TIMELINE_PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    CLEAR_NEXT_PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    icon: str
    tint: _proApiV1Color_pb2.API_v1_Color
    layers: _containers.RepeatedScalarFieldContainer[API_v1_ClearGroup.API_v1_ClearGroupLayerType]
    stop_timeline_announcements: bool
    stop_timeline_presentation: bool
    clear_next_presentation: bool
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., icon: _Optional[str] = ..., tint: _Optional[_Union[_proApiV1Color_pb2.API_v1_Color, _Mapping]] = ..., layers: _Optional[_Iterable[_Union[API_v1_ClearGroup.API_v1_ClearGroupLayerType, str]]] = ..., stop_timeline_announcements: bool = ..., stop_timeline_presentation: bool = ..., clear_next_presentation: bool = ...) -> None: ...

class API_v1_Clear_Request(_message.Message):
    __slots__ = ("clear_layer", "create_group", "get_group", "put_group", "get_group_icon", "put_group_icon", "delete_group", "trigger_group", "get_groups")
    class ClearLayer(_message.Message):
        __slots__ = ("layer",)
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
            props: _ClassVar[API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
            messages: _ClassVar[API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
            slide: _ClassVar[API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
            media: _ClassVar[API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Clear_Request.ClearLayer.API_v1_LayerType]
        audio: API_v1_Clear_Request.ClearLayer.API_v1_LayerType
        props: API_v1_Clear_Request.ClearLayer.API_v1_LayerType
        messages: API_v1_Clear_Request.ClearLayer.API_v1_LayerType
        announcements: API_v1_Clear_Request.ClearLayer.API_v1_LayerType
        slide: API_v1_Clear_Request.ClearLayer.API_v1_LayerType
        media: API_v1_Clear_Request.ClearLayer.API_v1_LayerType
        video_input: API_v1_Clear_Request.ClearLayer.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Clear_Request.ClearLayer.API_v1_LayerType
        def __init__(self, layer: _Optional[_Union[API_v1_Clear_Request.ClearLayer.API_v1_LayerType, str]] = ...) -> None: ...
    class CreateGroup(_message.Message):
        __slots__ = ("group",)
        GROUP_FIELD_NUMBER: _ClassVar[int]
        group: API_v1_ClearGroup
        def __init__(self, group: _Optional[_Union[API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
    class GetGroup(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PutGroup(_message.Message):
        __slots__ = ("id", "group")
        ID_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        id: str
        group: API_v1_ClearGroup
        def __init__(self, id: _Optional[str] = ..., group: _Optional[_Union[API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
    class GetGroupIcon(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PutGroupIcon(_message.Message):
        __slots__ = ("id", "content_type", "icon")
        ID_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        id: str
        content_type: str
        icon: bytes
        def __init__(self, id: _Optional[str] = ..., content_type: _Optional[str] = ..., icon: _Optional[bytes] = ...) -> None: ...
    class DeleteGroup(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class TriggerGroup(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class GetGroups(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    CLEAR_LAYER_FIELD_NUMBER: _ClassVar[int]
    CREATE_GROUP_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_FIELD_NUMBER: _ClassVar[int]
    PUT_GROUP_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_ICON_FIELD_NUMBER: _ClassVar[int]
    PUT_GROUP_ICON_FIELD_NUMBER: _ClassVar[int]
    DELETE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_GROUP_FIELD_NUMBER: _ClassVar[int]
    GET_GROUPS_FIELD_NUMBER: _ClassVar[int]
    clear_layer: API_v1_Clear_Request.ClearLayer
    create_group: API_v1_Clear_Request.CreateGroup
    get_group: API_v1_Clear_Request.GetGroup
    put_group: API_v1_Clear_Request.PutGroup
    get_group_icon: API_v1_Clear_Request.GetGroupIcon
    put_group_icon: API_v1_Clear_Request.PutGroupIcon
    delete_group: API_v1_Clear_Request.DeleteGroup
    trigger_group: API_v1_Clear_Request.TriggerGroup
    get_groups: API_v1_Clear_Request.GetGroups
    def __init__(self, clear_layer: _Optional[_Union[API_v1_Clear_Request.ClearLayer, _Mapping]] = ..., create_group: _Optional[_Union[API_v1_Clear_Request.CreateGroup, _Mapping]] = ..., get_group: _Optional[_Union[API_v1_Clear_Request.GetGroup, _Mapping]] = ..., put_group: _Optional[_Union[API_v1_Clear_Request.PutGroup, _Mapping]] = ..., get_group_icon: _Optional[_Union[API_v1_Clear_Request.GetGroupIcon, _Mapping]] = ..., put_group_icon: _Optional[_Union[API_v1_Clear_Request.PutGroupIcon, _Mapping]] = ..., delete_group: _Optional[_Union[API_v1_Clear_Request.DeleteGroup, _Mapping]] = ..., trigger_group: _Optional[_Union[API_v1_Clear_Request.TriggerGroup, _Mapping]] = ..., get_groups: _Optional[_Union[API_v1_Clear_Request.GetGroups, _Mapping]] = ...) -> None: ...

class API_v1_Clear_Response(_message.Message):
    __slots__ = ("clear_layer", "create_group", "get_group", "put_group", "delete_group", "trigger_group", "get_groups", "get_group_icon", "put_group_icon")
    class ClearLayer(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PutGroup(_message.Message):
        __slots__ = ("group",)
        GROUP_FIELD_NUMBER: _ClassVar[int]
        group: API_v1_ClearGroup
        def __init__(self, group: _Optional[_Union[API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
    class DeleteGroup(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TriggerGroup(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CreateGroup(_message.Message):
        __slots__ = ("group",)
        GROUP_FIELD_NUMBER: _ClassVar[int]
        group: API_v1_ClearGroup
        def __init__(self, group: _Optional[_Union[API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
    class GetGroup(_message.Message):
        __slots__ = ("group",)
        GROUP_FIELD_NUMBER: _ClassVar[int]
        group: API_v1_ClearGroup
        def __init__(self, group: _Optional[_Union[API_v1_ClearGroup, _Mapping]] = ...) -> None: ...
    class GetGroups(_message.Message):
        __slots__ = ("groups",)
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        groups: _containers.RepeatedCompositeFieldContainer[API_v1_ClearGroup]
        def __init__(self, groups: _Optional[_Iterable[_Union[API_v1_ClearGroup, _Mapping]]] = ...) -> None: ...
    class GetGroupIcon(_message.Message):
        __slots__ = ("content_type", "icon")
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        ICON_FIELD_NUMBER: _ClassVar[int]
        content_type: str
        icon: bytes
        def __init__(self, content_type: _Optional[str] = ..., icon: _Optional[bytes] = ...) -> None: ...
    class PutGroupIcon(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    CLEAR_LAYER_FIELD_NUMBER: _ClassVar[int]
    CREATE_GROUP_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_FIELD_NUMBER: _ClassVar[int]
    PUT_GROUP_FIELD_NUMBER: _ClassVar[int]
    DELETE_GROUP_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_GROUP_FIELD_NUMBER: _ClassVar[int]
    GET_GROUPS_FIELD_NUMBER: _ClassVar[int]
    GET_GROUP_ICON_FIELD_NUMBER: _ClassVar[int]
    PUT_GROUP_ICON_FIELD_NUMBER: _ClassVar[int]
    clear_layer: API_v1_Clear_Response.ClearLayer
    create_group: API_v1_Clear_Response.CreateGroup
    get_group: API_v1_Clear_Response.GetGroup
    put_group: API_v1_Clear_Response.PutGroup
    delete_group: API_v1_Clear_Response.DeleteGroup
    trigger_group: API_v1_Clear_Response.TriggerGroup
    get_groups: API_v1_Clear_Response.GetGroups
    get_group_icon: API_v1_Clear_Response.GetGroupIcon
    put_group_icon: API_v1_Clear_Response.PutGroupIcon
    def __init__(self, clear_layer: _Optional[_Union[API_v1_Clear_Response.ClearLayer, _Mapping]] = ..., create_group: _Optional[_Union[API_v1_Clear_Response.CreateGroup, _Mapping]] = ..., get_group: _Optional[_Union[API_v1_Clear_Response.GetGroup, _Mapping]] = ..., put_group: _Optional[_Union[API_v1_Clear_Response.PutGroup, _Mapping]] = ..., delete_group: _Optional[_Union[API_v1_Clear_Response.DeleteGroup, _Mapping]] = ..., trigger_group: _Optional[_Union[API_v1_Clear_Response.TriggerGroup, _Mapping]] = ..., get_groups: _Optional[_Union[API_v1_Clear_Response.GetGroups, _Mapping]] = ..., get_group_icon: _Optional[_Union[API_v1_Clear_Response.GetGroupIcon, _Mapping]] = ..., put_group_icon: _Optional[_Union[API_v1_Clear_Response.PutGroupIcon, _Mapping]] = ...) -> None: ...
