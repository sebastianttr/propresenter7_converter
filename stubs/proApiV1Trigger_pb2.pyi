from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Trigger_Request(_message.Message):
    __slots__ = ("cue", "playlist", "media", "audio", "video_input", "library", "next", "previous", "media_next", "media_previous", "audio_next", "audio_previous")
    class Cue(_message.Message):
        __slots__ = ("index",)
        INDEX_FIELD_NUMBER: _ClassVar[int]
        index: int
        def __init__(self, index: _Optional[int] = ...) -> None: ...
    class Playlist(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Media(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class MediaNext(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MediaPrevious(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Audio(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class AudioNext(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AudioPrevious(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class VideoInput(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Library(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Next(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Previous(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    CUE_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    MEDIA_NEXT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_NEXT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    cue: API_v1_Trigger_Request.Cue
    playlist: API_v1_Trigger_Request.Playlist
    media: API_v1_Trigger_Request.Media
    audio: API_v1_Trigger_Request.Audio
    video_input: API_v1_Trigger_Request.VideoInput
    library: API_v1_Trigger_Request.Library
    next: API_v1_Trigger_Request.Next
    previous: API_v1_Trigger_Request.Previous
    media_next: API_v1_Trigger_Request.MediaNext
    media_previous: API_v1_Trigger_Request.MediaPrevious
    audio_next: API_v1_Trigger_Request.AudioNext
    audio_previous: API_v1_Trigger_Request.AudioPrevious
    def __init__(self, cue: _Optional[_Union[API_v1_Trigger_Request.Cue, _Mapping]] = ..., playlist: _Optional[_Union[API_v1_Trigger_Request.Playlist, _Mapping]] = ..., media: _Optional[_Union[API_v1_Trigger_Request.Media, _Mapping]] = ..., audio: _Optional[_Union[API_v1_Trigger_Request.Audio, _Mapping]] = ..., video_input: _Optional[_Union[API_v1_Trigger_Request.VideoInput, _Mapping]] = ..., library: _Optional[_Union[API_v1_Trigger_Request.Library, _Mapping]] = ..., next: _Optional[_Union[API_v1_Trigger_Request.Next, _Mapping]] = ..., previous: _Optional[_Union[API_v1_Trigger_Request.Previous, _Mapping]] = ..., media_next: _Optional[_Union[API_v1_Trigger_Request.MediaNext, _Mapping]] = ..., media_previous: _Optional[_Union[API_v1_Trigger_Request.MediaPrevious, _Mapping]] = ..., audio_next: _Optional[_Union[API_v1_Trigger_Request.AudioNext, _Mapping]] = ..., audio_previous: _Optional[_Union[API_v1_Trigger_Request.AudioPrevious, _Mapping]] = ...) -> None: ...

class API_v1_Trigger_Response(_message.Message):
    __slots__ = ("cue", "playlist", "media", "audio", "video_input", "library", "next", "previous", "media_next", "media_previous", "audio_next", "audio_previous")
    class Cue(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Playlist(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Media(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MediaNext(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class MediaPrevious(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Audio(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AudioNext(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AudioPrevious(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class VideoInput(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Library(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Next(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Previous(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    CUE_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    MEDIA_NEXT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    AUDIO_NEXT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
    cue: API_v1_Trigger_Response.Cue
    playlist: API_v1_Trigger_Response.Playlist
    media: API_v1_Trigger_Response.Media
    audio: API_v1_Trigger_Response.Audio
    video_input: API_v1_Trigger_Response.VideoInput
    library: API_v1_Trigger_Response.Library
    next: API_v1_Trigger_Response.Next
    previous: API_v1_Trigger_Response.Previous
    media_next: API_v1_Trigger_Response.MediaNext
    media_previous: API_v1_Trigger_Response.MediaPrevious
    audio_next: API_v1_Trigger_Response.AudioNext
    audio_previous: API_v1_Trigger_Response.AudioPrevious
    def __init__(self, cue: _Optional[_Union[API_v1_Trigger_Response.Cue, _Mapping]] = ..., playlist: _Optional[_Union[API_v1_Trigger_Response.Playlist, _Mapping]] = ..., media: _Optional[_Union[API_v1_Trigger_Response.Media, _Mapping]] = ..., audio: _Optional[_Union[API_v1_Trigger_Response.Audio, _Mapping]] = ..., video_input: _Optional[_Union[API_v1_Trigger_Response.VideoInput, _Mapping]] = ..., library: _Optional[_Union[API_v1_Trigger_Response.Library, _Mapping]] = ..., next: _Optional[_Union[API_v1_Trigger_Response.Next, _Mapping]] = ..., previous: _Optional[_Union[API_v1_Trigger_Response.Previous, _Mapping]] = ..., media_next: _Optional[_Union[API_v1_Trigger_Response.MediaNext, _Mapping]] = ..., media_previous: _Optional[_Union[API_v1_Trigger_Response.MediaPrevious, _Mapping]] = ..., audio_next: _Optional[_Union[API_v1_Trigger_Response.AudioNext, _Mapping]] = ..., audio_previous: _Optional[_Union[API_v1_Trigger_Response.AudioPrevious, _Mapping]] = ...) -> None: ...
