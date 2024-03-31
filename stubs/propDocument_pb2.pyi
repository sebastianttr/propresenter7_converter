import applicationInfo_pb2 as _applicationInfo_pb2
import cue_pb2 as _cue_pb2
import effects_pb2 as _effects_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PropDocument(_message.Message):
    __slots__ = ("application_info", "cues", "transition")
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    CUES_FIELD_NUMBER: _ClassVar[int]
    TRANSITION_FIELD_NUMBER: _ClassVar[int]
    application_info: _applicationInfo_pb2.ApplicationInfo
    cues: _containers.RepeatedCompositeFieldContainer[_cue_pb2.Cue]
    transition: _effects_pb2.Transition
    def __init__(self, application_info: _Optional[_Union[_applicationInfo_pb2.ApplicationInfo, _Mapping]] = ..., cues: _Optional[_Iterable[_Union[_cue_pb2.Cue, _Mapping]]] = ..., transition: _Optional[_Union[_effects_pb2.Transition, _Mapping]] = ...) -> None: ...
