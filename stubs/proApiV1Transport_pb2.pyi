import proApiV1LayerType_pb2 as _proApiV1LayerType_pb2
import uuid_pb2 as _uuid_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Transport_Request(_message.Message):
    __slots__ = ("play", "pause", "skip_backward", "skip_forward", "go_to_end", "get_time", "put_time", "get_auto_advance", "delete_auto_advance", "get_current_media")
    class Play(_message.Message):
        __slots__ = ("layer",)
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.Play.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.Play.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.Play.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.Play.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.Play.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.Play.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.Play.API_v1_LayerType]
        audio: API_v1_Transport_Request.Play.API_v1_LayerType
        props: API_v1_Transport_Request.Play.API_v1_LayerType
        messages: API_v1_Transport_Request.Play.API_v1_LayerType
        announcements: API_v1_Transport_Request.Play.API_v1_LayerType
        slide: API_v1_Transport_Request.Play.API_v1_LayerType
        media: API_v1_Transport_Request.Play.API_v1_LayerType
        video_input: API_v1_Transport_Request.Play.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.Play.API_v1_LayerType
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.Play.API_v1_LayerType, str]] = ...) -> None: ...
    class Pause(_message.Message):
        __slots__ = ("layer",)
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.Pause.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.Pause.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.Pause.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.Pause.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.Pause.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.Pause.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.Pause.API_v1_LayerType]
        audio: API_v1_Transport_Request.Pause.API_v1_LayerType
        props: API_v1_Transport_Request.Pause.API_v1_LayerType
        messages: API_v1_Transport_Request.Pause.API_v1_LayerType
        announcements: API_v1_Transport_Request.Pause.API_v1_LayerType
        slide: API_v1_Transport_Request.Pause.API_v1_LayerType
        media: API_v1_Transport_Request.Pause.API_v1_LayerType
        video_input: API_v1_Transport_Request.Pause.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.Pause.API_v1_LayerType
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.Pause.API_v1_LayerType, str]] = ...) -> None: ...
    class SkipBackward(_message.Message):
        __slots__ = ("layer", "seconds")
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.SkipBackward.API_v1_LayerType]
        audio: API_v1_Transport_Request.SkipBackward.API_v1_LayerType
        props: API_v1_Transport_Request.SkipBackward.API_v1_LayerType
        messages: API_v1_Transport_Request.SkipBackward.API_v1_LayerType
        announcements: API_v1_Transport_Request.SkipBackward.API_v1_LayerType
        slide: API_v1_Transport_Request.SkipBackward.API_v1_LayerType
        media: API_v1_Transport_Request.SkipBackward.API_v1_LayerType
        video_input: API_v1_Transport_Request.SkipBackward.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.SkipBackward.API_v1_LayerType
        seconds: float
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.SkipBackward.API_v1_LayerType, str]] = ..., seconds: _Optional[float] = ...) -> None: ...
    class SkipForward(_message.Message):
        __slots__ = ("layer", "seconds")
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.SkipForward.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.SkipForward.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.SkipForward.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.SkipForward.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.SkipForward.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.SkipForward.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.SkipForward.API_v1_LayerType]
        audio: API_v1_Transport_Request.SkipForward.API_v1_LayerType
        props: API_v1_Transport_Request.SkipForward.API_v1_LayerType
        messages: API_v1_Transport_Request.SkipForward.API_v1_LayerType
        announcements: API_v1_Transport_Request.SkipForward.API_v1_LayerType
        slide: API_v1_Transport_Request.SkipForward.API_v1_LayerType
        media: API_v1_Transport_Request.SkipForward.API_v1_LayerType
        video_input: API_v1_Transport_Request.SkipForward.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.SkipForward.API_v1_LayerType
        seconds: float
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.SkipForward.API_v1_LayerType, str]] = ..., seconds: _Optional[float] = ...) -> None: ...
    class GoToEnd(_message.Message):
        __slots__ = ("layer", "seconds")
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.GoToEnd.API_v1_LayerType]
        audio: API_v1_Transport_Request.GoToEnd.API_v1_LayerType
        props: API_v1_Transport_Request.GoToEnd.API_v1_LayerType
        messages: API_v1_Transport_Request.GoToEnd.API_v1_LayerType
        announcements: API_v1_Transport_Request.GoToEnd.API_v1_LayerType
        slide: API_v1_Transport_Request.GoToEnd.API_v1_LayerType
        media: API_v1_Transport_Request.GoToEnd.API_v1_LayerType
        video_input: API_v1_Transport_Request.GoToEnd.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.GoToEnd.API_v1_LayerType
        seconds: float
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.GoToEnd.API_v1_LayerType, str]] = ..., seconds: _Optional[float] = ...) -> None: ...
    class GetTime(_message.Message):
        __slots__ = ("layer",)
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.GetTime.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.GetTime.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.GetTime.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.GetTime.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.GetTime.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.GetTime.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.GetTime.API_v1_LayerType]
        audio: API_v1_Transport_Request.GetTime.API_v1_LayerType
        props: API_v1_Transport_Request.GetTime.API_v1_LayerType
        messages: API_v1_Transport_Request.GetTime.API_v1_LayerType
        announcements: API_v1_Transport_Request.GetTime.API_v1_LayerType
        slide: API_v1_Transport_Request.GetTime.API_v1_LayerType
        media: API_v1_Transport_Request.GetTime.API_v1_LayerType
        video_input: API_v1_Transport_Request.GetTime.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.GetTime.API_v1_LayerType
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.GetTime.API_v1_LayerType, str]] = ...) -> None: ...
    class PutTime(_message.Message):
        __slots__ = ("layer", "seconds")
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.PutTime.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.PutTime.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.PutTime.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.PutTime.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.PutTime.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.PutTime.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.PutTime.API_v1_LayerType]
        audio: API_v1_Transport_Request.PutTime.API_v1_LayerType
        props: API_v1_Transport_Request.PutTime.API_v1_LayerType
        messages: API_v1_Transport_Request.PutTime.API_v1_LayerType
        announcements: API_v1_Transport_Request.PutTime.API_v1_LayerType
        slide: API_v1_Transport_Request.PutTime.API_v1_LayerType
        media: API_v1_Transport_Request.PutTime.API_v1_LayerType
        video_input: API_v1_Transport_Request.PutTime.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.PutTime.API_v1_LayerType
        seconds: float
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.PutTime.API_v1_LayerType, str]] = ..., seconds: _Optional[float] = ...) -> None: ...
    class GetAutoAdvance(_message.Message):
        __slots__ = ("layer",)
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType]
        audio: API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
        props: API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
        messages: API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
        announcements: API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
        slide: API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
        media: API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
        video_input: API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.GetAutoAdvance.API_v1_LayerType, str]] = ...) -> None: ...
    class DeleteAutoAdvance(_message.Message):
        __slots__ = ("layer",)
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType]
        audio: API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
        props: API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
        messages: API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
        announcements: API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
        slide: API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
        media: API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
        video_input: API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.DeleteAutoAdvance.API_v1_LayerType, str]] = ...) -> None: ...
    class GetCurrentMedia(_message.Message):
        __slots__ = ("layer",)
        class API_v1_LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            audio: _ClassVar[API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
            props: _ClassVar[API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
            messages: _ClassVar[API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
            announcements: _ClassVar[API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
            slide: _ClassVar[API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
            media: _ClassVar[API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
            video_input: _ClassVar[API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType]
        audio: API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
        props: API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
        messages: API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
        announcements: API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
        slide: API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
        media: API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
        video_input: API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
        LAYER_FIELD_NUMBER: _ClassVar[int]
        layer: API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType
        def __init__(self, layer: _Optional[_Union[API_v1_Transport_Request.GetCurrentMedia.API_v1_LayerType, str]] = ...) -> None: ...
    PLAY_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    SKIP_BACKWARD_FIELD_NUMBER: _ClassVar[int]
    SKIP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    GO_TO_END_FIELD_NUMBER: _ClassVar[int]
    GET_TIME_FIELD_NUMBER: _ClassVar[int]
    PUT_TIME_FIELD_NUMBER: _ClassVar[int]
    GET_AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
    DELETE_AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
    GET_CURRENT_MEDIA_FIELD_NUMBER: _ClassVar[int]
    play: API_v1_Transport_Request.Play
    pause: API_v1_Transport_Request.Pause
    skip_backward: API_v1_Transport_Request.SkipBackward
    skip_forward: API_v1_Transport_Request.SkipForward
    go_to_end: API_v1_Transport_Request.GoToEnd
    get_time: API_v1_Transport_Request.GetTime
    put_time: API_v1_Transport_Request.PutTime
    get_auto_advance: API_v1_Transport_Request.GetAutoAdvance
    delete_auto_advance: API_v1_Transport_Request.DeleteAutoAdvance
    get_current_media: API_v1_Transport_Request.GetCurrentMedia
    def __init__(self, play: _Optional[_Union[API_v1_Transport_Request.Play, _Mapping]] = ..., pause: _Optional[_Union[API_v1_Transport_Request.Pause, _Mapping]] = ..., skip_backward: _Optional[_Union[API_v1_Transport_Request.SkipBackward, _Mapping]] = ..., skip_forward: _Optional[_Union[API_v1_Transport_Request.SkipForward, _Mapping]] = ..., go_to_end: _Optional[_Union[API_v1_Transport_Request.GoToEnd, _Mapping]] = ..., get_time: _Optional[_Union[API_v1_Transport_Request.GetTime, _Mapping]] = ..., put_time: _Optional[_Union[API_v1_Transport_Request.PutTime, _Mapping]] = ..., get_auto_advance: _Optional[_Union[API_v1_Transport_Request.GetAutoAdvance, _Mapping]] = ..., delete_auto_advance: _Optional[_Union[API_v1_Transport_Request.DeleteAutoAdvance, _Mapping]] = ..., get_current_media: _Optional[_Union[API_v1_Transport_Request.GetCurrentMedia, _Mapping]] = ...) -> None: ...

class API_v1_Transport_Response(_message.Message):
    __slots__ = ("play", "pause", "skip_backward", "skip_forward", "go_to_end", "get_time", "put_time", "get_auto_advance", "delete_auto_advance", "get_current_media")
    class Play(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Pause(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SkipBackward(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SkipForward(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GoToEnd(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetTime(_message.Message):
        __slots__ = ("seconds",)
        SECONDS_FIELD_NUMBER: _ClassVar[int]
        seconds: float
        def __init__(self, seconds: _Optional[float] = ...) -> None: ...
    class PutTime(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetAutoAdvance(_message.Message):
        __slots__ = ("auto_advance",)
        AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
        auto_advance: bool
        def __init__(self, auto_advance: bool = ...) -> None: ...
    class DeleteAutoAdvance(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetCurrentMedia(_message.Message):
        __slots__ = ("is_playing", "uuid", "name", "artist", "audio_only", "duration")
        IS_PLAYING_FIELD_NUMBER: _ClassVar[int]
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ARTIST_FIELD_NUMBER: _ClassVar[int]
        AUDIO_ONLY_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        is_playing: bool
        uuid: _uuid_pb2.UUID
        name: str
        artist: str
        audio_only: bool
        duration: float
        def __init__(self, is_playing: bool = ..., uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., artist: _Optional[str] = ..., audio_only: bool = ..., duration: _Optional[float] = ...) -> None: ...
    PLAY_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    SKIP_BACKWARD_FIELD_NUMBER: _ClassVar[int]
    SKIP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    GO_TO_END_FIELD_NUMBER: _ClassVar[int]
    GET_TIME_FIELD_NUMBER: _ClassVar[int]
    PUT_TIME_FIELD_NUMBER: _ClassVar[int]
    GET_AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
    DELETE_AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
    GET_CURRENT_MEDIA_FIELD_NUMBER: _ClassVar[int]
    play: API_v1_Transport_Response.Play
    pause: API_v1_Transport_Response.Pause
    skip_backward: API_v1_Transport_Response.SkipBackward
    skip_forward: API_v1_Transport_Response.SkipForward
    go_to_end: API_v1_Transport_Response.GoToEnd
    get_time: API_v1_Transport_Response.GetTime
    put_time: API_v1_Transport_Response.PutTime
    get_auto_advance: API_v1_Transport_Response.GetAutoAdvance
    delete_auto_advance: API_v1_Transport_Response.DeleteAutoAdvance
    get_current_media: API_v1_Transport_Response.GetCurrentMedia
    def __init__(self, play: _Optional[_Union[API_v1_Transport_Response.Play, _Mapping]] = ..., pause: _Optional[_Union[API_v1_Transport_Response.Pause, _Mapping]] = ..., skip_backward: _Optional[_Union[API_v1_Transport_Response.SkipBackward, _Mapping]] = ..., skip_forward: _Optional[_Union[API_v1_Transport_Response.SkipForward, _Mapping]] = ..., go_to_end: _Optional[_Union[API_v1_Transport_Response.GoToEnd, _Mapping]] = ..., get_time: _Optional[_Union[API_v1_Transport_Response.GetTime, _Mapping]] = ..., put_time: _Optional[_Union[API_v1_Transport_Response.PutTime, _Mapping]] = ..., get_auto_advance: _Optional[_Union[API_v1_Transport_Response.GetAutoAdvance, _Mapping]] = ..., delete_auto_advance: _Optional[_Union[API_v1_Transport_Response.DeleteAutoAdvance, _Mapping]] = ..., get_current_media: _Optional[_Union[API_v1_Transport_Response.GetCurrentMedia, _Mapping]] = ...) -> None: ...
