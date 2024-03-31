import action_pb2 as _action_pb2
import alphaType_pb2 as _alphaType_pb2
import ccli_pb2 as _ccli_pb2
import cue_pb2 as _cue_pb2
import effects_pb2 as _effects_pb2
import graphicsData_pb2 as _graphicsData_pb2
import input_pb2 as _input_pb2
import macros_pb2 as _macros_pb2
import messages_pb2 as _messages_pb2
import playlist_pb2 as _playlist_pb2
import preferences_pb2 as _preferences_pb2
import presentation_pb2 as _presentation_pb2
import proCoreTestPatterns_pb2 as _proCoreTestPatterns_pb2
import propDocument_pb2 as _propDocument_pb2
import propresenter_pb2 as _propresenter_pb2
import slide_pb2 as _slide_pb2
import recording_pb2 as _recording_pb2
import stage_pb2 as _stage_pb2
import timers_pb2 as _timers_pb2
import url_pb2 as _url_pb2
import uuid_pb2 as _uuid_pb2
import proworkspace_pb2 as _proworkspace_pb2
import digitalAudio_pb2 as _digitalAudio_pb2
import proAudienceLook_pb2 as _proAudienceLook_pb2
import proMask_pb2 as _proMask_pb2
import timedPlayback_pb2 as _timedPlayback_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MediaMetadataRequestInfo(_message.Message):
    __slots__ = ("file_path", "time", "width", "height", "effects", "crop_insets", "native_rotation", "flipped_horizontally", "flipped_vertically", "alpha_type")
    class NativeRotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NATIVE_ROTATION_TYPE_ROTATE_STANDARD: _ClassVar[MediaMetadataRequestInfo.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_90: _ClassVar[MediaMetadataRequestInfo.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_180: _ClassVar[MediaMetadataRequestInfo.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_270: _ClassVar[MediaMetadataRequestInfo.NativeRotationType]
    NATIVE_ROTATION_TYPE_ROTATE_STANDARD: MediaMetadataRequestInfo.NativeRotationType
    NATIVE_ROTATION_TYPE_ROTATE_90: MediaMetadataRequestInfo.NativeRotationType
    NATIVE_ROTATION_TYPE_ROTATE_180: MediaMetadataRequestInfo.NativeRotationType
    NATIVE_ROTATION_TYPE_ROTATE_270: MediaMetadataRequestInfo.NativeRotationType
    class AlphaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALPHA_TYPE_UNKNOWN: _ClassVar[MediaMetadataRequestInfo.AlphaType]
        ALPHA_TYPE_STRAIGHT: _ClassVar[MediaMetadataRequestInfo.AlphaType]
        ALPHA_TYPE_PREMULTIPLIED: _ClassVar[MediaMetadataRequestInfo.AlphaType]
    ALPHA_TYPE_UNKNOWN: MediaMetadataRequestInfo.AlphaType
    ALPHA_TYPE_STRAIGHT: MediaMetadataRequestInfo.AlphaType
    ALPHA_TYPE_PREMULTIPLIED: MediaMetadataRequestInfo.AlphaType
    FILE_PATH_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    EFFECTS_FIELD_NUMBER: _ClassVar[int]
    CROP_INSETS_FIELD_NUMBER: _ClassVar[int]
    NATIVE_ROTATION_FIELD_NUMBER: _ClassVar[int]
    FLIPPED_HORIZONTALLY_FIELD_NUMBER: _ClassVar[int]
    FLIPPED_VERTICALLY_FIELD_NUMBER: _ClassVar[int]
    ALPHA_TYPE_FIELD_NUMBER: _ClassVar[int]
    file_path: str
    time: float
    width: int
    height: int
    effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
    crop_insets: _graphicsData_pb2.Graphics.EdgeInsets
    native_rotation: MediaMetadataRequestInfo.NativeRotationType
    flipped_horizontally: bool
    flipped_vertically: bool
    alpha_type: MediaMetadataRequestInfo.AlphaType
    def __init__(self, file_path: _Optional[str] = ..., time: _Optional[float] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ..., crop_insets: _Optional[_Union[_graphicsData_pb2.Graphics.EdgeInsets, _Mapping]] = ..., native_rotation: _Optional[_Union[MediaMetadataRequestInfo.NativeRotationType, str]] = ..., flipped_horizontally: bool = ..., flipped_vertically: bool = ..., alpha_type: _Optional[_Union[MediaMetadataRequestInfo.AlphaType, str]] = ...) -> None: ...

class MediaMetadataRequestResponse(_message.Message):
    __slots__ = ("metadata", "generated_bitmap_info")
    class Metadata(_message.Message):
        __slots__ = ("width", "height", "fps", "duration", "number_audio_channels", "codec", "artist", "title", "rotation", "content_type", "has_alpha_channel")
        class ContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_TYPE_UNKNOWN: _ClassVar[MediaMetadataRequestResponse.Metadata.ContentType]
            CONTENT_TYPE_AUDIO: _ClassVar[MediaMetadataRequestResponse.Metadata.ContentType]
            CONTENT_TYPE_IMAGE: _ClassVar[MediaMetadataRequestResponse.Metadata.ContentType]
            CONTENT_TYPE_VIDEO: _ClassVar[MediaMetadataRequestResponse.Metadata.ContentType]
        CONTENT_TYPE_UNKNOWN: MediaMetadataRequestResponse.Metadata.ContentType
        CONTENT_TYPE_AUDIO: MediaMetadataRequestResponse.Metadata.ContentType
        CONTENT_TYPE_IMAGE: MediaMetadataRequestResponse.Metadata.ContentType
        CONTENT_TYPE_VIDEO: MediaMetadataRequestResponse.Metadata.ContentType
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        FPS_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        NUMBER_AUDIO_CHANNELS_FIELD_NUMBER: _ClassVar[int]
        CODEC_FIELD_NUMBER: _ClassVar[int]
        ARTIST_FIELD_NUMBER: _ClassVar[int]
        TITLE_FIELD_NUMBER: _ClassVar[int]
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        CONTENT_TYPE_FIELD_NUMBER: _ClassVar[int]
        HAS_ALPHA_CHANNEL_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        fps: float
        duration: float
        number_audio_channels: int
        codec: str
        artist: str
        title: str
        rotation: float
        content_type: MediaMetadataRequestResponse.Metadata.ContentType
        has_alpha_channel: bool
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ..., fps: _Optional[float] = ..., duration: _Optional[float] = ..., number_audio_channels: _Optional[int] = ..., codec: _Optional[str] = ..., artist: _Optional[str] = ..., title: _Optional[str] = ..., rotation: _Optional[float] = ..., content_type: _Optional[_Union[MediaMetadataRequestResponse.Metadata.ContentType, str]] = ..., has_alpha_channel: bool = ...) -> None: ...
    class BitmapInfo(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    METADATA_FIELD_NUMBER: _ClassVar[int]
    GENERATED_BITMAP_INFO_FIELD_NUMBER: _ClassVar[int]
    metadata: MediaMetadataRequestResponse.Metadata
    generated_bitmap_info: MediaMetadataRequestResponse.BitmapInfo
    def __init__(self, metadata: _Optional[_Union[MediaMetadataRequestResponse.Metadata, _Mapping]] = ..., generated_bitmap_info: _Optional[_Union[MediaMetadataRequestResponse.BitmapInfo, _Mapping]] = ...) -> None: ...

class NetworkIdentifier(_message.Message):
    __slots__ = ("identifiers",)
    class IndexOrName(_message.Message):
        __slots__ = ("index", "name")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        index: int
        name: str
        def __init__(self, index: _Optional[int] = ..., name: _Optional[str] = ...) -> None: ...
    IDENTIFIERS_FIELD_NUMBER: _ClassVar[int]
    identifiers: _containers.RepeatedCompositeFieldContainer[NetworkIdentifier.IndexOrName]
    def __init__(self, identifiers: _Optional[_Iterable[_Union[NetworkIdentifier.IndexOrName, _Mapping]]] = ...) -> None: ...

class TriggerOptions(_message.Message):
    __slots__ = ("content_destination", "suppress_auto_start_video", "suppress_media_background", "force_retrigger", "reset_chord_chart", "from_playlist_library", "from_timeline", "ignore_analytics", "start_position", "trigger_source", "network_identifier", "request_client_context")
    class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONTENT_DESTINATION_GLOBAL: _ClassVar[TriggerOptions.ContentDestination]
        CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[TriggerOptions.ContentDestination]
    CONTENT_DESTINATION_GLOBAL: TriggerOptions.ContentDestination
    CONTENT_DESTINATION_ANNOUNCEMENTS: TriggerOptions.ContentDestination
    CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_AUTO_START_VIDEO_FIELD_NUMBER: _ClassVar[int]
    SUPPRESS_MEDIA_BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    FORCE_RETRIGGER_FIELD_NUMBER: _ClassVar[int]
    RESET_CHORD_CHART_FIELD_NUMBER: _ClassVar[int]
    FROM_PLAYLIST_LIBRARY_FIELD_NUMBER: _ClassVar[int]
    FROM_TIMELINE_FIELD_NUMBER: _ClassVar[int]
    IGNORE_ANALYTICS_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_SOURCE_FIELD_NUMBER: _ClassVar[int]
    NETWORK_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    REQUEST_CLIENT_CONTEXT_FIELD_NUMBER: _ClassVar[int]
    content_destination: TriggerOptions.ContentDestination
    suppress_auto_start_video: bool
    suppress_media_background: bool
    force_retrigger: bool
    reset_chord_chart: bool
    from_playlist_library: bool
    from_timeline: bool
    ignore_analytics: bool
    start_position: float
    trigger_source: _timedPlayback_pb2.TriggerSource
    network_identifier: NetworkIdentifier
    request_client_context: bool
    def __init__(self, content_destination: _Optional[_Union[TriggerOptions.ContentDestination, str]] = ..., suppress_auto_start_video: bool = ..., suppress_media_background: bool = ..., force_retrigger: bool = ..., reset_chord_chart: bool = ..., from_playlist_library: bool = ..., from_timeline: bool = ..., ignore_analytics: bool = ..., start_position: _Optional[float] = ..., trigger_source: _Optional[_Union[_timedPlayback_pb2.TriggerSource, _Mapping]] = ..., network_identifier: _Optional[_Union[NetworkIdentifier, _Mapping]] = ..., request_client_context: bool = ...) -> None: ...

class ControlTransport(_message.Message):
    __slots__ = ("play", "pause", "rewind", "fastforward", "skip_back", "skip_forward", "step_back", "step_forward", "go_to_start", "go_to_end", "jump_to_time", "jump_to_percent", "mark_in", "mark_out", "set_scale_mode", "set_flipped_mode", "set_play_rate", "set_rotation", "toggle_playback", "set_effects", "update_effect", "begin_scrub", "end_scrub", "scrub_to_time", "scrub_to_percent", "set_audio_fade", "set_audio_properties", "set_alpha_type")
    class PlayControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PauseControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class RewindControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class FastForwardControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SkipBackControlType(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: float
        def __init__(self, offset: _Optional[float] = ...) -> None: ...
    class SkipForwardControlType(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: float
        def __init__(self, offset: _Optional[float] = ...) -> None: ...
    class StepBackControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class StepForwardControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GoToStartControlType(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: float
        def __init__(self, offset: _Optional[float] = ...) -> None: ...
    class GoToEndControlType(_message.Message):
        __slots__ = ("offset",)
        OFFSET_FIELD_NUMBER: _ClassVar[int]
        offset: float
        def __init__(self, offset: _Optional[float] = ...) -> None: ...
    class JumpToTimeControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class JumpToPercentControlType(_message.Message):
        __slots__ = ("percent",)
        PERCENT_FIELD_NUMBER: _ClassVar[int]
        percent: float
        def __init__(self, percent: _Optional[float] = ...) -> None: ...
    class MarkInPointControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class MarkOutPointControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class SetScaleModeControlType(_message.Message):
        __slots__ = ("mode", "is_blurred", "alignment")
        class ScaleBehavior(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_BEHAVIOR_FIT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleBehavior]
            SCALE_BEHAVIOR_FILL: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleBehavior]
            SCALE_BEHAVIOR_STRETCH: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleBehavior]
            SCALE_BEHAVIOR_CUSTOM: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleBehavior]
        SCALE_BEHAVIOR_FIT: ControlTransport.SetScaleModeControlType.ScaleBehavior
        SCALE_BEHAVIOR_FILL: ControlTransport.SetScaleModeControlType.ScaleBehavior
        SCALE_BEHAVIOR_STRETCH: ControlTransport.SetScaleModeControlType.ScaleBehavior
        SCALE_BEHAVIOR_CUSTOM: ControlTransport.SetScaleModeControlType.ScaleBehavior
        class ScaleAlignment(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            SCALE_ALIGNMENT_MIDDLE_CENTER: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_LEFT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_CENTER: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_TOP_RIGHT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_MIDDLE_RIGHT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_RIGHT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_CENTER: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_BOTTOM_LEFT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
            SCALE_ALIGNMENT_MIDDLE_LEFT: _ClassVar[ControlTransport.SetScaleModeControlType.ScaleAlignment]
        SCALE_ALIGNMENT_MIDDLE_CENTER: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_TOP_LEFT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_TOP_CENTER: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_TOP_RIGHT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_MIDDLE_RIGHT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_RIGHT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_CENTER: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_BOTTOM_LEFT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        SCALE_ALIGNMENT_MIDDLE_LEFT: ControlTransport.SetScaleModeControlType.ScaleAlignment
        MODE_FIELD_NUMBER: _ClassVar[int]
        IS_BLURRED_FIELD_NUMBER: _ClassVar[int]
        ALIGNMENT_FIELD_NUMBER: _ClassVar[int]
        mode: ControlTransport.SetScaleModeControlType.ScaleBehavior
        is_blurred: bool
        alignment: ControlTransport.SetScaleModeControlType.ScaleAlignment
        def __init__(self, mode: _Optional[_Union[ControlTransport.SetScaleModeControlType.ScaleBehavior, str]] = ..., is_blurred: bool = ..., alignment: _Optional[_Union[ControlTransport.SetScaleModeControlType.ScaleAlignment, str]] = ...) -> None: ...
    class SetFlippedModeControlType(_message.Message):
        __slots__ = ("horizontal", "vertical")
        HORIZONTAL_FIELD_NUMBER: _ClassVar[int]
        VERTICAL_FIELD_NUMBER: _ClassVar[int]
        horizontal: bool
        vertical: bool
        def __init__(self, horizontal: bool = ..., vertical: bool = ...) -> None: ...
    class SetPlayRateControlType(_message.Message):
        __slots__ = ("play_rate",)
        PLAY_RATE_FIELD_NUMBER: _ClassVar[int]
        play_rate: float
        def __init__(self, play_rate: _Optional[float] = ...) -> None: ...
    class SetNativeRotationControlType(_message.Message):
        __slots__ = ("rotation",)
        class NativeRotationType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            NATIVE_ROTATION_TYPE_ROTATE_STANDARD: _ClassVar[ControlTransport.SetNativeRotationControlType.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_90: _ClassVar[ControlTransport.SetNativeRotationControlType.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_180: _ClassVar[ControlTransport.SetNativeRotationControlType.NativeRotationType]
            NATIVE_ROTATION_TYPE_ROTATE_270: _ClassVar[ControlTransport.SetNativeRotationControlType.NativeRotationType]
        NATIVE_ROTATION_TYPE_ROTATE_STANDARD: ControlTransport.SetNativeRotationControlType.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_90: ControlTransport.SetNativeRotationControlType.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_180: ControlTransport.SetNativeRotationControlType.NativeRotationType
        NATIVE_ROTATION_TYPE_ROTATE_270: ControlTransport.SetNativeRotationControlType.NativeRotationType
        ROTATION_FIELD_NUMBER: _ClassVar[int]
        rotation: ControlTransport.SetNativeRotationControlType.NativeRotationType
        def __init__(self, rotation: _Optional[_Union[ControlTransport.SetNativeRotationControlType.NativeRotationType, str]] = ...) -> None: ...
    class SetAlphaTypeControlType(_message.Message):
        __slots__ = ("alpha_type",)
        class AlphaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ALPHA_TYPE_UNKNOWN: _ClassVar[ControlTransport.SetAlphaTypeControlType.AlphaType]
            ALPHA_TYPE_STRAIGHT: _ClassVar[ControlTransport.SetAlphaTypeControlType.AlphaType]
            ALPHA_TYPE_PREMULTIPLIED: _ClassVar[ControlTransport.SetAlphaTypeControlType.AlphaType]
        ALPHA_TYPE_UNKNOWN: ControlTransport.SetAlphaTypeControlType.AlphaType
        ALPHA_TYPE_STRAIGHT: ControlTransport.SetAlphaTypeControlType.AlphaType
        ALPHA_TYPE_PREMULTIPLIED: ControlTransport.SetAlphaTypeControlType.AlphaType
        ALPHA_TYPE_FIELD_NUMBER: _ClassVar[int]
        alpha_type: ControlTransport.SetAlphaTypeControlType.AlphaType
        def __init__(self, alpha_type: _Optional[_Union[ControlTransport.SetAlphaTypeControlType.AlphaType, str]] = ...) -> None: ...
    class TogglePlaybackControlType(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SetEffectsControlType(_message.Message):
        __slots__ = ("effects",)
        EFFECTS_FIELD_NUMBER: _ClassVar[int]
        effects: _containers.RepeatedCompositeFieldContainer[_effects_pb2.Effect]
        def __init__(self, effects: _Optional[_Iterable[_Union[_effects_pb2.Effect, _Mapping]]] = ...) -> None: ...
    class UpdateEffectControlType(_message.Message):
        __slots__ = ("effect",)
        EFFECT_FIELD_NUMBER: _ClassVar[int]
        effect: _effects_pb2.Effect
        def __init__(self, effect: _Optional[_Union[_effects_pb2.Effect, _Mapping]] = ...) -> None: ...
    class BeginScrubControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class EndScrubControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class ScrubToTimeControlType(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: float
        def __init__(self, time: _Optional[float] = ...) -> None: ...
    class ScrubToPercentControlType(_message.Message):
        __slots__ = ("percent",)
        PERCENT_FIELD_NUMBER: _ClassVar[int]
        percent: float
        def __init__(self, percent: _Optional[float] = ...) -> None: ...
    class SetAudioFadeType(_message.Message):
        __slots__ = ("fade_in_duration", "fade_out_duration", "should_fade_in", "should_fade_out")
        FADE_IN_DURATION_FIELD_NUMBER: _ClassVar[int]
        FADE_OUT_DURATION_FIELD_NUMBER: _ClassVar[int]
        SHOULD_FADE_IN_FIELD_NUMBER: _ClassVar[int]
        SHOULD_FADE_OUT_FIELD_NUMBER: _ClassVar[int]
        fade_in_duration: float
        fade_out_duration: float
        should_fade_in: bool
        should_fade_out: bool
        def __init__(self, fade_in_duration: _Optional[float] = ..., fade_out_duration: _Optional[float] = ..., should_fade_in: bool = ..., should_fade_out: bool = ...) -> None: ...
    class SetAudioPropertiesType(_message.Message):
        __slots__ = ("audio_properties", "solo")
        AUDIO_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
        SOLO_FIELD_NUMBER: _ClassVar[int]
        audio_properties: _graphicsData_pb2.Media.AudioProperties
        solo: _containers.RepeatedScalarFieldContainer[bool]
        def __init__(self, audio_properties: _Optional[_Union[_graphicsData_pb2.Media.AudioProperties, _Mapping]] = ..., solo: _Optional[_Iterable[bool]] = ...) -> None: ...
    PLAY_FIELD_NUMBER: _ClassVar[int]
    PAUSE_FIELD_NUMBER: _ClassVar[int]
    REWIND_FIELD_NUMBER: _ClassVar[int]
    FASTFORWARD_FIELD_NUMBER: _ClassVar[int]
    SKIP_BACK_FIELD_NUMBER: _ClassVar[int]
    SKIP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    STEP_BACK_FIELD_NUMBER: _ClassVar[int]
    STEP_FORWARD_FIELD_NUMBER: _ClassVar[int]
    GO_TO_START_FIELD_NUMBER: _ClassVar[int]
    GO_TO_END_FIELD_NUMBER: _ClassVar[int]
    JUMP_TO_TIME_FIELD_NUMBER: _ClassVar[int]
    JUMP_TO_PERCENT_FIELD_NUMBER: _ClassVar[int]
    MARK_IN_FIELD_NUMBER: _ClassVar[int]
    MARK_OUT_FIELD_NUMBER: _ClassVar[int]
    SET_SCALE_MODE_FIELD_NUMBER: _ClassVar[int]
    SET_FLIPPED_MODE_FIELD_NUMBER: _ClassVar[int]
    SET_PLAY_RATE_FIELD_NUMBER: _ClassVar[int]
    SET_ROTATION_FIELD_NUMBER: _ClassVar[int]
    TOGGLE_PLAYBACK_FIELD_NUMBER: _ClassVar[int]
    SET_EFFECTS_FIELD_NUMBER: _ClassVar[int]
    UPDATE_EFFECT_FIELD_NUMBER: _ClassVar[int]
    BEGIN_SCRUB_FIELD_NUMBER: _ClassVar[int]
    END_SCRUB_FIELD_NUMBER: _ClassVar[int]
    SCRUB_TO_TIME_FIELD_NUMBER: _ClassVar[int]
    SCRUB_TO_PERCENT_FIELD_NUMBER: _ClassVar[int]
    SET_AUDIO_FADE_FIELD_NUMBER: _ClassVar[int]
    SET_AUDIO_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    SET_ALPHA_TYPE_FIELD_NUMBER: _ClassVar[int]
    play: ControlTransport.PlayControlType
    pause: ControlTransport.PauseControlType
    rewind: ControlTransport.RewindControlType
    fastforward: ControlTransport.FastForwardControlType
    skip_back: ControlTransport.SkipBackControlType
    skip_forward: ControlTransport.SkipForwardControlType
    step_back: ControlTransport.StepBackControlType
    step_forward: ControlTransport.StepForwardControlType
    go_to_start: ControlTransport.GoToStartControlType
    go_to_end: ControlTransport.GoToEndControlType
    jump_to_time: ControlTransport.JumpToTimeControlType
    jump_to_percent: ControlTransport.JumpToPercentControlType
    mark_in: ControlTransport.MarkInPointControlType
    mark_out: ControlTransport.MarkOutPointControlType
    set_scale_mode: ControlTransport.SetScaleModeControlType
    set_flipped_mode: ControlTransport.SetFlippedModeControlType
    set_play_rate: ControlTransport.SetPlayRateControlType
    set_rotation: ControlTransport.SetNativeRotationControlType
    toggle_playback: ControlTransport.TogglePlaybackControlType
    set_effects: ControlTransport.SetEffectsControlType
    update_effect: ControlTransport.UpdateEffectControlType
    begin_scrub: ControlTransport.BeginScrubControlType
    end_scrub: ControlTransport.EndScrubControlType
    scrub_to_time: ControlTransport.ScrubToTimeControlType
    scrub_to_percent: ControlTransport.ScrubToPercentControlType
    set_audio_fade: ControlTransport.SetAudioFadeType
    set_audio_properties: ControlTransport.SetAudioPropertiesType
    set_alpha_type: ControlTransport.SetAlphaTypeControlType
    def __init__(self, play: _Optional[_Union[ControlTransport.PlayControlType, _Mapping]] = ..., pause: _Optional[_Union[ControlTransport.PauseControlType, _Mapping]] = ..., rewind: _Optional[_Union[ControlTransport.RewindControlType, _Mapping]] = ..., fastforward: _Optional[_Union[ControlTransport.FastForwardControlType, _Mapping]] = ..., skip_back: _Optional[_Union[ControlTransport.SkipBackControlType, _Mapping]] = ..., skip_forward: _Optional[_Union[ControlTransport.SkipForwardControlType, _Mapping]] = ..., step_back: _Optional[_Union[ControlTransport.StepBackControlType, _Mapping]] = ..., step_forward: _Optional[_Union[ControlTransport.StepForwardControlType, _Mapping]] = ..., go_to_start: _Optional[_Union[ControlTransport.GoToStartControlType, _Mapping]] = ..., go_to_end: _Optional[_Union[ControlTransport.GoToEndControlType, _Mapping]] = ..., jump_to_time: _Optional[_Union[ControlTransport.JumpToTimeControlType, _Mapping]] = ..., jump_to_percent: _Optional[_Union[ControlTransport.JumpToPercentControlType, _Mapping]] = ..., mark_in: _Optional[_Union[ControlTransport.MarkInPointControlType, _Mapping]] = ..., mark_out: _Optional[_Union[ControlTransport.MarkOutPointControlType, _Mapping]] = ..., set_scale_mode: _Optional[_Union[ControlTransport.SetScaleModeControlType, _Mapping]] = ..., set_flipped_mode: _Optional[_Union[ControlTransport.SetFlippedModeControlType, _Mapping]] = ..., set_play_rate: _Optional[_Union[ControlTransport.SetPlayRateControlType, _Mapping]] = ..., set_rotation: _Optional[_Union[ControlTransport.SetNativeRotationControlType, _Mapping]] = ..., toggle_playback: _Optional[_Union[ControlTransport.TogglePlaybackControlType, _Mapping]] = ..., set_effects: _Optional[_Union[ControlTransport.SetEffectsControlType, _Mapping]] = ..., update_effect: _Optional[_Union[ControlTransport.UpdateEffectControlType, _Mapping]] = ..., begin_scrub: _Optional[_Union[ControlTransport.BeginScrubControlType, _Mapping]] = ..., end_scrub: _Optional[_Union[ControlTransport.EndScrubControlType, _Mapping]] = ..., scrub_to_time: _Optional[_Union[ControlTransport.ScrubToTimeControlType, _Mapping]] = ..., scrub_to_percent: _Optional[_Union[ControlTransport.ScrubToPercentControlType, _Mapping]] = ..., set_audio_fade: _Optional[_Union[ControlTransport.SetAudioFadeType, _Mapping]] = ..., set_audio_properties: _Optional[_Union[ControlTransport.SetAudioPropertiesType, _Mapping]] = ..., set_alpha_type: _Optional[_Union[ControlTransport.SetAlphaTypeControlType, _Mapping]] = ...) -> None: ...

class AudioInputSettings(_message.Message):
    __slots__ = ("inputs", "transitionTime")
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    TRANSITIONTIME_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.RepeatedCompositeFieldContainer[_input_pb2.AudioInput]
    transitionTime: float
    def __init__(self, inputs: _Optional[_Iterable[_Union[_input_pb2.AudioInput, _Mapping]]] = ..., transitionTime: _Optional[float] = ...) -> None: ...

class VideoInputSettings(_message.Message):
    __slots__ = ("inputs",)
    INPUTS_FIELD_NUMBER: _ClassVar[int]
    inputs: _containers.RepeatedCompositeFieldContainer[_input_pb2.VideoInput]
    def __init__(self, inputs: _Optional[_Iterable[_Union[_input_pb2.VideoInput, _Mapping]]] = ...) -> None: ...

class RecordRequest(_message.Message):
    __slots__ = ("stream", "working_directory", "resi")
    class Resi(_message.Message):
        __slots__ = ("gop", "segmentSize", "destinationGroupId", "bufSize", "minRate", "maxRate", "eventName", "social_description")
        GOP_FIELD_NUMBER: _ClassVar[int]
        SEGMENTSIZE_FIELD_NUMBER: _ClassVar[int]
        DESTINATIONGROUPID_FIELD_NUMBER: _ClassVar[int]
        BUFSIZE_FIELD_NUMBER: _ClassVar[int]
        MINRATE_FIELD_NUMBER: _ClassVar[int]
        MAXRATE_FIELD_NUMBER: _ClassVar[int]
        EVENTNAME_FIELD_NUMBER: _ClassVar[int]
        SOCIAL_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        gop: int
        segmentSize: float
        destinationGroupId: str
        bufSize: int
        minRate: int
        maxRate: int
        eventName: str
        social_description: str
        def __init__(self, gop: _Optional[int] = ..., segmentSize: _Optional[float] = ..., destinationGroupId: _Optional[str] = ..., bufSize: _Optional[int] = ..., minRate: _Optional[int] = ..., maxRate: _Optional[int] = ..., eventName: _Optional[str] = ..., social_description: _Optional[str] = ...) -> None: ...
    STREAM_FIELD_NUMBER: _ClassVar[int]
    WORKING_DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    RESI_FIELD_NUMBER: _ClassVar[int]
    stream: _recording_pb2.Recording.Stream
    working_directory: _url_pb2.URL
    resi: RecordRequest.Resi
    def __init__(self, stream: _Optional[_Union[_recording_pb2.Recording.Stream, _Mapping]] = ..., working_directory: _Optional[_Union[_url_pb2.URL, _Mapping]] = ..., resi: _Optional[_Union[RecordRequest.Resi, _Mapping]] = ...) -> None: ...

class TextSegmentRequest(_message.Message):
    __slots__ = ("segments", "start_position")
    class Segment(_message.Message):
        __slots__ = ("index", "size")
        INDEX_FIELD_NUMBER: _ClassVar[int]
        SIZE_FIELD_NUMBER: _ClassVar[int]
        index: int
        size: float
        def __init__(self, index: _Optional[int] = ..., size: _Optional[float] = ...) -> None: ...
    SEGMENTS_FIELD_NUMBER: _ClassVar[int]
    START_POSITION_FIELD_NUMBER: _ClassVar[int]
    segments: _containers.RepeatedCompositeFieldContainer[TextSegmentRequest.Segment]
    start_position: float
    def __init__(self, segments: _Optional[_Iterable[_Union[TextSegmentRequest.Segment, _Mapping]]] = ..., start_position: _Optional[float] = ...) -> None: ...

class TriggerCue(_message.Message):
    __slots__ = ("trigger_handle", "trigger_options", "cue", "presentation", "playlist", "client_data")
    class PresentationCue(_message.Message):
        __slots__ = ("presentation", "arrangement_id", "cue_index")
        PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        ARRANGEMENT_ID_FIELD_NUMBER: _ClassVar[int]
        CUE_INDEX_FIELD_NUMBER: _ClassVar[int]
        presentation: _presentation_pb2.Presentation
        arrangement_id: _uuid_pb2.UUID
        cue_index: int
        def __init__(self, presentation: _Optional[_Union[_presentation_pb2.Presentation, _Mapping]] = ..., arrangement_id: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., cue_index: _Optional[int] = ...) -> None: ...
    TRIGGER_HANDLE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    CUE_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_FIELD_NUMBER: _ClassVar[int]
    CLIENT_DATA_FIELD_NUMBER: _ClassVar[int]
    trigger_handle: int
    trigger_options: TriggerOptions
    cue: _cue_pb2.Cue
    presentation: TriggerCue.PresentationCue
    playlist: _playlist_pb2.Playlist
    client_data: int
    def __init__(self, trigger_handle: _Optional[int] = ..., trigger_options: _Optional[_Union[TriggerOptions, _Mapping]] = ..., cue: _Optional[_Union[_cue_pb2.Cue, _Mapping]] = ..., presentation: _Optional[_Union[TriggerCue.PresentationCue, _Mapping]] = ..., playlist: _Optional[_Union[_playlist_pb2.Playlist, _Mapping]] = ..., client_data: _Optional[int] = ...) -> None: ...

class NetworkTriggerDataItem(_message.Message):
    __slots__ = ("trigger_options", "trigger_cue", "action", "cue")
    TRIGGER_OPTIONS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CUE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CUE_FIELD_NUMBER: _ClassVar[int]
    trigger_options: TriggerOptions
    trigger_cue: TriggerCue
    action: _action_pb2.Action
    cue: _cue_pb2.Cue
    def __init__(self, trigger_options: _Optional[_Union[TriggerOptions, _Mapping]] = ..., trigger_cue: _Optional[_Union[TriggerCue, _Mapping]] = ..., action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ..., cue: _Optional[_Union[_cue_pb2.Cue, _Mapping]] = ...) -> None: ...

class SlideElementTextRenderInfo(_message.Message):
    __slots__ = ("layers",)
    class Layer(_message.Message):
        __slots__ = ("layer_type", "text_build_index", "cut_out_fill", "media_fill", "background_effect")
        class LayerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LAYER_TYPE_COMPOSITE: _ClassVar[SlideElementTextRenderInfo.Layer.LayerType]
            LAYER_TYPE_MASK: _ClassVar[SlideElementTextRenderInfo.Layer.LayerType]
            LAYER_TYPE_OVER: _ClassVar[SlideElementTextRenderInfo.Layer.LayerType]
            LAYER_TYPE_UNDER: _ClassVar[SlideElementTextRenderInfo.Layer.LayerType]
        LAYER_TYPE_COMPOSITE: SlideElementTextRenderInfo.Layer.LayerType
        LAYER_TYPE_MASK: SlideElementTextRenderInfo.Layer.LayerType
        LAYER_TYPE_OVER: SlideElementTextRenderInfo.Layer.LayerType
        LAYER_TYPE_UNDER: SlideElementTextRenderInfo.Layer.LayerType
        LAYER_TYPE_FIELD_NUMBER: _ClassVar[int]
        TEXT_BUILD_INDEX_FIELD_NUMBER: _ClassVar[int]
        CUT_OUT_FILL_FIELD_NUMBER: _ClassVar[int]
        MEDIA_FILL_FIELD_NUMBER: _ClassVar[int]
        BACKGROUND_EFFECT_FIELD_NUMBER: _ClassVar[int]
        layer_type: SlideElementTextRenderInfo.Layer.LayerType
        text_build_index: int
        cut_out_fill: _graphicsData_pb2.Graphics.Text.CutOutFill
        media_fill: _graphicsData_pb2.Graphics.Text.MediaFill
        background_effect: _graphicsData_pb2.Graphics.BackgroundEffect
        def __init__(self, layer_type: _Optional[_Union[SlideElementTextRenderInfo.Layer.LayerType, str]] = ..., text_build_index: _Optional[int] = ..., cut_out_fill: _Optional[_Union[_graphicsData_pb2.Graphics.Text.CutOutFill, _Mapping]] = ..., media_fill: _Optional[_Union[_graphicsData_pb2.Graphics.Text.MediaFill, _Mapping]] = ..., background_effect: _Optional[_Union[_graphicsData_pb2.Graphics.BackgroundEffect, _Mapping]] = ...) -> None: ...
    LAYERS_FIELD_NUMBER: _ClassVar[int]
    layers: _containers.RepeatedCompositeFieldContainer[SlideElementTextRenderInfo.Layer]
    def __init__(self, layers: _Optional[_Iterable[_Union[SlideElementTextRenderInfo.Layer, _Mapping]]] = ...) -> None: ...

class ValidateEncoderRequest(_message.Message):
    __slots__ = ("encoder",)
    ENCODER_FIELD_NUMBER: _ClassVar[int]
    encoder: _recording_pb2.Recording.Stream.Encoder
    def __init__(self, encoder: _Optional[_Union[_recording_pb2.Recording.Stream.Encoder, _Mapping]] = ...) -> None: ...

class ValidateEncoderResponse(_message.Message):
    __slots__ = ("is_valid",)
    IS_VALID_FIELD_NUMBER: _ClassVar[int]
    is_valid: bool
    def __init__(self, is_valid: bool = ...) -> None: ...

class CaptureActionRequest(_message.Message):
    __slots__ = ("start_resi", "stop_capture", "error")
    class StartResi(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class StopCapture(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Error(_message.Message):
        __slots__ = ("error_code", "capture_action")
        ERROR_CODE_FIELD_NUMBER: _ClassVar[int]
        CAPTURE_ACTION_FIELD_NUMBER: _ClassVar[int]
        error_code: int
        capture_action: _action_pb2.Action.CaptureType
        def __init__(self, error_code: _Optional[int] = ..., capture_action: _Optional[_Union[_action_pb2.Action.CaptureType, _Mapping]] = ...) -> None: ...
    START_RESI_FIELD_NUMBER: _ClassVar[int]
    STOP_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    start_resi: CaptureActionRequest.StartResi
    stop_capture: CaptureActionRequest.StopCapture
    error: CaptureActionRequest.Error
    def __init__(self, start_resi: _Optional[_Union[CaptureActionRequest.StartResi, _Mapping]] = ..., stop_capture: _Optional[_Union[CaptureActionRequest.StopCapture, _Mapping]] = ..., error: _Optional[_Union[CaptureActionRequest.Error, _Mapping]] = ...) -> None: ...

class CaptureActionResponse(_message.Message):
    __slots__ = ("start_resi", "stop_capture", "cancel_capture_action")
    class CancelCaptureAction(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class StartResi(_message.Message):
        __slots__ = ("event_name", "event_description")
        EVENT_NAME_FIELD_NUMBER: _ClassVar[int]
        EVENT_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
        event_name: str
        event_description: str
        def __init__(self, event_name: _Optional[str] = ..., event_description: _Optional[str] = ...) -> None: ...
    class StopCapture(_message.Message):
        __slots__ = ("stop_capture",)
        STOP_CAPTURE_FIELD_NUMBER: _ClassVar[int]
        stop_capture: bool
        def __init__(self, stop_capture: bool = ...) -> None: ...
    START_RESI_FIELD_NUMBER: _ClassVar[int]
    STOP_CAPTURE_FIELD_NUMBER: _ClassVar[int]
    CANCEL_CAPTURE_ACTION_FIELD_NUMBER: _ClassVar[int]
    start_resi: CaptureActionResponse.StartResi
    stop_capture: CaptureActionResponse.StopCapture
    cancel_capture_action: CaptureActionResponse.CancelCaptureAction
    def __init__(self, start_resi: _Optional[_Union[CaptureActionResponse.StartResi, _Mapping]] = ..., stop_capture: _Optional[_Union[CaptureActionResponse.StopCapture, _Mapping]] = ..., cancel_capture_action: _Optional[_Union[CaptureActionResponse.CancelCaptureAction, _Mapping]] = ...) -> None: ...

class MacroIcons(_message.Message):
    __slots__ = ("icons",)
    class MacroIcon(_message.Message):
        __slots__ = ("image_type", "image_data")
        class ImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ImageTypeDefault: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeOne: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeTwo: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeThree: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeFour: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeFive: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeSix: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeSeven: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeEight: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeNine: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeZero: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeArrow: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeAudio: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeBell: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeBulb: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeCloud: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeCupcake: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeExclamation: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeFlask: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeFlower: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeGlasses: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeHashtag: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeHat: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeHeart: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeMegaphone: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeMessage: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypePaperclip: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypePlay: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeSlide: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeStar: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeSun: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeSunglasses: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeTarget: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeTimer: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeVideoInput: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeXClear: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterA: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterB: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterC: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterD: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterE: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterF: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterG: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterH: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterI: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterJ: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterK: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterL: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterM: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterN: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterO: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterP: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterQ: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterR: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterS: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterT: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterU: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterV: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterW: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterX: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterY: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeLetterZ: _ClassVar[MacroIcons.MacroIcon.ImageType]
            ImageTypeCustom: _ClassVar[MacroIcons.MacroIcon.ImageType]
        ImageTypeDefault: MacroIcons.MacroIcon.ImageType
        ImageTypeOne: MacroIcons.MacroIcon.ImageType
        ImageTypeTwo: MacroIcons.MacroIcon.ImageType
        ImageTypeThree: MacroIcons.MacroIcon.ImageType
        ImageTypeFour: MacroIcons.MacroIcon.ImageType
        ImageTypeFive: MacroIcons.MacroIcon.ImageType
        ImageTypeSix: MacroIcons.MacroIcon.ImageType
        ImageTypeSeven: MacroIcons.MacroIcon.ImageType
        ImageTypeEight: MacroIcons.MacroIcon.ImageType
        ImageTypeNine: MacroIcons.MacroIcon.ImageType
        ImageTypeZero: MacroIcons.MacroIcon.ImageType
        ImageTypeArrow: MacroIcons.MacroIcon.ImageType
        ImageTypeAudio: MacroIcons.MacroIcon.ImageType
        ImageTypeBell: MacroIcons.MacroIcon.ImageType
        ImageTypeBulb: MacroIcons.MacroIcon.ImageType
        ImageTypeCloud: MacroIcons.MacroIcon.ImageType
        ImageTypeCupcake: MacroIcons.MacroIcon.ImageType
        ImageTypeExclamation: MacroIcons.MacroIcon.ImageType
        ImageTypeFlask: MacroIcons.MacroIcon.ImageType
        ImageTypeFlower: MacroIcons.MacroIcon.ImageType
        ImageTypeGlasses: MacroIcons.MacroIcon.ImageType
        ImageTypeHashtag: MacroIcons.MacroIcon.ImageType
        ImageTypeHat: MacroIcons.MacroIcon.ImageType
        ImageTypeHeart: MacroIcons.MacroIcon.ImageType
        ImageTypeMegaphone: MacroIcons.MacroIcon.ImageType
        ImageTypeMessage: MacroIcons.MacroIcon.ImageType
        ImageTypePaperclip: MacroIcons.MacroIcon.ImageType
        ImageTypePlay: MacroIcons.MacroIcon.ImageType
        ImageTypeSlide: MacroIcons.MacroIcon.ImageType
        ImageTypeStar: MacroIcons.MacroIcon.ImageType
        ImageTypeSun: MacroIcons.MacroIcon.ImageType
        ImageTypeSunglasses: MacroIcons.MacroIcon.ImageType
        ImageTypeTarget: MacroIcons.MacroIcon.ImageType
        ImageTypeTimer: MacroIcons.MacroIcon.ImageType
        ImageTypeVideoInput: MacroIcons.MacroIcon.ImageType
        ImageTypeXClear: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterA: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterB: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterC: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterD: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterE: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterF: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterG: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterH: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterI: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterJ: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterK: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterL: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterM: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterN: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterO: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterP: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterQ: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterR: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterS: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterT: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterU: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterV: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterW: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterX: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterY: MacroIcons.MacroIcon.ImageType
        ImageTypeLetterZ: MacroIcons.MacroIcon.ImageType
        ImageTypeCustom: MacroIcons.MacroIcon.ImageType
        IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
        image_type: MacroIcons.MacroIcon.ImageType
        image_data: bytes
        def __init__(self, image_type: _Optional[_Union[MacroIcons.MacroIcon.ImageType, str]] = ..., image_data: _Optional[bytes] = ...) -> None: ...
    ICONS_FIELD_NUMBER: _ClassVar[int]
    icons: _containers.RepeatedCompositeFieldContainer[MacroIcons.MacroIcon]
    def __init__(self, icons: _Optional[_Iterable[_Union[MacroIcons.MacroIcon, _Mapping]]] = ...) -> None: ...

class GenericEvent(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class SendData(_message.Message):
    __slots__ = ("message_id", "workspace", "stage_document", "timers_document", "validate_encoder_request", "trigger_cue", "digital_audio_setup", "macros_document", "message_document", "prop_document", "ccli_document", "audience_looks", "live_audience_look", "masks", "recording_settings_document", "capture_action_response", "copyright_layout", "global_background_transition", "global_messages_transition", "global_foreground_transition", "global_bible_transition", "global_props_transition", "global_audio_transition", "preferences", "test_pattern", "startup_complete", "visual_playlist_doc", "audio_playlist_doc", "kill_watchdog", "macro_icons", "debug_trigger_data_dump", "library_playlist_doc", "audio_playlist_focus_uuid")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    WORKSPACE_FIELD_NUMBER: _ClassVar[int]
    STAGE_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    TIMERS_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ENCODER_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_CUE_FIELD_NUMBER: _ClassVar[int]
    DIGITAL_AUDIO_SETUP_FIELD_NUMBER: _ClassVar[int]
    MACROS_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    PROP_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    CCLI_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    AUDIENCE_LOOKS_FIELD_NUMBER: _ClassVar[int]
    LIVE_AUDIENCE_LOOK_FIELD_NUMBER: _ClassVar[int]
    MASKS_FIELD_NUMBER: _ClassVar[int]
    RECORDING_SETTINGS_DOCUMENT_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ACTION_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    COPYRIGHT_LAYOUT_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_BACKGROUND_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_MESSAGES_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_FOREGROUND_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_BIBLE_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_PROPS_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    GLOBAL_AUDIO_TRANSITION_FIELD_NUMBER: _ClassVar[int]
    PREFERENCES_FIELD_NUMBER: _ClassVar[int]
    TEST_PATTERN_FIELD_NUMBER: _ClassVar[int]
    STARTUP_COMPLETE_FIELD_NUMBER: _ClassVar[int]
    VISUAL_PLAYLIST_DOC_FIELD_NUMBER: _ClassVar[int]
    AUDIO_PLAYLIST_DOC_FIELD_NUMBER: _ClassVar[int]
    KILL_WATCHDOG_FIELD_NUMBER: _ClassVar[int]
    MACRO_ICONS_FIELD_NUMBER: _ClassVar[int]
    DEBUG_TRIGGER_DATA_DUMP_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_PLAYLIST_DOC_FIELD_NUMBER: _ClassVar[int]
    AUDIO_PLAYLIST_FOCUS_UUID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    workspace: _proworkspace_pb2.ProPresenterWorkspace
    stage_document: _stage_pb2.Stage.Document
    timers_document: _timers_pb2.TimersDocument
    validate_encoder_request: ValidateEncoderRequest
    trigger_cue: TriggerCue
    digital_audio_setup: _digitalAudio_pb2.DigitalAudio.Setup
    macros_document: _macros_pb2.MacrosDocument
    message_document: _messages_pb2.MessageDocument
    prop_document: _propDocument_pb2.PropDocument
    ccli_document: _ccli_pb2.CCLIDocument
    audience_looks: _proAudienceLook_pb2.AudienceLookCollection
    live_audience_look: _proAudienceLook_pb2.ProAudienceLook
    masks: _proMask_pb2.MaskCollection
    recording_settings_document: _recording_pb2.Recording.SettingsDocument
    capture_action_response: CaptureActionResponse
    copyright_layout: _ccli_pb2.CopyrightLayout
    global_background_transition: _effects_pb2.Transition
    global_messages_transition: _effects_pb2.Transition
    global_foreground_transition: _effects_pb2.Transition
    global_bible_transition: _effects_pb2.Transition
    global_props_transition: _effects_pb2.Transition
    global_audio_transition: _effects_pb2.Transition
    preferences: _preferences_pb2.Preferences
    test_pattern: _proCoreTestPatterns_pb2.TestPatternRequest
    startup_complete: GenericEvent
    visual_playlist_doc: _propresenter_pb2.PlaylistDocument
    audio_playlist_doc: _propresenter_pb2.PlaylistDocument
    kill_watchdog: GenericEvent
    macro_icons: MacroIcons
    debug_trigger_data_dump: GenericEvent
    library_playlist_doc: _propresenter_pb2.PlaylistDocument
    audio_playlist_focus_uuid: _uuid_pb2.UUID
    def __init__(self, message_id: _Optional[int] = ..., workspace: _Optional[_Union[_proworkspace_pb2.ProPresenterWorkspace, _Mapping]] = ..., stage_document: _Optional[_Union[_stage_pb2.Stage.Document, _Mapping]] = ..., timers_document: _Optional[_Union[_timers_pb2.TimersDocument, _Mapping]] = ..., validate_encoder_request: _Optional[_Union[ValidateEncoderRequest, _Mapping]] = ..., trigger_cue: _Optional[_Union[TriggerCue, _Mapping]] = ..., digital_audio_setup: _Optional[_Union[_digitalAudio_pb2.DigitalAudio.Setup, _Mapping]] = ..., macros_document: _Optional[_Union[_macros_pb2.MacrosDocument, _Mapping]] = ..., message_document: _Optional[_Union[_messages_pb2.MessageDocument, _Mapping]] = ..., prop_document: _Optional[_Union[_propDocument_pb2.PropDocument, _Mapping]] = ..., ccli_document: _Optional[_Union[_ccli_pb2.CCLIDocument, _Mapping]] = ..., audience_looks: _Optional[_Union[_proAudienceLook_pb2.AudienceLookCollection, _Mapping]] = ..., live_audience_look: _Optional[_Union[_proAudienceLook_pb2.ProAudienceLook, _Mapping]] = ..., masks: _Optional[_Union[_proMask_pb2.MaskCollection, _Mapping]] = ..., recording_settings_document: _Optional[_Union[_recording_pb2.Recording.SettingsDocument, _Mapping]] = ..., capture_action_response: _Optional[_Union[CaptureActionResponse, _Mapping]] = ..., copyright_layout: _Optional[_Union[_ccli_pb2.CopyrightLayout, _Mapping]] = ..., global_background_transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., global_messages_transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., global_foreground_transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., global_bible_transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., global_props_transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., global_audio_transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ..., preferences: _Optional[_Union[_preferences_pb2.Preferences, _Mapping]] = ..., test_pattern: _Optional[_Union[_proCoreTestPatterns_pb2.TestPatternRequest, _Mapping]] = ..., startup_complete: _Optional[_Union[GenericEvent, _Mapping]] = ..., visual_playlist_doc: _Optional[_Union[_propresenter_pb2.PlaylistDocument, _Mapping]] = ..., audio_playlist_doc: _Optional[_Union[_propresenter_pb2.PlaylistDocument, _Mapping]] = ..., kill_watchdog: _Optional[_Union[GenericEvent, _Mapping]] = ..., macro_icons: _Optional[_Union[MacroIcons, _Mapping]] = ..., debug_trigger_data_dump: _Optional[_Union[GenericEvent, _Mapping]] = ..., library_playlist_doc: _Optional[_Union[_propresenter_pb2.PlaylistDocument, _Mapping]] = ..., audio_playlist_focus_uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ...) -> None: ...

class TimerRuntimeState(_message.Message):
    __slots__ = ("timer_uuid", "timer_name", "action_type", "is_running", "has_overrun", "state", "current_time")
    class ResourceState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PREROLLING: _ClassVar[TimerRuntimeState.ResourceState]
        ACTIVATED: _ClassVar[TimerRuntimeState.ResourceState]
        UPDATED: _ClassVar[TimerRuntimeState.ResourceState]
        DEACTIVATED: _ClassVar[TimerRuntimeState.ResourceState]
        RELEASED: _ClassVar[TimerRuntimeState.ResourceState]
    PREROLLING: TimerRuntimeState.ResourceState
    ACTIVATED: TimerRuntimeState.ResourceState
    UPDATED: TimerRuntimeState.ResourceState
    DEACTIVATED: TimerRuntimeState.ResourceState
    RELEASED: TimerRuntimeState.ResourceState
    TIMER_UUID_FIELD_NUMBER: _ClassVar[int]
    TIMER_NAME_FIELD_NUMBER: _ClassVar[int]
    ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
    HAS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
    timer_uuid: _uuid_pb2.UUID
    timer_name: str
    action_type: _action_pb2.Action.TimerType
    is_running: bool
    has_overrun: bool
    state: TimerRuntimeState.ResourceState
    current_time: float
    def __init__(self, timer_uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., timer_name: _Optional[str] = ..., action_type: _Optional[_Union[_action_pb2.Action.TimerType, _Mapping]] = ..., is_running: bool = ..., has_overrun: bool = ..., state: _Optional[_Union[TimerRuntimeState.ResourceState, str]] = ..., current_time: _Optional[float] = ...) -> None: ...

class TimerStateUpdate(_message.Message):
    __slots__ = ("timer", "state")
    TIMER_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    timer: _timers_pb2.Timer
    state: TimerRuntimeState
    def __init__(self, timer: _Optional[_Union[_timers_pb2.Timer, _Mapping]] = ..., state: _Optional[_Union[TimerRuntimeState, _Mapping]] = ...) -> None: ...

class HandledException(_message.Message):
    __slots__ = ("description",)
    DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    description: str
    def __init__(self, description: _Optional[str] = ...) -> None: ...

class CoreDataStateDump(_message.Message):
    __slots__ = ("macros",)
    MACROS_FIELD_NUMBER: _ClassVar[int]
    macros: _macros_pb2.MacrosDocument
    def __init__(self, macros: _Optional[_Union[_macros_pb2.MacrosDocument, _Mapping]] = ...) -> None: ...

class SendDataResponse(_message.Message):
    __slots__ = ("message_id", "validate_encoder_response", "timer_state", "capture_action_request", "test_pattern", "handled_exception", "test_state_dump", "audio_playlist_focus_uuid", "audio_playlist_item_triggered_uuid")
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDATE_ENCODER_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    TIMER_STATE_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_ACTION_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TEST_PATTERN_FIELD_NUMBER: _ClassVar[int]
    HANDLED_EXCEPTION_FIELD_NUMBER: _ClassVar[int]
    TEST_STATE_DUMP_FIELD_NUMBER: _ClassVar[int]
    AUDIO_PLAYLIST_FOCUS_UUID_FIELD_NUMBER: _ClassVar[int]
    AUDIO_PLAYLIST_ITEM_TRIGGERED_UUID_FIELD_NUMBER: _ClassVar[int]
    message_id: int
    validate_encoder_response: ValidateEncoderResponse
    timer_state: TimerStateUpdate
    capture_action_request: CaptureActionRequest
    test_pattern: _proCoreTestPatterns_pb2.TestPatternResponse
    handled_exception: HandledException
    test_state_dump: CoreDataStateDump
    audio_playlist_focus_uuid: _uuid_pb2.UUID
    audio_playlist_item_triggered_uuid: _uuid_pb2.UUID
    def __init__(self, message_id: _Optional[int] = ..., validate_encoder_response: _Optional[_Union[ValidateEncoderResponse, _Mapping]] = ..., timer_state: _Optional[_Union[TimerStateUpdate, _Mapping]] = ..., capture_action_request: _Optional[_Union[CaptureActionRequest, _Mapping]] = ..., test_pattern: _Optional[_Union[_proCoreTestPatterns_pb2.TestPatternResponse, _Mapping]] = ..., handled_exception: _Optional[_Union[HandledException, _Mapping]] = ..., test_state_dump: _Optional[_Union[CoreDataStateDump, _Mapping]] = ..., audio_playlist_focus_uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., audio_playlist_item_triggered_uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ...) -> None: ...

class TriggerTransferRenderState(_message.Message):
    __slots__ = ("slide", "stage_message", "presentation_media", "announcement_media", "audio_media", "live_video_media", "presentation", "announcement", "timers", "capture", "timecode", "system_time")
    class TimerState(_message.Message):
        __slots__ = ("timer", "is_running", "has_overrun", "value")
        TIMER_FIELD_NUMBER: _ClassVar[int]
        IS_RUNNING_FIELD_NUMBER: _ClassVar[int]
        HAS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        timer: _timers_pb2.Timer
        is_running: bool
        has_overrun: bool
        value: float
        def __init__(self, timer: _Optional[_Union[_timers_pb2.Timer, _Mapping]] = ..., is_running: bool = ..., has_overrun: bool = ..., value: _Optional[float] = ...) -> None: ...
    class MediaState(_message.Message):
        __slots__ = ("current_media", "is_playing", "is_looping", "current_time", "time_remaining", "playlist_uuid", "playlist_name", "markers")
        CURRENT_MEDIA_FIELD_NUMBER: _ClassVar[int]
        IS_PLAYING_FIELD_NUMBER: _ClassVar[int]
        IS_LOOPING_FIELD_NUMBER: _ClassVar[int]
        CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
        TIME_REMAINING_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_UUID_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_NAME_FIELD_NUMBER: _ClassVar[int]
        MARKERS_FIELD_NUMBER: _ClassVar[int]
        current_media: _graphicsData_pb2.Media
        is_playing: bool
        is_looping: bool
        current_time: float
        time_remaining: float
        playlist_uuid: _uuid_pb2.UUID
        playlist_name: str
        markers: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action.MediaType.PlaybackMarker]
        def __init__(self, current_media: _Optional[_Union[_graphicsData_pb2.Media, _Mapping]] = ..., is_playing: bool = ..., is_looping: bool = ..., current_time: _Optional[float] = ..., time_remaining: _Optional[float] = ..., playlist_uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., playlist_name: _Optional[str] = ..., markers: _Optional[_Iterable[_Union[_action_pb2.Action.MediaType.PlaybackMarker, _Mapping]]] = ...) -> None: ...
    class CaptureState(_message.Message):
        __slots__ = ("status", "time")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            Stopped: _ClassVar[TriggerTransferRenderState.CaptureState.Status]
            Active: _ClassVar[TriggerTransferRenderState.CaptureState.Status]
            Caution: _ClassVar[TriggerTransferRenderState.CaptureState.Status]
            Error: _ClassVar[TriggerTransferRenderState.CaptureState.Status]
        Stopped: TriggerTransferRenderState.CaptureState.Status
        Active: TriggerTransferRenderState.CaptureState.Status
        Caution: TriggerTransferRenderState.CaptureState.Status
        Error: TriggerTransferRenderState.CaptureState.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        status: TriggerTransferRenderState.CaptureState.Status
        time: float
        def __init__(self, status: _Optional[_Union[TriggerTransferRenderState.CaptureState.Status, str]] = ..., time: _Optional[float] = ...) -> None: ...
    class AutoAdvanceState(_message.Message):
        __slots__ = ("active", "remaining_time")
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        REMAINING_TIME_FIELD_NUMBER: _ClassVar[int]
        active: bool
        remaining_time: float
        def __init__(self, active: bool = ..., remaining_time: _Optional[float] = ...) -> None: ...
    class TimelineState(_message.Message):
        __slots__ = ("active", "current_time", "last_slide_index")
        ACTIVE_FIELD_NUMBER: _ClassVar[int]
        CURRENT_TIME_FIELD_NUMBER: _ClassVar[int]
        LAST_SLIDE_INDEX_FIELD_NUMBER: _ClassVar[int]
        active: bool
        current_time: float
        last_slide_index: int
        def __init__(self, active: bool = ..., current_time: _Optional[float] = ..., last_slide_index: _Optional[int] = ...) -> None: ...
    class SlideState(_message.Message):
        __slots__ = ("presentation", "playlist", "current_cue", "next_cue", "auto_advance", "timeline_state", "current_cue_index", "current_playlist_index")
        PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        PLAYLIST_FIELD_NUMBER: _ClassVar[int]
        CURRENT_CUE_FIELD_NUMBER: _ClassVar[int]
        NEXT_CUE_FIELD_NUMBER: _ClassVar[int]
        AUTO_ADVANCE_FIELD_NUMBER: _ClassVar[int]
        TIMELINE_STATE_FIELD_NUMBER: _ClassVar[int]
        CURRENT_CUE_INDEX_FIELD_NUMBER: _ClassVar[int]
        CURRENT_PLAYLIST_INDEX_FIELD_NUMBER: _ClassVar[int]
        presentation: _presentation_pb2.Presentation
        playlist: _playlist_pb2.Playlist
        current_cue: _uuid_pb2.UUID
        next_cue: _uuid_pb2.UUID
        auto_advance: TriggerTransferRenderState.AutoAdvanceState
        timeline_state: TriggerTransferRenderState.TimelineState
        current_cue_index: int
        current_playlist_index: int
        def __init__(self, presentation: _Optional[_Union[_presentation_pb2.Presentation, _Mapping]] = ..., playlist: _Optional[_Union[_playlist_pb2.Playlist, _Mapping]] = ..., current_cue: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., next_cue: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., auto_advance: _Optional[_Union[TriggerTransferRenderState.AutoAdvanceState, _Mapping]] = ..., timeline_state: _Optional[_Union[TriggerTransferRenderState.TimelineState, _Mapping]] = ..., current_cue_index: _Optional[int] = ..., current_playlist_index: _Optional[int] = ...) -> None: ...
    class TimecodeState(_message.Message):
        __slots__ = ("status", "time")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            Stopped: _ClassVar[TriggerTransferRenderState.TimecodeState.Status]
            Playing: _ClassVar[TriggerTransferRenderState.TimecodeState.Status]
            Error: _ClassVar[TriggerTransferRenderState.TimecodeState.Status]
        Stopped: TriggerTransferRenderState.TimecodeState.Status
        Playing: TriggerTransferRenderState.TimecodeState.Status
        Error: TriggerTransferRenderState.TimecodeState.Status
        STATUS_FIELD_NUMBER: _ClassVar[int]
        TIME_FIELD_NUMBER: _ClassVar[int]
        status: TriggerTransferRenderState.TimecodeState.Status
        time: float
        def __init__(self, status: _Optional[_Union[TriggerTransferRenderState.TimecodeState.Status, str]] = ..., time: _Optional[float] = ...) -> None: ...
    SLIDE_FIELD_NUMBER: _ClassVar[int]
    STAGE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_MEDIA_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_MEDIA_FIELD_NUMBER: _ClassVar[int]
    AUDIO_MEDIA_FIELD_NUMBER: _ClassVar[int]
    LIVE_VIDEO_MEDIA_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENT_FIELD_NUMBER: _ClassVar[int]
    TIMERS_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_TIME_FIELD_NUMBER: _ClassVar[int]
    slide: _slide_pb2.Slide
    stage_message: str
    presentation_media: TriggerTransferRenderState.MediaState
    announcement_media: TriggerTransferRenderState.MediaState
    audio_media: TriggerTransferRenderState.MediaState
    live_video_media: _graphicsData_pb2.Media
    presentation: TriggerTransferRenderState.SlideState
    announcement: TriggerTransferRenderState.SlideState
    timers: _containers.RepeatedCompositeFieldContainer[TriggerTransferRenderState.TimerState]
    capture: TriggerTransferRenderState.CaptureState
    timecode: TriggerTransferRenderState.TimecodeState
    system_time: int
    def __init__(self, slide: _Optional[_Union[_slide_pb2.Slide, _Mapping]] = ..., stage_message: _Optional[str] = ..., presentation_media: _Optional[_Union[TriggerTransferRenderState.MediaState, _Mapping]] = ..., announcement_media: _Optional[_Union[TriggerTransferRenderState.MediaState, _Mapping]] = ..., audio_media: _Optional[_Union[TriggerTransferRenderState.MediaState, _Mapping]] = ..., live_video_media: _Optional[_Union[_graphicsData_pb2.Media, _Mapping]] = ..., presentation: _Optional[_Union[TriggerTransferRenderState.SlideState, _Mapping]] = ..., announcement: _Optional[_Union[TriggerTransferRenderState.SlideState, _Mapping]] = ..., timers: _Optional[_Iterable[_Union[TriggerTransferRenderState.TimerState, _Mapping]]] = ..., capture: _Optional[_Union[TriggerTransferRenderState.CaptureState, _Mapping]] = ..., timecode: _Optional[_Union[TriggerTransferRenderState.TimecodeState, _Mapping]] = ..., system_time: _Optional[int] = ...) -> None: ...
