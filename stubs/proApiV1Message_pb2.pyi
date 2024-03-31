import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
import proApiV1Timer_pb2 as _proApiV1Timer_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Message(_message.Message):
    __slots__ = ("id", "message", "tokens", "theme", "visible_on_network")
    class API_v1_MessageToken(_message.Message):
        __slots__ = ("name", "text", "timer", "clock")
        class API_v1_TextToken(_message.Message):
            __slots__ = ("text",)
            TEXT_FIELD_NUMBER: _ClassVar[int]
            text: str
            def __init__(self, text: _Optional[str] = ...) -> None: ...
        class API_v1_TimerToken(_message.Message):
            __slots__ = ("id", "allows_overrun", "format", "countdown", "count_down_to_time", "elapsed")
            ID_FIELD_NUMBER: _ClassVar[int]
            ALLOWS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
            FORMAT_FIELD_NUMBER: _ClassVar[int]
            COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
            COUNT_DOWN_TO_TIME_FIELD_NUMBER: _ClassVar[int]
            ELAPSED_FIELD_NUMBER: _ClassVar[int]
            id: _proApiV1Identifier_pb2.API_v1_Identifier
            allows_overrun: bool
            format: _proApiV1Timer_pb2.API_v1_TimerFormat
            countdown: _proApiV1Timer_pb2.API_v1_Timer.API_v1_Timer_Countdown
            count_down_to_time: _proApiV1Timer_pb2.API_v1_Timer.API_v1_Timer_CountdownToTime
            elapsed: _proApiV1Timer_pb2.API_v1_Timer.API_v1_Timer_Elapsed
            def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., allows_overrun: bool = ..., format: _Optional[_Union[_proApiV1Timer_pb2.API_v1_TimerFormat, _Mapping]] = ..., countdown: _Optional[_Union[_proApiV1Timer_pb2.API_v1_Timer.API_v1_Timer_Countdown, _Mapping]] = ..., count_down_to_time: _Optional[_Union[_proApiV1Timer_pb2.API_v1_Timer.API_v1_Timer_CountdownToTime, _Mapping]] = ..., elapsed: _Optional[_Union[_proApiV1Timer_pb2.API_v1_Timer.API_v1_Timer_Elapsed, _Mapping]] = ...) -> None: ...
        class API_v1_ClockToken(_message.Message):
            __slots__ = ("date", "time", "is_24_hours")
            class API_v1_ClockTokenFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                none: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
                short: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
                medium: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
                long: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
                full: _ClassVar[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat]
            none: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            short: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            medium: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            long: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            full: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            DATE_FIELD_NUMBER: _ClassVar[int]
            TIME_FIELD_NUMBER: _ClassVar[int]
            IS_24_HOURS_FIELD_NUMBER: _ClassVar[int]
            date: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            time: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat
            is_24_hours: bool
            def __init__(self, date: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat, str]] = ..., time: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat, str]] = ..., is_24_hours: bool = ...) -> None: ...
        NAME_FIELD_NUMBER: _ClassVar[int]
        TEXT_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        CLOCK_FIELD_NUMBER: _ClassVar[int]
        name: str
        text: API_v1_Message.API_v1_MessageToken.API_v1_TextToken
        timer: API_v1_Message.API_v1_MessageToken.API_v1_TimerToken
        clock: API_v1_Message.API_v1_MessageToken.API_v1_ClockToken
        def __init__(self, name: _Optional[str] = ..., text: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_TextToken, _Mapping]] = ..., timer: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_TimerToken, _Mapping]] = ..., clock: _Optional[_Union[API_v1_Message.API_v1_MessageToken.API_v1_ClockToken, _Mapping]] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TOKENS_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_ON_NETWORK_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    message: str
    tokens: _containers.RepeatedCompositeFieldContainer[API_v1_Message.API_v1_MessageToken]
    theme: _proApiV1Identifier_pb2.API_v1_Identifier
    visible_on_network: bool
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., message: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[API_v1_Message.API_v1_MessageToken, _Mapping]]] = ..., theme: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., visible_on_network: bool = ...) -> None: ...

