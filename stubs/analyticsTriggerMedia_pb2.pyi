from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerMediaInformation(_message.Message):
    __slots__ = ("source_type", "video", "image", "audio", "live_video")
    class SourceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        SOURCE_TYPE_LOCAL: _ClassVar[TriggerMediaInformation.SourceType]
        SOURCE_TYPE_PROCONTENT: _ClassVar[TriggerMediaInformation.SourceType]
    SOURCE_TYPE_LOCAL: TriggerMediaInformation.SourceType
    SOURCE_TYPE_PROCONTENT: TriggerMediaInformation.SourceType
    class Transition(_message.Message):
        __slots__ = ("is_default", "name")
        IS_DEFAULT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        is_default: bool
        name: str
        def __init__(self, is_default: bool = ..., name: _Optional[str] = ...) -> None: ...
    class VisualMedia(_message.Message):
        __slots__ = ("behavior", "scale_mode", "flip_mode", "native_rotation", "resolution", "enabled_effects_count", "has_effect_preset", "transition")
        class Behavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BEHAVIOR_BACKGROUND: _ClassVar[TriggerMediaInformation.VisualMedia.Behavior]
            BEHAVIOR_FOREGROUND: _ClassVar[TriggerMediaInformation.VisualMedia.Behavior]
            BEHAVIOR_VIDEO_INPUT: _ClassVar[TriggerMediaInformation.VisualMedia.Behavior]
        BEHAVIOR_BACKGROUND: TriggerMediaInformation.VisualMedia.Behavior
        BEHAVIOR_FOREGROUND: TriggerMediaInformation.VisualMedia.Behavior
        BEHAVIOR_VIDEO_INPUT: TriggerMediaInformation.VisualMedia.Behavior
        class ScaleMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_MODE_FIT: _ClassVar[TriggerMediaInformation.VisualMedia.ScaleMode]
            SCALE_MODE_FILL: _ClassVar[TriggerMediaInformation.VisualMedia.ScaleMode]
            SCALE_MODE_STRETCH: _ClassVar[TriggerMediaInformation.VisualMedia.ScaleMode]
            SCALE_MODE_BLUR: _ClassVar[TriggerMediaInformation.VisualMedia.ScaleMode]
        SCALE_MODE_FIT: TriggerMediaInformation.VisualMedia.ScaleMode
        SCALE_MODE_FILL: TriggerMediaInformation.VisualMedia.ScaleMode
        SCALE_MODE_STRETCH: TriggerMediaInformation.VisualMedia.ScaleMode
        SCALE_MODE_BLUR: TriggerMediaInformation.VisualMedia.ScaleMode
        class FlipMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FLIP_MODE_NONE: _ClassVar[TriggerMediaInformation.VisualMedia.FlipMode]
            FLIP_MODE_HORIZONTAL: _ClassVar[TriggerMediaInformation.VisualMedia.FlipMode]
            FLIP_MODE_VERTICAL: _ClassVar[TriggerMediaInformation.VisualMedia.FlipMode]
            FLIP_MODE_BOTH: _ClassVar[TriggerMediaInformation.VisualMedia.FlipMode]
        FLIP_MODE_NONE: TriggerMediaInformation.VisualMedia.FlipMode
        FLIP_MODE_HORIZONTAL: TriggerMediaInformation.VisualMedia.FlipMode
        FLIP_MODE_VERTICAL: TriggerMediaInformation.VisualMedia.FlipMode
        FLIP_MODE_BOTH: TriggerMediaInformation.VisualMedia.FlipMode
        class NativeRotation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NATIVE_ROTATION_STANDARD: _ClassVar[TriggerMediaInformation.VisualMedia.NativeRotation]
            NATIVE_ROTATION_90: _ClassVar[TriggerMediaInformation.VisualMedia.NativeRotation]
            NATIVE_ROTATION_180: _ClassVar[TriggerMediaInformation.VisualMedia.NativeRotation]
            NATIVE_ROTATION_270: _ClassVar[TriggerMediaInformation.VisualMedia.NativeRotation]
        NATIVE_ROTATION_STANDARD: TriggerMediaInformation.VisualMedia.NativeRotation
        NATIVE_ROTATION_90: TriggerMediaInformation.VisualMedia.NativeRotation
        NATIVE_ROTATION_180: TriggerMediaInformation.VisualMedia.NativeRotation
        NATIVE_ROTATION_270: TriggerMediaInformation.VisualMedia.NativeRotation
        class Size(_message.Message):
            __slots__ = ("width", "height")
            WIDTH_FIELD_NUMBER: _ClassVar[int]
            HEIGHT_FIELD_NUMBER: _ClassVar[int]
            width: int
            height: int
            def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
        BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        SCALE_MODE_FIELD_NUMBER: _ClassVar[int]
        FLIP_MODE_FIELD_NUMBER: _ClassVar[int]
        NATIVE_ROTATION_FIELD_NUMBER: _ClassVar[int]
        RESOLUTION_FIELD_NUMBER: _ClassVar[int]
        ENABLED_EFFECTS_COUNT_FIELD_NUMBER: _ClassVar[int]
        HAS_EFFECT_PRESET_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_FIELD_NUMBER: _ClassVar[int]
        behavior: TriggerMediaInformation.VisualMedia.Behavior
        scale_mode: TriggerMediaInformation.VisualMedia.ScaleMode
        flip_mode: TriggerMediaInformation.VisualMedia.FlipMode
        native_rotation: TriggerMediaInformation.VisualMedia.NativeRotation
        resolution: TriggerMediaInformation.VisualMedia.Size
        enabled_effects_count: int
        has_effect_preset: bool
        transition: TriggerMediaInformation.Transition
        def __init__(self, behavior: _Optional[_Union[TriggerMediaInformation.VisualMedia.Behavior, str]] = ..., scale_mode: _Optional[_Union[TriggerMediaInformation.VisualMedia.ScaleMode, str]] = ..., flip_mode: _Optional[_Union[TriggerMediaInformation.VisualMedia.FlipMode, str]] = ..., native_rotation: _Optional[_Union[TriggerMediaInformation.VisualMedia.NativeRotation, str]] = ..., resolution: _Optional[_Union[TriggerMediaInformation.VisualMedia.Size, _Mapping]] = ..., enabled_effects_count: _Optional[int] = ..., has_effect_preset: bool = ..., transition: _Optional[_Union[TriggerMediaInformation.Transition, _Mapping]] = ...) -> None: ...
    class Transport(_message.Message):
        __slots__ = ("source_duration_range", "has_audio_ramp_in", "has_audio_ramp_out", "has_in_point", "has_out_point", "play_rate", "playback_marker_count")
        class DurationRange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            DURATION_UNDER_10S: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
            DURATION_10S_TO_30S: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
            DURATION_30S_TO_60S: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
            DURATION_1M_TO_5M: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
            DURATION_5M_TO_10M: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
            DURATION_10M_TO_30M: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
            DURATION_30M_TO_60M: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
            DURATION_1H_TO_2H: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
            DURATION_OVER_2H: _ClassVar[TriggerMediaInformation.Transport.DurationRange]
        DURATION_UNDER_10S: TriggerMediaInformation.Transport.DurationRange
        DURATION_10S_TO_30S: TriggerMediaInformation.Transport.DurationRange
        DURATION_30S_TO_60S: TriggerMediaInformation.Transport.DurationRange
        DURATION_1M_TO_5M: TriggerMediaInformation.Transport.DurationRange
        DURATION_5M_TO_10M: TriggerMediaInformation.Transport.DurationRange
        DURATION_10M_TO_30M: TriggerMediaInformation.Transport.DurationRange
        DURATION_30M_TO_60M: TriggerMediaInformation.Transport.DurationRange
        DURATION_1H_TO_2H: TriggerMediaInformation.Transport.DurationRange
        DURATION_OVER_2H: TriggerMediaInformation.Transport.DurationRange
        SOURCE_DURATION_RANGE_FIELD_NUMBER: _ClassVar[int]
        HAS_AUDIO_RAMP_IN_FIELD_NUMBER: _ClassVar[int]
        HAS_AUDIO_RAMP_OUT_FIELD_NUMBER: _ClassVar[int]
        HAS_IN_POINT_FIELD_NUMBER: _ClassVar[int]
        HAS_OUT_POINT_FIELD_NUMBER: _ClassVar[int]
        PLAY_RATE_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_MARKER_COUNT_FIELD_NUMBER: _ClassVar[int]
        source_duration_range: TriggerMediaInformation.Transport.DurationRange
        has_audio_ramp_in: bool
        has_audio_ramp_out: bool
        has_in_point: bool
        has_out_point: bool
        play_rate: float
        playback_marker_count: int
        def __init__(self, source_duration_range: _Optional[_Union[TriggerMediaInformation.Transport.DurationRange, str]] = ..., has_audio_ramp_in: bool = ..., has_audio_ramp_out: bool = ..., has_in_point: bool = ..., has_out_point: bool = ..., play_rate: _Optional[float] = ..., playback_marker_count: _Optional[int] = ...) -> None: ...
    class Video(_message.Message):
        __slots__ = ("visual_media", "playback_behavior", "completion_target", "soft_loop_enabled", "soft_loop_duration", "frame_rate", "audio_channel_count", "transport")
        class PlaybackBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PLAYBACK_BEHAVIOR_STOP: _ClassVar[TriggerMediaInformation.Video.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_LOOP: _ClassVar[TriggerMediaInformation.Video.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_LOOP_FOR_PLAY_COUNT: _ClassVar[TriggerMediaInformation.Video.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: _ClassVar[TriggerMediaInformation.Video.PlaybackBehavior]
        PLAYBACK_BEHAVIOR_STOP: TriggerMediaInformation.Video.PlaybackBehavior
        PLAYBACK_BEHAVIOR_LOOP: TriggerMediaInformation.Video.PlaybackBehavior
        PLAYBACK_BEHAVIOR_LOOP_FOR_PLAY_COUNT: TriggerMediaInformation.Video.PlaybackBehavior
        PLAYBACK_BEHAVIOR_LOOP_FOR_TIME: TriggerMediaInformation.Video.PlaybackBehavior
        class CompletionTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            COMPLETION_TARGET_NONE: _ClassVar[TriggerMediaInformation.Video.CompletionTarget]
            COMPLETION_TARGET_NEXT: _ClassVar[TriggerMediaInformation.Video.CompletionTarget]
            COMPLETION_TARGET_RANDOM: _ClassVar[TriggerMediaInformation.Video.CompletionTarget]
            COMPLETION_TARGET_CUE: _ClassVar[TriggerMediaInformation.Video.CompletionTarget]
            COMPLETION_TARGET_FIRST: _ClassVar[TriggerMediaInformation.Video.CompletionTarget]
        COMPLETION_TARGET_NONE: TriggerMediaInformation.Video.CompletionTarget
        COMPLETION_TARGET_NEXT: TriggerMediaInformation.Video.CompletionTarget
        COMPLETION_TARGET_RANDOM: TriggerMediaInformation.Video.CompletionTarget
        COMPLETION_TARGET_CUE: TriggerMediaInformation.Video.CompletionTarget
        COMPLETION_TARGET_FIRST: TriggerMediaInformation.Video.CompletionTarget
        VISUAL_MEDIA_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_TARGET_FIELD_NUMBER: _ClassVar[int]
        SOFT_LOOP_ENABLED_FIELD_NUMBER: _ClassVar[int]
        SOFT_LOOP_DURATION_FIELD_NUMBER: _ClassVar[int]
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        AUDIO_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_FIELD_NUMBER: _ClassVar[int]
        visual_media: TriggerMediaInformation.VisualMedia
        playback_behavior: TriggerMediaInformation.Video.PlaybackBehavior
        completion_target: TriggerMediaInformation.Video.CompletionTarget
        soft_loop_enabled: bool
        soft_loop_duration: float
        frame_rate: float
        audio_channel_count: int
        transport: TriggerMediaInformation.Transport
        def __init__(self, visual_media: _Optional[_Union[TriggerMediaInformation.VisualMedia, _Mapping]] = ..., playback_behavior: _Optional[_Union[TriggerMediaInformation.Video.PlaybackBehavior, str]] = ..., completion_target: _Optional[_Union[TriggerMediaInformation.Video.CompletionTarget, str]] = ..., soft_loop_enabled: bool = ..., soft_loop_duration: _Optional[float] = ..., frame_rate: _Optional[float] = ..., audio_channel_count: _Optional[int] = ..., transport: _Optional[_Union[TriggerMediaInformation.Transport, _Mapping]] = ...) -> None: ...
    class Audio(_message.Message):
        __slots__ = ("behavior", "playback_behavior", "transition", "audio_channel_count", "transport")
        class Behavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            BEHAVIOR_TUNE: _ClassVar[TriggerMediaInformation.Audio.Behavior]
            BEHAVIOR_SOUND: _ClassVar[TriggerMediaInformation.Audio.Behavior]
        BEHAVIOR_TUNE: TriggerMediaInformation.Audio.Behavior
        BEHAVIOR_SOUND: TriggerMediaInformation.Audio.Behavior
        class PlaybackBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            PLAYBACK_BEHAVIOR_STOP: _ClassVar[TriggerMediaInformation.Audio.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_LOOP: _ClassVar[TriggerMediaInformation.Audio.PlaybackBehavior]
            PLAYBACK_BEHAVIOR_NEXT: _ClassVar[TriggerMediaInformation.Audio.PlaybackBehavior]
        PLAYBACK_BEHAVIOR_STOP: TriggerMediaInformation.Audio.PlaybackBehavior
        PLAYBACK_BEHAVIOR_LOOP: TriggerMediaInformation.Audio.PlaybackBehavior
        PLAYBACK_BEHAVIOR_NEXT: TriggerMediaInformation.Audio.PlaybackBehavior
        BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        PLAYBACK_BEHAVIOR_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_FIELD_NUMBER: _ClassVar[int]
        AUDIO_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        TRANSPORT_FIELD_NUMBER: _ClassVar[int]
        behavior: TriggerMediaInformation.Audio.Behavior
        playback_behavior: TriggerMediaInformation.Audio.PlaybackBehavior
        transition: TriggerMediaInformation.Transition
        audio_channel_count: int
        transport: TriggerMediaInformation.Transport
        def __init__(self, behavior: _Optional[_Union[TriggerMediaInformation.Audio.Behavior, str]] = ..., playback_behavior: _Optional[_Union[TriggerMediaInformation.Audio.PlaybackBehavior, str]] = ..., transition: _Optional[_Union[TriggerMediaInformation.Transition, _Mapping]] = ..., audio_channel_count: _Optional[int] = ..., transport: _Optional[_Union[TriggerMediaInformation.Transport, _Mapping]] = ...) -> None: ...
    class Image(_message.Message):
        __slots__ = ("visual_media", "transition", "completion_target")
        class CompletionTarget(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            COMPLETION_TARGET_NONE: _ClassVar[TriggerMediaInformation.Image.CompletionTarget]
            COMPLETION_TARGET_NEXT: _ClassVar[TriggerMediaInformation.Image.CompletionTarget]
            COMPLETION_TARGET_RANDOM: _ClassVar[TriggerMediaInformation.Image.CompletionTarget]
            COMPLETION_TARGET_CUE: _ClassVar[TriggerMediaInformation.Image.CompletionTarget]
            COMPLETION_TARGET_FIRST: _ClassVar[TriggerMediaInformation.Image.CompletionTarget]
        COMPLETION_TARGET_NONE: TriggerMediaInformation.Image.CompletionTarget
        COMPLETION_TARGET_NEXT: TriggerMediaInformation.Image.CompletionTarget
        COMPLETION_TARGET_RANDOM: TriggerMediaInformation.Image.CompletionTarget
        COMPLETION_TARGET_CUE: TriggerMediaInformation.Image.CompletionTarget
        COMPLETION_TARGET_FIRST: TriggerMediaInformation.Image.CompletionTarget
        VISUAL_MEDIA_FIELD_NUMBER: _ClassVar[int]
        TRANSITION_FIELD_NUMBER: _ClassVar[int]
        COMPLETION_TARGET_FIELD_NUMBER: _ClassVar[int]
        visual_media: TriggerMediaInformation.VisualMedia
        transition: TriggerMediaInformation.Transition
        completion_target: TriggerMediaInformation.Image.CompletionTarget
        def __init__(self, visual_media: _Optional[_Union[TriggerMediaInformation.VisualMedia, _Mapping]] = ..., transition: _Optional[_Union[TriggerMediaInformation.Transition, _Mapping]] = ..., completion_target: _Optional[_Union[TriggerMediaInformation.Image.CompletionTarget, str]] = ...) -> None: ...
    class LiveVideo(_message.Message):
        __slots__ = ("visual_media", "frame_rate", "audio_channel_count")
        VISUAL_MEDIA_FIELD_NUMBER: _ClassVar[int]
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        AUDIO_CHANNEL_COUNT_FIELD_NUMBER: _ClassVar[int]
        visual_media: TriggerMediaInformation.VisualMedia
        frame_rate: float
        audio_channel_count: int
        def __init__(self, visual_media: _Optional[_Union[TriggerMediaInformation.VisualMedia, _Mapping]] = ..., frame_rate: _Optional[float] = ..., audio_channel_count: _Optional[int] = ...) -> None: ...
    SOURCE_TYPE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_FIELD_NUMBER: _ClassVar[int]
    IMAGE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIDEO_FIELD_NUMBER: _ClassVar[int]
    source_type: TriggerMediaInformation.SourceType
    video: TriggerMediaInformation.Video
    image: TriggerMediaInformation.Image
    audio: TriggerMediaInformation.Audio
    live_video: TriggerMediaInformation.LiveVideo
    def __init__(self, source_type: _Optional[_Union[TriggerMediaInformation.SourceType, str]] = ..., video: _Optional[_Union[TriggerMediaInformation.Video, _Mapping]] = ..., image: _Optional[_Union[TriggerMediaInformation.Image, _Mapping]] = ..., audio: _Optional[_Union[TriggerMediaInformation.Audio, _Mapping]] = ..., live_video: _Optional[_Union[TriggerMediaInformation.LiveVideo, _Mapping]] = ...) -> None: ...
