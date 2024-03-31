from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Timeline(_message.Message):
    __slots__ = ("trigger_cue", "action", "record_cue")
    class TriggerCue(_message.Message):
        __slots__ = ("trigger_type", "timing_source")
        class TriggerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TRIGGER_TYPE_SLIDE: _ClassVar[Timeline.TriggerCue.TriggerType]
            TRIGGER_TYPE_MEDIA: _ClassVar[Timeline.TriggerCue.TriggerType]
            TRIGGER_TYPE_AUDIO: _ClassVar[Timeline.TriggerCue.TriggerType]
            TRIGGER_TYPE_ACTION: _ClassVar[Timeline.TriggerCue.TriggerType]
        TRIGGER_TYPE_SLIDE: Timeline.TriggerCue.TriggerType
        TRIGGER_TYPE_MEDIA: Timeline.TriggerCue.TriggerType
        TRIGGER_TYPE_AUDIO: Timeline.TriggerCue.TriggerType
        TRIGGER_TYPE_ACTION: Timeline.TriggerCue.TriggerType
        class TimingSource(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            TIMING_SOURCE_INTERNAL: _ClassVar[Timeline.TriggerCue.TimingSource]
            TIMING_SOURCE_SMPTE: _ClassVar[Timeline.TriggerCue.TimingSource]
        TIMING_SOURCE_INTERNAL: Timeline.TriggerCue.TimingSource
        TIMING_SOURCE_SMPTE: Timeline.TriggerCue.TimingSource
        TRIGGER_TYPE_FIELD_NUMBER: _ClassVar[int]
        TIMING_SOURCE_FIELD_NUMBER: _ClassVar[int]
        trigger_type: Timeline.TriggerCue.TriggerType
        timing_source: Timeline.TriggerCue.TimingSource
        def __init__(self, trigger_type: _Optional[_Union[Timeline.TriggerCue.TriggerType, str]] = ..., timing_source: _Optional[_Union[Timeline.TriggerCue.TimingSource, str]] = ...) -> None: ...
    class Action(_message.Message):
        __slots__ = ("action_type",)
        class ActionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ACTION_TYPE_PLAY: _ClassVar[Timeline.Action.ActionType]
            ACTION_TYPE_STOP: _ClassVar[Timeline.Action.ActionType]
            ACTION_TYPE_RESET: _ClassVar[Timeline.Action.ActionType]
        ACTION_TYPE_PLAY: Timeline.Action.ActionType
        ACTION_TYPE_STOP: Timeline.Action.ActionType
        ACTION_TYPE_RESET: Timeline.Action.ActionType
        ACTION_TYPE_FIELD_NUMBER: _ClassVar[int]
        action_type: Timeline.Action.ActionType
        def __init__(self, action_type: _Optional[_Union[Timeline.Action.ActionType, str]] = ...) -> None: ...
    class RecordCue(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    TRIGGER_CUE_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    RECORD_CUE_FIELD_NUMBER: _ClassVar[int]
    trigger_cue: Timeline.TriggerCue
    action: Timeline.Action
    record_cue: Timeline.RecordCue
    def __init__(self, trigger_cue: _Optional[_Union[Timeline.TriggerCue, _Mapping]] = ..., action: _Optional[_Union[Timeline.Action, _Mapping]] = ..., record_cue: _Optional[_Union[Timeline.RecordCue, _Mapping]] = ...) -> None: ...
