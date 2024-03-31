import action_pb2 as _action_pb2
import applicationInfo_pb2 as _applicationInfo_pb2
import slide_pb2 as _slide_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Template(_message.Message):
    __slots__ = ()
    class Slide(_message.Message):
        __slots__ = ("base_slide", "name", "actions")
        BASE_SLIDE_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        base_slide: _slide_pb2.Slide
        name: str
        actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
        def __init__(self, base_slide: _Optional[_Union[_slide_pb2.Slide, _Mapping]] = ..., name: _Optional[str] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ...) -> None: ...
    class Document(_message.Message):
        __slots__ = ("application_info", "slides")
        APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
        SLIDES_FIELD_NUMBER: _ClassVar[int]
        application_info: _applicationInfo_pb2.ApplicationInfo
        slides: _containers.RepeatedCompositeFieldContainer[Template.Slide]
        def __init__(self, application_info: _Optional[_Union[_applicationInfo_pb2.ApplicationInfo, _Mapping]] = ..., slides: _Optional[_Iterable[_Union[Template.Slide, _Mapping]]] = ...) -> None: ...
    def __init__(self) -> None: ...
