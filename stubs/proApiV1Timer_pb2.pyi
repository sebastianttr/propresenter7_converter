import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_TimerFormat(_message.Message):
    __slots__ = ("hour", "minute", "second", "millisecond")
    class API_v1_TimerUnitDisplayFormat(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        none: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
        short: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
        long: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
        remove_short: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
        remove_long: _ClassVar[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat]
    none: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    short: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    long: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    remove_short: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    remove_long: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    HOUR_FIELD_NUMBER: _ClassVar[int]
    MINUTE_FIELD_NUMBER: _ClassVar[int]
    SECOND_FIELD_NUMBER: _ClassVar[int]
    MILLISECOND_FIELD_NUMBER: _ClassVar[int]
    hour: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    minute: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    second: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    millisecond: API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat
    def __init__(self, hour: _Optional[_Union[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat, str]] = ..., minute: _Optional[_Union[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat, str]] = ..., second: _Optional[_Union[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat, str]] = ..., millisecond: _Optional[_Union[API_v1_TimerFormat.API_v1_TimerUnitDisplayFormat, str]] = ...) -> None: ...

class API_v1_TimerValue(_message.Message):
    __slots__ = ("id", "time", "state")
    class API_v1_TimerState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        stopped: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
        running: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
        complete: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
        overrunning: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
        overran: _ClassVar[API_v1_TimerValue.API_v1_TimerState]
    stopped: API_v1_TimerValue.API_v1_TimerState
    running: API_v1_TimerValue.API_v1_TimerState
    complete: API_v1_TimerValue.API_v1_TimerState
    overrunning: API_v1_TimerValue.API_v1_TimerState
    overran: API_v1_TimerValue.API_v1_TimerState
    ID_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    time: str
    state: API_v1_TimerValue.API_v1_TimerState
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., time: _Optional[str] = ..., state: _Optional[_Union[API_v1_TimerValue.API_v1_TimerState, str]] = ...) -> None: ...

