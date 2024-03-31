import rvtimestamp_pb2 as _rvtimestamp_pb2
import uuid_pb2 as _uuid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_GroupMember(_message.Message):
    __slots__ = ("ip", "port")
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ...) -> None: ...

class API_v1_GroupMemberStatus(_message.Message):
    __slots__ = ("ip", "port", "name", "platform", "os_version", "host_description", "api_version", "connection_status")
    class API_v1_GroupMemberStatus_Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNKNOWN: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform]
        PLATFORM_MACOS: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform]
        PLATFORM_WIN32: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform]
        PLATFORM_WEB: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform]
    PLATFORM_UNKNOWN: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    PLATFORM_MACOS: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    PLATFORM_WIN32: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    PLATFORM_WEB: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    class API_v1_GroupMemberStatus_ConnectionStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        CONNECTION_STATUS_UNKNOWN: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus]
        CONNECTION_STATUS_CONNECTED: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus]
        CONNECTION_STATUS_DISCONNECTED: _ClassVar[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus]
    CONNECTION_STATUS_UNKNOWN: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus
    CONNECTION_STATUS_CONNECTED: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus
    CONNECTION_STATUS_DISCONNECTED: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    OS_VERSION_FIELD_NUMBER: _ClassVar[int]
    HOST_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    API_VERSION_FIELD_NUMBER: _ClassVar[int]
    CONNECTION_STATUS_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: int
    name: str
    platform: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform
    os_version: str
    host_description: str
    api_version: str
    connection_status: API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[int] = ..., name: _Optional[str] = ..., platform: _Optional[_Union[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_Platform, str]] = ..., os_version: _Optional[str] = ..., host_description: _Optional[str] = ..., api_version: _Optional[str] = ..., connection_status: _Optional[_Union[API_v1_GroupMemberStatus.API_v1_GroupMemberStatus_ConnectionStatus, str]] = ...) -> None: ...

class API_v1_GroupDefinition(_message.Message):
    __slots__ = ("timestamp", "secret", "name", "members", "group_identifier")
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
    timestamp: _rvtimestamp_pb2.Timestamp
    secret: str
    name: str
    members: _containers.RepeatedCompositeFieldContainer[API_v1_GroupMember]
    group_identifier: _uuid_pb2.UUID
    def __init__(self, timestamp: _Optional[_Union[_rvtimestamp_pb2.Timestamp, _Mapping]] = ..., secret: _Optional[str] = ..., name: _Optional[str] = ..., members: _Optional[_Iterable[_Union[API_v1_GroupMember, _Mapping]]] = ..., group_identifier: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ...) -> None: ...

