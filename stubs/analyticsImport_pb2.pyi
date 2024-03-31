import analyticsMultiTracks_pb2 as _analyticsMultiTracks_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Import(_message.Message):
    __slots__ = ("song_select", "multitracks")
    class SongSelect(_message.Message):
        __slots__ = ("template_slide_text_element_count", "import_into_playlist", "line_delimiter", "line_delimiter_count", "did_open_edit_view")
        class LineDelimiter(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LINE_DELIMITER_UNKNOWN: _ClassVar[Import.SongSelect.LineDelimiter]
            LINE_DELIMITER_LINE_BREAK: _ClassVar[Import.SongSelect.LineDelimiter]
            LINE_DELIMITER_PARAGRAPH_BREAK: _ClassVar[Import.SongSelect.LineDelimiter]
        LINE_DELIMITER_UNKNOWN: Import.SongSelect.LineDelimiter
        LINE_DELIMITER_LINE_BREAK: Import.SongSelect.LineDelimiter
        LINE_DELIMITER_PARAGRAPH_BREAK: Import.SongSelect.LineDelimiter
        TEMPLATE_SLIDE_TEXT_ELEMENT_COUNT_FIELD_NUMBER: _ClassVar[int]
        IMPORT_INTO_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        LINE_DELIMITER_FIELD_NUMBER: _ClassVar[int]
        LINE_DELIMITER_COUNT_FIELD_NUMBER: _ClassVar[int]
        DID_OPEN_EDIT_VIEW_FIELD_NUMBER: _ClassVar[int]
        template_slide_text_element_count: int
        import_into_playlist: bool
        line_delimiter: Import.SongSelect.LineDelimiter
        line_delimiter_count: int
        did_open_edit_view: bool
        def __init__(self, template_slide_text_element_count: _Optional[int] = ..., import_into_playlist: bool = ..., line_delimiter: _Optional[_Union[Import.SongSelect.LineDelimiter, str]] = ..., line_delimiter_count: _Optional[int] = ..., did_open_edit_view: bool = ...) -> None: ...
    SONG_SELECT_FIELD_NUMBER: _ClassVar[int]
    MULTITRACKS_FIELD_NUMBER: _ClassVar[int]
    song_select: Import.SongSelect
    multitracks: _analyticsMultiTracks_pb2.MultiTracks.Import
    def __init__(self, song_select: _Optional[_Union[Import.SongSelect, _Mapping]] = ..., multitracks: _Optional[_Union[_analyticsMultiTracks_pb2.MultiTracks.Import, _Mapping]] = ...) -> None: ...
