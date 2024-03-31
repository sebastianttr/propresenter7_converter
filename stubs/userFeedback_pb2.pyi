from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class UserFeedback(_message.Message):
    __slots__ = ()
    class ApplicationMetadata(_message.Message):
        __slots__ = ("application_version", "os_version", "application_instances", "blackmagic_desktop_video_instances", "screens", "crash_reporting_enabled", "analytics_reporting_enabled")
        class ApplicationInstance(_message.Message):
            __slots__ = ("path", "version")
            PATH_FIELD_NUMBER: _ClassVar[int]
            VERSION_FIELD_NUMBER: _ClassVar[int]
            path: str
            version: str
            def __init__(self, path: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...
        class Screen(_message.Message):
            __slots__ = ("name", "resolution", "type", "output_name")
            class Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                UNKNOWN: _ClassVar[UserFeedback.ApplicationMetadata.Screen.Type]
                AUDIENCE: _ClassVar[UserFeedback.ApplicationMetadata.Screen.Type]
                STAGE: _ClassVar[UserFeedback.ApplicationMetadata.Screen.Type]
            UNKNOWN: UserFeedback.ApplicationMetadata.Screen.Type
            AUDIENCE: UserFeedback.ApplicationMetadata.Screen.Type
            STAGE: UserFeedback.ApplicationMetadata.Screen.Type
            class Resolution(_message.Message):
                __slots__ = ("width", "height")
                WIDTH_FIELD_NUMBER: _ClassVar[int]
                HEIGHT_FIELD_NUMBER: _ClassVar[int]
                width: int
                height: int
                def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
            NAME_FIELD_NUMBER: _ClassVar[int]
            RESOLUTION_FIELD_NUMBER: _ClassVar[int]
            TYPE_FIELD_NUMBER: _ClassVar[int]
            OUTPUT_NAME_FIELD_NUMBER: _ClassVar[int]
            name: str
            resolution: UserFeedback.ApplicationMetadata.Screen.Resolution
            type: UserFeedback.ApplicationMetadata.Screen.Type
            output_name: str
            def __init__(self, name: _Optional[str] = ..., resolution: _Optional[_Union[UserFeedback.ApplicationMetadata.Screen.Resolution, _Mapping]] = ..., type: _Optional[_Union[UserFeedback.ApplicationMetadata.Screen.Type, str]] = ..., output_name: _Optional[str] = ...) -> None: ...
        APPLICATION_VERSION_FIELD_NUMBER: _ClassVar[int]
        OS_VERSION_FIELD_NUMBER: _ClassVar[int]
        APPLICATION_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        BLACKMAGIC_DESKTOP_VIDEO_INSTANCES_FIELD_NUMBER: _ClassVar[int]
        SCREENS_FIELD_NUMBER: _ClassVar[int]
        CRASH_REPORTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        ANALYTICS_REPORTING_ENABLED_FIELD_NUMBER: _ClassVar[int]
        application_version: str
        os_version: str
        application_instances: _containers.RepeatedCompositeFieldContainer[UserFeedback.ApplicationMetadata.ApplicationInstance]
        blackmagic_desktop_video_instances: _containers.RepeatedCompositeFieldContainer[UserFeedback.ApplicationMetadata.ApplicationInstance]
        screens: _containers.RepeatedCompositeFieldContainer[UserFeedback.ApplicationMetadata.Screen]
        crash_reporting_enabled: bool
        analytics_reporting_enabled: bool
        def __init__(self, application_version: _Optional[str] = ..., os_version: _Optional[str] = ..., application_instances: _Optional[_Iterable[_Union[UserFeedback.ApplicationMetadata.ApplicationInstance, _Mapping]]] = ..., blackmagic_desktop_video_instances: _Optional[_Iterable[_Union[UserFeedback.ApplicationMetadata.ApplicationInstance, _Mapping]]] = ..., screens: _Optional[_Iterable[_Union[UserFeedback.ApplicationMetadata.Screen, _Mapping]]] = ..., crash_reporting_enabled: bool = ..., analytics_reporting_enabled: bool = ...) -> None: ...
    def __init__(self) -> None: ...