class API_v1_Link_Request(_message.Message):
    __slots__ = ("heartbeat", "status", "add_member", "remove_member")
    class Heartbeat(_message.Message):
        __slots__ = ("port", "if_modified_since")
        PORT_FIELD_NUMBER: _ClassVar[int]
        IF_MODIFIED_SINCE_FIELD_NUMBER: _ClassVar[int]
        port: int
        if_modified_since: str
        def __init__(self, port: _Optional[int] = ..., if_modified_since: _Optional[str] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AddMember(_message.Message):
        __slots__ = ("group_definition", "member_details")
        GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
        MEMBER_DETAILS_FIELD_NUMBER: _ClassVar[int]
        group_definition: API_v1_GroupDefinition
        member_details: API_v1_GroupMember
        def __init__(self, group_definition: _Optional[_Union[API_v1_GroupDefinition, _Mapping]] = ..., member_details: _Optional[_Union[API_v1_GroupMember, _Mapping]] = ...) -> None: ...
    class RemoveMember(_message.Message):
        __slots__ = ("member_details",)
        MEMBER_DETAILS_FIELD_NUMBER: _ClassVar[int]
        member_details: API_v1_GroupMember
        def __init__(self, member_details: _Optional[_Union[API_v1_GroupMember, _Mapping]] = ...) -> None: ...
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADD_MEMBER_FIELD_NUMBER: _ClassVar[int]
    REMOVE_MEMBER_FIELD_NUMBER: _ClassVar[int]
    heartbeat: API_v1_Link_Request.Heartbeat
    status: API_v1_Link_Request.Status
    add_member: API_v1_Link_Request.AddMember
    remove_member: API_v1_Link_Request.RemoveMember
    def __init__(self, heartbeat: _Optional[_Union[API_v1_Link_Request.Heartbeat, _Mapping]] = ..., status: _Optional[_Union[API_v1_Link_Request.Status, _Mapping]] = ..., add_member: _Optional[_Union[API_v1_Link_Request.AddMember, _Mapping]] = ..., remove_member: _Optional[_Union[API_v1_Link_Request.RemoveMember, _Mapping]] = ...) -> None: ...

class API_v1_Link_Response(_message.Message):
    __slots__ = ("heartbeat", "status", "add_member", "remove_member")
    class Heartbeat(_message.Message):
        __slots__ = ("group_definition", "status")
        GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
        STATUS_FIELD_NUMBER: _ClassVar[int]
        group_definition: API_v1_GroupDefinition
        status: API_v1_GroupMemberStatus
        def __init__(self, group_definition: _Optional[_Union[API_v1_GroupDefinition, _Mapping]] = ..., status: _Optional[_Union[API_v1_GroupMemberStatus, _Mapping]] = ...) -> None: ...
    class Status(_message.Message):
        __slots__ = ("group_definition", "member_name")
        GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
        MEMBER_NAME_FIELD_NUMBER: _ClassVar[int]
        group_definition: API_v1_GroupDefinition
        member_name: str
        def __init__(self, group_definition: _Optional[_Union[API_v1_GroupDefinition, _Mapping]] = ..., member_name: _Optional[str] = ...) -> None: ...
    class AddMember(_message.Message):
        __slots__ = ("group_definition", "accept", "decline")
        class RemoteMachineAccepts(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class RemoteMachineDecline(_message.Message):
            __slots__ = ("reason",)
            class DeclineReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                ALREADY_IN_GROUP: _ClassVar[API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason]
                USER_DECLINED: _ClassVar[API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason]
            ALREADY_IN_GROUP: API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason
            USER_DECLINED: API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason
            REASON_FIELD_NUMBER: _ClassVar[int]
            reason: API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason
            def __init__(self, reason: _Optional[_Union[API_v1_Link_Response.AddMember.RemoteMachineDecline.DeclineReason, str]] = ...) -> None: ...
        GROUP_DEFINITION_FIELD_NUMBER: _ClassVar[int]
        ACCEPT_FIELD_NUMBER: _ClassVar[int]
        DECLINE_FIELD_NUMBER: _ClassVar[int]
        group_definition: API_v1_GroupDefinition
        accept: API_v1_Link_Response.AddMember.RemoteMachineAccepts
        decline: API_v1_Link_Response.AddMember.RemoteMachineDecline
        def __init__(self, group_definition: _Optional[_Union[API_v1_GroupDefinition, _Mapping]] = ..., accept: _Optional[_Union[API_v1_Link_Response.AddMember.RemoteMachineAccepts, _Mapping]] = ..., decline: _Optional[_Union[API_v1_Link_Response.AddMember.RemoteMachineDecline, _Mapping]] = ...) -> None: ...
    class RemoveMember(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    HEARTBEAT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    ADD_MEMBER_FIELD_NUMBER: _ClassVar[int]
    REMOVE_MEMBER_FIELD_NUMBER: _ClassVar[int]
    heartbeat: API_v1_Link_Response.Heartbeat
    status: API_v1_Link_Response.Status
    add_member: API_v1_Link_Response.AddMember
    remove_member: API_v1_Link_Response.RemoveMember
    def __init__(self, heartbeat: _Optional[_Union[API_v1_Link_Response.Heartbeat, _Mapping]] = ..., status: _Optional[_Union[API_v1_Link_Response.Status, _Mapping]] = ..., add_member: _Optional[_Union[API_v1_Link_Response.AddMember, _Mapping]] = ..., remove_member: _Optional[_Union[API_v1_Link_Response.RemoveMember, _Mapping]] = ...) -> None: ...
