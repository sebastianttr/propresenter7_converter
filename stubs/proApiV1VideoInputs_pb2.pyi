import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Video_Inputs_Request(_message.Message):
    __slots__ = ("get_all", "trigger")
    class GetAll(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Trigger(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    GET_ALL_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    get_all: API_v1_Video_Inputs_Request.GetAll
    trigger: API_v1_Video_Inputs_Request.Trigger
    def __init__(self, get_all: _Optional[_Union[API_v1_Video_Inputs_Request.GetAll, _Mapping]] = ..., trigger: _Optional[_Union[API_v1_Video_Inputs_Request.Trigger, _Mapping]] = ...) -> None: ...

class API_v1_Video_Inputs_Response(_message.Message):
    __slots__ = ("get_all", "trigger")
    class GetAll(_message.Message):
        __slots__ = ("inputs",)
        INPUTS_FIELD_NUMBER: _ClassVar[int]
        inputs: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        def __init__(self, inputs: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
    class Trigger(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    GET_ALL_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    get_all: API_v1_Video_Inputs_Response.GetAll
    trigger: API_v1_Video_Inputs_Response.Trigger
    def __init__(self, get_all: _Optional[_Union[API_v1_Video_Inputs_Response.GetAll, _Mapping]] = ..., trigger: _Optional[_Union[API_v1_Video_Inputs_Response.Trigger, _Mapping]] = ...) -> None: ...