class API_v1_Timer(_message.Message):
    __slots__ = ("id", "allows_overrun", "countdown", "count_down_to_time", "elapsed")
    class API_v1_Timer_Countdown(_message.Message):
        __slots__ = ("duration",)
        DURATION_FIELD_NUMBER: _ClassVar[int]
        duration: int
        def __init__(self, duration: _Optional[int] = ...) -> None: ...
    class API_v1_Timer_CountdownToTime(_message.Message):
        __slots__ = ("time_of_day", "period")
        class API_v1_TimePeriod(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            am: _ClassVar[API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod]
            pm: _ClassVar[API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod]
            is_24_hour: _ClassVar[API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod]
        am: API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod
        pm: API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod
        is_24_hour: API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod
        TIME_OF_DAY_FIELD_NUMBER: _ClassVar[int]
        PERIOD_FIELD_NUMBER: _ClassVar[int]
        time_of_day: int
        period: API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod
        def __init__(self, time_of_day: _Optional[int] = ..., period: _Optional[_Union[API_v1_Timer.API_v1_Timer_CountdownToTime.API_v1_TimePeriod, str]] = ...) -> None: ...
    class API_v1_Timer_Elapsed(_message.Message):
        __slots__ = ("start_time", "end_time", "has_end_time")
        START_TIME_FIELD_NUMBER: _ClassVar[int]
        END_TIME_FIELD_NUMBER: _ClassVar[int]
        HAS_END_TIME_FIELD_NUMBER: _ClassVar[int]
        start_time: int
        end_time: int
        has_end_time: bool
        def __init__(self, start_time: _Optional[int] = ..., end_time: _Optional[int] = ..., has_end_time: bool = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    ALLOWS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
    COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
    COUNT_DOWN_TO_TIME_FIELD_NUMBER: _ClassVar[int]
    ELAPSED_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    allows_overrun: bool
    countdown: API_v1_Timer.API_v1_Timer_Countdown
    count_down_to_time: API_v1_Timer.API_v1_Timer_CountdownToTime
    elapsed: API_v1_Timer.API_v1_Timer_Elapsed
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., allows_overrun: bool = ..., countdown: _Optional[_Union[API_v1_Timer.API_v1_Timer_Countdown, _Mapping]] = ..., count_down_to_time: _Optional[_Union[API_v1_Timer.API_v1_Timer_CountdownToTime, _Mapping]] = ..., elapsed: _Optional[_Union[API_v1_Timer.API_v1_Timer_Elapsed, _Mapping]] = ...) -> None: ...

class API_v1_Timer_Request(_message.Message):
    __slots__ = ("timers", "create_timer", "current_times", "all_timers_operation", "get_timer", "put_timer", "delete_timer", "timer_operation", "put_timer_operation", "timer_increment", "system_time", "video_countdown")
    class Timers(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CreateTimer(_message.Message):
        __slots__ = ("name", "allows_overrun", "countdown", "count_down_to_time", "elapsed")
        NAME_FIELD_NUMBER: _ClassVar[int]
        ALLOWS_OVERRUN_FIELD_NUMBER: _ClassVar[int]
        COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
        COUNT_DOWN_TO_TIME_FIELD_NUMBER: _ClassVar[int]
        ELAPSED_FIELD_NUMBER: _ClassVar[int]
        name: str
        allows_overrun: bool
        countdown: API_v1_Timer.API_v1_Timer_Countdown
        count_down_to_time: API_v1_Timer.API_v1_Timer_CountdownToTime
        elapsed: API_v1_Timer.API_v1_Timer_Elapsed
        def __init__(self, name: _Optional[str] = ..., allows_overrun: bool = ..., countdown: _Optional[_Union[API_v1_Timer.API_v1_Timer_Countdown, _Mapping]] = ..., count_down_to_time: _Optional[_Union[API_v1_Timer.API_v1_Timer_CountdownToTime, _Mapping]] = ..., elapsed: _Optional[_Union[API_v1_Timer.API_v1_Timer_Elapsed, _Mapping]] = ...) -> None: ...
    class CurrentTimes(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class AllTimersOperation(_message.Message):
        __slots__ = ("operation",)
        class API_v1_TimerOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            start: _ClassVar[API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation]
            stop: _ClassVar[API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation]
            reset: _ClassVar[API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation]
        start: API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation
        stop: API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation
        reset: API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        operation: API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation
        def __init__(self, operation: _Optional[_Union[API_v1_Timer_Request.AllTimersOperation.API_v1_TimerOperation, str]] = ...) -> None: ...
    class GetTimer(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PutTimer(_message.Message):
        __slots__ = ("id", "timer")
        ID_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        id: str
        timer: API_v1_Timer
        def __init__(self, id: _Optional[str] = ..., timer: _Optional[_Union[API_v1_Timer, _Mapping]] = ...) -> None: ...
    class DeleteTimer(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class TimerOperation(_message.Message):
        __slots__ = ("id", "operation")
        class API_v1_TimerOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            start: _ClassVar[API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation]
            stop: _ClassVar[API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation]
            reset: _ClassVar[API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation]
        start: API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation
        stop: API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation
        reset: API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation
        ID_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        id: str
        operation: API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation
        def __init__(self, id: _Optional[str] = ..., operation: _Optional[_Union[API_v1_Timer_Request.TimerOperation.API_v1_TimerOperation, str]] = ...) -> None: ...
    class PutTimerOperation(_message.Message):
        __slots__ = ("id", "operation", "timer")
        class API_v1_TimerOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            start: _ClassVar[API_v1_Timer_Request.PutTimerOperation.API_v1_TimerOperation]
            stop: _ClassVar[API_v1_Timer_Request.PutTimerOperation.API_v1_TimerOperation]
            reset: _ClassVar[API_v1_Timer_Request.PutTimerOperation.API_v1_TimerOperation]
        start: API_v1_Timer_Request.PutTimerOperation.API_v1_TimerOperation
        stop: API_v1_Timer_Request.PutTimerOperation.API_v1_TimerOperation
        reset: API_v1_Timer_Request.PutTimerOperation.API_v1_TimerOperation
        ID_FIELD_NUMBER: _ClassVar[int]
        OPERATION_FIELD_NUMBER: _ClassVar[int]
        TIMER_FIELD_NUMBER: _ClassVar[int]
        id: str
        operation: API_v1_Timer_Request.PutTimerOperation.API_v1_TimerOperation
        timer: API_v1_Timer
        def __init__(self, id: _Optional[str] = ..., operation: _Optional[_Union[API_v1_Timer_Request.PutTimerOperation.API_v1_TimerOperation, str]] = ..., timer: _Optional[_Union[API_v1_Timer, _Mapping]] = ...) -> None: ...
    class TimerIncrement(_message.Message):
        __slots__ = ("id", "amount")
        ID_FIELD_NUMBER: _ClassVar[int]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        id: str
        amount: float
        def __init__(self, id: _Optional[str] = ..., amount: _Optional[float] = ...) -> None: ...
    class SystemTime(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class VideoCountdown(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    TIMERS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIMES_FIELD_NUMBER: _ClassVar[int]
    ALL_TIMERS_OPERATION_FIELD_NUMBER: _ClassVar[int]
    GET_TIMER_FIELD_NUMBER: _ClassVar[int]
    PUT_TIMER_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIMER_FIELD_NUMBER: _ClassVar[int]
    TIMER_OPERATION_FIELD_NUMBER: _ClassVar[int]
    PUT_TIMER_OPERATION_FIELD_NUMBER: _ClassVar[int]
    TIMER_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_TIME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
    timers: API_v1_Timer_Request.Timers
    create_timer: API_v1_Timer_Request.CreateTimer
    current_times: API_v1_Timer_Request.CurrentTimes
    all_timers_operation: API_v1_Timer_Request.AllTimersOperation
    get_timer: API_v1_Timer_Request.GetTimer
    put_timer: API_v1_Timer_Request.PutTimer
    delete_timer: API_v1_Timer_Request.DeleteTimer
    timer_operation: API_v1_Timer_Request.TimerOperation
    put_timer_operation: API_v1_Timer_Request.PutTimerOperation
    timer_increment: API_v1_Timer_Request.TimerIncrement
    system_time: API_v1_Timer_Request.SystemTime
    video_countdown: API_v1_Timer_Request.VideoCountdown
    def __init__(self, timers: _Optional[_Union[API_v1_Timer_Request.Timers, _Mapping]] = ..., create_timer: _Optional[_Union[API_v1_Timer_Request.CreateTimer, _Mapping]] = ..., current_times: _Optional[_Union[API_v1_Timer_Request.CurrentTimes, _Mapping]] = ..., all_timers_operation: _Optional[_Union[API_v1_Timer_Request.AllTimersOperation, _Mapping]] = ..., get_timer: _Optional[_Union[API_v1_Timer_Request.GetTimer, _Mapping]] = ..., put_timer: _Optional[_Union[API_v1_Timer_Request.PutTimer, _Mapping]] = ..., delete_timer: _Optional[_Union[API_v1_Timer_Request.DeleteTimer, _Mapping]] = ..., timer_operation: _Optional[_Union[API_v1_Timer_Request.TimerOperation, _Mapping]] = ..., put_timer_operation: _Optional[_Union[API_v1_Timer_Request.PutTimerOperation, _Mapping]] = ..., timer_increment: _Optional[_Union[API_v1_Timer_Request.TimerIncrement, _Mapping]] = ..., system_time: _Optional[_Union[API_v1_Timer_Request.SystemTime, _Mapping]] = ..., video_countdown: _Optional[_Union[API_v1_Timer_Request.VideoCountdown, _Mapping]] = ...) -> None: ...

class API_v1_Timer_Response(_message.Message):
    __slots__ = ("timers", "create_timer", "current_times", "all_timers_operation", "get_timer", "put_timer", "delete_timer", "timer_operation", "put_timer_operation", "timer_increment", "system_time", "video_countdown")
    class Timers(_message.Message):
        __slots__ = ("timers",)
        TIMERS_FIELD_NUMBER: _ClassVar[int]
        timers: _containers.RepeatedCompositeFieldContainer[API_v1_Timer]
        def __init__(self, timers: _Optional[_Iterable[_Union[API_v1_Timer, _Mapping]]] = ...) -> None: ...
    class CreateTimer(_message.Message):
        __slots__ = ("timer",)
        TIMER_FIELD_NUMBER: _ClassVar[int]
        timer: API_v1_Timer
        def __init__(self, timer: _Optional[_Union[API_v1_Timer, _Mapping]] = ...) -> None: ...
    class CurrentTimes(_message.Message):
        __slots__ = ("timers",)
        TIMERS_FIELD_NUMBER: _ClassVar[int]
        timers: _containers.RepeatedCompositeFieldContainer[API_v1_TimerValue]
        def __init__(self, timers: _Optional[_Iterable[_Union[API_v1_TimerValue, _Mapping]]] = ...) -> None: ...
    class AllTimersOperation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetTimer(_message.Message):
        __slots__ = ("timer",)
        TIMER_FIELD_NUMBER: _ClassVar[int]
        timer: API_v1_Timer
        def __init__(self, timer: _Optional[_Union[API_v1_Timer, _Mapping]] = ...) -> None: ...
    class PutTimer(_message.Message):
        __slots__ = ("timer",)
        TIMER_FIELD_NUMBER: _ClassVar[int]
        timer: API_v1_Timer
        def __init__(self, timer: _Optional[_Union[API_v1_Timer, _Mapping]] = ...) -> None: ...
    class DeleteTimer(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TimerOperation(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PutTimerOperation(_message.Message):
        __slots__ = ("timer",)
        TIMER_FIELD_NUMBER: _ClassVar[int]
        timer: API_v1_Timer
        def __init__(self, timer: _Optional[_Union[API_v1_Timer, _Mapping]] = ...) -> None: ...
    class TimerIncrement(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class SystemTime(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: int
        def __init__(self, time: _Optional[int] = ...) -> None: ...
    class VideoCountdown(_message.Message):
        __slots__ = ("time",)
        TIME_FIELD_NUMBER: _ClassVar[int]
        time: str
        def __init__(self, time: _Optional[str] = ...) -> None: ...
    TIMERS_FIELD_NUMBER: _ClassVar[int]
    CREATE_TIMER_FIELD_NUMBER: _ClassVar[int]
    CURRENT_TIMES_FIELD_NUMBER: _ClassVar[int]
    ALL_TIMERS_OPERATION_FIELD_NUMBER: _ClassVar[int]
    GET_TIMER_FIELD_NUMBER: _ClassVar[int]
    PUT_TIMER_FIELD_NUMBER: _ClassVar[int]
    DELETE_TIMER_FIELD_NUMBER: _ClassVar[int]
    TIMER_OPERATION_FIELD_NUMBER: _ClassVar[int]
    PUT_TIMER_OPERATION_FIELD_NUMBER: _ClassVar[int]
    TIMER_INCREMENT_FIELD_NUMBER: _ClassVar[int]
    SYSTEM_TIME_FIELD_NUMBER: _ClassVar[int]
    VIDEO_COUNTDOWN_FIELD_NUMBER: _ClassVar[int]
    timers: API_v1_Timer_Response.Timers
    create_timer: API_v1_Timer_Response.CreateTimer
    current_times: API_v1_Timer_Response.CurrentTimes
    all_timers_operation: API_v1_Timer_Response.AllTimersOperation
    get_timer: API_v1_Timer_Response.GetTimer
    put_timer: API_v1_Timer_Response.PutTimer
    delete_timer: API_v1_Timer_Response.DeleteTimer
    timer_operation: API_v1_Timer_Response.TimerOperation
    put_timer_operation: API_v1_Timer_Response.PutTimerOperation
    timer_increment: API_v1_Timer_Response.TimerIncrement
    system_time: API_v1_Timer_Response.SystemTime
    video_countdown: API_v1_Timer_Response.VideoCountdown
    def __init__(self, timers: _Optional[_Union[API_v1_Timer_Response.Timers, _Mapping]] = ..., create_timer: _Optional[_Union[API_v1_Timer_Response.CreateTimer, _Mapping]] = ..., current_times: _Optional[_Union[API_v1_Timer_Response.CurrentTimes, _Mapping]] = ..., all_timers_operation: _Optional[_Union[API_v1_Timer_Response.AllTimersOperation, _Mapping]] = ..., get_timer: _Optional[_Union[API_v1_Timer_Response.GetTimer, _Mapping]] = ..., put_timer: _Optional[_Union[API_v1_Timer_Response.PutTimer, _Mapping]] = ..., delete_timer: _Optional[_Union[API_v1_Timer_Response.DeleteTimer, _Mapping]] = ..., timer_operation: _Optional[_Union[API_v1_Timer_Response.TimerOperation, _Mapping]] = ..., put_timer_operation: _Optional[_Union[API_v1_Timer_Response.PutTimerOperation, _Mapping]] = ..., timer_increment: _Optional[_Union[API_v1_Timer_Response.TimerIncrement, _Mapping]] = ..., system_time: _Optional[_Union[API_v1_Timer_Response.SystemTime, _Mapping]] = ..., video_countdown: _Optional[_Union[API_v1_Timer_Response.VideoCountdown, _Mapping]] = ...) -> None: ...
