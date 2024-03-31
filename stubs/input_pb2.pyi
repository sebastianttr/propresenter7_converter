import alphaType_pb2 as _alphaType_pb2
import color_pb2 as _color_pb2
import digitalAudio_pb2 as _digitalAudio_pb2
import graphicsData_pb2 as _graphicsData_pb2
import url_pb2 as _url_pb2
import uuid_pb2 as _uuid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class VideoInput(_message.Message):
    __slots__ = ("uuid", "user_description", "video_input_device", "display_color", "thumbnail_path", "audio_type", "alpha_type", "audio_device", "video_device")
    class AudioDeviceType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        AUDIO_DEVICE_TYPE_DEFAULT: _ClassVar[VideoInput.AudioDeviceType]
        AUDIO_DEVICE_TYPE_NONE: _ClassVar[VideoInput.AudioDeviceType]
        AUDIO_DEVICE_TYPE_ALTERNATE: _ClassVar[VideoInput.AudioDeviceType]
    AUDIO_DEVICE_TYPE_DEFAULT: VideoInput.AudioDeviceType
    AUDIO_DEVICE_TYPE_NONE: VideoInput.AudioDeviceType
    AUDIO_DEVICE_TYPE_ALTERNATE: VideoInput.AudioDeviceType
    class AlphaType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        ALPHA_TYPE_UNKNOWN: _ClassVar[VideoInput.AlphaType]
        ALPHA_TYPE_STRAIGHT: _ClassVar[VideoInput.AlphaType]
        ALPHA_TYPE_PREMULTIPLIED: _ClassVar[VideoInput.AlphaType]
    ALPHA_TYPE_UNKNOWN: VideoInput.AlphaType
    ALPHA_TYPE_STRAIGHT: VideoInput.AlphaType
    ALPHA_TYPE_PREMULTIPLIED: VideoInput.AlphaType
    class SettingsDocument(_message.Message):
        __slots__ = ("inputs",)
        INPUTS_FIELD_NUMBER: _ClassVar[int]
        inputs: _containers.RepeatedCompositeFieldContainer[VideoInput]
        def __init__(self, inputs: _Optional[_Iterable[_Union[VideoInput, _Mapping]]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    USER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    VIDEO_INPUT_DEVICE_FIELD_NUMBER: _ClassVar[int]
    DISPLAY_COLOR_FIELD_NUMBER: _ClassVar[int]
    THUMBNAIL_PATH_FIELD_NUMBER: _ClassVar[int]
    AUDIO_TYPE_FIELD_NUMBER: _ClassVar[int]
    ALPHA_TYPE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DEVICE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DEVICE_FIELD_NUMBER: _ClassVar[int]
    uuid: _uuid_pb2.UUID
    user_description: str
    video_input_device: _graphicsData_pb2.Media.VideoDevice
    display_color: _color_pb2.Color
    thumbnail_path: _url_pb2.URL
    audio_type: VideoInput.AudioDeviceType
    alpha_type: VideoInput.AlphaType
    audio_device: _digitalAudio_pb2.DigitalAudio.Device
    video_device: _graphicsData_pb2.Media.VideoDevice
    def __init__(self, uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., user_description: _Optional[str] = ..., video_input_device: _Optional[_Union[_graphicsData_pb2.Media.VideoDevice, _Mapping]] = ..., display_color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., thumbnail_path: _Optional[_Union[_url_pb2.URL, _Mapping]] = ..., audio_type: _Optional[_Union[VideoInput.AudioDeviceType, str]] = ..., alpha_type: _Optional[_Union[VideoInput.AlphaType, str]] = ..., audio_device: _Optional[_Union[_digitalAudio_pb2.DigitalAudio.Device, _Mapping]] = ..., video_device: _Optional[_Union[_graphicsData_pb2.Media.VideoDevice, _Mapping]] = ...) -> None: ...

class AudioInput(_message.Message):
    __slots__ = ("uuid", "user_description", "behavior_mode", "audio_device", "video_device")
    class BehaviorMode(_message.Message):
        __slots__ = ("on", "off", "auto_on", "auto_off")
        class On(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class Off(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AutoOff(_message.Message):
            __slots__ = ()
            def __init__(self) -> None: ...
        class AutoOn(_message.Message):
            __slots__ = ("linked_video_inputs",)
            LINKED_VIDEO_INPUTS_FIELD_NUMBER: _ClassVar[int]
            linked_video_inputs: _containers.RepeatedScalarFieldContainer[int]
            def __init__(self, linked_video_inputs: _Optional[_Iterable[int]] = ...) -> None: ...
        ON_FIELD_NUMBER: _ClassVar[int]
        OFF_FIELD_NUMBER: _ClassVar[int]
        AUTO_ON_FIELD_NUMBER: _ClassVar[int]
        AUTO_OFF_FIELD_NUMBER: _ClassVar[int]
        on: AudioInput.BehaviorMode.On
        off: AudioInput.BehaviorMode.Off
        auto_on: AudioInput.BehaviorMode.AutoOn
        auto_off: AudioInput.BehaviorMode.AutoOff
        def __init__(self, on: _Optional[_Union[AudioInput.BehaviorMode.On, _Mapping]] = ..., off: _Optional[_Union[AudioInput.BehaviorMode.Off, _Mapping]] = ..., auto_on: _Optional[_Union[AudioInput.BehaviorMode.AutoOn, _Mapping]] = ..., auto_off: _Optional[_Union[AudioInput.BehaviorMode.AutoOff, _Mapping]] = ...) -> None: ...
    UUID_FIELD_NUMBER: _ClassVar[int]
    USER_DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
    BEHAVIOR_MODE_FIELD_NUMBER: _ClassVar[int]
    AUDIO_DEVICE_FIELD_NUMBER: _ClassVar[int]
    VIDEO_DEVICE_FIELD_NUMBER: _ClassVar[int]
    uuid: _uuid_pb2.UUID
    user_description: str
    behavior_mode: AudioInput.BehaviorMode
    audio_device: _digitalAudio_pb2.DigitalAudio.Device
    video_device: _graphicsData_pb2.Media.VideoDevice
    def __init__(self, uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., user_description: _Optional[str] = ..., behavior_mode: _Optional[_Union[AudioInput.BehaviorMode, _Mapping]] = ..., audio_device: _Optional[_Union[_digitalAudio_pb2.DigitalAudio.Device, _Mapping]] = ..., video_device: _Optional[_Union[_graphicsData_pb2.Media.VideoDevice, _Mapping]] = ...) -> None: ...
