from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MultiTracks(_message.Message):
    __slots__ = ()
    class Account(_message.Message):
        __slots__ = ("chart_pro", "propresenter_addon")
        class Status(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            STATUS_DISABLED: _ClassVar[MultiTracks.Account.Status]
            STATUS_CANCELLED: _ClassVar[MultiTracks.Account.Status]
            STATUS_ACTIVE: _ClassVar[MultiTracks.Account.Status]
        STATUS_DISABLED: MultiTracks.Account.Status
        STATUS_CANCELLED: MultiTracks.Account.Status
        STATUS_ACTIVE: MultiTracks.Account.Status
        CHART_PRO_FIELD_NUMBER: _ClassVar[int]
        PROPRESENTER_ADDON_FIELD_NUMBER: _ClassVar[int]
        chart_pro: MultiTracks.Account.Status
        propresenter_addon: MultiTracks.Account.Status
        def __init__(self, chart_pro: _Optional[_Union[MultiTracks.Account.Status, str]] = ..., propresenter_addon: _Optional[_Union[MultiTracks.Account.Status, str]] = ...) -> None: ...
    class Startup(_message.Message):
        __slots__ = ("account",)
        ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        account: MultiTracks.Account
        def __init__(self, account: _Optional[_Union[MultiTracks.Account, _Mapping]] = ...) -> None: ...
    class Import(_message.Message):
        __slots__ = ("account", "charts_automation", "lines")
        ACCOUNT_FIELD_NUMBER: _ClassVar[int]
        CHARTS_AUTOMATION_FIELD_NUMBER: _ClassVar[int]
        LINES_FIELD_NUMBER: _ClassVar[int]
        account: MultiTracks.Account
        charts_automation: bool
        lines: int
        def __init__(self, account: _Optional[_Union[MultiTracks.Account, _Mapping]] = ..., charts_automation: bool = ..., lines: _Optional[int] = ...) -> None: ...
    def __init__(self) -> None: ...
