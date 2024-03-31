from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UI(_message.Message):
    __slots__ = ("quick_search", "toolbar", "main_view", "looks", "screen_configuration", "lower_right", "text_inspector", "show", "in_app_store", "editor", "whats_new", "clear_groups", "preview_area", "placeholder", "planning_center_live", "network_group", "ccli", "capture", "welcomeToProPresenter", "test_pattern", "preferences")
    class QuickSearch(_message.Message):
        __slots__ = ("shown", "search", "open_items")
        class Shown(_message.Message):
            __slots__ = ("source",)
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_UNKNOWN: _ClassVar[UI.QuickSearch.Shown.Source]
                SOURCE_APPLICATION_MENU: _ClassVar[UI.QuickSearch.Shown.Source]
                SOURCE_TOOLBAR: _ClassVar[UI.QuickSearch.Shown.Source]
                SOURCE_UNLINKED_HEADER: _ClassVar[UI.QuickSearch.Shown.Source]
            SOURCE_UNKNOWN: UI.QuickSearch.Shown.Source
            SOURCE_APPLICATION_MENU: UI.QuickSearch.Shown.Source
            SOURCE_TOOLBAR: UI.QuickSearch.Shown.Source
            SOURCE_UNLINKED_HEADER: UI.QuickSearch.Shown.Source
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            source: UI.QuickSearch.Shown.Source
            def __init__(self, source: _Optional[_Union[UI.QuickSearch.Shown.Source, str]] = ...) -> None: ...
        class Search(_message.Message):
            __slots__ = ("source",)
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_UNKNOWN: _ClassVar[UI.QuickSearch.Search.Source]
                SOURCE_LIBRARY: _ClassVar[UI.QuickSearch.Search.Source]
                SOURCE_SONG_SELECT: _ClassVar[UI.QuickSearch.Search.Source]
                SOURCE_MULTI_TRACKS: _ClassVar[UI.QuickSearch.Search.Source]
            SOURCE_UNKNOWN: UI.QuickSearch.Search.Source
            SOURCE_LIBRARY: UI.QuickSearch.Search.Source
            SOURCE_SONG_SELECT: UI.QuickSearch.Search.Source
            SOURCE_MULTI_TRACKS: UI.QuickSearch.Search.Source
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            source: UI.QuickSearch.Search.Source
            def __init__(self, source: _Optional[_Union[UI.QuickSearch.Search.Source, str]] = ...) -> None: ...
        class OpenItems(_message.Message):
            __slots__ = ("source", "style", "count")
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_UNKNOWN: _ClassVar[UI.QuickSearch.OpenItems.Source]
                SOURCE_LIBRARY: _ClassVar[UI.QuickSearch.OpenItems.Source]
                SOURCE_SONG_SELECT: _ClassVar[UI.QuickSearch.OpenItems.Source]
                SOURCE_MULTI_TRACKS: _ClassVar[UI.QuickSearch.OpenItems.Source]
            SOURCE_UNKNOWN: UI.QuickSearch.OpenItems.Source
            SOURCE_LIBRARY: UI.QuickSearch.OpenItems.Source
            SOURCE_SONG_SELECT: UI.QuickSearch.OpenItems.Source
            SOURCE_MULTI_TRACKS: UI.QuickSearch.OpenItems.Source
            class Style(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                STYLE_UNKNOWN: _ClassVar[UI.QuickSearch.OpenItems.Style]
                STYLE_RETURN_KEY: _ClassVar[UI.QuickSearch.OpenItems.Style]
                STYLE_COMMAND_RETURN_KEY: _ClassVar[UI.QuickSearch.OpenItems.Style]
                STYLE_DRAG_DROP: _ClassVar[UI.QuickSearch.OpenItems.Style]
            STYLE_UNKNOWN: UI.QuickSearch.OpenItems.Style
            STYLE_RETURN_KEY: UI.QuickSearch.OpenItems.Style
            STYLE_COMMAND_RETURN_KEY: UI.QuickSearch.OpenItems.Style
            STYLE_DRAG_DROP: UI.QuickSearch.OpenItems.Style
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            STYLE_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            source: UI.QuickSearch.OpenItems.Source
            style: UI.QuickSearch.OpenItems.Style
            count: int
            def __init__(self, source: _Optional[_Union[UI.QuickSearch.OpenItems.Source, str]] = ..., style: _Optional[_Union[UI.QuickSearch.OpenItems.Style, str]] = ..., count: _Optional[int] = ...) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        SEARCH_FIELD_NUMBER: _ClassVar[int]
        OPEN_ITEMS_FIELD_NUMBER: _ClassVar[int]
        shown: UI.QuickSearch.Shown
        search: UI.QuickSearch.Search
        open_items: UI.QuickSearch.OpenItems
        def __init__(self, shown: _Optional[_Union[UI.QuickSearch.Shown, _Mapping]] = ..., search: _Optional[_Union[UI.QuickSearch.Search, _Mapping]] = ..., open_items: _Optional[_Union[UI.QuickSearch.OpenItems, _Mapping]] = ...) -> None: ...
    class Toolbar(_message.Message):
        __slots__ = ("text_style", "theme")
        class TextStyle(_message.Message):
            __slots__ = ("shown", "change")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Change(_message.Message):
                __slots__ = ("property", "target")
                class Property(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    PROPERTY_UNKNOWN: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_FONT_TYPEFACE: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_FONT_WEIGHT: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_FONT_CAPITALIZATION: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_FONT_SIZE: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_FONT_COLOR: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_HORIZONTAL_ALIGNMENT: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_VERTICAL_ALIGNMENT: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_STROKE_ENABLE: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_STROKE_WIDTH: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_STROKE_COLOR: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_SHADOW_ENABLE: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_SHADOW_BLUR: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_SHADOW_OPACITY: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_SHADOW_COLOR: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_SHADOW_ANGLE: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                    PROPERTY_SHADOW_OFFSET: _ClassVar[UI.Toolbar.TextStyle.Change.Property]
                PROPERTY_UNKNOWN: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_FONT_TYPEFACE: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_FONT_WEIGHT: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_FONT_CAPITALIZATION: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_FONT_SIZE: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_FONT_COLOR: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_HORIZONTAL_ALIGNMENT: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_VERTICAL_ALIGNMENT: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_STROKE_ENABLE: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_STROKE_WIDTH: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_STROKE_COLOR: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_SHADOW_ENABLE: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_SHADOW_BLUR: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_SHADOW_OPACITY: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_SHADOW_COLOR: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_SHADOW_ANGLE: UI.Toolbar.TextStyle.Change.Property
                PROPERTY_SHADOW_OFFSET: UI.Toolbar.TextStyle.Change.Property
                class Target(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    TARGET_UNKNOWN: _ClassVar[UI.Toolbar.TextStyle.Change.Target]
                    TARGET_SLIDE_SELECTION: _ClassVar[UI.Toolbar.TextStyle.Change.Target]
                    TARGET_PRESENTATION_SELECTION: _ClassVar[UI.Toolbar.TextStyle.Change.Target]
                TARGET_UNKNOWN: UI.Toolbar.TextStyle.Change.Target
                TARGET_SLIDE_SELECTION: UI.Toolbar.TextStyle.Change.Target
                TARGET_PRESENTATION_SELECTION: UI.Toolbar.TextStyle.Change.Target
                PROPERTY_FIELD_NUMBER: _ClassVar[int]
                TARGET_FIELD_NUMBER: _ClassVar[int]
                property: UI.Toolbar.TextStyle.Change.Property
                target: UI.Toolbar.TextStyle.Change.Target
                def __init__(self, property: _Optional[_Union[UI.Toolbar.TextStyle.Change.Property, str]] = ..., target: _Optional[_Union[UI.Toolbar.TextStyle.Change.Target, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            CHANGE_FIELD_NUMBER: _ClassVar[int]
            shown: UI.Toolbar.TextStyle.Shown
            change: UI.Toolbar.TextStyle.Change
            def __init__(self, shown: _Optional[_Union[UI.Toolbar.TextStyle.Shown, _Mapping]] = ..., change: _Optional[_Union[UI.Toolbar.TextStyle.Change, _Mapping]] = ...) -> None: ...
        class Theme(_message.Message):
            __slots__ = ("shown", "applied")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Applied(_message.Message):
                __slots__ = ("target",)
                class Target(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    TARGET_UNKNOWN: _ClassVar[UI.Toolbar.Theme.Applied.Target]
                    TARGET_SLIDE_SELECTION: _ClassVar[UI.Toolbar.Theme.Applied.Target]
                    TARGET_PRESENTATION_SELECTION: _ClassVar[UI.Toolbar.Theme.Applied.Target]
                TARGET_UNKNOWN: UI.Toolbar.Theme.Applied.Target
                TARGET_SLIDE_SELECTION: UI.Toolbar.Theme.Applied.Target
                TARGET_PRESENTATION_SELECTION: UI.Toolbar.Theme.Applied.Target
                TARGET_FIELD_NUMBER: _ClassVar[int]
                target: UI.Toolbar.Theme.Applied.Target
                def __init__(self, target: _Optional[_Union[UI.Toolbar.Theme.Applied.Target, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            APPLIED_FIELD_NUMBER: _ClassVar[int]
            shown: UI.Toolbar.Theme.Shown
            applied: UI.Toolbar.Theme.Applied
            def __init__(self, shown: _Optional[_Union[UI.Toolbar.Theme.Shown, _Mapping]] = ..., applied: _Optional[_Union[UI.Toolbar.Theme.Applied, _Mapping]] = ...) -> None: ...
        TEXT_STYLE_FIELD_NUMBER: _ClassVar[int]
        THEME_FIELD_NUMBER: _ClassVar[int]
        text_style: UI.Toolbar.TextStyle
        theme: UI.Toolbar.Theme
        def __init__(self, text_style: _Optional[_Union[UI.Toolbar.TextStyle, _Mapping]] = ..., theme: _Optional[_Union[UI.Toolbar.Theme, _Mapping]] = ...) -> None: ...
    class MainView(_message.Message):
        __slots__ = ("show", "presentation_editor", "reflow_editor", "bible", "stage_editor", "theme_editor", "copyright_editor", "props_editor", "mask_editor")
        class Show(_message.Message):
            __slots__ = ("shown",)
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.Show.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.Show.Shown.Source]
                    SOURCE_APPLICATION_MENU: _ClassVar[UI.MainView.Show.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.Show.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.Show.Shown.Source
                SOURCE_APPLICATION_MENU: UI.MainView.Show.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.Show.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.Show.Shown.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.Show.Shown
            def __init__(self, shown: _Optional[_Union[UI.MainView.Show.Shown, _Mapping]] = ...) -> None: ...
        class PresentationEditor(_message.Message):
            __slots__ = ("shown",)
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.PresentationEditor.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.PresentationEditor.Shown.Source]
                    SOURCE_APPLICATION_MENU: _ClassVar[UI.MainView.PresentationEditor.Shown.Source]
                    SOURCE_CONTEXT_MENU: _ClassVar[UI.MainView.PresentationEditor.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.PresentationEditor.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.PresentationEditor.Shown.Source
                SOURCE_APPLICATION_MENU: UI.MainView.PresentationEditor.Shown.Source
                SOURCE_CONTEXT_MENU: UI.MainView.PresentationEditor.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.PresentationEditor.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.PresentationEditor.Shown.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.PresentationEditor.Shown
            def __init__(self, shown: _Optional[_Union[UI.MainView.PresentationEditor.Shown, _Mapping]] = ...) -> None: ...
        class ReflowEditor(_message.Message):
            __slots__ = ("shown",)
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.ReflowEditor.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.ReflowEditor.Shown.Source]
                    SOURCE_APPLICATION_MENU: _ClassVar[UI.MainView.ReflowEditor.Shown.Source]
                    SOURCE_LIBRARY_CONTEXT_MENU: _ClassVar[UI.MainView.ReflowEditor.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.ReflowEditor.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.ReflowEditor.Shown.Source
                SOURCE_APPLICATION_MENU: UI.MainView.ReflowEditor.Shown.Source
                SOURCE_LIBRARY_CONTEXT_MENU: UI.MainView.ReflowEditor.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.ReflowEditor.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.ReflowEditor.Shown.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.ReflowEditor.Shown
            def __init__(self, shown: _Optional[_Union[UI.MainView.ReflowEditor.Shown, _Mapping]] = ...) -> None: ...
        class Bible(_message.Message):
            __slots__ = ("shown", "trigger", "generate_slides", "generate_next", "generate_previous", "save_slides", "lookup", "install", "remove", "startup")
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.Bible.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.Bible.Shown.Source]
                    SOURCE_APPLICATION_MENU: _ClassVar[UI.MainView.Bible.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.Bible.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.Bible.Shown.Source
                SOURCE_APPLICATION_MENU: UI.MainView.Bible.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.Bible.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.Bible.Shown.Source, str]] = ...) -> None: ...
            class Trigger(_message.Message):
                __slots__ = ("location",)
                class Location(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    LOCATION_UNKNOWN: _ClassVar[UI.MainView.Bible.Trigger.Location]
                    LOCATION_PRESENTATION: _ClassVar[UI.MainView.Bible.Trigger.Location]
                    LOCATION_BIBLE_MODULE: _ClassVar[UI.MainView.Bible.Trigger.Location]
                LOCATION_UNKNOWN: UI.MainView.Bible.Trigger.Location
                LOCATION_PRESENTATION: UI.MainView.Bible.Trigger.Location
                LOCATION_BIBLE_MODULE: UI.MainView.Bible.Trigger.Location
                LOCATION_FIELD_NUMBER: _ClassVar[int]
                location: UI.MainView.Bible.Trigger.Location
                def __init__(self, location: _Optional[_Union[UI.MainView.Bible.Trigger.Location, str]] = ...) -> None: ...
            class GenerateSlides(_message.Message):
                __slots__ = ("translation_count", "slide_count", "verse_location", "reference_location", "show_verse_numbers", "break_new_verse", "display_translation", "preserve_font_color", "reference_style")
                class TextBoxLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    TEXT_BOX_LOCATION_UNKNOWN: _ClassVar[UI.MainView.Bible.GenerateSlides.TextBoxLocation]
                    TEXT_BOX_LOCATION_NONE: _ClassVar[UI.MainView.Bible.GenerateSlides.TextBoxLocation]
                    TEXT_BOX_LOCATION_TEXT_BOX: _ClassVar[UI.MainView.Bible.GenerateSlides.TextBoxLocation]
                    TEXT_BOX_LOCATION_WITH_VERSE: _ClassVar[UI.MainView.Bible.GenerateSlides.TextBoxLocation]
                TEXT_BOX_LOCATION_UNKNOWN: UI.MainView.Bible.GenerateSlides.TextBoxLocation
                TEXT_BOX_LOCATION_NONE: UI.MainView.Bible.GenerateSlides.TextBoxLocation
                TEXT_BOX_LOCATION_TEXT_BOX: UI.MainView.Bible.GenerateSlides.TextBoxLocation
                TEXT_BOX_LOCATION_WITH_VERSE: UI.MainView.Bible.GenerateSlides.TextBoxLocation
                class ReferenceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    REFERENCE_TYPE_UNKNOWN: _ClassVar[UI.MainView.Bible.GenerateSlides.ReferenceType]
                    REFERENCE_TYPE_PASSAGE_NONE: _ClassVar[UI.MainView.Bible.GenerateSlides.ReferenceType]
                    REFERENCE_TYPE_PASSAGE_EACH: _ClassVar[UI.MainView.Bible.GenerateSlides.ReferenceType]
                    REFERENCE_TYPE_PASSAGE_LAST: _ClassVar[UI.MainView.Bible.GenerateSlides.ReferenceType]
                    REFERENCE_TYPE_VERSE: _ClassVar[UI.MainView.Bible.GenerateSlides.ReferenceType]
                REFERENCE_TYPE_UNKNOWN: UI.MainView.Bible.GenerateSlides.ReferenceType
                REFERENCE_TYPE_PASSAGE_NONE: UI.MainView.Bible.GenerateSlides.ReferenceType
                REFERENCE_TYPE_PASSAGE_EACH: UI.MainView.Bible.GenerateSlides.ReferenceType
                REFERENCE_TYPE_PASSAGE_LAST: UI.MainView.Bible.GenerateSlides.ReferenceType
                REFERENCE_TYPE_VERSE: UI.MainView.Bible.GenerateSlides.ReferenceType
                TRANSLATION_COUNT_FIELD_NUMBER: _ClassVar[int]
                SLIDE_COUNT_FIELD_NUMBER: _ClassVar[int]
                VERSE_LOCATION_FIELD_NUMBER: _ClassVar[int]
                REFERENCE_LOCATION_FIELD_NUMBER: _ClassVar[int]
                SHOW_VERSE_NUMBERS_FIELD_NUMBER: _ClassVar[int]
                BREAK_NEW_VERSE_FIELD_NUMBER: _ClassVar[int]
                DISPLAY_TRANSLATION_FIELD_NUMBER: _ClassVar[int]
                PRESERVE_FONT_COLOR_FIELD_NUMBER: _ClassVar[int]
                REFERENCE_STYLE_FIELD_NUMBER: _ClassVar[int]
                translation_count: int
                slide_count: int
                verse_location: UI.MainView.Bible.GenerateSlides.TextBoxLocation
                reference_location: UI.MainView.Bible.GenerateSlides.TextBoxLocation
                show_verse_numbers: bool
                break_new_verse: bool
                display_translation: bool
                preserve_font_color: bool
                reference_style: UI.MainView.Bible.GenerateSlides.ReferenceType
                def __init__(self, translation_count: _Optional[int] = ..., slide_count: _Optional[int] = ..., verse_location: _Optional[_Union[UI.MainView.Bible.GenerateSlides.TextBoxLocation, str]] = ..., reference_location: _Optional[_Union[UI.MainView.Bible.GenerateSlides.TextBoxLocation, str]] = ..., show_verse_numbers: bool = ..., break_new_verse: bool = ..., display_translation: bool = ..., preserve_font_color: bool = ..., reference_style: _Optional[_Union[UI.MainView.Bible.GenerateSlides.ReferenceType, str]] = ...) -> None: ...
            class GenerateNext(_message.Message):
                __slots__ = ("location",)
                class Location(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    LOCATION_UNKNOWN: _ClassVar[UI.MainView.Bible.GenerateNext.Location]
                    LOCATION_PRESENTATION: _ClassVar[UI.MainView.Bible.GenerateNext.Location]
                    LOCATION_BIBLE_MODULE: _ClassVar[UI.MainView.Bible.GenerateNext.Location]
                LOCATION_UNKNOWN: UI.MainView.Bible.GenerateNext.Location
                LOCATION_PRESENTATION: UI.MainView.Bible.GenerateNext.Location
                LOCATION_BIBLE_MODULE: UI.MainView.Bible.GenerateNext.Location
                LOCATION_FIELD_NUMBER: _ClassVar[int]
                location: UI.MainView.Bible.GenerateNext.Location
                def __init__(self, location: _Optional[_Union[UI.MainView.Bible.GenerateNext.Location, str]] = ...) -> None: ...
            class GeneratePrevious(_message.Message):
                __slots__ = ("location",)
                class Location(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    LOCATION_UNKNOWN: _ClassVar[UI.MainView.Bible.GeneratePrevious.Location]
                    LOCATION_PRESENTATION: _ClassVar[UI.MainView.Bible.GeneratePrevious.Location]
                    LOCATION_BIBLE_MODULE: _ClassVar[UI.MainView.Bible.GeneratePrevious.Location]
                LOCATION_UNKNOWN: UI.MainView.Bible.GeneratePrevious.Location
                LOCATION_PRESENTATION: UI.MainView.Bible.GeneratePrevious.Location
                LOCATION_BIBLE_MODULE: UI.MainView.Bible.GeneratePrevious.Location
                LOCATION_FIELD_NUMBER: _ClassVar[int]
                location: UI.MainView.Bible.GeneratePrevious.Location
                def __init__(self, location: _Optional[_Union[UI.MainView.Bible.GeneratePrevious.Location, str]] = ...) -> None: ...
            class SaveSlides(_message.Message):
                __slots__ = ("destination",)
                class SlideDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SLIDE_DESTINATION_UNKNOWN: _ClassVar[UI.MainView.Bible.SaveSlides.SlideDestination]
                    SLIDE_DESTINATION_SAVE_TO_LIBRARY: _ClassVar[UI.MainView.Bible.SaveSlides.SlideDestination]
                    SLIDE_DESTINATION_SAVE_TO_PLAYLIST: _ClassVar[UI.MainView.Bible.SaveSlides.SlideDestination]
                    SLIDE_DESTINATION_COPY_TO_PRESENTATION: _ClassVar[UI.MainView.Bible.SaveSlides.SlideDestination]
                SLIDE_DESTINATION_UNKNOWN: UI.MainView.Bible.SaveSlides.SlideDestination
                SLIDE_DESTINATION_SAVE_TO_LIBRARY: UI.MainView.Bible.SaveSlides.SlideDestination
                SLIDE_DESTINATION_SAVE_TO_PLAYLIST: UI.MainView.Bible.SaveSlides.SlideDestination
                SLIDE_DESTINATION_COPY_TO_PRESENTATION: UI.MainView.Bible.SaveSlides.SlideDestination
                DESTINATION_FIELD_NUMBER: _ClassVar[int]
                destination: UI.MainView.Bible.SaveSlides.SlideDestination
                def __init__(self, destination: _Optional[_Union[UI.MainView.Bible.SaveSlides.SlideDestination, str]] = ...) -> None: ...
            class Lookup(_message.Message):
                __slots__ = ("location",)
                class LookupLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    LOOKUP_LOCATION_UNKNOWN: _ClassVar[UI.MainView.Bible.Lookup.LookupLocation]
                    LOOKUP_LOCATION_TEXT_REFERENCE: _ClassVar[UI.MainView.Bible.Lookup.LookupLocation]
                    LOOKUP_LOCATION_MENU_BOOK: _ClassVar[UI.MainView.Bible.Lookup.LookupLocation]
                    LOOKUP_LOCATION_MENU_CHAPTER: _ClassVar[UI.MainView.Bible.Lookup.LookupLocation]
                    LOOKUP_LOCATION_MENU_VERSE: _ClassVar[UI.MainView.Bible.Lookup.LookupLocation]
                    LOOKUP_LOCATION_TEXT_SEARCH_CHAPTER: _ClassVar[UI.MainView.Bible.Lookup.LookupLocation]
                    LOOKUP_LOCATION_TEXT_SEARCH_VERSE: _ClassVar[UI.MainView.Bible.Lookup.LookupLocation]
                LOOKUP_LOCATION_UNKNOWN: UI.MainView.Bible.Lookup.LookupLocation
                LOOKUP_LOCATION_TEXT_REFERENCE: UI.MainView.Bible.Lookup.LookupLocation
                LOOKUP_LOCATION_MENU_BOOK: UI.MainView.Bible.Lookup.LookupLocation
                LOOKUP_LOCATION_MENU_CHAPTER: UI.MainView.Bible.Lookup.LookupLocation
                LOOKUP_LOCATION_MENU_VERSE: UI.MainView.Bible.Lookup.LookupLocation
                LOOKUP_LOCATION_TEXT_SEARCH_CHAPTER: UI.MainView.Bible.Lookup.LookupLocation
                LOOKUP_LOCATION_TEXT_SEARCH_VERSE: UI.MainView.Bible.Lookup.LookupLocation
                LOCATION_FIELD_NUMBER: _ClassVar[int]
                location: UI.MainView.Bible.Lookup.LookupLocation
                def __init__(self, location: _Optional[_Union[UI.MainView.Bible.Lookup.LookupLocation, str]] = ...) -> None: ...
            class BibleCount(_message.Message):
                __slots__ = ("free_installed_count", "purchased_installed_count")
                FREE_INSTALLED_COUNT_FIELD_NUMBER: _ClassVar[int]
                PURCHASED_INSTALLED_COUNT_FIELD_NUMBER: _ClassVar[int]
                free_installed_count: int
                purchased_installed_count: int
                def __init__(self, free_installed_count: _Optional[int] = ..., purchased_installed_count: _Optional[int] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            GENERATE_SLIDES_FIELD_NUMBER: _ClassVar[int]
            GENERATE_NEXT_FIELD_NUMBER: _ClassVar[int]
            GENERATE_PREVIOUS_FIELD_NUMBER: _ClassVar[int]
            SAVE_SLIDES_FIELD_NUMBER: _ClassVar[int]
            LOOKUP_FIELD_NUMBER: _ClassVar[int]
            INSTALL_FIELD_NUMBER: _ClassVar[int]
            REMOVE_FIELD_NUMBER: _ClassVar[int]
            STARTUP_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.Bible.Shown
            trigger: UI.MainView.Bible.Trigger
            generate_slides: UI.MainView.Bible.GenerateSlides
            generate_next: UI.MainView.Bible.GenerateNext
            generate_previous: UI.MainView.Bible.GeneratePrevious
            save_slides: UI.MainView.Bible.SaveSlides
            lookup: UI.MainView.Bible.Lookup
            install: UI.MainView.Bible.BibleCount
            remove: UI.MainView.Bible.BibleCount
            startup: UI.MainView.Bible.BibleCount
            def __init__(self, shown: _Optional[_Union[UI.MainView.Bible.Shown, _Mapping]] = ..., trigger: _Optional[_Union[UI.MainView.Bible.Trigger, _Mapping]] = ..., generate_slides: _Optional[_Union[UI.MainView.Bible.GenerateSlides, _Mapping]] = ..., generate_next: _Optional[_Union[UI.MainView.Bible.GenerateNext, _Mapping]] = ..., generate_previous: _Optional[_Union[UI.MainView.Bible.GeneratePrevious, _Mapping]] = ..., save_slides: _Optional[_Union[UI.MainView.Bible.SaveSlides, _Mapping]] = ..., lookup: _Optional[_Union[UI.MainView.Bible.Lookup, _Mapping]] = ..., install: _Optional[_Union[UI.MainView.Bible.BibleCount, _Mapping]] = ..., remove: _Optional[_Union[UI.MainView.Bible.BibleCount, _Mapping]] = ..., startup: _Optional[_Union[UI.MainView.Bible.BibleCount, _Mapping]] = ...) -> None: ...
        class StageEditor(_message.Message):
            __slots__ = ("shown",)
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.StageEditor.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.StageEditor.Shown.Source]
                    SOURCE_APPLICATION_MENU: _ClassVar[UI.MainView.StageEditor.Shown.Source]
                    SOURCE_LOWER_RIGHT: _ClassVar[UI.MainView.StageEditor.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.StageEditor.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.StageEditor.Shown.Source
                SOURCE_APPLICATION_MENU: UI.MainView.StageEditor.Shown.Source
                SOURCE_LOWER_RIGHT: UI.MainView.StageEditor.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.StageEditor.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.StageEditor.Shown.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.StageEditor.Shown
            def __init__(self, shown: _Optional[_Union[UI.MainView.StageEditor.Shown, _Mapping]] = ...) -> None: ...
        class ThemeEditor(_message.Message):
            __slots__ = ("shown",)
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.ThemeEditor.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.ThemeEditor.Shown.Source]
                    SOURCE_THEME_CONTEXT_MENU: _ClassVar[UI.MainView.ThemeEditor.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.ThemeEditor.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.ThemeEditor.Shown.Source
                SOURCE_THEME_CONTEXT_MENU: UI.MainView.ThemeEditor.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.ThemeEditor.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.ThemeEditor.Shown.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.ThemeEditor.Shown
            def __init__(self, shown: _Optional[_Union[UI.MainView.ThemeEditor.Shown, _Mapping]] = ...) -> None: ...
        class CopyrightEditor(_message.Message):
            __slots__ = ("shown",)
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.CopyrightEditor.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.CopyrightEditor.Shown.Source]
                    SOURCE_PREFERENCE: _ClassVar[UI.MainView.CopyrightEditor.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.CopyrightEditor.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.CopyrightEditor.Shown.Source
                SOURCE_PREFERENCE: UI.MainView.CopyrightEditor.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.CopyrightEditor.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.CopyrightEditor.Shown.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.CopyrightEditor.Shown
            def __init__(self, shown: _Optional[_Union[UI.MainView.CopyrightEditor.Shown, _Mapping]] = ...) -> None: ...
        class PropsEditor(_message.Message):
            __slots__ = ("shown",)
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.PropsEditor.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.PropsEditor.Shown.Source]
                    SOURCE_LOWER_RIGHT: _ClassVar[UI.MainView.PropsEditor.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.PropsEditor.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.PropsEditor.Shown.Source
                SOURCE_LOWER_RIGHT: UI.MainView.PropsEditor.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.PropsEditor.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.PropsEditor.Shown.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.PropsEditor.Shown
            def __init__(self, shown: _Optional[_Union[UI.MainView.PropsEditor.Shown, _Mapping]] = ...) -> None: ...
        class MaskEditor(_message.Message):
            __slots__ = ("shown",)
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.MainView.MaskEditor.Shown.Source]
                    SOURCE_TOOLBAR: _ClassVar[UI.MainView.MaskEditor.Shown.Source]
                    SOURCE_LOOKS_WINDOW: _ClassVar[UI.MainView.MaskEditor.Shown.Source]
                SOURCE_UNKNOWN: UI.MainView.MaskEditor.Shown.Source
                SOURCE_TOOLBAR: UI.MainView.MaskEditor.Shown.Source
                SOURCE_LOOKS_WINDOW: UI.MainView.MaskEditor.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.MainView.MaskEditor.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.MainView.MaskEditor.Shown.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            shown: UI.MainView.MaskEditor.Shown
            def __init__(self, shown: _Optional[_Union[UI.MainView.MaskEditor.Shown, _Mapping]] = ...) -> None: ...
        SHOW_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_EDITOR_FIELD_NUMBER: _ClassVar[int]
        REFLOW_EDITOR_FIELD_NUMBER: _ClassVar[int]
        BIBLE_FIELD_NUMBER: _ClassVar[int]
        STAGE_EDITOR_FIELD_NUMBER: _ClassVar[int]
        THEME_EDITOR_FIELD_NUMBER: _ClassVar[int]
        COPYRIGHT_EDITOR_FIELD_NUMBER: _ClassVar[int]
        PROPS_EDITOR_FIELD_NUMBER: _ClassVar[int]
        MASK_EDITOR_FIELD_NUMBER: _ClassVar[int]
        show: UI.MainView.Show
        presentation_editor: UI.MainView.PresentationEditor
        reflow_editor: UI.MainView.ReflowEditor
        bible: UI.MainView.Bible
        stage_editor: UI.MainView.StageEditor
        theme_editor: UI.MainView.ThemeEditor
        copyright_editor: UI.MainView.CopyrightEditor
        props_editor: UI.MainView.PropsEditor
        mask_editor: UI.MainView.MaskEditor
        def __init__(self, show: _Optional[_Union[UI.MainView.Show, _Mapping]] = ..., presentation_editor: _Optional[_Union[UI.MainView.PresentationEditor, _Mapping]] = ..., reflow_editor: _Optional[_Union[UI.MainView.ReflowEditor, _Mapping]] = ..., bible: _Optional[_Union[UI.MainView.Bible, _Mapping]] = ..., stage_editor: _Optional[_Union[UI.MainView.StageEditor, _Mapping]] = ..., theme_editor: _Optional[_Union[UI.MainView.ThemeEditor, _Mapping]] = ..., copyright_editor: _Optional[_Union[UI.MainView.CopyrightEditor, _Mapping]] = ..., props_editor: _Optional[_Union[UI.MainView.PropsEditor, _Mapping]] = ..., mask_editor: _Optional[_Union[UI.MainView.MaskEditor, _Mapping]] = ...) -> None: ...
    class Looks(_message.Message):
        __slots__ = ("shown",)
        class Shown(_message.Message):
            __slots__ = ("source",)
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_UNKNOWN: _ClassVar[UI.Looks.Shown.Source]
                SOURCE_APPLICATION_MENU: _ClassVar[UI.Looks.Shown.Source]
                SOURCE_PRESENTATION_VIEW: _ClassVar[UI.Looks.Shown.Source]
            SOURCE_UNKNOWN: UI.Looks.Shown.Source
            SOURCE_APPLICATION_MENU: UI.Looks.Shown.Source
            SOURCE_PRESENTATION_VIEW: UI.Looks.Shown.Source
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            source: UI.Looks.Shown.Source
            def __init__(self, source: _Optional[_Union[UI.Looks.Shown.Source, str]] = ...) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        shown: UI.Looks.Shown
        def __init__(self, shown: _Optional[_Union[UI.Looks.Shown, _Mapping]] = ...) -> None: ...
    class ScreenConfiguration(_message.Message):
        __slots__ = ("shown",)
        class Shown(_message.Message):
            __slots__ = ("source",)
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_UNKNOWN: _ClassVar[UI.ScreenConfiguration.Shown.Source]
                SOURCE_APPLICATION_MENU: _ClassVar[UI.ScreenConfiguration.Shown.Source]
                SOURCE_STAGE: _ClassVar[UI.ScreenConfiguration.Shown.Source]
            SOURCE_UNKNOWN: UI.ScreenConfiguration.Shown.Source
            SOURCE_APPLICATION_MENU: UI.ScreenConfiguration.Shown.Source
            SOURCE_STAGE: UI.ScreenConfiguration.Shown.Source
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            source: UI.ScreenConfiguration.Shown.Source
            def __init__(self, source: _Optional[_Union[UI.ScreenConfiguration.Shown.Source, str]] = ...) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        shown: UI.ScreenConfiguration.Shown
        def __init__(self, shown: _Optional[_Union[UI.ScreenConfiguration.Shown, _Mapping]] = ...) -> None: ...
    class LowerRight(_message.Message):
        __slots__ = ("timers", "messages", "props", "stage", "audio_bin", "macros")
        class Timers(_message.Message):
            __slots__ = ("shown", "collapse", "edit", "state", "create", "delete")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Collapse(_message.Message):
                __slots__ = ("state",)
                class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    STATE_UNKNOWN: _ClassVar[UI.LowerRight.Timers.Collapse.State]
                    STATE_COLLAPSED: _ClassVar[UI.LowerRight.Timers.Collapse.State]
                    STATE_EXPANDED: _ClassVar[UI.LowerRight.Timers.Collapse.State]
                STATE_UNKNOWN: UI.LowerRight.Timers.Collapse.State
                STATE_COLLAPSED: UI.LowerRight.Timers.Collapse.State
                STATE_EXPANDED: UI.LowerRight.Timers.Collapse.State
                STATE_FIELD_NUMBER: _ClassVar[int]
                state: UI.LowerRight.Timers.Collapse.State
                def __init__(self, state: _Optional[_Union[UI.LowerRight.Timers.Collapse.State, str]] = ...) -> None: ...
            class Edit(_message.Message):
                __slots__ = ("field",)
                class Field(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    FIELD_UNKNOWN: _ClassVar[UI.LowerRight.Timers.Edit.Field]
                    FIELD_TYPE: _ClassVar[UI.LowerRight.Timers.Edit.Field]
                    FIELD_VALUE: _ClassVar[UI.LowerRight.Timers.Edit.Field]
                    FIELD_OVERRUN: _ClassVar[UI.LowerRight.Timers.Edit.Field]
                    FIELD_NAME: _ClassVar[UI.LowerRight.Timers.Edit.Field]
                FIELD_UNKNOWN: UI.LowerRight.Timers.Edit.Field
                FIELD_TYPE: UI.LowerRight.Timers.Edit.Field
                FIELD_VALUE: UI.LowerRight.Timers.Edit.Field
                FIELD_OVERRUN: UI.LowerRight.Timers.Edit.Field
                FIELD_NAME: UI.LowerRight.Timers.Edit.Field
                FIELD_FIELD_NUMBER: _ClassVar[int]
                field: UI.LowerRight.Timers.Edit.Field
                def __init__(self, field: _Optional[_Union[UI.LowerRight.Timers.Edit.Field, str]] = ...) -> None: ...
            class State(_message.Message):
                __slots__ = ("state",)
                class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    STATE_UNKNOWN: _ClassVar[UI.LowerRight.Timers.State.State]
                    STATE_START: _ClassVar[UI.LowerRight.Timers.State.State]
                    STATE_STOP: _ClassVar[UI.LowerRight.Timers.State.State]
                    STATE_RESET: _ClassVar[UI.LowerRight.Timers.State.State]
                STATE_UNKNOWN: UI.LowerRight.Timers.State.State
                STATE_START: UI.LowerRight.Timers.State.State
                STATE_STOP: UI.LowerRight.Timers.State.State
                STATE_RESET: UI.LowerRight.Timers.State.State
                STATE_FIELD_NUMBER: _ClassVar[int]
                state: UI.LowerRight.Timers.State.State
                def __init__(self, state: _Optional[_Union[UI.LowerRight.Timers.State.State, str]] = ...) -> None: ...
            class Create(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Delete(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            COLLAPSE_FIELD_NUMBER: _ClassVar[int]
            EDIT_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            CREATE_FIELD_NUMBER: _ClassVar[int]
            DELETE_FIELD_NUMBER: _ClassVar[int]
            shown: UI.LowerRight.Timers.Shown
            collapse: UI.LowerRight.Timers.Collapse
            edit: UI.LowerRight.Timers.Edit
            state: UI.LowerRight.Timers.State
            create: UI.LowerRight.Timers.Create
            delete: UI.LowerRight.Timers.Delete
            def __init__(self, shown: _Optional[_Union[UI.LowerRight.Timers.Shown, _Mapping]] = ..., collapse: _Optional[_Union[UI.LowerRight.Timers.Collapse, _Mapping]] = ..., edit: _Optional[_Union[UI.LowerRight.Timers.Edit, _Mapping]] = ..., state: _Optional[_Union[UI.LowerRight.Timers.State, _Mapping]] = ..., create: _Optional[_Union[UI.LowerRight.Timers.Create, _Mapping]] = ..., delete: _Optional[_Union[UI.LowerRight.Timers.Delete, _Mapping]] = ...) -> None: ...
        class Messages(_message.Message):
            __slots__ = ("shown", "edit", "state", "create", "delete")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Edit(_message.Message):
                __slots__ = ("action",)
                class Action(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    ACTION_UNKNOWN: _ClassVar[UI.LowerRight.Messages.Edit.Action]
                    ACTION_ADD_TEXT_TOKEN: _ClassVar[UI.LowerRight.Messages.Edit.Action]
                    ACTION_ADD_TIMER_TOKEN: _ClassVar[UI.LowerRight.Messages.Edit.Action]
                    ACTION_ADD_CUSTOM_TOKEN: _ClassVar[UI.LowerRight.Messages.Edit.Action]
                    ACTION_SET_THEME: _ClassVar[UI.LowerRight.Messages.Edit.Action]
                    ACTION_SET_TEXT: _ClassVar[UI.LowerRight.Messages.Edit.Action]
                    ACTION_SET_WEB_NOTIFICATION: _ClassVar[UI.LowerRight.Messages.Edit.Action]
                    ACTION_SET_DISMISS_BEHAVIOR: _ClassVar[UI.LowerRight.Messages.Edit.Action]
                ACTION_UNKNOWN: UI.LowerRight.Messages.Edit.Action
                ACTION_ADD_TEXT_TOKEN: UI.LowerRight.Messages.Edit.Action
                ACTION_ADD_TIMER_TOKEN: UI.LowerRight.Messages.Edit.Action
                ACTION_ADD_CUSTOM_TOKEN: UI.LowerRight.Messages.Edit.Action
                ACTION_SET_THEME: UI.LowerRight.Messages.Edit.Action
                ACTION_SET_TEXT: UI.LowerRight.Messages.Edit.Action
                ACTION_SET_WEB_NOTIFICATION: UI.LowerRight.Messages.Edit.Action
                ACTION_SET_DISMISS_BEHAVIOR: UI.LowerRight.Messages.Edit.Action
                ACTION_FIELD_NUMBER: _ClassVar[int]
                action: UI.LowerRight.Messages.Edit.Action
                def __init__(self, action: _Optional[_Union[UI.LowerRight.Messages.Edit.Action, str]] = ...) -> None: ...
            class State(_message.Message):
                __slots__ = ("state",)
                class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    STATE_UNKNOWN: _ClassVar[UI.LowerRight.Messages.State.State]
                    STATE_SHOW: _ClassVar[UI.LowerRight.Messages.State.State]
                    STATE_CLEAR: _ClassVar[UI.LowerRight.Messages.State.State]
                STATE_UNKNOWN: UI.LowerRight.Messages.State.State
                STATE_SHOW: UI.LowerRight.Messages.State.State
                STATE_CLEAR: UI.LowerRight.Messages.State.State
                STATE_FIELD_NUMBER: _ClassVar[int]
                state: UI.LowerRight.Messages.State.State
                def __init__(self, state: _Optional[_Union[UI.LowerRight.Messages.State.State, str]] = ...) -> None: ...
            class Create(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Delete(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            EDIT_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            CREATE_FIELD_NUMBER: _ClassVar[int]
            DELETE_FIELD_NUMBER: _ClassVar[int]
            shown: UI.LowerRight.Messages.Shown
            edit: UI.LowerRight.Messages.Edit
            state: UI.LowerRight.Messages.State
            create: UI.LowerRight.Messages.Create
            delete: UI.LowerRight.Messages.Delete
            def __init__(self, shown: _Optional[_Union[UI.LowerRight.Messages.Shown, _Mapping]] = ..., edit: _Optional[_Union[UI.LowerRight.Messages.Edit, _Mapping]] = ..., state: _Optional[_Union[UI.LowerRight.Messages.State, _Mapping]] = ..., create: _Optional[_Union[UI.LowerRight.Messages.Create, _Mapping]] = ..., delete: _Optional[_Union[UI.LowerRight.Messages.Delete, _Mapping]] = ...) -> None: ...
        class Props(_message.Message):
            __slots__ = ("shown", "transition", "state", "create", "delete")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Transition(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class State(_message.Message):
                __slots__ = ("state",)
                class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    STATE_UNKNOWN: _ClassVar[UI.LowerRight.Props.State.State]
                    STATE_SHOW: _ClassVar[UI.LowerRight.Props.State.State]
                    STATE_CLEAR: _ClassVar[UI.LowerRight.Props.State.State]
                STATE_UNKNOWN: UI.LowerRight.Props.State.State
                STATE_SHOW: UI.LowerRight.Props.State.State
                STATE_CLEAR: UI.LowerRight.Props.State.State
                STATE_FIELD_NUMBER: _ClassVar[int]
                state: UI.LowerRight.Props.State.State
                def __init__(self, state: _Optional[_Union[UI.LowerRight.Props.State.State, str]] = ...) -> None: ...
            class Create(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Delete(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            TRANSITION_FIELD_NUMBER: _ClassVar[int]
            STATE_FIELD_NUMBER: _ClassVar[int]
            CREATE_FIELD_NUMBER: _ClassVar[int]
            DELETE_FIELD_NUMBER: _ClassVar[int]
            shown: UI.LowerRight.Props.Shown
            transition: UI.LowerRight.Props.Transition
            state: UI.LowerRight.Props.State
            create: UI.LowerRight.Props.Create
            delete: UI.LowerRight.Props.Delete
            def __init__(self, shown: _Optional[_Union[UI.LowerRight.Props.Shown, _Mapping]] = ..., transition: _Optional[_Union[UI.LowerRight.Props.Transition, _Mapping]] = ..., state: _Optional[_Union[UI.LowerRight.Props.State, _Mapping]] = ..., create: _Optional[_Union[UI.LowerRight.Props.Create, _Mapping]] = ..., delete: _Optional[_Union[UI.LowerRight.Props.Delete, _Mapping]] = ...) -> None: ...
        class Stage(_message.Message):
            __slots__ = ("shown", "change_layout", "message_state", "configure_screens", "edit_layouts")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class ChangeLayout(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class MessageState(_message.Message):
                __slots__ = ("state",)
                class State(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    STATE_UNKNOWN: _ClassVar[UI.LowerRight.Stage.MessageState.State]
                    STATE_SHOW: _ClassVar[UI.LowerRight.Stage.MessageState.State]
                    STATE_CLEAR: _ClassVar[UI.LowerRight.Stage.MessageState.State]
                STATE_UNKNOWN: UI.LowerRight.Stage.MessageState.State
                STATE_SHOW: UI.LowerRight.Stage.MessageState.State
                STATE_CLEAR: UI.LowerRight.Stage.MessageState.State
                STATE_FIELD_NUMBER: _ClassVar[int]
                state: UI.LowerRight.Stage.MessageState.State
                def __init__(self, state: _Optional[_Union[UI.LowerRight.Stage.MessageState.State, str]] = ...) -> None: ...
            class ConfigureScreens(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class EditLayouts(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            CHANGE_LAYOUT_FIELD_NUMBER: _ClassVar[int]
            MESSAGE_STATE_FIELD_NUMBER: _ClassVar[int]
            CONFIGURE_SCREENS_FIELD_NUMBER: _ClassVar[int]
            EDIT_LAYOUTS_FIELD_NUMBER: _ClassVar[int]
            shown: UI.LowerRight.Stage.Shown
            change_layout: UI.LowerRight.Stage.ChangeLayout
            message_state: UI.LowerRight.Stage.MessageState
            configure_screens: UI.LowerRight.Stage.ConfigureScreens
            edit_layouts: UI.LowerRight.Stage.EditLayouts
            def __init__(self, shown: _Optional[_Union[UI.LowerRight.Stage.Shown, _Mapping]] = ..., change_layout: _Optional[_Union[UI.LowerRight.Stage.ChangeLayout, _Mapping]] = ..., message_state: _Optional[_Union[UI.LowerRight.Stage.MessageState, _Mapping]] = ..., configure_screens: _Optional[_Union[UI.LowerRight.Stage.ConfigureScreens, _Mapping]] = ..., edit_layouts: _Optional[_Union[UI.LowerRight.Stage.EditLayouts, _Mapping]] = ...) -> None: ...
        class AudioBin(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Macros(_message.Message):
            __slots__ = ("shown", "trigger", "create", "delete")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Trigger(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Create(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Delete(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            CREATE_FIELD_NUMBER: _ClassVar[int]
            DELETE_FIELD_NUMBER: _ClassVar[int]
            shown: UI.LowerRight.Macros.Shown
            trigger: UI.LowerRight.Macros.Trigger
            create: UI.LowerRight.Macros.Create
            delete: UI.LowerRight.Macros.Delete
            def __init__(self, shown: _Optional[_Union[UI.LowerRight.Macros.Shown, _Mapping]] = ..., trigger: _Optional[_Union[UI.LowerRight.Macros.Trigger, _Mapping]] = ..., create: _Optional[_Union[UI.LowerRight.Macros.Create, _Mapping]] = ..., delete: _Optional[_Union[UI.LowerRight.Macros.Delete, _Mapping]] = ...) -> None: ...
        TIMERS_FIELD_NUMBER: _ClassVar[int]
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        PROPS_FIELD_NUMBER: _ClassVar[int]
        STAGE_FIELD_NUMBER: _ClassVar[int]
        AUDIO_BIN_FIELD_NUMBER: _ClassVar[int]
        MACROS_FIELD_NUMBER: _ClassVar[int]
        timers: UI.LowerRight.Timers
        messages: UI.LowerRight.Messages
        props: UI.LowerRight.Props
        stage: UI.LowerRight.Stage
        audio_bin: UI.LowerRight.AudioBin
        macros: UI.LowerRight.Macros
        def __init__(self, timers: _Optional[_Union[UI.LowerRight.Timers, _Mapping]] = ..., messages: _Optional[_Union[UI.LowerRight.Messages, _Mapping]] = ..., props: _Optional[_Union[UI.LowerRight.Props, _Mapping]] = ..., stage: _Optional[_Union[UI.LowerRight.Stage, _Mapping]] = ..., audio_bin: _Optional[_Union[UI.LowerRight.AudioBin, _Mapping]] = ..., macros: _Optional[_Union[UI.LowerRight.Macros, _Mapping]] = ...) -> None: ...
    class TextInspector(_message.Message):
        __slots__ = ("shown", "foreground", "underline_color", "background_color", "scrolling_text", "line_transform")
        class Shown(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Foreground(_message.Message):
            __slots__ = ("fill_type", "selection_mode")
            class FillType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FILL_TYPE_UNKNOWN: _ClassVar[UI.TextInspector.Foreground.FillType]
                FILL_TYPE_SOLID: _ClassVar[UI.TextInspector.Foreground.FillType]
                FILL_TYPE_GRADIENT: _ClassVar[UI.TextInspector.Foreground.FillType]
            FILL_TYPE_UNKNOWN: UI.TextInspector.Foreground.FillType
            FILL_TYPE_SOLID: UI.TextInspector.Foreground.FillType
            FILL_TYPE_GRADIENT: UI.TextInspector.Foreground.FillType
            class SelectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SELECTION_MODE_UNKNOWN: _ClassVar[UI.TextInspector.Foreground.SelectionMode]
                SELECTION_MODE_OBJECT: _ClassVar[UI.TextInspector.Foreground.SelectionMode]
                SELECTION_MODE_RANGE: _ClassVar[UI.TextInspector.Foreground.SelectionMode]
            SELECTION_MODE_UNKNOWN: UI.TextInspector.Foreground.SelectionMode
            SELECTION_MODE_OBJECT: UI.TextInspector.Foreground.SelectionMode
            SELECTION_MODE_RANGE: UI.TextInspector.Foreground.SelectionMode
            FILL_TYPE_FIELD_NUMBER: _ClassVar[int]
            SELECTION_MODE_FIELD_NUMBER: _ClassVar[int]
            fill_type: UI.TextInspector.Foreground.FillType
            selection_mode: UI.TextInspector.Foreground.SelectionMode
            def __init__(self, fill_type: _Optional[_Union[UI.TextInspector.Foreground.FillType, str]] = ..., selection_mode: _Optional[_Union[UI.TextInspector.Foreground.SelectionMode, str]] = ...) -> None: ...
        class UnderlineColor(_message.Message):
            __slots__ = ("is_enabled", "selection_mode")
            class SelectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SELECTION_MODE_UNKNOWN: _ClassVar[UI.TextInspector.UnderlineColor.SelectionMode]
                SELECTION_MODE_OBJECT: _ClassVar[UI.TextInspector.UnderlineColor.SelectionMode]
                SELECTION_MODE_RANGE: _ClassVar[UI.TextInspector.UnderlineColor.SelectionMode]
            SELECTION_MODE_UNKNOWN: UI.TextInspector.UnderlineColor.SelectionMode
            SELECTION_MODE_OBJECT: UI.TextInspector.UnderlineColor.SelectionMode
            SELECTION_MODE_RANGE: UI.TextInspector.UnderlineColor.SelectionMode
            IS_ENABLED_FIELD_NUMBER: _ClassVar[int]
            SELECTION_MODE_FIELD_NUMBER: _ClassVar[int]
            is_enabled: bool
            selection_mode: UI.TextInspector.UnderlineColor.SelectionMode
            def __init__(self, is_enabled: bool = ..., selection_mode: _Optional[_Union[UI.TextInspector.UnderlineColor.SelectionMode, str]] = ...) -> None: ...
        class BackgroundColor(_message.Message):
            __slots__ = ("color_type", "selection_mode")
            class ColorType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                COLOR_TYPE_UNKNOWN: _ClassVar[UI.TextInspector.BackgroundColor.ColorType]
                COLOR_TYPE_CLEAR: _ClassVar[UI.TextInspector.BackgroundColor.ColorType]
                COLOR_TYPE_OTHER: _ClassVar[UI.TextInspector.BackgroundColor.ColorType]
            COLOR_TYPE_UNKNOWN: UI.TextInspector.BackgroundColor.ColorType
            COLOR_TYPE_CLEAR: UI.TextInspector.BackgroundColor.ColorType
            COLOR_TYPE_OTHER: UI.TextInspector.BackgroundColor.ColorType
            class SelectionMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SELECTION_MODE_UNKNOWN: _ClassVar[UI.TextInspector.BackgroundColor.SelectionMode]
                SELECTION_MODE_OBJECT: _ClassVar[UI.TextInspector.BackgroundColor.SelectionMode]
                SELECTION_MODE_RANGE: _ClassVar[UI.TextInspector.BackgroundColor.SelectionMode]
            SELECTION_MODE_UNKNOWN: UI.TextInspector.BackgroundColor.SelectionMode
            SELECTION_MODE_OBJECT: UI.TextInspector.BackgroundColor.SelectionMode
            SELECTION_MODE_RANGE: UI.TextInspector.BackgroundColor.SelectionMode
            COLOR_TYPE_FIELD_NUMBER: _ClassVar[int]
            SELECTION_MODE_FIELD_NUMBER: _ClassVar[int]
            color_type: UI.TextInspector.BackgroundColor.ColorType
            selection_mode: UI.TextInspector.BackgroundColor.SelectionMode
            def __init__(self, color_type: _Optional[_Union[UI.TextInspector.BackgroundColor.ColorType, str]] = ..., selection_mode: _Optional[_Union[UI.TextInspector.BackgroundColor.SelectionMode, str]] = ...) -> None: ...
        class ScrollingText(_message.Message):
            __slots__ = ("enable",)
            class Enable(_message.Message):
                __slots__ = ("enabled",)
                ENABLED_FIELD_NUMBER: _ClassVar[int]
                enabled: bool
                def __init__(self, enabled: bool = ...) -> None: ...
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            enable: UI.TextInspector.ScrollingText.Enable
            def __init__(self, enable: _Optional[_Union[UI.TextInspector.ScrollingText.Enable, _Mapping]] = ...) -> None: ...
        class LineTransform(_message.Message):
            __slots__ = ("transform_type",)
            class TransformType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TRANSFORM_TYPE_UNKNOWN: _ClassVar[UI.TextInspector.LineTransform.TransformType]
                TRANSFORM_TYPE_NONE: _ClassVar[UI.TextInspector.LineTransform.TransformType]
                TRANSFORM_TYPE_REMOVE_LINE_RETURNS: _ClassVar[UI.TextInspector.LineTransform.TransformType]
                TRANSFORM_TYPE_REPLACE_LINE_RETURNS: _ClassVar[UI.TextInspector.LineTransform.TransformType]
                TRANSFORM_TYPE_ONE_WORD_PER_LINE: _ClassVar[UI.TextInspector.LineTransform.TransformType]
                TRANSFORM_TYPE_ONE_CHARACTER_PER_LINE: _ClassVar[UI.TextInspector.LineTransform.TransformType]
            TRANSFORM_TYPE_UNKNOWN: UI.TextInspector.LineTransform.TransformType
            TRANSFORM_TYPE_NONE: UI.TextInspector.LineTransform.TransformType
            TRANSFORM_TYPE_REMOVE_LINE_RETURNS: UI.TextInspector.LineTransform.TransformType
            TRANSFORM_TYPE_REPLACE_LINE_RETURNS: UI.TextInspector.LineTransform.TransformType
            TRANSFORM_TYPE_ONE_WORD_PER_LINE: UI.TextInspector.LineTransform.TransformType
            TRANSFORM_TYPE_ONE_CHARACTER_PER_LINE: UI.TextInspector.LineTransform.TransformType
            TRANSFORM_TYPE_FIELD_NUMBER: _ClassVar[int]
            transform_type: UI.TextInspector.LineTransform.TransformType
            def __init__(self, transform_type: _Optional[_Union[UI.TextInspector.LineTransform.TransformType, str]] = ...) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        FOREGROUND_FIELD_NUMBER: _ClassVar[int]
        UNDERLINE_COLOR_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_COLOR_FIELD_NUMBER: _ClassVar[int]
        SCROLLING_TEXT_FIELD_NUMBER: _ClassVar[int]
        LINE_TRANSFORM_FIELD_NUMBER: _ClassVar[int]
        shown: UI.TextInspector.Shown
        foreground: UI.TextInspector.Foreground
        underline_color: UI.TextInspector.UnderlineColor
        background_color: UI.TextInspector.BackgroundColor
        scrolling_text: UI.TextInspector.ScrollingText
        line_transform: UI.TextInspector.LineTransform
        def __init__(self, shown: _Optional[_Union[UI.TextInspector.Shown, _Mapping]] = ..., foreground: _Optional[_Union[UI.TextInspector.Foreground, _Mapping]] = ..., underline_color: _Optional[_Union[UI.TextInspector.UnderlineColor, _Mapping]] = ..., background_color: _Optional[_Union[UI.TextInspector.BackgroundColor, _Mapping]] = ..., scrolling_text: _Optional[_Union[UI.TextInspector.ScrollingText, _Mapping]] = ..., line_transform: _Optional[_Union[UI.TextInspector.LineTransform, _Mapping]] = ...) -> None: ...
    class Show(_message.Message):
        __slots__ = ("slide_label",)
        class SlideLabel(_message.Message):
            __slots__ = ("shown", "change")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Change(_message.Message):
                __slots__ = ("number_of_slides", "source")
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.Show.SlideLabel.Change.Source]
                    SOURCE_CONTEXT_MENU: _ClassVar[UI.Show.SlideLabel.Change.Source]
                    SOURCE_POPOVER: _ClassVar[UI.Show.SlideLabel.Change.Source]
                SOURCE_UNKNOWN: UI.Show.SlideLabel.Change.Source
                SOURCE_CONTEXT_MENU: UI.Show.SlideLabel.Change.Source
                SOURCE_POPOVER: UI.Show.SlideLabel.Change.Source
                NUMBER_OF_SLIDES_FIELD_NUMBER: _ClassVar[int]
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                number_of_slides: int
                source: UI.Show.SlideLabel.Change.Source
                def __init__(self, number_of_slides: _Optional[int] = ..., source: _Optional[_Union[UI.Show.SlideLabel.Change.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            CHANGE_FIELD_NUMBER: _ClassVar[int]
            shown: UI.Show.SlideLabel.Shown
            change: UI.Show.SlideLabel.Change
            def __init__(self, shown: _Optional[_Union[UI.Show.SlideLabel.Shown, _Mapping]] = ..., change: _Optional[_Union[UI.Show.SlideLabel.Change, _Mapping]] = ...) -> None: ...
        SLIDE_LABEL_FIELD_NUMBER: _ClassVar[int]
        slide_label: UI.Show.SlideLabel
        def __init__(self, slide_label: _Optional[_Union[UI.Show.SlideLabel, _Mapping]] = ...) -> None: ...
    class InAppStore(_message.Message):
        __slots__ = ("trial",)
        class Trial(_message.Message):
            __slots__ = ("shown", "complete")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Complete(_message.Message):
                __slots__ = ("result",)
                class Result(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    RESULT_UNKNOWN: _ClassVar[UI.InAppStore.Trial.Complete.Result]
                    RESULT_SUCCESS: _ClassVar[UI.InAppStore.Trial.Complete.Result]
                    RESULT_EARLY_EXIT: _ClassVar[UI.InAppStore.Trial.Complete.Result]
                RESULT_UNKNOWN: UI.InAppStore.Trial.Complete.Result
                RESULT_SUCCESS: UI.InAppStore.Trial.Complete.Result
                RESULT_EARLY_EXIT: UI.InAppStore.Trial.Complete.Result
                RESULT_FIELD_NUMBER: _ClassVar[int]
                result: UI.InAppStore.Trial.Complete.Result
                def __init__(self, result: _Optional[_Union[UI.InAppStore.Trial.Complete.Result, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            COMPLETE_FIELD_NUMBER: _ClassVar[int]
            shown: UI.InAppStore.Trial.Shown
            complete: UI.InAppStore.Trial.Complete
            def __init__(self, shown: _Optional[_Union[UI.InAppStore.Trial.Shown, _Mapping]] = ..., complete: _Optional[_Union[UI.InAppStore.Trial.Complete, _Mapping]] = ...) -> None: ...
        TRIAL_FIELD_NUMBER: _ClassVar[int]
        trial: UI.InAppStore.Trial
        def __init__(self, trial: _Optional[_Union[UI.InAppStore.Trial, _Mapping]] = ...) -> None: ...
    class Editor(_message.Message):
        __slots__ = ("overlay",)
        class Overlay(_message.Message):
            __slots__ = ("shown", "closed")
            class Shown(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.Editor.Overlay.Shown.Source]
                    SOURCE_DOUBLE_CLICK: _ClassVar[UI.Editor.Overlay.Shown.Source]
                    SOURCE_CONTEXTUAL_MENU: _ClassVar[UI.Editor.Overlay.Shown.Source]
                    SOURCE_PLUS_BUTTON_MENU: _ClassVar[UI.Editor.Overlay.Shown.Source]
                SOURCE_UNKNOWN: UI.Editor.Overlay.Shown.Source
                SOURCE_DOUBLE_CLICK: UI.Editor.Overlay.Shown.Source
                SOURCE_CONTEXTUAL_MENU: UI.Editor.Overlay.Shown.Source
                SOURCE_PLUS_BUTTON_MENU: UI.Editor.Overlay.Shown.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.Editor.Overlay.Shown.Source
                def __init__(self, source: _Optional[_Union[UI.Editor.Overlay.Shown.Source, str]] = ...) -> None: ...
            class Closed(_message.Message):
                __slots__ = ("source",)
                class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SOURCE_UNKNOWN: _ClassVar[UI.Editor.Overlay.Closed.Source]
                    SOURCE_CLICK_OFF_ELEMENT: _ClassVar[UI.Editor.Overlay.Closed.Source]
                    SOURCE_ESCAPE_KEY: _ClassVar[UI.Editor.Overlay.Closed.Source]
                    SOURCE_CLOSE_BUTTON: _ClassVar[UI.Editor.Overlay.Closed.Source]
                SOURCE_UNKNOWN: UI.Editor.Overlay.Closed.Source
                SOURCE_CLICK_OFF_ELEMENT: UI.Editor.Overlay.Closed.Source
                SOURCE_ESCAPE_KEY: UI.Editor.Overlay.Closed.Source
                SOURCE_CLOSE_BUTTON: UI.Editor.Overlay.Closed.Source
                SOURCE_FIELD_NUMBER: _ClassVar[int]
                source: UI.Editor.Overlay.Closed.Source
                def __init__(self, source: _Optional[_Union[UI.Editor.Overlay.Closed.Source, str]] = ...) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            CLOSED_FIELD_NUMBER: _ClassVar[int]
            shown: UI.Editor.Overlay.Shown
            closed: UI.Editor.Overlay.Closed
            def __init__(self, shown: _Optional[_Union[UI.Editor.Overlay.Shown, _Mapping]] = ..., closed: _Optional[_Union[UI.Editor.Overlay.Closed, _Mapping]] = ...) -> None: ...
        OVERLAY_FIELD_NUMBER: _ClassVar[int]
        overlay: UI.Editor.Overlay
        def __init__(self, overlay: _Optional[_Union[UI.Editor.Overlay, _Mapping]] = ...) -> None: ...
    class WhatsNew(_message.Message):
        __slots__ = ("viewed",)
        class Viewed(_message.Message):
            __slots__ = ("version", "resource_name", "view_time")
            VERSION_FIELD_NUMBER: _ClassVar[int]
            RESOURCE_NAME_FIELD_NUMBER: _ClassVar[int]
            VIEW_TIME_FIELD_NUMBER: _ClassVar[int]
            version: str
            resource_name: str
            view_time: int
            def __init__(self, version: _Optional[str] = ..., resource_name: _Optional[str] = ..., view_time: _Optional[int] = ...) -> None: ...
        VIEWED_FIELD_NUMBER: _ClassVar[int]
        viewed: UI.WhatsNew.Viewed
        def __init__(self, viewed: _Optional[_Union[UI.WhatsNew.Viewed, _Mapping]] = ...) -> None: ...
    class ClearGroups(_message.Message):
        __slots__ = ("shown", "create", "delete", "group")
        class Shown(_message.Message):
            __slots__ = ("source",)
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_UNKNOWN: _ClassVar[UI.ClearGroups.Shown.Source]
                SOURCE_APPLICATION_MENU: _ClassVar[UI.ClearGroups.Shown.Source]
                SOURCE_PREVIEW_MENU: _ClassVar[UI.ClearGroups.Shown.Source]
                SOURCE_ACTION_MENU: _ClassVar[UI.ClearGroups.Shown.Source]
            SOURCE_UNKNOWN: UI.ClearGroups.Shown.Source
            SOURCE_APPLICATION_MENU: UI.ClearGroups.Shown.Source
            SOURCE_PREVIEW_MENU: UI.ClearGroups.Shown.Source
            SOURCE_ACTION_MENU: UI.ClearGroups.Shown.Source
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            source: UI.ClearGroups.Shown.Source
            def __init__(self, source: _Optional[_Union[UI.ClearGroups.Shown.Source, str]] = ...) -> None: ...
        class Create(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Delete(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Group(_message.Message):
            __slots__ = ("change_visibility", "change_icon")
            class ChangeVisibility(_message.Message):
                __slots__ = ("visibility",)
                class Visibility(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    VISIBILITY_UNKNOWN: _ClassVar[UI.ClearGroups.Group.ChangeVisibility.Visibility]
                    VISIBILITY_SHOWN: _ClassVar[UI.ClearGroups.Group.ChangeVisibility.Visibility]
                    VISIBILITY_HIDDEN: _ClassVar[UI.ClearGroups.Group.ChangeVisibility.Visibility]
                VISIBILITY_UNKNOWN: UI.ClearGroups.Group.ChangeVisibility.Visibility
                VISIBILITY_SHOWN: UI.ClearGroups.Group.ChangeVisibility.Visibility
                VISIBILITY_HIDDEN: UI.ClearGroups.Group.ChangeVisibility.Visibility
                VISIBILITY_FIELD_NUMBER: _ClassVar[int]
                visibility: UI.ClearGroups.Group.ChangeVisibility.Visibility
                def __init__(self, visibility: _Optional[_Union[UI.ClearGroups.Group.ChangeVisibility.Visibility, str]] = ...) -> None: ...
            class ChangeIcon(_message.Message):
                __slots__ = ("icon_type", "is_tinted")
                class IconType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    ICON_TYPE_UNKNOWN: _ClassVar[UI.ClearGroups.Group.ChangeIcon.IconType]
                    ICON_TYPE_DEFAULT: _ClassVar[UI.ClearGroups.Group.ChangeIcon.IconType]
                    ICON_TYPE_CUSTOM: _ClassVar[UI.ClearGroups.Group.ChangeIcon.IconType]
                ICON_TYPE_UNKNOWN: UI.ClearGroups.Group.ChangeIcon.IconType
                ICON_TYPE_DEFAULT: UI.ClearGroups.Group.ChangeIcon.IconType
                ICON_TYPE_CUSTOM: UI.ClearGroups.Group.ChangeIcon.IconType
                ICON_TYPE_FIELD_NUMBER: _ClassVar[int]
                IS_TINTED_FIELD_NUMBER: _ClassVar[int]
                icon_type: UI.ClearGroups.Group.ChangeIcon.IconType
                is_tinted: bool
                def __init__(self, icon_type: _Optional[_Union[UI.ClearGroups.Group.ChangeIcon.IconType, str]] = ..., is_tinted: bool = ...) -> None: ...
            CHANGE_VISIBILITY_FIELD_NUMBER: _ClassVar[int]
            CHANGE_ICON_FIELD_NUMBER: _ClassVar[int]
            change_visibility: UI.ClearGroups.Group.ChangeVisibility
            change_icon: UI.ClearGroups.Group.ChangeIcon
            def __init__(self, change_visibility: _Optional[_Union[UI.ClearGroups.Group.ChangeVisibility, _Mapping]] = ..., change_icon: _Optional[_Union[UI.ClearGroups.Group.ChangeIcon, _Mapping]] = ...) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        CREATE_FIELD_NUMBER: _ClassVar[int]
        DELETE_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        shown: UI.ClearGroups.Shown
        create: UI.ClearGroups.Create
        delete: UI.ClearGroups.Delete
        group: UI.ClearGroups.Group
        def __init__(self, shown: _Optional[_Union[UI.ClearGroups.Shown, _Mapping]] = ..., create: _Optional[_Union[UI.ClearGroups.Create, _Mapping]] = ..., delete: _Optional[_Union[UI.ClearGroups.Delete, _Mapping]] = ..., group: _Optional[_Union[UI.ClearGroups.Group, _Mapping]] = ...) -> None: ...
    class PreviewArea(_message.Message):
        __slots__ = ("clear_groups",)
        class ClearGroups(_message.Message):
            __slots__ = ("trigger", "changed")
            class Trigger(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Changed(_message.Message):
                __slots__ = ("count",)
                COUNT_FIELD_NUMBER: _ClassVar[int]
                count: int
                def __init__(self, count: _Optional[int] = ...) -> None: ...
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            CHANGED_FIELD_NUMBER: _ClassVar[int]
            trigger: UI.PreviewArea.ClearGroups.Trigger
            changed: UI.PreviewArea.ClearGroups.Changed
            def __init__(self, trigger: _Optional[_Union[UI.PreviewArea.ClearGroups.Trigger, _Mapping]] = ..., changed: _Optional[_Union[UI.PreviewArea.ClearGroups.Changed, _Mapping]] = ...) -> None: ...
        CLEAR_GROUPS_FIELD_NUMBER: _ClassVar[int]
        clear_groups: UI.PreviewArea.ClearGroups
        def __init__(self, clear_groups: _Optional[_Union[UI.PreviewArea.ClearGroups, _Mapping]] = ...) -> None: ...
    class Placeholder(_message.Message):
        __slots__ = ("link", "unlink")
        class Link(_message.Message):
            __slots__ = ("link_type", "link_source")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_UNKNOWN: _ClassVar[UI.Placeholder.Link.Type]
                TYPE_PRESENTATION: _ClassVar[UI.Placeholder.Link.Type]
                TYPE_MEDIA: _ClassVar[UI.Placeholder.Link.Type]
                TYPE_EXTERNAL_PRESENTATION: _ClassVar[UI.Placeholder.Link.Type]
            TYPE_UNKNOWN: UI.Placeholder.Link.Type
            TYPE_PRESENTATION: UI.Placeholder.Link.Type
            TYPE_MEDIA: UI.Placeholder.Link.Type
            TYPE_EXTERNAL_PRESENTATION: UI.Placeholder.Link.Type
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_UNKNOWN: _ClassVar[UI.Placeholder.Link.Source]
                SOURCE_QUICK_SEARCH: _ClassVar[UI.Placeholder.Link.Source]
                SOURCE_IMPORT_BUTTON: _ClassVar[UI.Placeholder.Link.Source]
                SOURCE_CREATE_BUTTON: _ClassVar[UI.Placeholder.Link.Source]
                SOURCE_DRAG_DROP: _ClassVar[UI.Placeholder.Link.Source]
                SOURCE_AUTOMATIC: _ClassVar[UI.Placeholder.Link.Source]
            SOURCE_UNKNOWN: UI.Placeholder.Link.Source
            SOURCE_QUICK_SEARCH: UI.Placeholder.Link.Source
            SOURCE_IMPORT_BUTTON: UI.Placeholder.Link.Source
            SOURCE_CREATE_BUTTON: UI.Placeholder.Link.Source
            SOURCE_DRAG_DROP: UI.Placeholder.Link.Source
            SOURCE_AUTOMATIC: UI.Placeholder.Link.Source
            LINK_TYPE_FIELD_NUMBER: _ClassVar[int]
            LINK_SOURCE_FIELD_NUMBER: _ClassVar[int]
            link_type: UI.Placeholder.Link.Type
            link_source: UI.Placeholder.Link.Source
            def __init__(self, link_type: _Optional[_Union[UI.Placeholder.Link.Type, str]] = ..., link_source: _Optional[_Union[UI.Placeholder.Link.Source, str]] = ...) -> None: ...
        class Unlink(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        LINK_FIELD_NUMBER: _ClassVar[int]
        UNLINK_FIELD_NUMBER: _ClassVar[int]
        link: UI.Placeholder.Link
        unlink: UI.Placeholder.Unlink
        def __init__(self, link: _Optional[_Union[UI.Placeholder.Link, _Mapping]] = ..., unlink: _Optional[_Union[UI.Placeholder.Unlink, _Mapping]] = ...) -> None: ...
    class PlanningCenterLive(_message.Message):
        __slots__ = ("shown",)
        class Shown(_message.Message):
            __slots__ = ("window_type",)
            class WindowType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                WINDOW_TYPE_UNKNOWN: _ClassVar[UI.PlanningCenterLive.Shown.WindowType]
                WINDOW_TYPE_DOCKED: _ClassVar[UI.PlanningCenterLive.Shown.WindowType]
                WINDOW_TYPE_FLOATING: _ClassVar[UI.PlanningCenterLive.Shown.WindowType]
            WINDOW_TYPE_UNKNOWN: UI.PlanningCenterLive.Shown.WindowType
            WINDOW_TYPE_DOCKED: UI.PlanningCenterLive.Shown.WindowType
            WINDOW_TYPE_FLOATING: UI.PlanningCenterLive.Shown.WindowType
            WINDOW_TYPE_FIELD_NUMBER: _ClassVar[int]
            window_type: UI.PlanningCenterLive.Shown.WindowType
            def __init__(self, window_type: _Optional[_Union[UI.PlanningCenterLive.Shown.WindowType, str]] = ...) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        shown: UI.PlanningCenterLive.Shown
        def __init__(self, shown: _Optional[_Union[UI.PlanningCenterLive.Shown, _Mapping]] = ...) -> None: ...
    class NetworkGroup(_message.Message):
        __slots__ = ("create", "add", "join", "invite", "leave", "remove")
        class Create(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Add(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Join(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Invite(_message.Message):
            __slots__ = ("did_accept",)
            DID_ACCEPT_FIELD_NUMBER: _ClassVar[int]
            did_accept: bool
            def __init__(self, did_accept: bool = ...) -> None: ...
        class Leave(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Remove(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        CREATE_FIELD_NUMBER: _ClassVar[int]
        ADD_FIELD_NUMBER: _ClassVar[int]
        JOIN_FIELD_NUMBER: _ClassVar[int]
        INVITE_FIELD_NUMBER: _ClassVar[int]
        LEAVE_FIELD_NUMBER: _ClassVar[int]
        REMOVE_FIELD_NUMBER: _ClassVar[int]
        create: UI.NetworkGroup.Create
        add: UI.NetworkGroup.Add
        join: UI.NetworkGroup.Join
        invite: UI.NetworkGroup.Invite
        leave: UI.NetworkGroup.Leave
        remove: UI.NetworkGroup.Remove
        def __init__(self, create: _Optional[_Union[UI.NetworkGroup.Create, _Mapping]] = ..., add: _Optional[_Union[UI.NetworkGroup.Add, _Mapping]] = ..., join: _Optional[_Union[UI.NetworkGroup.Join, _Mapping]] = ..., invite: _Optional[_Union[UI.NetworkGroup.Invite, _Mapping]] = ..., leave: _Optional[_Union[UI.NetworkGroup.Leave, _Mapping]] = ..., remove: _Optional[_Union[UI.NetworkGroup.Remove, _Mapping]] = ...) -> None: ...
    class CCLI(_message.Message):
        __slots__ = ("report",)
        class Report(_message.Message):
            __slots__ = ("shown", "reset", "export")
            class Shown(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Reset(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            class Export(_message.Message):
                __slots__ = ()
                def __init__(self) -> None: ...
            SHOWN_FIELD_NUMBER: _ClassVar[int]
            RESET_FIELD_NUMBER: _ClassVar[int]
            EXPORT_FIELD_NUMBER: _ClassVar[int]
            shown: UI.CCLI.Report.Shown
            reset: UI.CCLI.Report.Reset
            export: UI.CCLI.Report.Export
            def __init__(self, shown: _Optional[_Union[UI.CCLI.Report.Shown, _Mapping]] = ..., reset: _Optional[_Union[UI.CCLI.Report.Reset, _Mapping]] = ..., export: _Optional[_Union[UI.CCLI.Report.Export, _Mapping]] = ...) -> None: ...
        REPORT_FIELD_NUMBER: _ClassVar[int]
        report: UI.CCLI.Report
        def __init__(self, report: _Optional[_Union[UI.CCLI.Report, _Mapping]] = ...) -> None: ...
    class Capture(_message.Message):
        __slots__ = ("shown",)
        class Shown(_message.Message):
            __slots__ = ("source",)
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_UNKNOWN: _ClassVar[UI.Capture.Shown.Source]
                SOURCE_TOOLBAR: _ClassVar[UI.Capture.Shown.Source]
                SOURCE_ACTION_POPOVER: _ClassVar[UI.Capture.Shown.Source]
                SOURCE_ACTION_CONTEXTUAL_MENU: _ClassVar[UI.Capture.Shown.Source]
                SOURCE_CALENDAR: _ClassVar[UI.Capture.Shown.Source]
                SOURCE_PREFERENCES_RESI: _ClassVar[UI.Capture.Shown.Source]
                SOURCE_MAIN_MENU: _ClassVar[UI.Capture.Shown.Source]
            SOURCE_UNKNOWN: UI.Capture.Shown.Source
            SOURCE_TOOLBAR: UI.Capture.Shown.Source
            SOURCE_ACTION_POPOVER: UI.Capture.Shown.Source
            SOURCE_ACTION_CONTEXTUAL_MENU: UI.Capture.Shown.Source
            SOURCE_CALENDAR: UI.Capture.Shown.Source
            SOURCE_PREFERENCES_RESI: UI.Capture.Shown.Source
            SOURCE_MAIN_MENU: UI.Capture.Shown.Source
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            source: UI.Capture.Shown.Source
            def __init__(self, source: _Optional[_Union[UI.Capture.Shown.Source, str]] = ...) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        shown: UI.Capture.Shown
        def __init__(self, shown: _Optional[_Union[UI.Capture.Shown, _Mapping]] = ...) -> None: ...
    class WelcomeToProPresenter(_message.Message):
        __slots__ = ("shown", "migration", "screen_configuration_help", "download_sample_content", "user_group", "tutorials", "knowledge_base", "blog", "instagram", "facebook")
        class Shown(_message.Message):
            __slots__ = ("source",)
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_FIRST_LAUNCH: _ClassVar[UI.WelcomeToProPresenter.Shown.Source]
                SOURCE_APPLICATION_MENU: _ClassVar[UI.WelcomeToProPresenter.Shown.Source]
            SOURCE_FIRST_LAUNCH: UI.WelcomeToProPresenter.Shown.Source
            SOURCE_APPLICATION_MENU: UI.WelcomeToProPresenter.Shown.Source
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            source: UI.WelcomeToProPresenter.Shown.Source
            def __init__(self, source: _Optional[_Union[UI.WelcomeToProPresenter.Shown.Source, str]] = ...) -> None: ...
        class Migration(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class ScreenConfigurationHelp(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class DownloadSampleContent(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class UserGroup(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Tutorials(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class KnowledgeBase(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Blog(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Instagram(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Facebook(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        MIGRATION_FIELD_NUMBER: _ClassVar[int]
        SCREEN_CONFIGURATION_HELP_FIELD_NUMBER: _ClassVar[int]
        DOWNLOAD_SAMPLE_CONTENT_FIELD_NUMBER: _ClassVar[int]
        USER_GROUP_FIELD_NUMBER: _ClassVar[int]
        TUTORIALS_FIELD_NUMBER: _ClassVar[int]
        KNOWLEDGE_BASE_FIELD_NUMBER: _ClassVar[int]
        BLOG_FIELD_NUMBER: _ClassVar[int]
        INSTAGRAM_FIELD_NUMBER: _ClassVar[int]
        FACEBOOK_FIELD_NUMBER: _ClassVar[int]
        shown: UI.WelcomeToProPresenter.Shown
        migration: UI.WelcomeToProPresenter.Migration
        screen_configuration_help: UI.WelcomeToProPresenter.ScreenConfigurationHelp
        download_sample_content: UI.WelcomeToProPresenter.DownloadSampleContent
        user_group: UI.WelcomeToProPresenter.UserGroup
        tutorials: UI.WelcomeToProPresenter.Tutorials
        knowledge_base: UI.WelcomeToProPresenter.KnowledgeBase
        blog: UI.WelcomeToProPresenter.Blog
        instagram: UI.WelcomeToProPresenter.Instagram
        facebook: UI.WelcomeToProPresenter.Facebook
        def __init__(self, shown: _Optional[_Union[UI.WelcomeToProPresenter.Shown, _Mapping]] = ..., migration: _Optional[_Union[UI.WelcomeToProPresenter.Migration, _Mapping]] = ..., screen_configuration_help: _Optional[_Union[UI.WelcomeToProPresenter.ScreenConfigurationHelp, _Mapping]] = ..., download_sample_content: _Optional[_Union[UI.WelcomeToProPresenter.DownloadSampleContent, _Mapping]] = ..., user_group: _Optional[_Union[UI.WelcomeToProPresenter.UserGroup, _Mapping]] = ..., tutorials: _Optional[_Union[UI.WelcomeToProPresenter.Tutorials, _Mapping]] = ..., knowledge_base: _Optional[_Union[UI.WelcomeToProPresenter.KnowledgeBase, _Mapping]] = ..., blog: _Optional[_Union[UI.WelcomeToProPresenter.Blog, _Mapping]] = ..., instagram: _Optional[_Union[UI.WelcomeToProPresenter.Instagram, _Mapping]] = ..., facebook: _Optional[_Union[UI.WelcomeToProPresenter.Facebook, _Mapping]] = ...) -> None: ...
    class TestPattern(_message.Message):
        __slots__ = ("shown",)
        class Shown(_message.Message):
            __slots__ = ("source",)
            class Source(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SOURCE_APPLICATION_MENU: _ClassVar[UI.TestPattern.Shown.Source]
                SOURCE_SCREEN_CONFIGURATION: _ClassVar[UI.TestPattern.Shown.Source]
            SOURCE_APPLICATION_MENU: UI.TestPattern.Shown.Source
            SOURCE_SCREEN_CONFIGURATION: UI.TestPattern.Shown.Source
            SOURCE_FIELD_NUMBER: _ClassVar[int]
            source: UI.TestPattern.Shown.Source
            def __init__(self, source: _Optional[_Union[UI.TestPattern.Shown.Source, str]] = ...) -> None: ...
        SHOWN_FIELD_NUMBER: _ClassVar[int]
        shown: UI.TestPattern.Shown
        def __init__(self, shown: _Optional[_Union[UI.TestPattern.Shown, _Mapping]] = ...) -> None: ...
    class Preferences(_message.Message):
        __slots__ = ("custom_logo",)
        class CustomLogo(_message.Message):
            __slots__ = ("has_logo",)
            HAS_LOGO_FIELD_NUMBER: _ClassVar[int]
            has_logo: bool
            def __init__(self, has_logo: bool = ...) -> None: ...
        CUSTOM_LOGO_FIELD_NUMBER: _ClassVar[int]
        custom_logo: UI.Preferences.CustomLogo
        def __init__(self, custom_logo: _Optional[_Union[UI.Preferences.CustomLogo, _Mapping]] = ...) -> None: ...
    QUICK_SEARCH_FIELD_NUMBER: _ClassVar[int]
    TOOLBAR_FIELD_NUMBER: _ClassVar[int]
    MAIN_VIEW_FIELD_NUMBER: _ClassVar[int]
    LOOKS_FIELD_NUMBER: _ClassVar[int]
    SCREEN_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    LOWER_RIGHT_FIELD_NUMBER: _ClassVar[int]
    TEXT_INSPECTOR_FIELD_NUMBER: _ClassVar[int]
    SHOW_FIELD_NUMBER: _ClassVar[int]
    IN_APP_STORE_FIELD_NUMBER: _ClassVar[int]
    EDITOR_FIELD_NUMBER: _ClassVar[int]
    WHATS_NEW_FIELD_NUMBER: _ClassVar[int]
    CLEAR_GROUPS_FIELD_NUMBER: _ClassVar[int]
    PREVIEW_AREA_FIELD_NUMBER: _ClassVar[int]
    PLACEHOLDER_FIELD_NUMBER: _ClassVar[int]
    PLANNING_CENTER_LIVE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_GROUP_FIELD_NUMBER: _ClassVar[int]
    CCLI_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_FIELD_NUMBER: _ClassVar[int]
    WELCOMETOPROPRESENTER_FIELD_NUMBER: _ClassVar[int]
    TEST_PATTERN_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    quick_search: UI.QuickSearch
    toolbar: UI.Toolbar
    main_view: UI.MainView
    looks: UI.Looks
    screen_configuration: UI.ScreenConfiguration
    lower_right: UI.LowerRight
    text_inspector: UI.TextInspector
    show: UI.Show
    in_app_store: UI.InAppStore
    editor: UI.Editor
    whats_new: UI.WhatsNew
    clear_groups: UI.ClearGroups
    preview_area: UI.PreviewArea
    placeholder: UI.Placeholder
    planning_center_live: UI.PlanningCenterLive
    network_group: UI.NetworkGroup
    ccli: UI.CCLI
    capture: UI.Capture
    welcomeToProPresenter: UI.WelcomeToProPresenter
    test_pattern: UI.TestPattern
    preferences: UI.Preferences
    def __init__(self, quick_search: _Optional[_Union[UI.QuickSearch, _Mapping]] = ..., toolbar: _Optional[_Union[UI.Toolbar, _Mapping]] = ..., main_view: _Optional[_Union[UI.MainView, _Mapping]] = ..., looks: _Optional[_Union[UI.Looks, _Mapping]] = ..., screen_configuration: _Optional[_Union[UI.ScreenConfiguration, _Mapping]] = ..., lower_right: _Optional[_Union[UI.LowerRight, _Mapping]] = ..., text_inspector: _Optional[_Union[UI.TextInspector, _Mapping]] = ..., show: _Optional[_Union[UI.Show, _Mapping]] = ..., in_app_store: _Optional[_Union[UI.InAppStore, _Mapping]] = ..., editor: _Optional[_Union[UI.Editor, _Mapping]] = ..., whats_new: _Optional[_Union[UI.WhatsNew, _Mapping]] = ..., clear_groups: _Optional[_Union[UI.ClearGroups, _Mapping]] = ..., preview_area: _Optional[_Union[UI.PreviewArea, _Mapping]] = ..., placeholder: _Optional[_Union[UI.Placeholder, _Mapping]] = ..., planning_center_live: _Optional[_Union[UI.PlanningCenterLive, _Mapping]] = ..., network_group: _Optional[_Union[UI.NetworkGroup, _Mapping]] = ..., ccli: _Optional[_Union[UI.CCLI, _Mapping]] = ..., capture: _Optional[_Union[UI.Capture, _Mapping]] = ..., welcomeToProPresenter: _Optional[_Union[UI.WelcomeToProPresenter, _Mapping]] = ..., test_pattern: _Optional[_Union[UI.TestPattern, _Mapping]] = ..., preferences: _Optional[_Union[UI.Preferences, _Mapping]] = ...) -> None: ...
