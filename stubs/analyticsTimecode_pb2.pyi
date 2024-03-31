from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Timecode(_message.Message):
    __slots__ = ("startup", "activate")
    class Startup(_message.Message):
        __slots__ = ("is_input_configured", "is_enabled", "is_playlist_selected")
        IS_INPUT_CONFIGURED_FIELD_NUMBER: _ClassVar[int]
        IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
        IS_PLAYLIST_SELECTED_FIELD_NUMBER: _ClassVar[int]
        is_input_configured: bool
        is_enabled: bool
        is_playlist_selected: bool
        def __init__(self, is_input_configured: bool = ..., is_enabled: bool = ..., is_playlist_selected: bool = ...) -> None: ...
    class Activate(_message.Message):
        __slots__ = ("playlist_item_count", "cue_count", "is_startup")
        PLAYLIST_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
        CUE_COUNT_FIELD_NUMBER: _ClassVar[int]
        IS_STARTUP_FIELD_NUMBER: _ClassVar[int]
        playlist_item_count: int
        cue_count: int
        is_startup: bool
        def __init__(self, playlist_item_count: _Optional[int] = ..., cue_count: _Optional[int] = ..., is_startup: bool = ...) -> None: ...
    STARTUP_FIELD_NUMBER: _ClassVar[int]
    ACTIVATE_FIELD_NUMBER: _ClassVar[int]
    startup: Timecode.Startup
    activate: Timecode.Activate
    def __init__(self, startup: _Optional[_Union[Timecode.Startup, _Mapping]] = ..., activate: _Optional[_Union[Timecode.Activate, _Mapping]] = ...) -> None: ...
