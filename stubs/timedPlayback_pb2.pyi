import action_pb2 as _action_pb2
import cue_pb2 as _cue_pb2
import presentation_pb2 as _presentation_pb2
import uuid_pb2 as _uuid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerSource(_message.Message):
    __slots__ = ("library_location", "playlist_location")
    class Library(_message.Message):
        __slots__ = ("path", "presentation_name")
        PATH_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_NAME_FIELD_NUMBER: _ClassVar[int]
        path: str
        presentation_name: str
        def __init__(self, path: _Optional[str] = ..., presentation_name: _Optional[str] = ...) -> None: ...
    class Playlist(_message.Message):
        __slots__ = ("identifier", "item_identifier")
        IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        ITEM_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
        identifier: _uuid_pb2.UUID
        item_identifier: _uuid_pb2.UUID
        def __init__(self, identifier: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., item_identifier: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ...) -> None: ...
    LIBRARY_LOCATION_FIELD_NUMBER: _ClassVar[int]
    PLAYLIST_LOCATION_FIELD_NUMBER: _ClassVar[int]
    library_location: TriggerSource.Library
    playlist_location: TriggerSource.Playlist
    def __init__(self, library_location: _Optional[_Union[TriggerSource.Library, _Mapping]] = ..., playlist_location: _Optional[_Union[TriggerSource.Playlist, _Mapping]] = ...) -> None: ...

