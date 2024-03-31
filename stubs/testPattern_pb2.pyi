import color_pb2 as _color_pb2
import font_pb2 as _font_pb2
import uuid_pb2 as _uuid_pb2
import url_pb2 as _url_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestPattern(_message.Message):
    __slots__ = ("type", "blend_grid", "custom_color", "intensity")
    class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        TYPE_UNKNOWN: _ClassVar[TestPattern.Type]
        TYPE_BLEND_GRID: _ClassVar[TestPattern.Type]
        TYPE_COLOR_BARS: _ClassVar[TestPattern.Type]
        TYPE_FOCUS: _ClassVar[TestPattern.Type]
        TYPE_GRAY_SCALE: _ClassVar[TestPattern.Type]
        TYPE_BLACK_COLOR: _ClassVar[TestPattern.Type]
        TYPE_WHITE_COLOR: _ClassVar[TestPattern.Type]
        TYPE_CUSTOM_COLOR: _ClassVar[TestPattern.Type]
        TYPE_TEXT: _ClassVar[TestPattern.Type]
        TYPE_VIDEO_SYNC: _ClassVar[TestPattern.Type]
    TYPE_UNKNOWN: TestPattern.Type
    TYPE_BLEND_GRID: TestPattern.Type
    TYPE_COLOR_BARS: TestPattern.Type
    TYPE_FOCUS: TestPattern.Type
    TYPE_GRAY_SCALE: TestPattern.Type
    TYPE_BLACK_COLOR: TestPattern.Type
    TYPE_WHITE_COLOR: TestPattern.Type
    TYPE_CUSTOM_COLOR: TestPattern.Type
    TYPE_TEXT: TestPattern.Type
    TYPE_VIDEO_SYNC: TestPattern.Type
    class BlendGrid(_message.Message):
        __slots__ = ("draw_grid", "draw_circles", "draw_lines", "invert_colors", "grid_spacing")
        DRAW_GRID_FIELD_NUMBER: _ClassVar[int]
        DRAW_CIRCLES_FIELD_NUMBER: _ClassVar[int]
        DRAW_LINES_FIELD_NUMBER: _ClassVar[int]
        INVERT_COLORS_FIELD_NUMBER: _ClassVar[int]
        GRID_SPACING_FIELD_NUMBER: _ClassVar[int]
        draw_grid: bool
        draw_circles: bool
        draw_lines: bool
        invert_colors: bool
        grid_spacing: float
        def __init__(self, draw_grid: bool = ..., draw_circles: bool = ..., draw_lines: bool = ..., invert_colors: bool = ..., grid_spacing: _Optional[float] = ...) -> None: ...
    class CustomColor(_message.Message):
        __slots__ = ("color",)
        COLOR_FIELD_NUMBER: _ClassVar[int]
        color: _color_pb2.Color
        def __init__(self, color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ...) -> None: ...
    class IntensityColor(_message.Message):
        __slots__ = ("intensity",)
        INTENSITY_FIELD_NUMBER: _ClassVar[int]
        intensity: float
        def __init__(self, intensity: _Optional[float] = ...) -> None: ...
    TYPE_FIELD_NUMBER: _ClassVar[int]
    BLEND_GRID_FIELD_NUMBER: _ClassVar[int]
    CUSTOM_COLOR_FIELD_NUMBER: _ClassVar[int]
    INTENSITY_FIELD_NUMBER: _ClassVar[int]
    type: TestPattern.Type
    blend_grid: TestPattern.BlendGrid
    custom_color: TestPattern.CustomColor
    intensity: TestPattern.IntensityColor
    def __init__(self, type: _Optional[_Union[TestPattern.Type, str]] = ..., blend_grid: _Optional[_Union[TestPattern.BlendGrid, _Mapping]] = ..., custom_color: _Optional[_Union[TestPattern.CustomColor, _Mapping]] = ..., intensity: _Optional[_Union[TestPattern.IntensityColor, _Mapping]] = ...) -> None: ...

