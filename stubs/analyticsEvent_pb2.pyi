import analyticsApi_pb2 as _analyticsApi_pb2
import analyticsCapture_pb2 as _analyticsCapture_pb2
import analyticsCreate_pb2 as _analyticsCreate_pb2
import analyticsImport_pb2 as _analyticsImport_pb2
import analyticsPlaybackMarker_pb2 as _analyticsPlaybackMarker_pb2
import analyticsProContent_pb2 as _analyticsProContent_pb2
import analyticsStartup_pb2 as _analyticsStartup_pb2
import analyticsSync_pb2 as _analyticsSync_pb2
import analyticsTimecode_pb2 as _analyticsTimecode_pb2
import analyticsTimeline_pb2 as _analyticsTimeline_pb2
import analyticsTrigger_pb2 as _analyticsTrigger_pb2
import analyticsUI_pb2 as _analyticsUI_pb2
import analyticsUpdate_pb2 as _analyticsUpdate_pb2
import analyticsWHMStore_pb2 as _analyticsWHMStore_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Event(_message.Message):
    __slots__ = ("ui", "startup", "trigger", "create", "timeline", "sync", "api", "timecode", "playback_marker", "update", "whm_store", "proContent", "capture")
    UI_FIELD_NUMBER: _ClassVar[int]
    STARTUP_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    CREATE_FIELD_NUMBER: _ClassVar[int]
    IMPORT_FIELD_NUMBER: _ClassVar[int]
    TIMELINE_FIELD_NUMBER: _ClassVar[int]
    SYNC_FIELD_NUMBER: _ClassVar[int]
    API_FIELD_NUMBER: _ClassVar[int]
    TIMECODE_FIELD_NUMBER: _ClassVar[int]
    PLAYBACK_MARKER_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    WHM_STORE_FIELD_NUMBER: _ClassVar[int]
    PROCONTENT_FIELD_NUMBER: _ClassVar[int]
    CAPTURE_FIELD_NUMBER: _ClassVar[int]
    ui: _analyticsUI_pb2.UI
    startup: _analyticsStartup_pb2.Startup
    trigger: _analyticsTrigger_pb2.Trigger
    create: _analyticsCreate_pb2.Create
    timeline: _analyticsTimeline_pb2.Timeline
    sync: _analyticsSync_pb2.Sync
    api: _analyticsApi_pb2.API
    timecode: _analyticsTimecode_pb2.Timecode
    playback_marker: _analyticsPlaybackMarker_pb2.PlaybackMarker
    update: _analyticsUpdate_pb2.Update
    whm_store: _analyticsWHMStore_pb2.WHMStore
    proContent: _analyticsProContent_pb2.ProContent
    capture: _analyticsCapture_pb2.Capture
    def __init__(self, ui: _Optional[_Union[_analyticsUI_pb2.UI, _Mapping]] = ..., startup: _Optional[_Union[_analyticsStartup_pb2.Startup, _Mapping]] = ..., trigger: _Optional[_Union[_analyticsTrigger_pb2.Trigger, _Mapping]] = ..., create: _Optional[_Union[_analyticsCreate_pb2.Create, _Mapping]] = ..., timeline: _Optional[_Union[_analyticsTimeline_pb2.Timeline, _Mapping]] = ..., sync: _Optional[_Union[_analyticsSync_pb2.Sync, _Mapping]] = ..., api: _Optional[_Union[_analyticsApi_pb2.API, _Mapping]] = ..., timecode: _Optional[_Union[_analyticsTimecode_pb2.Timecode, _Mapping]] = ..., playback_marker: _Optional[_Union[_analyticsPlaybackMarker_pb2.PlaybackMarker, _Mapping]] = ..., update: _Optional[_Union[_analyticsUpdate_pb2.Update, _Mapping]] = ..., whm_store: _Optional[_Union[_analyticsWHMStore_pb2.WHMStore, _Mapping]] = ..., proContent: _Optional[_Union[_analyticsProContent_pb2.ProContent, _Mapping]] = ..., capture: _Optional[_Union[_analyticsCapture_pb2.Capture, _Mapping]] = ..., **kwargs) -> None: ...