class API_v1_Message_Request(_message.Message):
    __slots__ = ("messages", "create_message", "get_message", "put_message", "delete_message", "trigger_message", "clear_message")
    class Messages(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CreateMessage(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: API_v1_Message
        def __init__(self, message: _Optional[_Union[API_v1_Message, _Mapping]] = ...) -> None: ...
    class GetMessage(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PutMessage(_message.Message):
        __slots__ = ("id", "message")
        ID_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        id: str
        message: API_v1_Message
        def __init__(self, id: _Optional[str] = ..., message: _Optional[_Union[API_v1_Message, _Mapping]] = ...) -> None: ...
    class DeleteMessage(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class TriggerMessage(_message.Message):
        __slots__ = ("id", "tokens")
        ID_FIELD_NUMBER: _ClassVar[int]
        TOKENS_FIELD_NUMBER: _ClassVar[int]
        id: str
        tokens: _containers.RepeatedCompositeFieldContainer[API_v1_Message.API_v1_MessageToken]
        def __init__(self, id: _Optional[str] = ..., tokens: _Optional[_Iterable[_Union[API_v1_Message.API_v1_MessageToken, _Mapping]]] = ...) -> None: ...
    class ClearMessage(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CREATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    messages: API_v1_Message_Request.Messages
    create_message: API_v1_Message_Request.CreateMessage
    get_message: API_v1_Message_Request.GetMessage
    put_message: API_v1_Message_Request.PutMessage
    delete_message: API_v1_Message_Request.DeleteMessage
    trigger_message: API_v1_Message_Request.TriggerMessage
    clear_message: API_v1_Message_Request.ClearMessage
    def __init__(self, messages: _Optional[_Union[API_v1_Message_Request.Messages, _Mapping]] = ..., create_message: _Optional[_Union[API_v1_Message_Request.CreateMessage, _Mapping]] = ..., get_message: _Optional[_Union[API_v1_Message_Request.GetMessage, _Mapping]] = ..., put_message: _Optional[_Union[API_v1_Message_Request.PutMessage, _Mapping]] = ..., delete_message: _Optional[_Union[API_v1_Message_Request.DeleteMessage, _Mapping]] = ..., trigger_message: _Optional[_Union[API_v1_Message_Request.TriggerMessage, _Mapping]] = ..., clear_message: _Optional[_Union[API_v1_Message_Request.ClearMessage, _Mapping]] = ...) -> None: ...

class API_v1_Message_Response(_message.Message):
    __slots__ = ("messages", "create_message", "get_message", "put_message", "delete_message", "trigger_message", "clear_message")
    class Messages(_message.Message):
        __slots__ = ("messages",)
        MESSAGES_FIELD_NUMBER: _ClassVar[int]
        messages: _containers.RepeatedCompositeFieldContainer[API_v1_Message]
        def __init__(self, messages: _Optional[_Iterable[_Union[API_v1_Message, _Mapping]]] = ...) -> None: ...
    class CreateMessage(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: API_v1_Message
        def __init__(self, message: _Optional[_Union[API_v1_Message, _Mapping]] = ...) -> None: ...
    class GetMessage(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: API_v1_Message
        def __init__(self, message: _Optional[_Union[API_v1_Message, _Mapping]] = ...) -> None: ...
    class PutMessage(_message.Message):
        __slots__ = ("message",)
        MESSAGE_FIELD_NUMBER: _ClassVar[int]
        message: API_v1_Message
        def __init__(self, message: _Optional[_Union[API_v1_Message, _Mapping]] = ...) -> None: ...
    class DeleteMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TriggerMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class ClearMessage(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    CREATE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    GET_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PUT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    CLEAR_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    messages: API_v1_Message_Response.Messages
    create_message: API_v1_Message_Response.CreateMessage
    get_message: API_v1_Message_Response.GetMessage
    put_message: API_v1_Message_Response.PutMessage
    delete_message: API_v1_Message_Response.DeleteMessage
    trigger_message: API_v1_Message_Response.TriggerMessage
    clear_message: API_v1_Message_Response.ClearMessage
    def __init__(self, messages: _Optional[_Union[API_v1_Message_Response.Messages, _Mapping]] = ..., create_message: _Optional[_Union[API_v1_Message_Response.CreateMessage, _Mapping]] = ..., get_message: _Optional[_Union[API_v1_Message_Response.GetMessage, _Mapping]] = ..., put_message: _Optional[_Union[API_v1_Message_Response.PutMessage, _Mapping]] = ..., delete_message: _Optional[_Union[API_v1_Message_Response.DeleteMessage, _Mapping]] = ..., trigger_message: _Optional[_Union[API_v1_Message_Response.TriggerMessage, _Mapping]] = ..., clear_message: _Optional[_Union[API_v1_Message_Response.ClearMessage, _Mapping]] = ...) -> None: ...