class TestPatternDefinition(_message.Message):
    __slots__ = ("uuid", "name_localization_key", "properties", "show_delay_settings", "is_default")
    class ColorProperty(_message.Message):
        __slots__ = ("value", "allow_alpha", "default_colors")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        ALLOW_ALPHA_FIELD_NUMBER: _ClassVar[int]
        DEFAULT_COLORS_FIELD_NUMBER: _ClassVar[int]
        value: _color_pb2.Color
        allow_alpha: bool
        default_colors: _containers.RepeatedCompositeFieldContainer[_color_pb2.Color]
        def __init__(self, value: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., allow_alpha: bool = ..., default_colors: _Optional[_Iterable[_Union[_color_pb2.Color, _Mapping]]] = ...) -> None: ...
    class DoubleProperty(_message.Message):
        __slots__ = ("value", "min", "max", "step", "units", "viewType")
        class ViewType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            VIEW_TYPE_STEPPER: _ClassVar[TestPatternDefinition.DoubleProperty.ViewType]
            VIEW_TYPE_SLIDER: _ClassVar[TestPatternDefinition.DoubleProperty.ViewType]
            VIEW_TYPE_SPEED_SLIDER: _ClassVar[TestPatternDefinition.DoubleProperty.ViewType]
        VIEW_TYPE_STEPPER: TestPatternDefinition.DoubleProperty.ViewType
        VIEW_TYPE_SLIDER: TestPatternDefinition.DoubleProperty.ViewType
        VIEW_TYPE_SPEED_SLIDER: TestPatternDefinition.DoubleProperty.ViewType
        VALUE_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        STEP_FIELD_NUMBER: _ClassVar[int]
        UNITS_FIELD_NUMBER: _ClassVar[int]
        VIEWTYPE_FIELD_NUMBER: _ClassVar[int]
        value: float
        min: float
        max: float
        step: float
        units: str
        viewType: TestPatternDefinition.DoubleProperty.ViewType
        def __init__(self, value: _Optional[float] = ..., min: _Optional[float] = ..., max: _Optional[float] = ..., step: _Optional[float] = ..., units: _Optional[str] = ..., viewType: _Optional[_Union[TestPatternDefinition.DoubleProperty.ViewType, str]] = ...) -> None: ...
    class IntProperty(_message.Message):
        __slots__ = ("value", "min", "max", "units")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        MIN_FIELD_NUMBER: _ClassVar[int]
        MAX_FIELD_NUMBER: _ClassVar[int]
        UNITS_FIELD_NUMBER: _ClassVar[int]
        value: int
        min: int
        max: int
        units: str
        def __init__(self, value: _Optional[int] = ..., min: _Optional[int] = ..., max: _Optional[int] = ..., units: _Optional[str] = ...) -> None: ...
    class BoolProperty(_message.Message):
        __slots__ = ("value", "dependent_properties")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        DEPENDENT_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        value: bool
        dependent_properties: _containers.RepeatedCompositeFieldContainer[TestPatternDefinition.Property]
        def __init__(self, value: bool = ..., dependent_properties: _Optional[_Iterable[_Union[TestPatternDefinition.Property, _Mapping]]] = ...) -> None: ...
    class StringProperty(_message.Message):
        __slots__ = ("value", "min_chars", "max_chars")
        VALUE_FIELD_NUMBER: _ClassVar[int]
        MIN_CHARS_FIELD_NUMBER: _ClassVar[int]
        MAX_CHARS_FIELD_NUMBER: _ClassVar[int]
        value: str
        min_chars: int
        max_chars: int
        def __init__(self, value: _Optional[str] = ..., min_chars: _Optional[int] = ..., max_chars: _Optional[int] = ...) -> None: ...
    class FontProperty(_message.Message):
        __slots__ = ("font",)
        FONT_FIELD_NUMBER: _ClassVar[int]
        font: _font_pb2.Font
        def __init__(self, font: _Optional[_Union[_font_pb2.Font, _Mapping]] = ...) -> None: ...
    class SelectorProperty(_message.Message):
        __slots__ = ("selected_index", "value_localization_keys")
        SELECTED_INDEX_FIELD_NUMBER: _ClassVar[int]
        VALUE_LOCALIZATION_KEYS_FIELD_NUMBER: _ClassVar[int]
        selected_index: int
        value_localization_keys: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, selected_index: _Optional[int] = ..., value_localization_keys: _Optional[_Iterable[str]] = ...) -> None: ...
    class Property(_message.Message):
        __slots__ = ("name_localization_key", "color_property", "double_property", "int_property", "bool_property", "string_property", "font_property", "selector_property")
        NAME_LOCALIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
        COLOR_PROPERTY_FIELD_NUMBER: _ClassVar[int]
        DOUBLE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
        INT_PROPERTY_FIELD_NUMBER: _ClassVar[int]
        BOOL_PROPERTY_FIELD_NUMBER: _ClassVar[int]
        STRING_PROPERTY_FIELD_NUMBER: _ClassVar[int]
        FONT_PROPERTY_FIELD_NUMBER: _ClassVar[int]
        SELECTOR_PROPERTY_FIELD_NUMBER: _ClassVar[int]
        name_localization_key: str
        color_property: TestPatternDefinition.ColorProperty
        double_property: TestPatternDefinition.DoubleProperty
        int_property: TestPatternDefinition.IntProperty
        bool_property: TestPatternDefinition.BoolProperty
        string_property: TestPatternDefinition.StringProperty
        font_property: TestPatternDefinition.FontProperty
        selector_property: TestPatternDefinition.SelectorProperty
        def __init__(self, name_localization_key: _Optional[str] = ..., color_property: _Optional[_Union[TestPatternDefinition.ColorProperty, _Mapping]] = ..., double_property: _Optional[_Union[TestPatternDefinition.DoubleProperty, _Mapping]] = ..., int_property: _Optional[_Union[TestPatternDefinition.IntProperty, _Mapping]] = ..., bool_property: _Optional[_Union[TestPatternDefinition.BoolProperty, _Mapping]] = ..., string_property: _Optional[_Union[TestPatternDefinition.StringProperty, _Mapping]] = ..., font_property: _Optional[_Union[TestPatternDefinition.FontProperty, _Mapping]] = ..., selector_property: _Optional[_Union[TestPatternDefinition.SelectorProperty, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    NAME_LOCALIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
    PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SHOW_DELAY_SETTINGS_FIELD_NUMBER: _ClassVar[int]
    IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
    uuid: _uuid_pb2.UUID
    name_localization_key: str
    properties: _containers.RepeatedCompositeFieldContainer[TestPatternDefinition.Property]
    show_delay_settings: bool
    is_default: bool
    def __init__(self, uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., name_localization_key: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[TestPatternDefinition.Property, _Mapping]]] = ..., show_delay_settings: bool = ..., is_default: bool = ...) -> None: ...

class TestPatternRenderSettings(_message.Message):
    __slots__ = ("pattern", "screen_name", "outputs", "logo_type", "logo_file", "render_width", "render_height", "enable_audio")
    class LogoType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGO_TYPE_NONE: _ClassVar[TestPatternRenderSettings.LogoType]
        LOGO_TYPE_PROPRESENTER: _ClassVar[TestPatternRenderSettings.LogoType]
        LOGO_TYPE_USER: _ClassVar[TestPatternRenderSettings.LogoType]
    LOGO_TYPE_NONE: TestPatternRenderSettings.LogoType
    LOGO_TYPE_PROPRESENTER: TestPatternRenderSettings.LogoType
    LOGO_TYPE_USER: TestPatternRenderSettings.LogoType
    class Output(_message.Message):
        __slots__ = ("x", "y", "width", "height", "name", "frame_rate")
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        x: int
        y: int
        width: int
        height: int
        name: str
        frame_rate: float
        def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., name: _Optional[str] = ..., frame_rate: _Optional[float] = ...) -> None: ...
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    LOGO_TYPE_FIELD_NUMBER: _ClassVar[int]
    LOGO_FILE_FIELD_NUMBER: _ClassVar[int]
    RENDER_WIDTH_FIELD_NUMBER: _ClassVar[int]
    RENDER_HEIGHT_FIELD_NUMBER: _ClassVar[int]
    ENABLE_AUDIO_FIELD_NUMBER: _ClassVar[int]
    pattern: TestPatternDefinition
    screen_name: str
    outputs: _containers.RepeatedCompositeFieldContainer[TestPatternRenderSettings.Output]
    logo_type: TestPatternRenderSettings.LogoType
    logo_file: str
    render_width: int
    render_height: int
    enable_audio: bool
    def __init__(self, pattern: _Optional[_Union[TestPatternDefinition, _Mapping]] = ..., screen_name: _Optional[str] = ..., outputs: _Optional[_Iterable[_Union[TestPatternRenderSettings.Output, _Mapping]]] = ..., logo_type: _Optional[_Union[TestPatternRenderSettings.LogoType, str]] = ..., logo_file: _Optional[str] = ..., render_width: _Optional[int] = ..., render_height: _Optional[int] = ..., enable_audio: bool = ...) -> None: ...

