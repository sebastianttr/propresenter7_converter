from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MusicKeyScale(_message.Message):
    __slots__ = ("music_key", "music_scale")
    class MusicKey(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUSIC_KEY_A_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_A: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_A_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_B_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_B: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_B_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_C_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_C: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_C_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_D_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_D: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_D_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_E_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_E: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_E_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_F_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_F: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_F_SHARP: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_G_FLAT: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_G: _ClassVar[MusicKeyScale.MusicKey]
        MUSIC_KEY_G_SHARP: _ClassVar[MusicKeyScale.MusicKey]
    MUSIC_KEY_A_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_A: MusicKeyScale.MusicKey
    MUSIC_KEY_A_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_B_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_B: MusicKeyScale.MusicKey
    MUSIC_KEY_B_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_C_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_C: MusicKeyScale.MusicKey
    MUSIC_KEY_C_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_D_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_D: MusicKeyScale.MusicKey
    MUSIC_KEY_D_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_E_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_E: MusicKeyScale.MusicKey
    MUSIC_KEY_E_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_F_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_F: MusicKeyScale.MusicKey
    MUSIC_KEY_F_SHARP: MusicKeyScale.MusicKey
    MUSIC_KEY_G_FLAT: MusicKeyScale.MusicKey
    MUSIC_KEY_G: MusicKeyScale.MusicKey
    MUSIC_KEY_G_SHARP: MusicKeyScale.MusicKey
    class MusicScale(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        MUSIC_SCALE_MAJOR: _ClassVar[MusicKeyScale.MusicScale]
        MUSIC_SCALE_MINOR: _ClassVar[MusicKeyScale.MusicScale]
    MUSIC_SCALE_MAJOR: MusicKeyScale.MusicScale
    MUSIC_SCALE_MINOR: MusicKeyScale.MusicScale
    MUSIC_KEY_FIELD_NUMBER: _ClassVar[int]
    MUSIC_SCALE_FIELD_NUMBER: _ClassVar[int]
    music_key: MusicKeyScale.MusicKey
    music_scale: MusicKeyScale.MusicScale
    def __init__(self, music_key: _Optional[_Union[MusicKeyScale.MusicKey, str]] = ..., music_scale: _Optional[_Union[MusicKeyScale.MusicScale, str]] = ...) -> None: ...
