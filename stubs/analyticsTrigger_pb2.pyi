import analyticsTriggerMedia_pb2 as _analyticsTriggerMedia_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Trigger(_message.Message):
    __slots__ = ("cue", "action", "media_bin", "audio_bin", "test_pattern")
    class Cue(_message.Message):
        __slots__ = ("slide",)
        class Slide(_message.Message):
            __slots__ = ("trigger", "scrolling_text_element", "rss_feed_element", "file_feed_element")
            class Trigger(_message.Message):
                __slots__ = ("object_count", "scrolling_object_count", "background_fx_object_count", "action_count", "has_text_fx", "media_text_fill_object_count", "cut_out_text_fill_object_count", "background_blur_text_fill_object_count", "background_invert_text_fill_object_count")
                OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
                SCROLLING_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
                BACKGROUND_FX_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
                ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
                HAS_TEXT_FX_FIELD_NUMBER: _ClassVar[int]
                MEDIA_TEXT_FILL_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
                CUT_OUT_TEXT_FILL_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
                BACKGROUND_BLUR_TEXT_FILL_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
                BACKGROUND_INVERT_TEXT_FILL_OBJECT_COUNT_FIELD_NUMBER: _ClassVar[int]
                object_count: int
                scrolling_object_count: int
                background_fx_object_count: int
                action_count: int
                has_text_fx: bool
                media_text_fill_object_count: int
                cut_out_text_fill_object_count: int
                background_blur_text_fill_object_count: int
                background_invert_text_fill_object_count: int
                def __init__(self, object_count: _Optional[int] = ..., scrolling_object_count: _Optional[int] = ..., background_fx_object_count: _Optional[int] = ..., action_count: _Optional[int] = ..., has_text_fx: bool = ..., media_text_fill_object_count: _Optional[int] = ..., cut_out_text_fill_object_count: _Optional[int] = ..., background_blur_text_fill_object_count: _Optional[int] = ..., background_invert_text_fill_object_count: _Optional[int] = ...) -> None: ...
            class ScrollingTextElement(_message.Message):
                __slots__ = ("direction", "start_position", "is_repeat_enabled", "speed", "destination_layer")
                class Direction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    DIRECTION_UNKNOWN: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Direction]
                    DIRECTION_LEFT: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Direction]
                    DIRECTION_RIGHT: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Direction]
                    DIRECTION_UP: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Direction]
                    DIRECTION_DOWN: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Direction]
                DIRECTION_UNKNOWN: Trigger.Cue.Slide.ScrollingTextElement.Direction
                DIRECTION_LEFT: Trigger.Cue.Slide.ScrollingTextElement.Direction
                DIRECTION_RIGHT: Trigger.Cue.Slide.ScrollingTextElement.Direction
                DIRECTION_UP: Trigger.Cue.Slide.ScrollingTextElement.Direction
                DIRECTION_DOWN: Trigger.Cue.Slide.ScrollingTextElement.Direction
                class StartPosition(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    START_POSITION_UNKNOWN: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.StartPosition]
                    START_POSITION_AUTOMATIC: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.StartPosition]
                    START_POSITION_OFF_SCREEN: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.StartPosition]
                START_POSITION_UNKNOWN: Trigger.Cue.Slide.ScrollingTextElement.StartPosition
                START_POSITION_AUTOMATIC: Trigger.Cue.Slide.ScrollingTextElement.StartPosition
                START_POSITION_OFF_SCREEN: Trigger.Cue.Slide.ScrollingTextElement.StartPosition
                class Speed(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    SPEED_UNKNOWN: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Speed]
                    SPEED_VERY_SLOW: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Speed]
                    SPEED_SLOW: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Speed]
                    SPEED_MEDIUM: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Speed]
                    SPEED_FAST: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Speed]
                    SPEED_VERY_FAST: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.Speed]
                SPEED_UNKNOWN: Trigger.Cue.Slide.ScrollingTextElement.Speed
                SPEED_VERY_SLOW: Trigger.Cue.Slide.ScrollingTextElement.Speed
                SPEED_SLOW: Trigger.Cue.Slide.ScrollingTextElement.Speed
                SPEED_MEDIUM: Trigger.Cue.Slide.ScrollingTextElement.Speed
                SPEED_FAST: Trigger.Cue.Slide.ScrollingTextElement.Speed
                SPEED_VERY_FAST: Trigger.Cue.Slide.ScrollingTextElement.Speed
                class DestinationLayer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    DESTINATION_LAYER_UNKNOWN: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer]
                    DESTINATION_LAYER_ANNOUNCEMENT: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer]
                    DESTINATION_LAYER_PRESENTATION: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer]
                    DESTINATION_LAYER_STAGE: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer]
                    DESTINATION_LAYER_PROPS: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer]
                    DESTINATION_LAYER_MESSAGES: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer]
                    DESTINATION_LAYER_MASK: _ClassVar[Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer]
                DESTINATION_LAYER_UNKNOWN: Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer
                DESTINATION_LAYER_ANNOUNCEMENT: Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer
                DESTINATION_LAYER_PRESENTATION: Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer
                DESTINATION_LAYER_STAGE: Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer
                DESTINATION_LAYER_PROPS: Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer
                DESTINATION_LAYER_MESSAGES: Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer
                DESTINATION_LAYER_MASK: Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer
                DIRECTION_FIELD_NUMBER: _ClassVar[int]
                START_POSITION_FIELD_NUMBER: _ClassVar[int]
                IS_REPEAT_ENABLED_FIELD_NUMBER: _ClassVar[int]
                SPEED_FIELD_NUMBER: _ClassVar[int]
                DESTINATION_LAYER_FIELD_NUMBER: _ClassVar[int]
                direction: Trigger.Cue.Slide.ScrollingTextElement.Direction
                start_position: Trigger.Cue.Slide.ScrollingTextElement.StartPosition
                is_repeat_enabled: bool
                speed: Trigger.Cue.Slide.ScrollingTextElement.Speed
                destination_layer: Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer
                def __init__(self, direction: _Optional[_Union[Trigger.Cue.Slide.ScrollingTextElement.Direction, str]] = ..., start_position: _Optional[_Union[Trigger.Cue.Slide.ScrollingTextElement.StartPosition, str]] = ..., is_repeat_enabled: bool = ..., speed: _Optional[_Union[Trigger.Cue.Slide.ScrollingTextElement.Speed, str]] = ..., destination_layer: _Optional[_Union[Trigger.Cue.Slide.ScrollingTextElement.DestinationLayer, str]] = ...) -> None: ...
            class RSSFeedElement(_message.Message):
                __slots__ = ("content", "is_delimiter_enabled", "destination_layer")
                class Content(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    CONTENT_UNKNOWN: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.Content]
                    CONTENT_TITLE: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.Content]
                    CONTENT_TITLE_AND_DESCRIPTION: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.Content]
                CONTENT_UNKNOWN: Trigger.Cue.Slide.RSSFeedElement.Content
                CONTENT_TITLE: Trigger.Cue.Slide.RSSFeedElement.Content
                CONTENT_TITLE_AND_DESCRIPTION: Trigger.Cue.Slide.RSSFeedElement.Content
                class DestinationLayer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    DESTINATION_LAYER_UNKNOWN: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.DestinationLayer]
                    DESTINATION_LAYER_ANNOUNCEMENT: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.DestinationLayer]
                    DESTINATION_LAYER_PRESENTATION: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.DestinationLayer]
                    DESTINATION_LAYER_STAGE: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.DestinationLayer]
                    DESTINATION_LAYER_PROPS: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.DestinationLayer]
                    DESTINATION_LAYER_MESSAGES: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.DestinationLayer]
                    DESTINATION_LAYER_MASK: _ClassVar[Trigger.Cue.Slide.RSSFeedElement.DestinationLayer]
                DESTINATION_LAYER_UNKNOWN: Trigger.Cue.Slide.RSSFeedElement.DestinationLayer
                DESTINATION_LAYER_ANNOUNCEMENT: Trigger.Cue.Slide.RSSFeedElement.DestinationLayer
                DESTINATION_LAYER_PRESENTATION: Trigger.Cue.Slide.RSSFeedElement.DestinationLayer
                DESTINATION_LAYER_STAGE: Trigger.Cue.Slide.RSSFeedElement.DestinationLayer
                DESTINATION_LAYER_PROPS: Trigger.Cue.Slide.RSSFeedElement.DestinationLayer
                DESTINATION_LAYER_MESSAGES: Trigger.Cue.Slide.RSSFeedElement.DestinationLayer
                DESTINATION_LAYER_MASK: Trigger.Cue.Slide.RSSFeedElement.DestinationLayer
                CONTENT_FIELD_NUMBER: _ClassVar[int]
                IS_DELIMITER_ENABLED_FIELD_NUMBER: _ClassVar[int]
                DESTINATION_LAYER_FIELD_NUMBER: _ClassVar[int]
                content: Trigger.Cue.Slide.RSSFeedElement.Content
                is_delimiter_enabled: bool
                destination_layer: Trigger.Cue.Slide.RSSFeedElement.DestinationLayer
                def __init__(self, content: _Optional[_Union[Trigger.Cue.Slide.RSSFeedElement.Content, str]] = ..., is_delimiter_enabled: bool = ..., destination_layer: _Optional[_Union[Trigger.Cue.Slide.RSSFeedElement.DestinationLayer, str]] = ...) -> None: ...
            class FileFeedElement(_message.Message):
                __slots__ = ("destination_layer",)
                class DestinationLayer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                    __slots__ = ()
                    DESTINATION_LAYER_UNKNOWN: _ClassVar[Trigger.Cue.Slide.FileFeedElement.DestinationLayer]
                    DESTINATION_LAYER_ANNOUNCEMENT: _ClassVar[Trigger.Cue.Slide.FileFeedElement.DestinationLayer]
                    DESTINATION_LAYER_PRESENTATION: _ClassVar[Trigger.Cue.Slide.FileFeedElement.DestinationLayer]
                    DESTINATION_LAYER_STAGE: _ClassVar[Trigger.Cue.Slide.FileFeedElement.DestinationLayer]
                    DESTINATION_LAYER_PROPS: _ClassVar[Trigger.Cue.Slide.FileFeedElement.DestinationLayer]
                    DESTINATION_LAYER_MESSAGES: _ClassVar[Trigger.Cue.Slide.FileFeedElement.DestinationLayer]
                    DESTINATION_LAYER_MASK: _ClassVar[Trigger.Cue.Slide.FileFeedElement.DestinationLayer]
                DESTINATION_LAYER_UNKNOWN: Trigger.Cue.Slide.FileFeedElement.DestinationLayer
                DESTINATION_LAYER_ANNOUNCEMENT: Trigger.Cue.Slide.FileFeedElement.DestinationLayer
                DESTINATION_LAYER_PRESENTATION: Trigger.Cue.Slide.FileFeedElement.DestinationLayer
                DESTINATION_LAYER_STAGE: Trigger.Cue.Slide.FileFeedElement.DestinationLayer
                DESTINATION_LAYER_PROPS: Trigger.Cue.Slide.FileFeedElement.DestinationLayer
                DESTINATION_LAYER_MESSAGES: Trigger.Cue.Slide.FileFeedElement.DestinationLayer
                DESTINATION_LAYER_MASK: Trigger.Cue.Slide.FileFeedElement.DestinationLayer
                DESTINATION_LAYER_FIELD_NUMBER: _ClassVar[int]
                destination_layer: Trigger.Cue.Slide.FileFeedElement.DestinationLayer
                def __init__(self, destination_layer: _Optional[_Union[Trigger.Cue.Slide.FileFeedElement.DestinationLayer, str]] = ...) -> None: ...
            TRIGGER_FIELD_NUMBER: _ClassVar[int]
            SCROLLING_TEXT_ELEMENT_FIELD_NUMBER: _ClassVar[int]
            RSS_FEED_ELEMENT_FIELD_NUMBER: _ClassVar[int]
            FILE_FEED_ELEMENT_FIELD_NUMBER: _ClassVar[int]
            trigger: Trigger.Cue.Slide.Trigger
            scrolling_text_element: Trigger.Cue.Slide.ScrollingTextElement
            rss_feed_element: Trigger.Cue.Slide.RSSFeedElement
            file_feed_element: Trigger.Cue.Slide.FileFeedElement
            def __init__(self, trigger: _Optional[_Union[Trigger.Cue.Slide.Trigger, _Mapping]] = ..., scrolling_text_element: _Optional[_Union[Trigger.Cue.Slide.ScrollingTextElement, _Mapping]] = ..., rss_feed_element: _Optional[_Union[Trigger.Cue.Slide.RSSFeedElement, _Mapping]] = ..., file_feed_element: _Optional[_Union[Trigger.Cue.Slide.FileFeedElement, _Mapping]] = ...) -> None: ...
        SLIDE_FIELD_NUMBER: _ClassVar[int]
        slide: Trigger.Cue.Slide
        def __init__(self, slide: _Optional[_Union[Trigger.Cue.Slide, _Mapping]] = ...) -> None: ...
    class Action(_message.Message):
        __slots__ = ("clear", "media", "media_bin_playlist", "audio_bin_playlist", "stage", "timer", "prop", "look", "message", "communications", "slide_destination", "macro", "clear_group", "capture_start", "capture_stop")
        class ClearLayer(_message.Message):
            __slots__ = ("type",)
            class ClearLayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CLEAR_LAYER_TYPE_UNKNOWN: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_AUDIO: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_MESSAGES: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_PROPS: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_ANNOUNCEMENTS: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_SLIDE: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_MEDIA: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_VIDEO_INPUT: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_CLEAR_TO_LOGO: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
                CLEAR_LAYER_TYPE_CLEAR_GROUP: _ClassVar[Trigger.Action.ClearLayer.ClearLayerType]
            CLEAR_LAYER_TYPE_UNKNOWN: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_AUDIO: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_MESSAGES: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_PROPS: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_ANNOUNCEMENTS: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_SLIDE: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_MEDIA: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_VIDEO_INPUT: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_CLEAR_TO_LOGO: Trigger.Action.ClearLayer.ClearLayerType
            CLEAR_LAYER_TYPE_CLEAR_GROUP: Trigger.Action.ClearLayer.ClearLayerType
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: Trigger.Action.ClearLayer.ClearLayerType
            def __init__(self, type: _Optional[_Union[Trigger.Action.ClearLayer.ClearLayerType, str]] = ...) -> None: ...
        class MediaBinPlaylist(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AudioBinPlaylist(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Stage(_message.Message):
            __slots__ = ("layout_change_count", "total_stage_screens")
            LAYOUT_CHANGE_COUNT_FIELD_NUMBER: _ClassVar[int]
            TOTAL_STAGE_SCREENS_FIELD_NUMBER: _ClassVar[int]
            layout_change_count: int
            total_stage_screens: int
            def __init__(self, layout_change_count: _Optional[int] = ..., total_stage_screens: _Optional[int] = ...) -> None: ...
        class SlideDestination(_message.Message):
            __slots__ = ("change_slide_destination",)
            class ChangeSlideDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CHANGE_SLIDE_DESTINATION_UNKNOWN: _ClassVar[Trigger.Action.SlideDestination.ChangeSlideDestination]
                CHANGE_SLIDE_DESTINATION_NO_CHANGE: _ClassVar[Trigger.Action.SlideDestination.ChangeSlideDestination]
                CHANGE_SLIDE_DESTINATION_STAGE_ONLY: _ClassVar[Trigger.Action.SlideDestination.ChangeSlideDestination]
                CHANGE_SLIDE_DESTINATION_STAGE_AUDIENCE: _ClassVar[Trigger.Action.SlideDestination.ChangeSlideDestination]
            CHANGE_SLIDE_DESTINATION_UNKNOWN: Trigger.Action.SlideDestination.ChangeSlideDestination
            CHANGE_SLIDE_DESTINATION_NO_CHANGE: Trigger.Action.SlideDestination.ChangeSlideDestination
            CHANGE_SLIDE_DESTINATION_STAGE_ONLY: Trigger.Action.SlideDestination.ChangeSlideDestination
            CHANGE_SLIDE_DESTINATION_STAGE_AUDIENCE: Trigger.Action.SlideDestination.ChangeSlideDestination
            CHANGE_SLIDE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
            change_slide_destination: Trigger.Action.SlideDestination.ChangeSlideDestination
            def __init__(self, change_slide_destination: _Optional[_Union[Trigger.Action.SlideDestination.ChangeSlideDestination, str]] = ...) -> None: ...
        class Timer(_message.Message):
            __slots__ = ("type",)
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                TYPE_UNKNOWN: _ClassVar[Trigger.Action.Timer.Type]
                TYPE_START_SET_CONFIGURATION: _ClassVar[Trigger.Action.Timer.Type]
                TYPE_START: _ClassVar[Trigger.Action.Timer.Type]
                TYPE_STOP: _ClassVar[Trigger.Action.Timer.Type]
                TYPE_RESET: _ClassVar[Trigger.Action.Timer.Type]
                TYPE_STOP_SET_CONFIGURATION: _ClassVar[Trigger.Action.Timer.Type]
                TYPE_INCREMENT: _ClassVar[Trigger.Action.Timer.Type]
            TYPE_UNKNOWN: Trigger.Action.Timer.Type
            TYPE_START_SET_CONFIGURATION: Trigger.Action.Timer.Type
            TYPE_START: Trigger.Action.Timer.Type
            TYPE_STOP: Trigger.Action.Timer.Type
            TYPE_RESET: Trigger.Action.Timer.Type
            TYPE_STOP_SET_CONFIGURATION: Trigger.Action.Timer.Type
            TYPE_INCREMENT: Trigger.Action.Timer.Type
            TYPE_FIELD_NUMBER: _ClassVar[int]
            type: Trigger.Action.Timer.Type
            def __init__(self, type: _Optional[_Union[Trigger.Action.Timer.Type, str]] = ...) -> None: ...
        class Prop(_message.Message):
            __slots__ = ("transition",)
            TRANSITION_FIELD_NUMBER: _ClassVar[int]
            transition: str
            def __init__(self, transition: _Optional[str] = ...) -> None: ...
        class Look(_message.Message):
            __slots__ = ("total_screen_count", "mask", "messages", "props", "announcements", "presentation_theme", "slide", "media", "video_input")
            class Setting(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                SETTING_NONE: _ClassVar[Trigger.Action.Look.Setting]
                SETTING_SOME: _ClassVar[Trigger.Action.Look.Setting]
                SETTING_ALL: _ClassVar[Trigger.Action.Look.Setting]
            SETTING_NONE: Trigger.Action.Look.Setting
            SETTING_SOME: Trigger.Action.Look.Setting
            SETTING_ALL: Trigger.Action.Look.Setting
            TOTAL_SCREEN_COUNT_FIELD_NUMBER: _ClassVar[int]
            MASK_FIELD_NUMBER: _ClassVar[int]
            MESSAGES_FIELD_NUMBER: _ClassVar[int]
            PROPS_FIELD_NUMBER: _ClassVar[int]
            ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
            PRESENTATION_THEME_FIELD_NUMBER: _ClassVar[int]
            SLIDE_FIELD_NUMBER: _ClassVar[int]
            MEDIA_FIELD_NUMBER: _ClassVar[int]
            VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
            total_screen_count: int
            mask: Trigger.Action.Look.Setting
            messages: Trigger.Action.Look.Setting
            props: Trigger.Action.Look.Setting
            announcements: Trigger.Action.Look.Setting
            presentation_theme: Trigger.Action.Look.Setting
            slide: Trigger.Action.Look.Setting
            media: Trigger.Action.Look.Setting
            video_input: Trigger.Action.Look.Setting
            def __init__(self, total_screen_count: _Optional[int] = ..., mask: _Optional[_Union[Trigger.Action.Look.Setting, str]] = ..., messages: _Optional[_Union[Trigger.Action.Look.Setting, str]] = ..., props: _Optional[_Union[Trigger.Action.Look.Setting, str]] = ..., announcements: _Optional[_Union[Trigger.Action.Look.Setting, str]] = ..., presentation_theme: _Optional[_Union[Trigger.Action.Look.Setting, str]] = ..., slide: _Optional[_Union[Trigger.Action.Look.Setting, str]] = ..., media: _Optional[_Union[Trigger.Action.Look.Setting, str]] = ..., video_input: _Optional[_Union[Trigger.Action.Look.Setting, str]] = ...) -> None: ...
        class Message(_message.Message):
            __slots__ = ("token_count", "text_token_count", "timer_token_count", "clock_token_count", "showing_count")
            TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
            TEXT_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
            TIMER_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
            CLOCK_TOKEN_COUNT_FIELD_NUMBER: _ClassVar[int]
            SHOWING_COUNT_FIELD_NUMBER: _ClassVar[int]
            token_count: int
            text_token_count: int
            timer_token_count: int
            clock_token_count: int
            showing_count: int
            def __init__(self, token_count: _Optional[int] = ..., text_token_count: _Optional[int] = ..., timer_token_count: _Optional[int] = ..., clock_token_count: _Optional[int] = ..., showing_count: _Optional[int] = ...) -> None: ...
        class Communications(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Macro(_message.Message):
            __slots__ = ("action_count", "cue_action_count", "total_action_count")
            ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
            CUE_ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
            TOTAL_ACTION_COUNT_FIELD_NUMBER: _ClassVar[int]
            action_count: int
            cue_action_count: int
            total_action_count: int
            def __init__(self, action_count: _Optional[int] = ..., cue_action_count: _Optional[int] = ..., total_action_count: _Optional[int] = ...) -> None: ...
        class ClearGroup(_message.Message):
            __slots__ = ("layer_audio", "layer_messages", "layer_props", "layer_announcement", "layer_slide", "layer_media", "layer_video_input")
            LAYER_AUDIO_FIELD_NUMBER: _ClassVar[int]
            LAYER_MESSAGES_FIELD_NUMBER: _ClassVar[int]
            LAYER_PROPS_FIELD_NUMBER: _ClassVar[int]
            LAYER_ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
            LAYER_SLIDE_FIELD_NUMBER: _ClassVar[int]
            LAYER_MEDIA_FIELD_NUMBER: _ClassVar[int]
            LAYER_VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
            layer_audio: bool
            layer_messages: bool
            layer_props: bool
            layer_announcement: bool
            layer_slide: bool
            layer_media: bool
            layer_video_input: bool
            def __init__(self, layer_audio: bool = ..., layer_messages: bool = ..., layer_props: bool = ..., layer_announcement: bool = ..., layer_slide: bool = ..., layer_media: bool = ..., layer_video_input: bool = ...) -> None: ...
        class CaptureStart(_message.Message):
            __slots__ = ("preset_type",)
            class PresetType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                PRESET_TYPE_UNKNOWN: _ClassVar[Trigger.Action.CaptureStart.PresetType]
                PRESET_TYPE_ACTIVE_SETTINGS: _ClassVar[Trigger.Action.CaptureStart.PresetType]
                PRESET_TYPE_CAPTURE_PRESET: _ClassVar[Trigger.Action.CaptureStart.PresetType]
            PRESET_TYPE_UNKNOWN: Trigger.Action.CaptureStart.PresetType
            PRESET_TYPE_ACTIVE_SETTINGS: Trigger.Action.CaptureStart.PresetType
            PRESET_TYPE_CAPTURE_PRESET: Trigger.Action.CaptureStart.PresetType
            PRESET_TYPE_FIELD_NUMBER: _ClassVar[int]
            preset_type: Trigger.Action.CaptureStart.PresetType
            def __init__(self, preset_type: _Optional[_Union[Trigger.Action.CaptureStart.PresetType, str]] = ...) -> None: ...
        class CaptureStop(_message.Message):
            __slots__ = ("confirm_before_stopping",)
            CONFIRM_BEFORE_STOPPING_FIELD_NUMBER: _ClassVar[int]
            confirm_before_stopping: bool
            def __init__(self, confirm_before_stopping: bool = ...) -> None: ...
        CLEAR_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FIELD_NUMBER: _ClassVar[int]
        MEDIA_BIN_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        AUDIO_BIN_PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        STAGE_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        PROP_FIELD_NUMBER: _ClassVar[int]
        LOOK_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        COMMUNICATIONS_FIELD_NUMBER: _ClassVar[int]
        SLIDE_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        MACRO_FIELD_NUMBER: _ClassVar[int]
        CLEAR_GROUP_FIELD_NUMBER: _ClassVar[int]
        CAPTURE_START_FIELD_NUMBER: _ClassVar[int]
        CAPTURE_STOP_FIELD_NUMBER: _ClassVar[int]
        clear: Trigger.Action.ClearLayer
        media: _analyticsTriggerMedia_pb2.TriggerMediaInformation
        media_bin_playlist: Trigger.Action.MediaBinPlaylist
        audio_bin_playlist: Trigger.Action.AudioBinPlaylist
        stage: Trigger.Action.Stage
        timer: Trigger.Action.Timer
        prop: Trigger.Action.Prop
        look: Trigger.Action.Look
        message: Trigger.Action.Message
        communications: Trigger.Action.Communications
        slide_destination: Trigger.Action.SlideDestination
        macro: Trigger.Action.Macro
        clear_group: Trigger.Action.ClearGroup
        capture_start: Trigger.Action.CaptureStart
        capture_stop: Trigger.Action.CaptureStop
        def __init__(self, clear: _Optional[_Union[Trigger.Action.ClearLayer, _Mapping]] = ..., media: _Optional[_Union[_analyticsTriggerMedia_pb2.TriggerMediaInformation, _Mapping]] = ..., media_bin_playlist: _Optional[_Union[Trigger.Action.MediaBinPlaylist, _Mapping]] = ..., audio_bin_playlist: _Optional[_Union[Trigger.Action.AudioBinPlaylist, _Mapping]] = ..., stage: _Optional[_Union[Trigger.Action.Stage, _Mapping]] = ..., timer: _Optional[_Union[Trigger.Action.Timer, _Mapping]] = ..., prop: _Optional[_Union[Trigger.Action.Prop, _Mapping]] = ..., look: _Optional[_Union[Trigger.Action.Look, _Mapping]] = ..., message: _Optional[_Union[Trigger.Action.Message, _Mapping]] = ..., communications: _Optional[_Union[Trigger.Action.Communications, _Mapping]] = ..., slide_destination: _Optional[_Union[Trigger.Action.SlideDestination, _Mapping]] = ..., macro: _Optional[_Union[Trigger.Action.Macro, _Mapping]] = ..., clear_group: _Optional[_Union[Trigger.Action.ClearGroup, _Mapping]] = ..., capture_start: _Optional[_Union[Trigger.Action.CaptureStart, _Mapping]] = ..., capture_stop: _Optional[_Union[Trigger.Action.CaptureStop, _Mapping]] = ...) -> None: ...
    class MediaBin(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AudioBin(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TestPattern(_message.Message):
        __slots__ = ("test_pattern_type", "logo")
        class TestPatternType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TEST_PATTERN_TYPE_AUDIO_VIDEO_SYNC: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_BLEND_GRID: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_COLOR_BARS: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_CUSTOM_COLORS: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_FOCUS: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_GRAY_SCALE: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_LINES: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_LOGO_BOUNCE: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_RADAR: _ClassVar[Trigger.TestPattern.TestPatternType]
            TEST_PATTERN_TYPE_TEXT: _ClassVar[Trigger.TestPattern.TestPatternType]
        TEST_PATTERN_TYPE_AUDIO_VIDEO_SYNC: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_BLEND_GRID: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_COLOR_BARS: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_CUSTOM_COLORS: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_FOCUS: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_GRAY_SCALE: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_LINES: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_LOGO_BOUNCE: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_RADAR: Trigger.TestPattern.TestPatternType
        TEST_PATTERN_TYPE_TEXT: Trigger.TestPattern.TestPatternType
        class LogoType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LOGO_TYPE_NONE: _ClassVar[Trigger.TestPattern.LogoType]
            LOGO_TYPE_PROPRESENTER: _ClassVar[Trigger.TestPattern.LogoType]
            LOGO_TYPE_CUSTOM: _ClassVar[Trigger.TestPattern.LogoType]
        LOGO_TYPE_NONE: Trigger.TestPattern.LogoType
        LOGO_TYPE_PROPRESENTER: Trigger.TestPattern.LogoType
        LOGO_TYPE_CUSTOM: Trigger.TestPattern.LogoType
        TEST_PATTERN_TYPE_FIELD_NUMBER: _ClassVar[int]
        LOGO_FIELD_NUMBER: _ClassVar[int]
        test_pattern_type: Trigger.TestPattern.TestPatternType
        logo: Trigger.TestPattern.LogoType
        def __init__(self, test_pattern_type: _Optional[_Union[Trigger.TestPattern.TestPatternType, str]] = ..., logo: _Optional[_Union[Trigger.TestPattern.LogoType, str]] = ...) -> None: ...
    CUE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    MEDIA_BIN_FIELD_NUMBER: _ClassVar[int]
    AUDIO_BIN_FIELD_NUMBER: _ClassVar[int]
    TEST_PATTERN_FIELD_NUMBER: _ClassVar[int]
    cue: Trigger.Cue
    action: Trigger.Action
    media_bin: Trigger.MediaBin
    audio_bin: Trigger.AudioBin
    test_pattern: Trigger.TestPattern
    def __init__(self, cue: _Optional[_Union[Trigger.Cue, _Mapping]] = ..., action: _Optional[_Union[Trigger.Action, _Mapping]] = ..., media_bin: _Optional[_Union[Trigger.MediaBin, _Mapping]] = ..., audio_bin: _Optional[_Union[Trigger.AudioBin, _Mapping]] = ..., test_pattern: _Optional[_Union[Trigger.TestPattern, _Mapping]] = ...) -> None: ...
