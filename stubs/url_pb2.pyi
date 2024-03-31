from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class URL(_message.Message):
    __slots__ = ("platform", "absolute_string", "relative_path", "local", "external")
    class Platform(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        PLATFORM_UNKNOWN: _ClassVar[URL.Platform]
        PLATFORM_MACOS: _ClassVar[URL.Platform]
        PLATFORM_WIN32: _ClassVar[URL.Platform]
        PLATFORM_WEB: _ClassVar[URL.Platform]
    PLATFORM_UNKNOWN: URL.Platform
    PLATFORM_MACOS: URL.Platform
    PLATFORM_WIN32: URL.Platform
    PLATFORM_WEB: URL.Platform
    class LocalRelativePath(_message.Message):
        __slots__ = ("root", "path")
        class Root(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ROOT_UNKNOWN: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_BOOT_VOLUME: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_HOME: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_DOCUMENTS: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_DOWNLOADS: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_MUSIC: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_PICTURES: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_VIDEOS: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_DESKTOP: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_USER_APP_SUPPORT: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_SHARED: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_SHOW: _ClassVar[URL.LocalRelativePath.Root]
            ROOT_CURRENT_RESOURCE: _ClassVar[URL.LocalRelativePath.Root]
        ROOT_UNKNOWN: URL.LocalRelativePath.Root
        ROOT_BOOT_VOLUME: URL.LocalRelativePath.Root
        ROOT_USER_HOME: URL.LocalRelativePath.Root
        ROOT_USER_DOCUMENTS: URL.LocalRelativePath.Root
        ROOT_USER_DOWNLOADS: URL.LocalRelativePath.Root
        ROOT_USER_MUSIC: URL.LocalRelativePath.Root
        ROOT_USER_PICTURES: URL.LocalRelativePath.Root
        ROOT_USER_VIDEOS: URL.LocalRelativePath.Root
        ROOT_USER_DESKTOP: URL.LocalRelativePath.Root
        ROOT_USER_APP_SUPPORT: URL.LocalRelativePath.Root
        ROOT_SHARED: URL.LocalRelativePath.Root
        ROOT_SHOW: URL.LocalRelativePath.Root
        ROOT_CURRENT_RESOURCE: URL.LocalRelativePath.Root
        ROOT_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        root: URL.LocalRelativePath.Root
        path: str
        def __init__(self, root: _Optional[_Union[URL.LocalRelativePath.Root, str]] = ..., path: _Optional[str] = ...) -> None: ...
    class ExternalRelativePath(_message.Message):
        __slots__ = ("macos", "win32", "path")
        class MacOSExternalVolume(_message.Message):
            __slots__ = ("volume_name",)
            VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
            volume_name: str
            def __init__(self, volume_name: _Optional[str] = ...) -> None: ...
        class Win32ExternalVolume(_message.Message):
            __slots__ = ("drive_letter", "volume_name", "network_share")
            DRIVE_LETTER_FIELD_NUMBER: _ClassVar[int]
            VOLUME_NAME_FIELD_NUMBER: _ClassVar[int]
            NETWORK_SHARE_FIELD_NUMBER: _ClassVar[int]
            drive_letter: str
            volume_name: str
            network_share: bool
            def __init__(self, drive_letter: _Optional[str] = ..., volume_name: _Optional[str] = ..., network_share: bool = ...) -> None: ...
        MACOS_FIELD_NUMBER: _ClassVar[int]
        WIN32_FIELD_NUMBER: _ClassVar[int]
        PATH_FIELD_NUMBER: _ClassVar[int]
        macos: URL.ExternalRelativePath.MacOSExternalVolume
        win32: URL.ExternalRelativePath.Win32ExternalVolume
        path: str
        def __init__(self, macos: _Optional[_Union[URL.ExternalRelativePath.MacOSExternalVolume, _Mapping]] = ..., win32: _Optional[_Union[URL.ExternalRelativePath.Win32ExternalVolume, _Mapping]] = ..., path: _Optional[str] = ...) -> None: ...
    PLATFORM_FIELD_NUMBER: _ClassVar[int]
    ABSOLUTE_STRING_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_PATH_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    EXTERNAL_FIELD_NUMBER: _ClassVar[int]
    platform: URL.Platform
    absolute_string: str
    relative_path: str
    local: URL.LocalRelativePath
    external: URL.ExternalRelativePath
    def __init__(self, platform: _Optional[_Union[URL.Platform, str]] = ..., absolute_string: _Optional[str] = ..., relative_path: _Optional[str] = ..., local: _Optional[_Union[URL.LocalRelativePath, _Mapping]] = ..., external: _Optional[_Union[URL.ExternalRelativePath, _Mapping]] = ...) -> None: ...

class URLs(_message.Message):
    __slots__ = ("urls",)
    URLS_FIELD_NUMBER: _ClassVar[int]
    urls: _containers.RepeatedCompositeFieldContainer[URL]
    def __init__(self, urls: _Optional[_Iterable[_Union[URL, _Mapping]]] = ...) -> None: ...
