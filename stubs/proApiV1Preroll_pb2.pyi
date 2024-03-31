import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Preroll_Request(_message.Message):
    __slots__ = ("preroll_cue", "preroll_playlist_item", "preroll_media_item", "preroll_audio_item", "preroll_video_input", "preroll_library_item", "preroll_next", "preroll_previous", "activate_preroll_item", "cancel_preroll_item")
    class PrerollCue(_message.Message):
        __slots__ = ("index", "preroll_id")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
        index: int
        preroll_id: int
        def __init__(self, index: _Optional[int] = ..., preroll_id: _Optional[int] = ...) -> None: ...
    class PrerollPlaylistItem(_message.Message):
        __slots__ = ("path", "preroll_id")
        PATH_FIELD_NUMBER: _ClassVar[int]
        PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        preroll_id: int
        def __init__(self, path: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ..., preroll_id: _Optional[int] = ...) -> None: ...
    class PrerollMediaItem(_message.Message):
        __slots__ = ("path", "preroll_id")
        PATH_FIELD_NUMBER: _ClassVar[int]
        PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        preroll_id: int
        def __init__(self, path: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ..., preroll_id: _Optional[int] = ...) -> None: ...
    class PrerollAudioItem(_message.Message):
        __slots__ = ("path", "preroll_id")
        PATH_FIELD_NUMBER: _ClassVar[int]
        PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        preroll_id: int
        def __init__(self, path: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ..., preroll_id: _Optional[int] = ...) -> None: ...
    class PrerollVideoInput(_message.Message):
        __slots__ = ("id", "preroll_id")
        ID_FIELD_NUMBER: _ClassVar[int]
        PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        preroll_id: int
        def __init__(self, id: _Optional[str] = ..., preroll_id: _Optional[int] = ...) -> None: ...
    class PrerollLibraryItem(_message.Message):
        __slots__ = ("path", "preroll_id")
        PATH_FIELD_NUMBER: _ClassVar[int]
        PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
        path: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        preroll_id: int
        def __init__(self, path: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ..., preroll_id: _Optional[int] = ...) -> None: ...
    class PrerollNext(_message.Message):
        __slots__ = ("preroll_id",)
        PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
        preroll_id: int
        def __init__(self, preroll_id: _Optional[int] = ...) -> None: ...
    class PrerollPrevious(_message.Message):
        __slots__ = ("preroll_id",)
        PREROLL_ID_FIELD_NUMBER: _ClassVar[int]
        preroll_id: int
        def __init__(self, preroll_id: _Optional[int] = ...) -> None: ...
    class ActivatePrerollItem(_message.Message):
        __slots__ = ("id", "time")
        ID_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        id: int
        time: int
        def __init__(self, id: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...
    class CancelPrerollItem(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: int
        def __init__(self, id: _Optional[int] = ...) -> None: ...
    PREROLL_CUE_FIELD_NUMBER: _ClassVar[int]
    PREROLL_PLAYLIST_ITEM_FIELD_NUMBER: _ClassVar[int]
    PREROLL_MEDIA_ITEM_FIELD_NUMBER: _ClassVar[int]
    PREROLL_AUDIO_ITEM_FIELD_NUMBER: _ClassVar[int]
    PREROLL_VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
    PREROLL_LIBRARY_ITEM_FIELD_NUMBER: _ClassVar[int]
    PREROLL_NEXT_FIELD_NUMBER: _ClassVar[int]
    PREROLL_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_PREROLL_ITEM_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PREROLL_ITEM_FIELD_NUMBER: _ClassVar[int]
    preroll_cue: API_v1_Preroll_Request.PrerollCue
    preroll_playlist_item: API_v1_Preroll_Request.PrerollPlaylistItem
    preroll_media_item: API_v1_Preroll_Request.PrerollMediaItem
    preroll_audio_item: API_v1_Preroll_Request.PrerollAudioItem
    preroll_video_input: API_v1_Preroll_Request.PrerollVideoInput
    preroll_library_item: API_v1_Preroll_Request.PrerollLibraryItem
    preroll_next: API_v1_Preroll_Request.PrerollNext
    preroll_previous: API_v1_Preroll_Request.PrerollPrevious
    activate_preroll_item: API_v1_Preroll_Request.ActivatePrerollItem
    cancel_preroll_item: API_v1_Preroll_Request.CancelPrerollItem
    def __init__(self, preroll_cue: _Optional[_Union[API_v1_Preroll_Request.PrerollCue, _Mapping]] = ..., preroll_playlist_item: _Optional[_Union[API_v1_Preroll_Request.PrerollPlaylistItem, _Mapping]] = ..., preroll_media_item: _Optional[_Union[API_v1_Preroll_Request.PrerollMediaItem, _Mapping]] = ..., preroll_audio_item: _Optional[_Union[API_v1_Preroll_Request.PrerollAudioItem, _Mapping]] = ..., preroll_video_input: _Optional[_Union[API_v1_Preroll_Request.PrerollVideoInput, _Mapping]] = ..., preroll_library_item: _Optional[_Union[API_v1_Preroll_Request.PrerollLibraryItem, _Mapping]] = ..., preroll_next: _Optional[_Union[API_v1_Preroll_Request.PrerollNext, _Mapping]] = ..., preroll_previous: _Optional[_Union[API_v1_Preroll_Request.PrerollPrevious, _Mapping]] = ..., activate_preroll_item: _Optional[_Union[API_v1_Preroll_Request.ActivatePrerollItem, _Mapping]] = ..., cancel_preroll_item: _Optional[_Union[API_v1_Preroll_Request.CancelPrerollItem, _Mapping]] = ...) -> None: ...

class API_v1_Preroll_Response(_message.Message):
    __slots__ = ("preroll_ready", "activate_preroll_item", "cancel_preroll_item")
    class PrerollReady(_message.Message):
        __slots__ = ("id", "latency", "time")
        ID_FIELD_NUMBER: _ClassVar[int]
        LATENCY_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        id: int
        latency: int
        time: int
        def __init__(self, id: _Optional[int] = ..., latency: _Optional[int] = ..., time: _Optional[int] = ...) -> None: ...
    class ActivatePrerollItem(_message.Message):
        __slots__ = ("success",)
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        success: bool
        def __init__(self, success: bool = ...) -> None: ...
    class CancelPrerollItem(_message.Message):
        __slots__ = ("success",)
        SUCCESS_FIELD_NUMBER: _ClassVar[int]
        success: bool
        def __init__(self, success: bool = ...) -> None: ...
    PREROLL_READY_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_PREROLL_ITEM_FIELD_NUMBER: _ClassVar[int]
    CANCEL_PREROLL_ITEM_FIELD_NUMBER: _ClassVar[int]
    preroll_ready: API_v1_Preroll_Response.PrerollReady
    activate_preroll_item: API_v1_Preroll_Response.ActivatePrerollItem
    cancel_preroll_item: API_v1_Preroll_Response.CancelPrerollItem
    def __init__(self, preroll_ready: _Optional[_Union[API_v1_Preroll_Response.PrerollReady, _Mapping]] = ..., activate_preroll_item: _Optional[_Union[API_v1_Preroll_Response.ActivatePrerollItem, _Mapping]] = ..., cancel_preroll_item: _Optional[_Union[API_v1_Preroll_Response.CancelPrerollItem, _Mapping]] = ...) -> None: ...
