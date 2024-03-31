import analyticsMultiTracks_pb2 as _analyticsMultiTracks_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Startup(_message.Message):
    __slots__ = ("looks", "screen_configuration", "preferences", "screens", "planning_center", "song_select", "audio", "communications", "resi", "interface", "content", "themes", "macro", "clear_group", "key_mapping", "multitracks", "network_link", "capture")
    class Looks(_message.Message):
        __slots__ = ("number_presets",)
        NUMBER_PRESETS_FIELD_NUMBER: _ClassVar[int]
        number_presets: int
        def __init__(self, number_presets: _Optional[int] = ...) -> None: ...
    class ScreenConfiguration(_message.Message):
        __slots__ = ("summary", "output", "single", "mirrored", "edge_blend", "grouped")
        class Summary(_message.Message):
            __slots__ = ("total_screens", "audience_screen_count", "stage_screen_count")
            TOTAL_SCREENS_FIELD_NUMBER: _ClassVar[int]
            AUDIENCE_SCREEN_COUNT_FIELD_NUMBER: _ClassVar[int]
            STAGE_SCREEN_COUNT_FIELD_NUMBER: _ClassVar[int]
            total_screens: int
            audience_screen_count: int
            stage_screen_count: int
            def __init__(self, total_screens: _Optional[int] = ..., audience_screen_count: _Optional[int] = ..., stage_screen_count: _Optional[int] = ...) -> None: ...
        class Output(_message.Message):
            __slots__ = ("proscreen_type", "output_type", "color_correction_enabled", "corner_pin_enabled", "alignment", "width", "height", "screen")
            class ProScreenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PRO_SCREEN_TYPE_UNKNOWN: _ClassVar[Startup.ScreenConfiguration.Output.ProScreenType]
                PRO_SCREEN_TYPE_SINGLE: _ClassVar[Startup.ScreenConfiguration.Output.ProScreenType]
                PRO_SCREEN_TYPE_MIRRORED: _ClassVar[Startup.ScreenConfiguration.Output.ProScreenType]
                PRO_SCREEN_TYPE_EDGE_BLEND: _ClassVar[Startup.ScreenConfiguration.Output.ProScreenType]
                PRO_SCREEN_TYPE_GROUPED: _ClassVar[Startup.ScreenConfiguration.Output.ProScreenType]
            PRO_SCREEN_TYPE_UNKNOWN: Startup.ScreenConfiguration.Output.ProScreenType
            PRO_SCREEN_TYPE_SINGLE: Startup.ScreenConfiguration.Output.ProScreenType
            PRO_SCREEN_TYPE_MIRRORED: Startup.ScreenConfiguration.Output.ProScreenType
            PRO_SCREEN_TYPE_EDGE_BLEND: Startup.ScreenConfiguration.Output.ProScreenType
            PRO_SCREEN_TYPE_GROUPED: Startup.ScreenConfiguration.Output.ProScreenType
            class OutputType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                OUTPUT_TYPE_UNKNOWN: _ClassVar[Startup.ScreenConfiguration.Output.OutputType]
                OUTPUT_TYPE_SDI: _ClassVar[Startup.ScreenConfiguration.Output.OutputType]
                OUTPUT_TYPE_NDI: _ClassVar[Startup.ScreenConfiguration.Output.OutputType]
                OUTPUT_TYPE_SYPHON: _ClassVar[Startup.ScreenConfiguration.Output.OutputType]
                OUTPUT_TYPE_SYSTEM: _ClassVar[Startup.ScreenConfiguration.Output.OutputType]
                OUTPUT_TYPE_PLACEHOLDER: _ClassVar[Startup.ScreenConfiguration.Output.OutputType]
                OUTPUT_TYPE_DVI: _ClassVar[Startup.ScreenConfiguration.Output.OutputType]
            OUTPUT_TYPE_UNKNOWN: Startup.ScreenConfiguration.Output.OutputType
            OUTPUT_TYPE_SDI: Startup.ScreenConfiguration.Output.OutputType
            OUTPUT_TYPE_NDI: Startup.ScreenConfiguration.Output.OutputType
            OUTPUT_TYPE_SYPHON: Startup.ScreenConfiguration.Output.OutputType
            OUTPUT_TYPE_SYSTEM: Startup.ScreenConfiguration.Output.OutputType
            OUTPUT_TYPE_PLACEHOLDER: Startup.ScreenConfiguration.Output.OutputType
            OUTPUT_TYPE_DVI: Startup.ScreenConfiguration.Output.OutputType
            class Alignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ALIGNMENT_UNKNOWN: _ClassVar[Startup.ScreenConfiguration.Output.Alignment]
                ALIGNMENT_FULL: _ClassVar[Startup.ScreenConfiguration.Output.Alignment]
                ALIGNMENT_2X1: _ClassVar[Startup.ScreenConfiguration.Output.Alignment]
                ALIGNMENT_3X1: _ClassVar[Startup.ScreenConfiguration.Output.Alignment]
                ALIGNMENT_2X2: _ClassVar[Startup.ScreenConfiguration.Output.Alignment]
                ALIGNMENT_CUSTOM: _ClassVar[Startup.ScreenConfiguration.Output.Alignment]
            ALIGNMENT_UNKNOWN: Startup.ScreenConfiguration.Output.Alignment
            ALIGNMENT_FULL: Startup.ScreenConfiguration.Output.Alignment
            ALIGNMENT_2X1: Startup.ScreenConfiguration.Output.Alignment
            ALIGNMENT_3X1: Startup.ScreenConfiguration.Output.Alignment
            ALIGNMENT_2X2: Startup.ScreenConfiguration.Output.Alignment
            ALIGNMENT_CUSTOM: Startup.ScreenConfiguration.Output.Alignment
            PROSCREEN_TYPE_FIELD_NUMBER: _ClassVar[int]
            OUTPUT_TYPE_FIELD_NUMBER: _ClassVar[int]
            COLOR_CORRECTION_ENABLED_FIELD_NUMBER: _ClassVar[int]
            CORNER_PIN_ENABLED_FIELD_NUMBER: _ClassVar[int]
            ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
            WIDTH_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            SCREEN_FIELD_NUMBER: _ClassVar[int]
            proscreen_type: Startup.ScreenConfiguration.Output.ProScreenType
            output_type: Startup.ScreenConfiguration.Output.OutputType
            color_correction_enabled: bool
            corner_pin_enabled: bool
            alignment: Startup.ScreenConfiguration.Output.Alignment
            width: int
            height: int
            screen: Startup.ScreenConfiguration.Screen
            def __init__(self, proscreen_type: _Optional[_Union[Startup.ScreenConfiguration.Output.ProScreenType, str]] = ..., output_type: _Optional[_Union[Startup.ScreenConfiguration.Output.OutputType, str]] = ..., color_correction_enabled: bool = ..., corner_pin_enabled: bool = ..., alignment: _Optional[_Union[Startup.ScreenConfiguration.Output.Alignment, str]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., screen: _Optional[_Union[Startup.ScreenConfiguration.Screen, _Mapping]] = ...) -> None: ...
        class Single(_message.Message):
            __slots__ = ("screen_type", "screen_color_enabled")
            class ScreenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SCREEN_TYPE_UNKNOWN: _ClassVar[Startup.ScreenConfiguration.Single.ScreenType]
                SCREEN_TYPE_AUDIENCE: _ClassVar[Startup.ScreenConfiguration.Single.ScreenType]
                SCREEN_TYPE_STAGE: _ClassVar[Startup.ScreenConfiguration.Single.ScreenType]
            SCREEN_TYPE_UNKNOWN: Startup.ScreenConfiguration.Single.ScreenType
            SCREEN_TYPE_AUDIENCE: Startup.ScreenConfiguration.Single.ScreenType
            SCREEN_TYPE_STAGE: Startup.ScreenConfiguration.Single.ScreenType
            SCREEN_TYPE_FIELD_NUMBER: _ClassVar[int]
            SCREEN_COLOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
            screen_type: Startup.ScreenConfiguration.Single.ScreenType
            screen_color_enabled: bool
            def __init__(self, screen_type: _Optional[_Union[Startup.ScreenConfiguration.Single.ScreenType, str]] = ..., screen_color_enabled: bool = ...) -> None: ...
        class Mirrored(_message.Message):
            __slots__ = ("screen_type", "screen_color_enabled", "count")
            class ScreenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SCREEN_TYPE_UNKNOWN: _ClassVar[Startup.ScreenConfiguration.Mirrored.ScreenType]
                SCREEN_TYPE_AUDIENCE: _ClassVar[Startup.ScreenConfiguration.Mirrored.ScreenType]
                SCREEN_TYPE_STAGE: _ClassVar[Startup.ScreenConfiguration.Mirrored.ScreenType]
            SCREEN_TYPE_UNKNOWN: Startup.ScreenConfiguration.Mirrored.ScreenType
            SCREEN_TYPE_AUDIENCE: Startup.ScreenConfiguration.Mirrored.ScreenType
            SCREEN_TYPE_STAGE: Startup.ScreenConfiguration.Mirrored.ScreenType
            SCREEN_TYPE_FIELD_NUMBER: _ClassVar[int]
            SCREEN_COLOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            screen_type: Startup.ScreenConfiguration.Mirrored.ScreenType
            screen_color_enabled: bool
            count: int
            def __init__(self, screen_type: _Optional[_Union[Startup.ScreenConfiguration.Mirrored.ScreenType, str]] = ..., screen_color_enabled: bool = ..., count: _Optional[int] = ...) -> None: ...
        class EdgeBlend(_message.Message):
            __slots__ = ("screen_type", "screen_color_enabled", "count")
            class ScreenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SCREEN_TYPE_UNKNOWN: _ClassVar[Startup.ScreenConfiguration.EdgeBlend.ScreenType]
                SCREEN_TYPE_AUDIENCE: _ClassVar[Startup.ScreenConfiguration.EdgeBlend.ScreenType]
                SCREEN_TYPE_STAGE: _ClassVar[Startup.ScreenConfiguration.EdgeBlend.ScreenType]
            SCREEN_TYPE_UNKNOWN: Startup.ScreenConfiguration.EdgeBlend.ScreenType
            SCREEN_TYPE_AUDIENCE: Startup.ScreenConfiguration.EdgeBlend.ScreenType
            SCREEN_TYPE_STAGE: Startup.ScreenConfiguration.EdgeBlend.ScreenType
            SCREEN_TYPE_FIELD_NUMBER: _ClassVar[int]
            SCREEN_COLOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
            COUNT_FIELD_NUMBER: _ClassVar[int]
            screen_type: Startup.ScreenConfiguration.EdgeBlend.ScreenType
            screen_color_enabled: bool
            count: int
            def __init__(self, screen_type: _Optional[_Union[Startup.ScreenConfiguration.EdgeBlend.ScreenType, str]] = ..., screen_color_enabled: bool = ..., count: _Optional[int] = ...) -> None: ...
        class Grouped(_message.Message):
            __slots__ = ("screen_type", "screen_color_enabled", "columns", "rows")
            class ScreenType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SCREEN_TYPE_UNKNOWN: _ClassVar[Startup.ScreenConfiguration.Grouped.ScreenType]
                SCREEN_TYPE_AUDIENCE: _ClassVar[Startup.ScreenConfiguration.Grouped.ScreenType]
                SCREEN_TYPE_STAGE: _ClassVar[Startup.ScreenConfiguration.Grouped.ScreenType]
            SCREEN_TYPE_UNKNOWN: Startup.ScreenConfiguration.Grouped.ScreenType
            SCREEN_TYPE_AUDIENCE: Startup.ScreenConfiguration.Grouped.ScreenType
            SCREEN_TYPE_STAGE: Startup.ScreenConfiguration.Grouped.ScreenType
            SCREEN_TYPE_FIELD_NUMBER: _ClassVar[int]
            SCREEN_COLOR_ENABLED_FIELD_NUMBER: _ClassVar[int]
            COLUMNS_FIELD_NUMBER: _ClassVar[int]
            ROWS_FIELD_NUMBER: _ClassVar[int]
            screen_type: Startup.ScreenConfiguration.Grouped.ScreenType
            screen_color_enabled: bool
            columns: int
            rows: int
            def __init__(self, screen_type: _Optional[_Union[Startup.ScreenConfiguration.Grouped.ScreenType, str]] = ..., screen_color_enabled: bool = ..., columns: _Optional[int] = ..., rows: _Optional[int] = ...) -> None: ...
        class Screen(_message.Message):
            __slots__ = ("alpha_key_mode", "alpha_device")
            class AlphaKeyMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ALPHA_KEY_MODE_NONE: _ClassVar[Startup.ScreenConfiguration.Screen.AlphaKeyMode]
                ALPHA_KEY_MODE_PREMULTIPLIED: _ClassVar[Startup.ScreenConfiguration.Screen.AlphaKeyMode]
                ALPHA_KEY_MODE_STRAIGHT: _ClassVar[Startup.ScreenConfiguration.Screen.AlphaKeyMode]
            ALPHA_KEY_MODE_NONE: Startup.ScreenConfiguration.Screen.AlphaKeyMode
            ALPHA_KEY_MODE_PREMULTIPLIED: Startup.ScreenConfiguration.Screen.AlphaKeyMode
            ALPHA_KEY_MODE_STRAIGHT: Startup.ScreenConfiguration.Screen.AlphaKeyMode
            class AlphaDevice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ALPHA_DEVICE_NONE: _ClassVar[Startup.ScreenConfiguration.Screen.AlphaDevice]
                ALPHA_DEVICE_SELF: _ClassVar[Startup.ScreenConfiguration.Screen.AlphaDevice]
                ALPHA_DEVICE_OTHER: _ClassVar[Startup.ScreenConfiguration.Screen.AlphaDevice]
            ALPHA_DEVICE_NONE: Startup.ScreenConfiguration.Screen.AlphaDevice
            ALPHA_DEVICE_SELF: Startup.ScreenConfiguration.Screen.AlphaDevice
            ALPHA_DEVICE_OTHER: Startup.ScreenConfiguration.Screen.AlphaDevice
            ALPHA_KEY_MODE_FIELD_NUMBER: _ClassVar[int]
            ALPHA_DEVICE_FIELD_NUMBER: _ClassVar[int]
            alpha_key_mode: Startup.ScreenConfiguration.Screen.AlphaKeyMode
            alpha_device: Startup.ScreenConfiguration.Screen.AlphaDevice
            def __init__(self, alpha_key_mode: _Optional[_Union[Startup.ScreenConfiguration.Screen.AlphaKeyMode, str]] = ..., alpha_device: _Optional[_Union[Startup.ScreenConfiguration.Screen.AlphaDevice, str]] = ...) -> None: ...
        SUMMARY_FIELD_NUMBER: _ClassVar[int]
        OUTPUT_FIELD_NUMBER: _ClassVar[int]
        SINGLE_FIELD_NUMBER: _ClassVar[int]
        MIRRORED_FIELD_NUMBER: _ClassVar[int]
        EDGE_BLEND_FIELD_NUMBER: _ClassVar[int]
        GROUPED_FIELD_NUMBER: _ClassVar[int]
        summary: Startup.ScreenConfiguration.Summary
        output: Startup.ScreenConfiguration.Output
        single: Startup.ScreenConfiguration.Single
        mirrored: Startup.ScreenConfiguration.Mirrored
        edge_blend: Startup.ScreenConfiguration.EdgeBlend
        grouped: Startup.ScreenConfiguration.Grouped
        def __init__(self, summary: _Optional[_Union[Startup.ScreenConfiguration.Summary, _Mapping]] = ..., output: _Optional[_Union[Startup.ScreenConfiguration.Output, _Mapping]] = ..., single: _Optional[_Union[Startup.ScreenConfiguration.Single, _Mapping]] = ..., mirrored: _Optional[_Union[Startup.ScreenConfiguration.Mirrored, _Mapping]] = ..., edge_blend: _Optional[_Union[Startup.ScreenConfiguration.EdgeBlend, _Mapping]] = ..., grouped: _Optional[_Union[Startup.ScreenConfiguration.Grouped, _Mapping]] = ...) -> None: ...
    class Preferences(_message.Message):
        __slots__ = ("house_of_worship", "has_custom_logo", "copyright_enabled", "copyright_style", "copyright_has_license", "render_mode", "suppress_auto_start", "manage_media_automatically", "search_paths_relink", "update_channel")
        class CopyrightStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            COPYRIGHT_STYLE_UNKNOWN: _ClassVar[Startup.Preferences.CopyrightStyle]
            COPYRIGHT_STYLE_FIRST: _ClassVar[Startup.Preferences.CopyrightStyle]
            COPYRIGHT_STYLE_LAST: _ClassVar[Startup.Preferences.CopyrightStyle]
            COPYRIGHT_STYLE_FIRST_AND_LAST: _ClassVar[Startup.Preferences.CopyrightStyle]
            COPYRIGHT_STYLE_ALL_SLIDES: _ClassVar[Startup.Preferences.CopyrightStyle]
        COPYRIGHT_STYLE_UNKNOWN: Startup.Preferences.CopyrightStyle
        COPYRIGHT_STYLE_FIRST: Startup.Preferences.CopyrightStyle
        COPYRIGHT_STYLE_LAST: Startup.Preferences.CopyrightStyle
        COPYRIGHT_STYLE_FIRST_AND_LAST: Startup.Preferences.CopyrightStyle
        COPYRIGHT_STYLE_ALL_SLIDES: Startup.Preferences.CopyrightStyle
        class RenderMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            RENDER_MODE_UNKNOWN: _ClassVar[Startup.Preferences.RenderMode]
            RENDER_MODE_OPENGL: _ClassVar[Startup.Preferences.RenderMode]
            RENDER_MODE_METAL: _ClassVar[Startup.Preferences.RenderMode]
            RENDER_MODE_DIRECTX: _ClassVar[Startup.Preferences.RenderMode]
        RENDER_MODE_UNKNOWN: Startup.Preferences.RenderMode
        RENDER_MODE_OPENGL: Startup.Preferences.RenderMode
        RENDER_MODE_METAL: Startup.Preferences.RenderMode
        RENDER_MODE_DIRECTX: Startup.Preferences.RenderMode
        class UpdateChannel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            UPDATE_CHANNEL_UNKNOWN: _ClassVar[Startup.Preferences.UpdateChannel]
            UPDATE_CHANNEL_RELEASE: _ClassVar[Startup.Preferences.UpdateChannel]
            UPDATE_CHANNEL_BETA: _ClassVar[Startup.Preferences.UpdateChannel]
        UPDATE_CHANNEL_UNKNOWN: Startup.Preferences.UpdateChannel
        UPDATE_CHANNEL_RELEASE: Startup.Preferences.UpdateChannel
        UPDATE_CHANNEL_BETA: Startup.Preferences.UpdateChannel
        HOUSE_OF_WORSHIP_FIELD_NUMBER: _ClassVar[int]
        HAS_CUSTOM_LOGO_FIELD_NUMBER: _ClassVar[int]
        COPYRIGHT_ENABLED_FIELD_NUMBER: _ClassVar[int]
        COPYRIGHT_STYLE_FIELD_NUMBER: _ClassVar[int]
        COPYRIGHT_HAS_LICENSE_FIELD_NUMBER: _ClassVar[int]
        RENDER_MODE_FIELD_NUMBER: _ClassVar[int]
        SUPPRESS_AUTO_START_FIELD_NUMBER: _ClassVar[int]
        MANAGE_MEDIA_AUTOMATICALLY_FIELD_NUMBER: _ClassVar[int]
        SEARCH_PATHS_RELINK_FIELD_NUMBER: _ClassVar[int]
        UPDATE_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        house_of_worship: bool
        has_custom_logo: bool
        copyright_enabled: bool
        copyright_style: Startup.Preferences.CopyrightStyle
        copyright_has_license: bool
        render_mode: Startup.Preferences.RenderMode
        suppress_auto_start: bool
        manage_media_automatically: bool
        search_paths_relink: bool
        update_channel: Startup.Preferences.UpdateChannel
        def __init__(self, house_of_worship: bool = ..., has_custom_logo: bool = ..., copyright_enabled: bool = ..., copyright_style: _Optional[_Union[Startup.Preferences.CopyrightStyle, str]] = ..., copyright_has_license: bool = ..., render_mode: _Optional[_Union[Startup.Preferences.RenderMode, str]] = ..., suppress_auto_start: bool = ..., manage_media_automatically: bool = ..., search_paths_relink: bool = ..., update_channel: _Optional[_Union[Startup.Preferences.UpdateChannel, str]] = ...) -> None: ...
    class Screens(_message.Message):
        __slots__ = ("show_screens_launch", "show_performance_on_screen", "ignore_background_colors", "show_keynote_ppt_screens")
        SHOW_SCREENS_LAUNCH_FIELD_NUMBER: _ClassVar[int]
        SHOW_PERFORMANCE_ON_SCREEN_FIELD_NUMBER: _ClassVar[int]
        IGNORE_BACKGROUND_COLORS_FIELD_NUMBER: _ClassVar[int]
        SHOW_KEYNOTE_PPT_SCREENS_FIELD_NUMBER: _ClassVar[int]
        show_screens_launch: bool
        show_performance_on_screen: bool
        ignore_background_colors: bool
        show_keynote_ppt_screens: bool
        def __init__(self, show_screens_launch: bool = ..., show_performance_on_screen: bool = ..., ignore_background_colors: bool = ..., show_keynote_ppt_screens: bool = ...) -> None: ...
    class PlanningCenter(_message.Message):
        __slots__ = ("logged_in", "auto_update", "match_songs", "show_history", "make_arrangements", "auto_upload", "auto_download")
        LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
        AUTO_UPDATE_FIELD_NUMBER: _ClassVar[int]
        MATCH_SONGS_FIELD_NUMBER: _ClassVar[int]
        SHOW_HISTORY_FIELD_NUMBER: _ClassVar[int]
        MAKE_ARRANGEMENTS_FIELD_NUMBER: _ClassVar[int]
        AUTO_UPLOAD_FIELD_NUMBER: _ClassVar[int]
        AUTO_DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
        logged_in: bool
        auto_update: bool
        match_songs: bool
        show_history: bool
        make_arrangements: bool
        auto_upload: bool
        auto_download: bool
        def __init__(self, logged_in: bool = ..., auto_update: bool = ..., match_songs: bool = ..., show_history: bool = ..., make_arrangements: bool = ..., auto_upload: bool = ..., auto_download: bool = ...) -> None: ...
    class SongSelect(_message.Message):
        __slots__ = ("logged_in",)
        LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
        logged_in: bool
        def __init__(self, logged_in: bool = ...) -> None: ...
    class Audio(_message.Message):
        __slots__ = ("bus_count", "inspector_device", "inspector_routing", "main_device", "main_routing", "main_delay", "sdi_ndi", "sdi_ndi_routing", "sdi_ndi_delay")
        class AudioDevice(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AUDIO_DEVICE_UNKNOWN: _ClassVar[Startup.Audio.AudioDevice]
            AUDIO_DEVICE_MAIN: _ClassVar[Startup.Audio.AudioDevice]
            AUDIO_DEVICE_SYSTEM: _ClassVar[Startup.Audio.AudioDevice]
            AUDIO_DEVICE_OTHER: _ClassVar[Startup.Audio.AudioDevice]
            AUDIO_DEVICE_NONE: _ClassVar[Startup.Audio.AudioDevice]
        AUDIO_DEVICE_UNKNOWN: Startup.Audio.AudioDevice
        AUDIO_DEVICE_MAIN: Startup.Audio.AudioDevice
        AUDIO_DEVICE_SYSTEM: Startup.Audio.AudioDevice
        AUDIO_DEVICE_OTHER: Startup.Audio.AudioDevice
        AUDIO_DEVICE_NONE: Startup.Audio.AudioDevice
        class InspectorRouting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            INSPECTOR_ROUTING_UNKNOWN: _ClassVar[Startup.Audio.InspectorRouting]
            INSPECTOR_ROUTING_DEFAULT: _ClassVar[Startup.Audio.InspectorRouting]
            INSPECTOR_ROUTING_CUSTOM: _ClassVar[Startup.Audio.InspectorRouting]
        INSPECTOR_ROUTING_UNKNOWN: Startup.Audio.InspectorRouting
        INSPECTOR_ROUTING_DEFAULT: Startup.Audio.InspectorRouting
        INSPECTOR_ROUTING_CUSTOM: Startup.Audio.InspectorRouting
        class AudioRouting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            AUDIO_ROUTING_UNKNOWN: _ClassVar[Startup.Audio.AudioRouting]
            AUDIO_ROUTING_DEFAULT: _ClassVar[Startup.Audio.AudioRouting]
            AUDIO_ROUTING_CUSTOM: _ClassVar[Startup.Audio.AudioRouting]
        AUDIO_ROUTING_UNKNOWN: Startup.Audio.AudioRouting
        AUDIO_ROUTING_DEFAULT: Startup.Audio.AudioRouting
        AUDIO_ROUTING_CUSTOM: Startup.Audio.AudioRouting
        BUS_COUNT_FIELD_NUMBER: _ClassVar[int]
        INSPECTOR_DEVICE_FIELD_NUMBER: _ClassVar[int]
        INSPECTOR_ROUTING_FIELD_NUMBER: _ClassVar[int]
        MAIN_DEVICE_FIELD_NUMBER: _ClassVar[int]
        MAIN_ROUTING_FIELD_NUMBER: _ClassVar[int]
        MAIN_DELAY_FIELD_NUMBER: _ClassVar[int]
        SDI_NDI_FIELD_NUMBER: _ClassVar[int]
        SDI_NDI_ROUTING_FIELD_NUMBER: _ClassVar[int]
        SDI_NDI_DELAY_FIELD_NUMBER: _ClassVar[int]
        bus_count: int
        inspector_device: Startup.Audio.AudioDevice
        inspector_routing: Startup.Audio.InspectorRouting
        main_device: Startup.Audio.AudioDevice
        main_routing: Startup.Audio.AudioRouting
        main_delay: int
        sdi_ndi: bool
        sdi_ndi_routing: Startup.Audio.AudioRouting
        sdi_ndi_delay: int
        def __init__(self, bus_count: _Optional[int] = ..., inspector_device: _Optional[_Union[Startup.Audio.AudioDevice, str]] = ..., inspector_routing: _Optional[_Union[Startup.Audio.InspectorRouting, str]] = ..., main_device: _Optional[_Union[Startup.Audio.AudioDevice, str]] = ..., main_routing: _Optional[_Union[Startup.Audio.AudioRouting, str]] = ..., main_delay: _Optional[int] = ..., sdi_ndi: bool = ..., sdi_ndi_routing: _Optional[_Union[Startup.Audio.AudioRouting, str]] = ..., sdi_ndi_delay: _Optional[int] = ...) -> None: ...
    class Communications(_message.Message):
        __slots__ = ("total_device_count",)
        TOTAL_DEVICE_COUNT_FIELD_NUMBER: _ClassVar[int]
        total_device_count: int
        def __init__(self, total_device_count: _Optional[int] = ...) -> None: ...
    class Resi(_message.Message):
        __slots__ = ("logged_in",)
        LOGGED_IN_FIELD_NUMBER: _ClassVar[int]
        logged_in: bool
        def __init__(self, logged_in: bool = ...) -> None: ...
    class Interface(_message.Message):
        __slots__ = ("library_outline", "media_outline", "audio_outline", "continuous_playlist", "media_bin", "presentation_view_style", "presentation_grid_column_count", "presentation_table_column_count", "media_bin_view_style", "media_bin_grid_column_count", "media_bin_table_column_count", "presentation_transition", "media_transition", "audio_shuffle")
        class SplitViewState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SPLIT_VIEW_STATE_UNKNOWN: _ClassVar[Startup.Interface.SplitViewState]
            SPLIT_VIEW_STATE_COLLAPSED: _ClassVar[Startup.Interface.SplitViewState]
            SPLIT_VIEW_STATE_EXPANDED: _ClassVar[Startup.Interface.SplitViewState]
        SPLIT_VIEW_STATE_UNKNOWN: Startup.Interface.SplitViewState
        SPLIT_VIEW_STATE_COLLAPSED: Startup.Interface.SplitViewState
        SPLIT_VIEW_STATE_EXPANDED: Startup.Interface.SplitViewState
        class PresentationViewStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PRESENTATION_VIEW_STYLE_UNKNOWN: _ClassVar[Startup.Interface.PresentationViewStyle]
            PRESENTATION_VIEW_STYLE_GRID: _ClassVar[Startup.Interface.PresentationViewStyle]
            PRESENTATION_VIEW_STYLE_EASY: _ClassVar[Startup.Interface.PresentationViewStyle]
            PRESENTATION_VIEW_STYLE_TABLE: _ClassVar[Startup.Interface.PresentationViewStyle]
        PRESENTATION_VIEW_STYLE_UNKNOWN: Startup.Interface.PresentationViewStyle
        PRESENTATION_VIEW_STYLE_GRID: Startup.Interface.PresentationViewStyle
        PRESENTATION_VIEW_STYLE_EASY: Startup.Interface.PresentationViewStyle
        PRESENTATION_VIEW_STYLE_TABLE: Startup.Interface.PresentationViewStyle
        class MediaBinViewStyle(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            MEDIA_BIN_VIEW_STYLE_UNKNOWN: _ClassVar[Startup.Interface.MediaBinViewStyle]
            MEDIA_BIN_VIEW_STYLE_GRID: _ClassVar[Startup.Interface.MediaBinViewStyle]
            MEDIA_BIN_VIEW_STYLE_TABLE: _ClassVar[Startup.Interface.MediaBinViewStyle]
        MEDIA_BIN_VIEW_STYLE_UNKNOWN: Startup.Interface.MediaBinViewStyle
        MEDIA_BIN_VIEW_STYLE_GRID: Startup.Interface.MediaBinViewStyle
        MEDIA_BIN_VIEW_STYLE_TABLE: Startup.Interface.MediaBinViewStyle
        LIBRARY_OUTLINE_FIELD_NUMBER: _ClassVar[int]
        MEDIA_OUTLINE_FIELD_NUMBER: _ClassVar[int]
        AUDIO_OUTLINE_FIELD_NUMBER: _ClassVar[int]
        CONTINUOUS_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_VIEW_STYLE_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_GRID_COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_TABLE_COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_VIEW_STYLE_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_GRID_COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_TABLE_COLUMN_COUNT_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_TRANSITION_FIELD_NUMBER: _ClassVar[int]
        MEDIA_TRANSITION_FIELD_NUMBER: _ClassVar[int]
        AUDIO_SHUFFLE_FIELD_NUMBER: _ClassVar[int]
        library_outline: Startup.Interface.SplitViewState
        media_outline: Startup.Interface.SplitViewState
        audio_outline: Startup.Interface.SplitViewState
        continuous_playlist: bool
        media_bin: Startup.Interface.SplitViewState
        presentation_view_style: Startup.Interface.PresentationViewStyle
        presentation_grid_column_count: int
        presentation_table_column_count: int
        media_bin_view_style: Startup.Interface.MediaBinViewStyle
        media_bin_grid_column_count: int
        media_bin_table_column_count: int
        presentation_transition: str
        media_transition: str
        audio_shuffle: bool
        def __init__(self, library_outline: _Optional[_Union[Startup.Interface.SplitViewState, str]] = ..., media_outline: _Optional[_Union[Startup.Interface.SplitViewState, str]] = ..., audio_outline: _Optional[_Union[Startup.Interface.SplitViewState, str]] = ..., continuous_playlist: bool = ..., media_bin: _Optional[_Union[Startup.Interface.SplitViewState, str]] = ..., presentation_view_style: _Optional[_Union[Startup.Interface.PresentationViewStyle, str]] = ..., presentation_grid_column_count: _Optional[int] = ..., presentation_table_column_count: _Optional[int] = ..., media_bin_view_style: _Optional[_Union[Startup.Interface.MediaBinViewStyle, str]] = ..., media_bin_grid_column_count: _Optional[int] = ..., media_bin_table_column_count: _Optional[int] = ..., presentation_transition: _Optional[str] = ..., media_transition: _Optional[str] = ..., audio_shuffle: bool = ...) -> None: ...
    class Content(_message.Message):
        __slots__ = ("library_count", "library_playlist_count", "library_playlist_folder_count", "library_playlist_max_depth", "media_bin_total_playlist_count", "media_bin_playlist_folder_count", "media_bin_playlist_max_depth", "media_bin_normal_playlist_count", "media_bin_smart_playlist_count", "media_bin_video_input_count", "audio_bin_playlist_count", "audio_bin_playlist_folder_count", "audio_bin_playlist_max_depth", "timer_count", "messages_count", "props_count", "stage_layout_count", "macros_count", "macros_collections_count", "macros_custom_icons", "ubiquitous_show_directory")
        LIBRARY_COUNT_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_PLAYLIST_COUNT_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_PLAYLIST_FOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
        LIBRARY_PLAYLIST_MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_TOTAL_PLAYLIST_COUNT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_PLAYLIST_FOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_PLAYLIST_MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_NORMAL_PLAYLIST_COUNT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_SMART_PLAYLIST_COUNT_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_VIDEO_INPUT_COUNT_FIELD_NUMBER: _ClassVar[int]
        AUDIO_BIN_PLAYLIST_COUNT_FIELD_NUMBER: _ClassVar[int]
        AUDIO_BIN_PLAYLIST_FOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
        AUDIO_BIN_PLAYLIST_MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
        TIMER_COUNT_FIELD_NUMBER: _ClassVar[int]
        MESSAGES_COUNT_FIELD_NUMBER: _ClassVar[int]
        PROPS_COUNT_FIELD_NUMBER: _ClassVar[int]
        STAGE_LAYOUT_COUNT_FIELD_NUMBER: _ClassVar[int]
        MACROS_COUNT_FIELD_NUMBER: _ClassVar[int]
        MACROS_COLLECTIONS_COUNT_FIELD_NUMBER: _ClassVar[int]
        MACROS_CUSTOM_ICONS_FIELD_NUMBER: _ClassVar[int]
        UBIQUITOUS_SHOW_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
        library_count: int
        library_playlist_count: int
        library_playlist_folder_count: int
        library_playlist_max_depth: int
        media_bin_total_playlist_count: int
        media_bin_playlist_folder_count: int
        media_bin_playlist_max_depth: int
        media_bin_normal_playlist_count: int
        media_bin_smart_playlist_count: int
        media_bin_video_input_count: int
        audio_bin_playlist_count: int
        audio_bin_playlist_folder_count: int
        audio_bin_playlist_max_depth: int
        timer_count: int
        messages_count: int
        props_count: int
        stage_layout_count: int
        macros_count: int
        macros_collections_count: int
        macros_custom_icons: int
        ubiquitous_show_directory: bool
        def __init__(self, library_count: _Optional[int] = ..., library_playlist_count: _Optional[int] = ..., library_playlist_folder_count: _Optional[int] = ..., library_playlist_max_depth: _Optional[int] = ..., media_bin_total_playlist_count: _Optional[int] = ..., media_bin_playlist_folder_count: _Optional[int] = ..., media_bin_playlist_max_depth: _Optional[int] = ..., media_bin_normal_playlist_count: _Optional[int] = ..., media_bin_smart_playlist_count: _Optional[int] = ..., media_bin_video_input_count: _Optional[int] = ..., audio_bin_playlist_count: _Optional[int] = ..., audio_bin_playlist_folder_count: _Optional[int] = ..., audio_bin_playlist_max_depth: _Optional[int] = ..., timer_count: _Optional[int] = ..., messages_count: _Optional[int] = ..., props_count: _Optional[int] = ..., stage_layout_count: _Optional[int] = ..., macros_count: _Optional[int] = ..., macros_collections_count: _Optional[int] = ..., macros_custom_icons: _Optional[int] = ..., ubiquitous_show_directory: bool = ...) -> None: ...
    class Themes(_message.Message):
        __slots__ = ("theme_count", "theme_folder_count", "theme_folder_max_depth", "theme_slides_count")
        THEME_COUNT_FIELD_NUMBER: _ClassVar[int]
        THEME_FOLDER_COUNT_FIELD_NUMBER: _ClassVar[int]
        THEME_FOLDER_MAX_DEPTH_FIELD_NUMBER: _ClassVar[int]
        THEME_SLIDES_COUNT_FIELD_NUMBER: _ClassVar[int]
        theme_count: int
        theme_folder_count: int
        theme_folder_max_depth: int
        theme_slides_count: int
        def __init__(self, theme_count: _Optional[int] = ..., theme_folder_count: _Optional[int] = ..., theme_folder_max_depth: _Optional[int] = ..., theme_slides_count: _Optional[int] = ...) -> None: ...
    class Macro(_message.Message):
        __slots__ = ("trigger_on_startup_count",)
        TRIGGER_ON_STARTUP_COUNT_FIELD_NUMBER: _ClassVar[int]
        trigger_on_startup_count: int
        def __init__(self, trigger_on_startup_count: _Optional[int] = ...) -> None: ...
    class ClearGroup(_message.Message):
        __slots__ = ("clear_group_count", "hidden_clear_group_count", "default_icon_count", "custom_icon_count", "icon_tint_count")
        CLEAR_GROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
        HIDDEN_CLEAR_GROUP_COUNT_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_ICON_COUNT_FIELD_NUMBER: _ClassVar[int]
        CUSTOM_ICON_COUNT_FIELD_NUMBER: _ClassVar[int]
        ICON_TINT_COUNT_FIELD_NUMBER: _ClassVar[int]
        clear_group_count: int
        hidden_clear_group_count: int
        default_icon_count: int
        custom_icon_count: int
        icon_tint_count: int
        def __init__(self, clear_group_count: _Optional[int] = ..., hidden_clear_group_count: _Optional[int] = ..., default_icon_count: _Optional[int] = ..., custom_icon_count: _Optional[int] = ..., icon_tint_count: _Optional[int] = ...) -> None: ...
    class KeyMapping(_message.Message):
        __slots__ = ("total_mapped", "clear_groups", "groups", "macros", "props", "menus")
        TOTAL_MAPPED_FIELD_NUMBER: _ClassVar[int]
        CLEAR_GROUPS_FIELD_NUMBER: _ClassVar[int]
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        MACROS_FIELD_NUMBER: _ClassVar[int]
        PROPS_FIELD_NUMBER: _ClassVar[int]
        MENUS_FIELD_NUMBER: _ClassVar[int]
        total_mapped: int
        clear_groups: int
        groups: int
        macros: int
        props: int
        menus: int
        def __init__(self, total_mapped: _Optional[int] = ..., clear_groups: _Optional[int] = ..., groups: _Optional[int] = ..., macros: _Optional[int] = ..., props: _Optional[int] = ..., menus: _Optional[int] = ...) -> None: ...
    class NetworkLink(_message.Message):
        __slots__ = ("enabled", "member_count")
        ENABLED_FIELD_NUMBER: _ClassVar[int]
        MEMBER_COUNT_FIELD_NUMBER: _ClassVar[int]
        enabled: bool
        member_count: int
        def __init__(self, enabled: bool = ..., member_count: _Optional[int] = ...) -> None: ...
    class Capture(_message.Message):
        __slots__ = ("presets_count", "disk_presets_count", "rtmp_presets_count", "resi_presets_count")
        PRESETS_COUNT_FIELD_NUMBER: _ClassVar[int]
        DISK_PRESETS_COUNT_FIELD_NUMBER: _ClassVar[int]
        RTMP_PRESETS_COUNT_FIELD_NUMBER: _ClassVar[int]
        RESI_PRESETS_COUNT_FIELD_NUMBER: _ClassVar[int]
        presets_count: int
        disk_presets_count: int
        rtmp_presets_count: int
        resi_presets_count: int
        def __init__(self, presets_count: _Optional[int] = ..., disk_presets_count: _Optional[int] = ..., rtmp_presets_count: _Optional[int] = ..., resi_presets_count: _Optional[int] = ...) -> None: ...
    LOOKS_FIELD_NUMBER: _ClassVar[int]
    SCREEN_CONFIGURATION_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    SCREENS_FIELD_NUMBER: _ClassVar[int]
    PLANNING_CENTER_FIELD_NUMBER: _ClassVar[int]
    SONG_SELECT_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    COMMUNICATIONS_FIELD_NUMBER: _ClassVar[int]
    RESI_FIELD_NUMBER: _ClassVar[int]
    INTERFACE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    MACRO_FIELD_NUMBER: _ClassVar[int]
    CLEAR_GROUP_FIELD_NUMBER: _ClassVar[int]
    KEY_MAPPING_FIELD_NUMBER: _ClassVar[int]
    MULTITRACKS_FIELD_NUMBER: _ClassVar[int]
    NETWORK_LINK_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_FIELD_NUMBER: _ClassVar[int]
    looks: Startup.Looks
    screen_configuration: Startup.ScreenConfiguration
    preferences: Startup.Preferences
    screens: Startup.Screens
    planning_center: Startup.PlanningCenter
    song_select: Startup.SongSelect
    audio: Startup.Audio
    communications: Startup.Communications
    resi: Startup.Resi
    interface: Startup.Interface
    content: Startup.Content
    themes: Startup.Themes
    macro: Startup.Macro
    clear_group: Startup.ClearGroup
    key_mapping: Startup.KeyMapping
    multitracks: _analyticsMultiTracks_pb2.MultiTracks.Startup
    network_link: Startup.NetworkLink
    capture: Startup.Capture
    def __init__(self, looks: _Optional[_Union[Startup.Looks, _Mapping]] = ..., screen_configuration: _Optional[_Union[Startup.ScreenConfiguration, _Mapping]] = ..., preferences: _Optional[_Union[Startup.Preferences, _Mapping]] = ..., screens: _Optional[_Union[Startup.Screens, _Mapping]] = ..., planning_center: _Optional[_Union[Startup.PlanningCenter, _Mapping]] = ..., song_select: _Optional[_Union[Startup.SongSelect, _Mapping]] = ..., audio: _Optional[_Union[Startup.Audio, _Mapping]] = ..., communications: _Optional[_Union[Startup.Communications, _Mapping]] = ..., resi: _Optional[_Union[Startup.Resi, _Mapping]] = ..., interface: _Optional[_Union[Startup.Interface, _Mapping]] = ..., content: _Optional[_Union[Startup.Content, _Mapping]] = ..., themes: _Optional[_Union[Startup.Themes, _Mapping]] = ..., macro: _Optional[_Union[Startup.Macro, _Mapping]] = ..., clear_group: _Optional[_Union[Startup.ClearGroup, _Mapping]] = ..., key_mapping: _Optional[_Union[Startup.KeyMapping, _Mapping]] = ..., multitracks: _Optional[_Union[_analyticsMultiTracks_pb2.MultiTracks.Startup, _Mapping]] = ..., network_link: _Optional[_Union[Startup.NetworkLink, _Mapping]] = ..., capture: _Optional[_Union[Startup.Capture, _Mapping]] = ...) -> None: ...
