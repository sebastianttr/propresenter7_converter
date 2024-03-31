import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
import proApiV1Size_pb2 as _proApiV1Size_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_SlideDisplayDetails(_message.Message):
    __slots__ = ("text", "notes", "uuid")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    NOTES_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    text: str
    notes: str
    uuid: str
    def __init__(self, text: _Optional[str] = ..., notes: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class API_v1_ScreenConfig(_message.Message):
    __slots__ = ("id", "size", "screen_type")
    class API_v1_ScreenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        audience: _ClassVar[API_v1_ScreenConfig.API_v1_ScreenType]
        stage: _ClassVar[API_v1_ScreenConfig.API_v1_ScreenType]
    audience: API_v1_ScreenConfig.API_v1_ScreenType
    stage: API_v1_ScreenConfig.API_v1_ScreenType
    ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    SCREEN_TYPE_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    size: _proApiV1Size_pb2.API_v1_Size
    screen_type: API_v1_ScreenConfig.API_v1_ScreenType
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., size: _Optional[_Union[_proApiV1Size_pb2.API_v1_Size, _Mapping]] = ..., screen_type: _Optional[_Union[API_v1_ScreenConfig.API_v1_ScreenType, str]] = ...) -> None: ...

class API_v1_Status_Request(_message.Message):
    __slots__ = ("get_layers", "get_stage_screens", "put_stage_screens", "get_audience_screens", "put_audience_screens", "get_screens", "get_slide")
    class GetLayers(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetStageScreens(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PutStageScreens(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class GetAudienceScreens(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PutAudienceScreens(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class GetScreens(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetSlide(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    GET_LAYERS_FIELD_NUMBER: _ClassVar[int]
    GET_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
    PUT_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
    GET_AUDIENCE_SCREENS_FIELD_NUMBER: _ClassVar[int]
    PUT_AUDIENCE_SCREENS_FIELD_NUMBER: _ClassVar[int]
    GET_SCREENS_FIELD_NUMBER: _ClassVar[int]
    GET_SLIDE_FIELD_NUMBER: _ClassVar[int]
    get_layers: API_v1_Status_Request.GetLayers
    get_stage_screens: API_v1_Status_Request.GetStageScreens
    put_stage_screens: API_v1_Status_Request.PutStageScreens
    get_audience_screens: API_v1_Status_Request.GetAudienceScreens
    put_audience_screens: API_v1_Status_Request.PutAudienceScreens
    get_screens: API_v1_Status_Request.GetScreens
    get_slide: API_v1_Status_Request.GetSlide
    def __init__(self, get_layers: _Optional[_Union[API_v1_Status_Request.GetLayers, _Mapping]] = ..., get_stage_screens: _Optional[_Union[API_v1_Status_Request.GetStageScreens, _Mapping]] = ..., put_stage_screens: _Optional[_Union[API_v1_Status_Request.PutStageScreens, _Mapping]] = ..., get_audience_screens: _Optional[_Union[API_v1_Status_Request.GetAudienceScreens, _Mapping]] = ..., put_audience_screens: _Optional[_Union[API_v1_Status_Request.PutAudienceScreens, _Mapping]] = ..., get_screens: _Optional[_Union[API_v1_Status_Request.GetScreens, _Mapping]] = ..., get_slide: _Optional[_Union[API_v1_Status_Request.GetSlide, _Mapping]] = ...) -> None: ...

class API_v1_Status_Response(_message.Message):
    __slots__ = ("get_layers", "get_stage_screens", "put_stage_screens", "get_audience_screens", "put_audience_screens", "get_screens", "get_slide")
    class GetLayers(_message.Message):
        __slots__ = ("video_input", "media", "slide", "announcements", "props", "messages", "audio")
        VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        SLIDE_FIELD_NUMBER: _ClassVar[int]
        ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
        PROPS_FIELD_NUMBER: _ClassVar[int]
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        AUDIO_FIELD_NUMBER: _ClassVar[int]
        video_input: bool
        media: bool
        slide: bool
        announcements: bool
        props: bool
        messages: bool
        audio: bool
        def __init__(self, video_input: bool = ..., media: bool = ..., slide: bool = ..., announcements: bool = ..., props: bool = ..., messages: bool = ..., audio: bool = ...) -> None: ...
    class GetStageScreens(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class PutStageScreens(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetAudienceScreens(_message.Message):
        __slots__ = ("enabled",)
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        def __init__(self, enabled: bool = ...) -> None: ...
    class PutAudienceScreens(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetScreens(_message.Message):
        __slots__ = ("screens",)
        SCREENS_FIELD_NUMBER: _ClassVar[int]
        screens: _containers.RepeatedCompositeFieldContainer[API_v1_ScreenConfig]
        def __init__(self, screens: _Optional[_Iterable[_Union[API_v1_ScreenConfig, _Mapping]]] = ...) -> None: ...
    class GetSlide(_message.Message):
        __slots__ = ("current", "next")
        CURRENT_FIELD_NUMBER: _ClassVar[int]
        NEXT_FIELD_NUMBER: _ClassVar[int]
        current: API_v1_SlideDisplayDetails
        next: API_v1_SlideDisplayDetails
        def __init__(self, current: _Optional[_Union[API_v1_SlideDisplayDetails, _Mapping]] = ..., next: _Optional[_Union[API_v1_SlideDisplayDetails, _Mapping]] = ...) -> None: ...
    GET_LAYERS_FIELD_NUMBER: _ClassVar[int]
    GET_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
    PUT_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
    GET_AUDIENCE_SCREENS_FIELD_NUMBER: _ClassVar[int]
    PUT_AUDIENCE_SCREENS_FIELD_NUMBER: _ClassVar[int]
    GET_SCREENS_FIELD_NUMBER: _ClassVar[int]
    GET_SLIDE_FIELD_NUMBER: _ClassVar[int]
    get_layers: API_v1_Status_Response.GetLayers
    get_stage_screens: API_v1_Status_Response.GetStageScreens
    put_stage_screens: API_v1_Status_Response.PutStageScreens
    get_audience_screens: API_v1_Status_Response.GetAudienceScreens
    put_audience_screens: API_v1_Status_Response.PutAudienceScreens
    get_screens: API_v1_Status_Response.GetScreens
    get_slide: API_v1_Status_Response.GetSlide
    def __init__(self, get_layers: _Optional[_Union[API_v1_Status_Response.GetLayers, _Mapping]] = ..., get_stage_screens: _Optional[_Union[API_v1_Status_Response.GetStageScreens, _Mapping]] = ..., put_stage_screens: _Optional[_Union[API_v1_Status_Response.PutStageScreens, _Mapping]] = ..., get_audience_screens: _Optional[_Union[API_v1_Status_Response.GetAudienceScreens, _Mapping]] = ..., put_audience_screens: _Optional[_Union[API_v1_Status_Response.PutAudienceScreens, _Mapping]] = ..., get_screens: _Optional[_Union[API_v1_Status_Response.GetScreens, _Mapping]] = ..., get_slide: _Optional[_Union[API_v1_Status_Response.GetSlide, _Mapping]] = ...) -> None: ...
