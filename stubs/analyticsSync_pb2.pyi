from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Sync(_message.Message):
    __slots__ = ("local",)
    class Local(_message.Message):
        __slots__ = ("sync_type", "include_library", "include_media", "include_playlists", "include_themes", "include_support_files", "replace_files")
        class SyncType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SYNC_TYPE_UP: _ClassVar[Sync.Local.SyncType]
            SYNC_TYPE_DOWN: _ClassVar[Sync.Local.SyncType]
        SYNC_TYPE_UP: Sync.Local.SyncType
        SYNC_TYPE_DOWN: Sync.Local.SyncType
        SYNC_TYPE_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_LIBRARY_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_MEDIA_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_PLAYLISTS_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_THEMES_FIELD_NUMBER: _ClassVar[int]
        INCLUDE_SUPPORT_FILES_FIELD_NUMBER: _ClassVar[int]
        REPLACE_FILES_FIELD_NUMBER: _ClassVar[int]
        sync_type: Sync.Local.SyncType
        include_library: bool
        include_media: bool
        include_playlists: bool
        include_themes: bool
        include_support_files: bool
        replace_files: bool
        def __init__(self, sync_type: _Optional[_Union[Sync.Local.SyncType, str]] = ..., include_library: bool = ..., include_media: bool = ..., include_playlists: bool = ..., include_themes: bool = ..., include_support_files: bool = ..., replace_files: bool = ...) -> None: ...
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    local: Sync.Local
    def __init__(self, local: _Optional[_Union[Sync.Local, _Mapping]] = ...) -> None: ...