class TestPatternState(_message.Message):
    __slots__ = ("pattern", "show_pattern", "display_location", "specific_screen", "identify_screens", "logo_type", "user_logo_location")
    class DisplayLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        DISPLAY_LOCATION_ALL_SCREENS: _ClassVar[TestPatternState.DisplayLocation]
        DISPLAY_LOCATION_AUDIENCE_SCREENS: _ClassVar[TestPatternState.DisplayLocation]
        DISPLAY_LOCATION_STAGE_SCREENS: _ClassVar[TestPatternState.DisplayLocation]
        DISPLAY_LOCATION_SPECIFIC_SCREEN: _ClassVar[TestPatternState.DisplayLocation]
    DISPLAY_LOCATION_ALL_SCREENS: TestPatternState.DisplayLocation
    DISPLAY_LOCATION_AUDIENCE_SCREENS: TestPatternState.DisplayLocation
    DISPLAY_LOCATION_STAGE_SCREENS: TestPatternState.DisplayLocation
    DISPLAY_LOCATION_SPECIFIC_SCREEN: TestPatternState.DisplayLocation
    class LogoType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LOGO_TYPE_NONE: _ClassVar[TestPatternState.LogoType]
        LOGO_TYPE_PROPRESENTER: _ClassVar[TestPatternState.LogoType]
        LOGO_TYPE_USER: _ClassVar[TestPatternState.LogoType]
    LOGO_TYPE_NONE: TestPatternState.LogoType
    LOGO_TYPE_PROPRESENTER: TestPatternState.LogoType
    LOGO_TYPE_USER: TestPatternState.LogoType
    PATTERN_FIELD_NUMBER: _ClassVar[int]
    SHOW_PATTERN_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    SPECIFIC_SCREEN_FIELD_NUMBER: _ClassVar[int]
    IDENTIFY_SCREENS_FIELD_NUMBER: _ClassVar[int]
    LOGO_TYPE_FIELD_NUMBER: _ClassVar[int]
    USER_LOGO_LOCATION_FIELD_NUMBER: _ClassVar[int]
    pattern: TestPatternDefinition
    show_pattern: bool
    display_location: TestPatternState.DisplayLocation
    specific_screen: _uuid_pb2.UUID
    identify_screens: bool
    logo_type: TestPatternState.LogoType
    user_logo_location: _url_pb2.URL
    def __init__(self, pattern: _Optional[_Union[TestPatternDefinition, _Mapping]] = ..., show_pattern: bool = ..., display_location: _Optional[_Union[TestPatternState.DisplayLocation, str]] = ..., specific_screen: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., identify_screens: bool = ..., logo_type: _Optional[_Union[TestPatternState.LogoType, str]] = ..., user_logo_location: _Optional[_Union[_url_pb2.URL, _Mapping]] = ...) -> None: ...

