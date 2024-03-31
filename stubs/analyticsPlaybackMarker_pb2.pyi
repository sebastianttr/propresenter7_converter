from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PlaybackMarker(_message.Message):
    __slots__ = ("create",)
    class CreateMarker(_message.Message):
        __slots__ = ("location",)
        class Location(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            LOCATION_INSPECTOR: _ClassVar[PlaybackMarker.CreateMarker.Location]
            LOCATION_SIDEBAR: _ClassVar[PlaybackMarker.CreateMarker.Location]
        LOCATION_INSPECTOR: PlaybackMarker.CreateMarker.Location
        LOCATION_SIDEBAR: PlaybackMarker.CreateMarker.Location
        LOCATION_FIELD_NUMBER: _ClassVar[int]
        location: PlaybackMarker.CreateMarker.Location
        def __init__(self, location: _Optional[_Union[PlaybackMarker.CreateMarker.Location, str]] = ...) -> None: ...
    CREATE_FIELD_NUMBER: _ClassVar[int]
    create: PlaybackMarker.CreateMarker
    def __init__(self, create: _Optional[_Union[PlaybackMarker.CreateMarker, _Mapping]] = ...) -> None: ...