class TimedPlayback(_message.Message):
    __slots__ = ("sequence", "timing")
    class Sequence(_message.Message):
        __slots__ = ("sequence", "content_destination", "presentation")
        class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            CONTENT_DESTINATION_GLOBAL: _ClassVar[TimedPlayback.Sequence.ContentDestination]
            CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[TimedPlayback.Sequence.ContentDestination]
        CONTENT_DESTINATION_GLOBAL: TimedPlayback.Sequence.ContentDestination
        CONTENT_DESTINATION_ANNOUNCEMENTS: TimedPlayback.Sequence.ContentDestination
        class SequenceItem(_message.Message):
            __slots__ = ("identifier", "time", "trigger_source", "content_destination", "end_time", "cue", "action")
            class ContentDestination(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CONTENT_DESTINATION_GLOBAL: _ClassVar[TimedPlayback.Sequence.SequenceItem.ContentDestination]
                CONTENT_DESTINATION_ANNOUNCEMENTS: _ClassVar[TimedPlayback.Sequence.SequenceItem.ContentDestination]
            CONTENT_DESTINATION_GLOBAL: TimedPlayback.Sequence.SequenceItem.ContentDestination
            CONTENT_DESTINATION_ANNOUNCEMENTS: TimedPlayback.Sequence.SequenceItem.ContentDestination
            IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            TRIGGER_SOURCE_FIELD_NUMBER: _ClassVar[int]
            CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
            END_TIME_FIELD_NUMBER: _ClassVar[int]
            CUE_FIELD_NUMBER: _ClassVar[int]
            ACTION_FIELD_NUMBER: _ClassVar[int]
            identifier: _uuid_pb2.UUID
            time: float
            trigger_source: TriggerSource
            content_destination: TimedPlayback.Sequence.SequenceItem.ContentDestination
            end_time: float
            cue: _cue_pb2.Cue
            action: _action_pb2.Action
            def __init__(self, identifier: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., time: _Optional[float] = ..., trigger_source: _Optional[_Union[TriggerSource, _Mapping]] = ..., content_destination: _Optional[_Union[TimedPlayback.Sequence.SequenceItem.ContentDestination, str]] = ..., end_time: _Optional[float] = ..., cue: _Optional[_Union[_cue_pb2.Cue, _Mapping]] = ..., action: _Optional[_Union[_action_pb2.Action, _Mapping]] = ...) -> None: ...
        SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_DESTINATION_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_FIELD_NUMBER: _ClassVar[int]
        sequence: _containers.RepeatedCompositeFieldContainer[TimedPlayback.Sequence.SequenceItem]
        content_destination: TimedPlayback.Sequence.ContentDestination
        presentation: _presentation_pb2.Presentation
        def __init__(self, sequence: _Optional[_Iterable[_Union[TimedPlayback.Sequence.SequenceItem, _Mapping]]] = ..., content_destination: _Optional[_Union[TimedPlayback.Sequence.ContentDestination, str]] = ..., presentation: _Optional[_Union[_presentation_pb2.Presentation, _Mapping]] = ...) -> None: ...
    class Timing(_message.Message):
        __slots__ = ("layer_transport", "smpte_timecode", "internal")
        class LayerTransport(_message.Message):
            __slots__ = ("layer",)
            LAYER_FIELD_NUMBER: _ClassVar[int]
            layer: int
            def __init__(self, layer: _Optional[int] = ...) -> None: ...
        class SMPTETimecode(_message.Message):
            __slots__ = ("device_identifier", "channel", "format", "offset")
            class Format(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FORMAT_24_FPS: _ClassVar[TimedPlayback.Timing.SMPTETimecode.Format]
                FORMAT_25_FPS: _ClassVar[TimedPlayback.Timing.SMPTETimecode.Format]
                FORMAT_29_97_FPS: _ClassVar[TimedPlayback.Timing.SMPTETimecode.Format]
                FORMAT_30_FPS: _ClassVar[TimedPlayback.Timing.SMPTETimecode.Format]
            FORMAT_24_FPS: TimedPlayback.Timing.SMPTETimecode.Format
            FORMAT_25_FPS: TimedPlayback.Timing.SMPTETimecode.Format
            FORMAT_29_97_FPS: TimedPlayback.Timing.SMPTETimecode.Format
            FORMAT_30_FPS: TimedPlayback.Timing.SMPTETimecode.Format
            DEVICE_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            CHANNEL_FIELD_NUMBER: _ClassVar[int]
            FORMAT_FIELD_NUMBER: _ClassVar[int]
            OFFSET_FIELD_NUMBER: _ClassVar[int]
            device_identifier: str
            channel: int
            format: TimedPlayback.Timing.SMPTETimecode.Format
            offset: float
            def __init__(self, device_identifier: _Optional[str] = ..., channel: _Optional[int] = ..., format: _Optional[_Union[TimedPlayback.Timing.SMPTETimecode.Format, str]] = ..., offset: _Optional[float] = ...) -> None: ...
        class Internal(_message.Message):
            __slots__ = ("duration", "should_loop")
            DURATION_FIELD_NUMBER: _ClassVar[int]
            SHOULD_LOOP_FIELD_NUMBER: _ClassVar[int]
            duration: float
            should_loop: bool
            def __init__(self, duration: _Optional[float] = ..., should_loop: bool = ...) -> None: ...
        LAYER_TRANSPORT_FIELD_NUMBER: _ClassVar[int]
        SMPTE_TIMECODE_FIELD_NUMBER: _ClassVar[int]
        INTERNAL_FIELD_NUMBER: _ClassVar[int]
        layer_transport: TimedPlayback.Timing.LayerTransport
        smpte_timecode: TimedPlayback.Timing.SMPTETimecode
        internal: TimedPlayback.Timing.Internal
        def __init__(self, layer_transport: _Optional[_Union[TimedPlayback.Timing.LayerTransport, _Mapping]] = ..., smpte_timecode: _Optional[_Union[TimedPlayback.Timing.SMPTETimecode, _Mapping]] = ..., internal: _Optional[_Union[TimedPlayback.Timing.Internal, _Mapping]] = ...) -> None: ...
    class Update(_message.Message):
        __slots__ = ("play", "record", "pause", "reset", "jump_to_time", "start_scrub", "end_scrub", "duration", "loop", "update_sequence", "monitor_source")
        class Play(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Record(_message.Message):
            __slots__ = ("is_recording",)
            IS_RECORDING_FIELD_NUMBER: _ClassVar[int]
            is_recording: bool
            def __init__(self, is_recording: bool = ...) -> None: ...
        class Pause(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Reset(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class JumpToTime(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: float
            def __init__(self, time: _Optional[float] = ...) -> None: ...
        class StartScrub(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: float
            def __init__(self, time: _Optional[float] = ...) -> None: ...
        class EndScrub(_message.Message):
            __slots__ = ("time",)
            TIME_FIELD_NUMBER: _ClassVar[int]
            time: float
            def __init__(self, time: _Optional[float] = ...) -> None: ...
        class Duration(_message.Message):
            __slots__ = ("duration",)
            DURATION_FIELD_NUMBER: _ClassVar[int]
            duration: float
            def __init__(self, duration: _Optional[float] = ...) -> None: ...
        class Loop(_message.Message):
            __slots__ = ("loop",)
            LOOP_FIELD_NUMBER: _ClassVar[int]
            loop: bool
            def __init__(self, loop: bool = ...) -> None: ...
        class MonitorSource(_message.Message):
            __slots__ = ("enable",)
            ENABLE_FIELD_NUMBER: _ClassVar[int]
            enable: bool
            def __init__(self, enable: bool = ...) -> None: ...
        PLAY_FIELD_NUMBER: _ClassVar[int]
        RECORD_FIELD_NUMBER: _ClassVar[int]
        PAUSE_FIELD_NUMBER: _ClassVar[int]
        RESET_FIELD_NUMBER: _ClassVar[int]
        JUMP_TO_TIME_FIELD_NUMBER: _ClassVar[int]
        START_SCRUB_FIELD_NUMBER: _ClassVar[int]
        END_SCRUB_FIELD_NUMBER: _ClassVar[int]
        DURATION_FIELD_NUMBER: _ClassVar[int]
        LOOP_FIELD_NUMBER: _ClassVar[int]
        UPDATE_SEQUENCE_FIELD_NUMBER: _ClassVar[int]
        MONITOR_SOURCE_FIELD_NUMBER: _ClassVar[int]
        play: TimedPlayback.Update.Play
        record: TimedPlayback.Update.Record
        pause: TimedPlayback.Update.Pause
        reset: TimedPlayback.Update.Reset
        jump_to_time: TimedPlayback.Update.JumpToTime
        start_scrub: TimedPlayback.Update.StartScrub
        end_scrub: TimedPlayback.Update.EndScrub
        duration: TimedPlayback.Update.Duration
        loop: TimedPlayback.Update.Loop
        update_sequence: TimedPlayback.Sequence
        monitor_source: TimedPlayback.Update.MonitorSource
        def __init__(self, play: _Optional[_Union[TimedPlayback.Update.Play, _Mapping]] = ..., record: _Optional[_Union[TimedPlayback.Update.Record, _Mapping]] = ..., pause: _Optional[_Union[TimedPlayback.Update.Pause, _Mapping]] = ..., reset: _Optional[_Union[TimedPlayback.Update.Reset, _Mapping]] = ..., jump_to_time: _Optional[_Union[TimedPlayback.Update.JumpToTime, _Mapping]] = ..., start_scrub: _Optional[_Union[TimedPlayback.Update.StartScrub, _Mapping]] = ..., end_scrub: _Optional[_Union[TimedPlayback.Update.EndScrub, _Mapping]] = ..., duration: _Optional[_Union[TimedPlayback.Update.Duration, _Mapping]] = ..., loop: _Optional[_Union[TimedPlayback.Update.Loop, _Mapping]] = ..., update_sequence: _Optional[_Union[TimedPlayback.Sequence, _Mapping]] = ..., monitor_source: _Optional[_Union[TimedPlayback.Update.MonitorSource, _Mapping]] = ...) -> None: ...
    SEQUENCE_FIELD_NUMBER: _ClassVar[int]
    TIMING_FIELD_NUMBER: _ClassVar[int]
    sequence: TimedPlayback.Sequence
    timing: TimedPlayback.Timing
    def __init__(self, sequence: _Optional[_Union[TimedPlayback.Sequence, _Mapping]] = ..., timing: _Optional[_Union[TimedPlayback.Timing, _Mapping]] = ...) -> None: ...
