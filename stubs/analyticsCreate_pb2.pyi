from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Create(_message.Message):
    __slots__ = ("library", "playlist", "presentation", "template_playlist")
    class Library(_message.Message):
        __slots__ = ("source",)
        class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOURCE_UNKNOWN: _ClassVar[Create.Library.Source]
            SOURCE_APPLICATION_MENU: _ClassVar[Create.Library.Source]
            SOURCE_LIBRARY_OUTLINE_ADD_BUTTON: _ClassVar[Create.Library.Source]
        SOURCE_UNKNOWN: Create.Library.Source
        SOURCE_APPLICATION_MENU: Create.Library.Source
        SOURCE_LIBRARY_OUTLINE_ADD_BUTTON: Create.Library.Source
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        source: Create.Library.Source
        def __init__(self, source: _Optional[_Union[Create.Library.Source, str]] = ...) -> None: ...
    class Playlist(_message.Message):
        __slots__ = ("source", "type")
        class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOURCE_UNKNOWN: _ClassVar[Create.Playlist.Source]
            SOURCE_APPLICATION_MENU: _ClassVar[Create.Playlist.Source]
            SOURCE_LIBRARY_OUTLINE_ADD_BUTTON: _ClassVar[Create.Playlist.Source]
        SOURCE_UNKNOWN: Create.Playlist.Source
        SOURCE_APPLICATION_MENU: Create.Playlist.Source
        SOURCE_LIBRARY_OUTLINE_ADD_BUTTON: Create.Playlist.Source
        class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TYPE_UNKNOWN: _ClassVar[Create.Playlist.Type]
            TYPE_PRESENTATION: _ClassVar[Create.Playlist.Type]
            TYPE_PLANNING_CENTER: _ClassVar[Create.Playlist.Type]
            TYPE_FOLDER: _ClassVar[Create.Playlist.Type]
            TYPE_TEMPLATE_PLAYLIST: _ClassVar[Create.Playlist.Type]
        TYPE_UNKNOWN: Create.Playlist.Type
        TYPE_PRESENTATION: Create.Playlist.Type
        TYPE_PLANNING_CENTER: Create.Playlist.Type
        TYPE_FOLDER: Create.Playlist.Type
        TYPE_TEMPLATE_PLAYLIST: Create.Playlist.Type
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        source: Create.Playlist.Source
        type: Create.Playlist.Type
        def __init__(self, source: _Optional[_Union[Create.Playlist.Source, str]] = ..., type: _Optional[_Union[Create.Playlist.Type, str]] = ...) -> None: ...
    class Presentation(_message.Message):
        __slots__ = ("source",)
        class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SOURCE_UNKNOWN: _ClassVar[Create.Presentation.Source]
            SOURCE_APPLICATION_MENU: _ClassVar[Create.Presentation.Source]
            SOURCE_LIBRARY_OUTLINE_ADD_BUTTON: _ClassVar[Create.Presentation.Source]
            SOURCE_DETAIL_ADD_BUTTON: _ClassVar[Create.Presentation.Source]
            SOURCE_UNLINKED_HEADER: _ClassVar[Create.Presentation.Source]
        SOURCE_UNKNOWN: Create.Presentation.Source
        SOURCE_APPLICATION_MENU: Create.Presentation.Source
        SOURCE_LIBRARY_OUTLINE_ADD_BUTTON: Create.Presentation.Source
        SOURCE_DETAIL_ADD_BUTTON: Create.Presentation.Source
        SOURCE_UNLINKED_HEADER: Create.Presentation.Source
        SOURCE_FIELD_NUMBER: _ClassVar[int]
        source: Create.Presentation.Source
        def __init__(self, source: _Optional[_Union[Create.Presentation.Source, str]] = ...) -> None: ...
    class TemplatePlaylist(_message.Message):
        __slots__ = ("total_item_count", "header_count", "placeholder_count", "presentation_count", "media_count")
        TOTAL_ITEM_COUNT_FIELD_NUMBER: _ClassVar[int]
        HEADER_COUNT_FIELD_NUMBER: _ClassVar[int]
        PLACEHOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_COUNT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_COUNT_FIELD_NUMBER: _ClassVar[int]
        total_item_count: int
        header_count: int
        placeholder_count: int
        presentation_count: int
        media_count: int
        def __init__(self, total_item_count: _Optional[int] = ..., header_count: _Optional[int] = ..., placeholder_count: _Optional[int] = ..., presentation_count: _Optional[int] = ..., media_count: _Optional[int] = ...) -> None: ...
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    TEMPLATE_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    library: Create.Library
    playlist: Create.Playlist
    presentation: Create.Presentation
    template_playlist: Create.TemplatePlaylist
    def __init__(self, library: _Optional[_Union[Create.Library, _Mapping]] = ..., playlist: _Optional[_Union[Create.Playlist, _Mapping]] = ..., presentation: _Optional[_Union[Create.Presentation, _Mapping]] = ..., template_playlist: _Optional[_Union[Create.TemplatePlaylist, _Mapping]] = ...) -> None: ...
