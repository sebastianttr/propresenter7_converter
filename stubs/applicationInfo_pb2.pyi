import version_pb2 as _version_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ApplicationInfo(_message.Message):
    __slots__ = ("platform", "platform_version", "application", "application_version")
    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNDEFINED: _ClassVar[ApplicationInfo.Platform]
        PLATFORM_MACOS: _ClassVar[ApplicationInfo.Platform]
        PLATFORM_WINDOWS: _ClassVar[ApplicationInfo.Platform]
    PLATFORM_UNDEFINED: ApplicationInfo.Platform
    PLATFORM_MACOS: ApplicationInfo.Platform
    PLATFORM_WINDOWS: ApplicationInfo.Platform
    class Application(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        APPLICATION_UNDEFINED: _ClassVar[ApplicationInfo.Application]
        APPLICATION_PROPRESENTER: _ClassVar[ApplicationInfo.Application]
        APPLICATION_PVP: _ClassVar[ApplicationInfo.Application]
        APPLICATION_PROVIDEOSERVER: _ClassVar[ApplicationInfo.Application]
        APPLICATION_SCOREBOARD: _ClassVar[ApplicationInfo.Application]
    APPLICATION_UNDEFINED: ApplicationInfo.Application
    APPLICATION_PROPRESENTER: ApplicationInfo.Application
    APPLICATION_PVP: ApplicationInfo.Application
    APPLICATION_PROVIDEOSERVER: ApplicationInfo.Application
    APPLICATION_SCOREBOARD: ApplicationInfo.Application
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    PLATFORM_VERSION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_FIELD_NUMBER: _ClassVar[int]
    APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
    platform: ApplicationInfo.Platform
    platform_version: _version_pb2.Version
    application: ApplicationInfo.Application
    application_version: _version_pb2.Version
    def __init__(self, platform: _Optional[_Union[ApplicationInfo.Platform, str]] = ..., platform_version: _Optional[_Union[_version_pb2.Version, _Mapping]] = ..., application: _Optional[_Union[ApplicationInfo.Application, str]] = ..., application_version: _Optional[_Union[_version_pb2.Version, _Mapping]] = ...) -> None: ...