class TestPatternDocument(_message.Message):
    __slots__ = ("state", "patterns")
    class TestPatternStateData(_message.Message):
        __slots__ = ("test_pattern_id", "test_pattern_name_localization_key", "display_location", "specific_screen", "identify_screens", "logo_type", "user_logo_location")
        class DisplayLocation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DISPLAY_LOCATION_ALL_SCREENS: _ClassVar[TestPatternDocument.TestPatternStateData.DisplayLocation]
            DISPLAY_LOCATION_AUDIENCE_SCREENS: _ClassVar[TestPatternDocument.TestPatternStateData.DisplayLocation]
            DISPLAY_LOCATION_STAGE_SCREENS: _ClassVar[TestPatternDocument.TestPatternStateData.DisplayLocation]
            DISPLAY_LOCATION_SPECIFIC_SCREEN: _ClassVar[TestPatternDocument.TestPatternStateData.DisplayLocation]
        DISPLAY_LOCATION_ALL_SCREENS: TestPatternDocument.TestPatternStateData.DisplayLocation
        DISPLAY_LOCATION_AUDIENCE_SCREENS: TestPatternDocument.TestPatternStateData.DisplayLocation
        DISPLAY_LOCATION_STAGE_SCREENS: TestPatternDocument.TestPatternStateData.DisplayLocation
        DISPLAY_LOCATION_SPECIFIC_SCREEN: TestPatternDocument.TestPatternStateData.DisplayLocation
        class LogoType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LOGO_TYPE_NONE: _ClassVar[TestPatternDocument.TestPatternStateData.LogoType]
            LOGO_TYPE_PROPRESENTER: _ClassVar[TestPatternDocument.TestPatternStateData.LogoType]
            LOGO_TYPE_USER: _ClassVar[TestPatternDocument.TestPatternStateData.LogoType]
        LOGO_TYPE_NONE: TestPatternDocument.TestPatternStateData.LogoType
        LOGO_TYPE_PROPRESENTER: TestPatternDocument.TestPatternStateData.LogoType
        LOGO_TYPE_USER: TestPatternDocument.TestPatternStateData.LogoType
        TEST_PATTERN_ID_FIELD_NUMBER: _ClassVar[int]
        TEST_PATTERN_NAME_LOCALIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
        DISPLAY_LOCATION_FIELD_NUMBER: _ClassVar[int]
        SPECIFIC_SCREEN_FIELD_NUMBER: _ClassVar[int]
        IDENTIFY_SCREENS_FIELD_NUMBER: _ClassVar[int]
        LOGO_TYPE_FIELD_NUMBER: _ClassVar[int]
        USER_LOGO_LOCATION_FIELD_NUMBER: _ClassVar[int]
        test_pattern_id: _uuid_pb2.UUID
        test_pattern_name_localization_key: str
        display_location: TestPatternDocument.TestPatternStateData.DisplayLocation
        specific_screen: _uuid_pb2.UUID
        identify_screens: bool
        logo_type: TestPatternDocument.TestPatternStateData.LogoType
        user_logo_location: _url_pb2.URL
        def __init__(self, test_pattern_id: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., test_pattern_name_localization_key: _Optional[str] = ..., display_location: _Optional[_Union[TestPatternDocument.TestPatternStateData.DisplayLocation, str]] = ..., specific_screen: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., identify_screens: bool = ..., logo_type: _Optional[_Union[TestPatternDocument.TestPatternStateData.LogoType, str]] = ..., user_logo_location: _Optional[_Union[_url_pb2.URL, _Mapping]] = ...) -> None: ...
    class TestPatternData(_message.Message):
        __slots__ = ("uuid", "name_localization_key", "properties")
        class ColorProperty(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _color_pb2.Color
            def __init__(self, value: _Optional[_Union[_color_pb2.Color, _Mapping]] = ...) -> None: ...
        class DoubleProperty(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: float
            def __init__(self, value: _Optional[float] = ...) -> None: ...
        class IntProperty(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: int
            def __init__(self, value: _Optional[int] = ...) -> None: ...
        class BoolProperty(_message.Message):
            __slots__ = ("value", "dependent_properties")
            VALUE_FIELD_NUMBER: _ClassVar[int]
            DEPENDENT_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
            value: bool
            dependent_properties: _containers.RepeatedCompositeFieldContainer[TestPatternDocument.TestPatternData.Property]
            def __init__(self, value: bool = ..., dependent_properties: _Optional[_Iterable[_Union[TestPatternDocument.TestPatternData.Property, _Mapping]]] = ...) -> None: ...
        class StringProperty(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: str
            def __init__(self, value: _Optional[str] = ...) -> None: ...
        class FontProperty(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: _font_pb2.Font
            def __init__(self, value: _Optional[_Union[_font_pb2.Font, _Mapping]] = ...) -> None: ...
        class SelectorProperty(_message.Message):
            __slots__ = ("value",)
            VALUE_FIELD_NUMBER: _ClassVar[int]
            value: int
            def __init__(self, value: _Optional[int] = ...) -> None: ...
        class Property(_message.Message):
            __slots__ = ("name_localization_key", "color_property", "double_property", "int_property", "bool_property", "string_property", "font_property", "selector_property")
            NAME_LOCALIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
            COLOR_PROPERTY_FIELD_NUMBER: _ClassVar[int]
            DOUBLE_PROPERTY_FIELD_NUMBER: _ClassVar[int]
            INT_PROPERTY_FIELD_NUMBER: _ClassVar[int]
            BOOL_PROPERTY_FIELD_NUMBER: _ClassVar[int]
            STRING_PROPERTY_FIELD_NUMBER: _ClassVar[int]
            FONT_PROPERTY_FIELD_NUMBER: _ClassVar[int]
            SELECTOR_PROPERTY_FIELD_NUMBER: _ClassVar[int]
            name_localization_key: str
            color_property: TestPatternDocument.TestPatternData.ColorProperty
            double_property: TestPatternDocument.TestPatternData.DoubleProperty
            int_property: TestPatternDocument.TestPatternData.IntProperty
            bool_property: TestPatternDocument.TestPatternData.BoolProperty
            string_property: TestPatternDocument.TestPatternData.StringProperty
            font_property: TestPatternDocument.TestPatternData.FontProperty
            selector_property: TestPatternDocument.TestPatternData.SelectorProperty
            def __init__(self, name_localization_key: _Optional[str] = ..., color_property: _Optional[_Union[TestPatternDocument.TestPatternData.ColorProperty, _Mapping]] = ..., double_property: _Optional[_Union[TestPatternDocument.TestPatternData.DoubleProperty, _Mapping]] = ..., int_property: _Optional[_Union[TestPatternDocument.TestPatternData.IntProperty, _Mapping]] = ..., bool_property: _Optional[_Union[TestPatternDocument.TestPatternData.BoolProperty, _Mapping]] = ..., string_property: _Optional[_Union[TestPatternDocument.TestPatternData.StringProperty, _Mapping]] = ..., font_property: _Optional[_Union[TestPatternDocument.TestPatternData.FontProperty, _Mapping]] = ..., selector_property: _Optional[_Union[TestPatternDocument.TestPatternData.SelectorProperty, _Mapping]] = ...) -> None: ...
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_LOCALIZATION_KEY_FIELD_NUMBER: _ClassVar[int]
        PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        uuid: _uuid_pb2.UUID
        name_localization_key: str
        properties: _containers.RepeatedCompositeFieldContainer[TestPatternDocument.TestPatternData.Property]
        def __init__(self, uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., name_localization_key: _Optional[str] = ..., properties: _Optional[_Iterable[_Union[TestPatternDocument.TestPatternData.Property, _Mapping]]] = ...) -> None: ...
    STATE_FIELD_NUMBER: _ClassVar[int]
    PATTERNS_FIELD_NUMBER: _ClassVar[int]
    state: TestPatternDocument.TestPatternStateData
    patterns: _containers.RepeatedCompositeFieldContainer[TestPatternDocument.TestPatternData]
    def __init__(self, state: _Optional[_Union[TestPatternDocument.TestPatternStateData, _Mapping]] = ..., patterns: _Optional[_Iterable[_Union[TestPatternDocument.TestPatternData, _Mapping]]] = ...) -> None: ...
