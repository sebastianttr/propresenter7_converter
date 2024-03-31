import proApiV1Color_pb2 as _proApiV1Color_pb2
import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Groups_Request(_message.Message):
    __slots__ = ("groups_request", "trigger_group")
    class GroupsRequest(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TriggerGroup(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    GROUPS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_GROUP_FIELD_NUMBER: _ClassVar[int]
    groups_request: API_v1_Groups_Request.GroupsRequest
    trigger_group: API_v1_Groups_Request.TriggerGroup
    def __init__(self, groups_request: _Optional[_Union[API_v1_Groups_Request.GroupsRequest, _Mapping]] = ..., trigger_group: _Optional[_Union[API_v1_Groups_Request.TriggerGroup, _Mapping]] = ...) -> None: ...

class API_v1_Groups_Response(_message.Message):
    __slots__ = ("groups", "trigger_group")
    class GroupsRequest(_message.Message):
        __slots__ = ("groups",)
        class Group(_message.Message):
            __slots__ = ("id", "color")
            ID_FIELD_NUMBER: _ClassVar[int]
            COLOR_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1Identifier_pb2.API_v1_Identifier
            color: _proApiV1Color_pb2.API_v1_Color
            def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., color: _Optional[_Union[_proApiV1Color_pb2.API_v1_Color, _Mapping]] = ...) -> None: ...
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        groups: _containers.RepeatedCompositeFieldContainer[API_v1_Groups_Response.GroupsRequest.Group]
        def __init__(self, groups: _Optional[_Iterable[_Union[API_v1_Groups_Response.GroupsRequest.Group, _Mapping]]] = ...) -> None: ...
    class TriggerGroup(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_GROUP_FIELD_NUMBER: _ClassVar[int]
    groups: API_v1_Groups_Response.GroupsRequest
    trigger_group: API_v1_Groups_Response.TriggerGroup
    def __init__(self, groups: _Optional[_Union[API_v1_Groups_Response.GroupsRequest, _Mapping]] = ..., trigger_group: _Optional[_Union[API_v1_Groups_Response.TriggerGroup, _Mapping]] = ...) -> None: ...
