from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Update(_message.Message):
    __slots__ = ("downgrade",)
    class Downgrade(_message.Message):
        __slots__ = ("from_version_type",)
        class FromVersionType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            FROM_VERSION_TYPE_UNKNOWN: _ClassVar[Update.Downgrade.FromVersionType]
            FROM_VERSION_TYPE_BETA: _ClassVar[Update.Downgrade.FromVersionType]
            FROM_VERSION_TYPE_RELEASE: _ClassVar[Update.Downgrade.FromVersionType]
        FROM_VERSION_TYPE_UNKNOWN: Update.Downgrade.FromVersionType
        FROM_VERSION_TYPE_BETA: Update.Downgrade.FromVersionType
        FROM_VERSION_TYPE_RELEASE: Update.Downgrade.FromVersionType
        FROM_VERSION_TYPE_FIELD_NUMBER: _ClassVar[int]
        from_version_type: Update.Downgrade.FromVersionType
        def __init__(self, from_version_type: _Optional[_Union[Update.Downgrade.FromVersionType, str]] = ...) -> None: ...
    DOWNGRADE_FIELD_NUMBER: _ClassVar[int]
    downgrade: Update.Downgrade
    def __init__(self, downgrade: _Optional[_Union[Update.Downgrade, _Mapping]] = ...) -> None: ...
