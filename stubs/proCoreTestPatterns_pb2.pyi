import testPattern_pb2 as _testPattern_pb2
import uuid_pb2 as _uuid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TestPatternRequest(_message.Message):
    __slots__ = ("get_definitions", "set_current_state", "get_current_state", "get_thumbnail")
    class GetDefinitions(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetCurrentState(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetThumbnail(_message.Message):
        __slots__ = ("pattern", "width", "height")
        PATTERN_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        pattern: _testPattern_pb2.TestPatternDefinition
        width: int
        height: int
        def __init__(self, pattern: _Optional[_Union[_testPattern_pb2.TestPatternDefinition, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    GET_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    SET_CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    GET_CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    get_definitions: TestPatternRequest.GetDefinitions
    set_current_state: _testPattern_pb2.TestPatternState
    get_current_state: TestPatternRequest.GetCurrentState
    get_thumbnail: TestPatternRequest.GetThumbnail
    def __init__(self, get_definitions: _Optional[_Union[TestPatternRequest.GetDefinitions, _Mapping]] = ..., set_current_state: _Optional[_Union[_testPattern_pb2.TestPatternState, _Mapping]] = ..., get_current_state: _Optional[_Union[TestPatternRequest.GetCurrentState, _Mapping]] = ..., get_thumbnail: _Optional[_Union[TestPatternRequest.GetThumbnail, _Mapping]] = ...) -> None: ...

class TestPatternResponse(_message.Message):
    __slots__ = ("get_definitions", "get_current_state", "get_thumbnail")
    class GetDefinitions(_message.Message):
        __slots__ = ("patterns",)
        PATTERNS_FIELD_NUMBER: _ClassVar[int]
        patterns: _containers.RepeatedCompositeFieldContainer[_testPattern_pb2.TestPatternDefinition]
        def __init__(self, patterns: _Optional[_Iterable[_Union[_testPattern_pb2.TestPatternDefinition, _Mapping]]] = ...) -> None: ...
    class GetThumbnail(_message.Message):
        __slots__ = ("pattern", "image")
        PATTERN_FIELD_NUMBER: _ClassVar[int]
        IMAGE_FIELD_NUMBER: _ClassVar[int]
        pattern: _uuid_pb2.UUID
        image: bytes
        def __init__(self, pattern: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., image: _Optional[bytes] = ...) -> None: ...
    GET_DEFINITIONS_FIELD_NUMBER: _ClassVar[int]
    GET_CURRENT_STATE_FIELD_NUMBER: _ClassVar[int]
    GET_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    get_definitions: TestPatternResponse.GetDefinitions
    get_current_state: _testPattern_pb2.TestPatternState
    get_thumbnail: TestPatternResponse.GetThumbnail
    def __init__(self, get_definitions: _Optional[_Union[TestPatternResponse.GetDefinitions, _Mapping]] = ..., get_current_state: _Optional[_Union[_testPattern_pb2.TestPatternState, _Mapping]] = ..., get_thumbnail: _Optional[_Union[TestPatternResponse.GetThumbnail, _Mapping]] = ...) -> None: ...
