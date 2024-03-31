from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Capture(_message.Message):
    __slots__ = ("start",)
    class Resolution(_message.Message):
        __slots__ = ("width", "height")
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        width: int
        height: int
        def __init__(self, width: _Optional[int] = ..., height: _Optional[int] = ...) -> None: ...
    class Start(_message.Message):
        __slots__ = ("rtmp", "disk", "resi")
        class RTMP(_message.Message):
            __slots__ = ("codec", "frame_rate", "host", "resolution", "stream_started", "video_bitrate")
            class Codec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CODEC_UNKNOWN: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_AUTOMATIC: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_H264: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_H264_SOFTWARE: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_H265: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_H265_SOFTWARE: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_PRORES_422_PROXY: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_PRORES_422_LT: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_PRORES_422: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_PRORES_422_HQ: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_PRORES_4444: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_PRORES_4444_XQ: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_HAP: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_HAP_ALPHA: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_HAP_Q: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_HAP_Q_ALPHA: _ClassVar[Capture.Start.RTMP.Codec]
                CODEC_NOTCH: _ClassVar[Capture.Start.RTMP.Codec]
            CODEC_UNKNOWN: Capture.Start.RTMP.Codec
            CODEC_AUTOMATIC: Capture.Start.RTMP.Codec
            CODEC_H264: Capture.Start.RTMP.Codec
            CODEC_H264_SOFTWARE: Capture.Start.RTMP.Codec
            CODEC_H265: Capture.Start.RTMP.Codec
            CODEC_H265_SOFTWARE: Capture.Start.RTMP.Codec
            CODEC_PRORES_422_PROXY: Capture.Start.RTMP.Codec
            CODEC_PRORES_422_LT: Capture.Start.RTMP.Codec
            CODEC_PRORES_422: Capture.Start.RTMP.Codec
            CODEC_PRORES_422_HQ: Capture.Start.RTMP.Codec
            CODEC_PRORES_4444: Capture.Start.RTMP.Codec
            CODEC_PRORES_4444_XQ: Capture.Start.RTMP.Codec
            CODEC_HAP: Capture.Start.RTMP.Codec
            CODEC_HAP_ALPHA: Capture.Start.RTMP.Codec
            CODEC_HAP_Q: Capture.Start.RTMP.Codec
            CODEC_HAP_Q_ALPHA: Capture.Start.RTMP.Codec
            CODEC_NOTCH: Capture.Start.RTMP.Codec
            class FrameRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FRAME_RATE_UNKNOWN: _ClassVar[Capture.Start.RTMP.FrameRate]
                FRAME_RATE_24: _ClassVar[Capture.Start.RTMP.FrameRate]
                FRAME_RATE_25: _ClassVar[Capture.Start.RTMP.FrameRate]
                FRAME_RATE_29_97: _ClassVar[Capture.Start.RTMP.FrameRate]
                FRAME_RATE_30: _ClassVar[Capture.Start.RTMP.FrameRate]
                FRAME_RATE_50: _ClassVar[Capture.Start.RTMP.FrameRate]
                FRAME_RATE_59_94: _ClassVar[Capture.Start.RTMP.FrameRate]
                FRAME_RATE_60: _ClassVar[Capture.Start.RTMP.FrameRate]
            FRAME_RATE_UNKNOWN: Capture.Start.RTMP.FrameRate
            FRAME_RATE_24: Capture.Start.RTMP.FrameRate
            FRAME_RATE_25: Capture.Start.RTMP.FrameRate
            FRAME_RATE_29_97: Capture.Start.RTMP.FrameRate
            FRAME_RATE_30: Capture.Start.RTMP.FrameRate
            FRAME_RATE_50: Capture.Start.RTMP.FrameRate
            FRAME_RATE_59_94: Capture.Start.RTMP.FrameRate
            FRAME_RATE_60: Capture.Start.RTMP.FrameRate
            CODEC_FIELD_NUMBER: _ClassVar[int]
            FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
            HOST_FIELD_NUMBER: _ClassVar[int]
            RESOLUTION_FIELD_NUMBER: _ClassVar[int]
            STREAM_STARTED_FIELD_NUMBER: _ClassVar[int]
            VIDEO_BITRATE_FIELD_NUMBER: _ClassVar[int]
            codec: Capture.Start.RTMP.Codec
            frame_rate: Capture.Start.RTMP.FrameRate
            host: str
            resolution: Capture.Resolution
            stream_started: bool
            video_bitrate: int
            def __init__(self, codec: _Optional[_Union[Capture.Start.RTMP.Codec, str]] = ..., frame_rate: _Optional[_Union[Capture.Start.RTMP.FrameRate, str]] = ..., host: _Optional[str] = ..., resolution: _Optional[_Union[Capture.Resolution, _Mapping]] = ..., stream_started: bool = ..., video_bitrate: _Optional[int] = ...) -> None: ...
        class Disk(_message.Message):
            __slots__ = ("codec", "frame_rate", "resolution", "stream_started", "video_bitrate")
            class Codec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CODEC_UNKNOWN: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_AUTOMATIC: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_H264: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_H264_SOFTWARE: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_H265: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_H265_SOFTWARE: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_PRORES_422_PROXY: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_PRORES_422_LT: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_PRORES_422: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_PRORES_422_HQ: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_PRORES_4444: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_PRORES_4444_XQ: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_HAP: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_HAP_ALPHA: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_HAP_Q: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_HAP_Q_ALPHA: _ClassVar[Capture.Start.Disk.Codec]
                CODEC_NOTCH: _ClassVar[Capture.Start.Disk.Codec]
            CODEC_UNKNOWN: Capture.Start.Disk.Codec
            CODEC_AUTOMATIC: Capture.Start.Disk.Codec
            CODEC_H264: Capture.Start.Disk.Codec
            CODEC_H264_SOFTWARE: Capture.Start.Disk.Codec
            CODEC_H265: Capture.Start.Disk.Codec
            CODEC_H265_SOFTWARE: Capture.Start.Disk.Codec
            CODEC_PRORES_422_PROXY: Capture.Start.Disk.Codec
            CODEC_PRORES_422_LT: Capture.Start.Disk.Codec
            CODEC_PRORES_422: Capture.Start.Disk.Codec
            CODEC_PRORES_422_HQ: Capture.Start.Disk.Codec
            CODEC_PRORES_4444: Capture.Start.Disk.Codec
            CODEC_PRORES_4444_XQ: Capture.Start.Disk.Codec
            CODEC_HAP: Capture.Start.Disk.Codec
            CODEC_HAP_ALPHA: Capture.Start.Disk.Codec
            CODEC_HAP_Q: Capture.Start.Disk.Codec
            CODEC_HAP_Q_ALPHA: Capture.Start.Disk.Codec
            CODEC_NOTCH: Capture.Start.Disk.Codec
            class FrameRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FRAME_RATE_UNKNOWN: _ClassVar[Capture.Start.Disk.FrameRate]
                FRAME_RATE_24: _ClassVar[Capture.Start.Disk.FrameRate]
                FRAME_RATE_25: _ClassVar[Capture.Start.Disk.FrameRate]
                FRAME_RATE_29_97: _ClassVar[Capture.Start.Disk.FrameRate]
                FRAME_RATE_30: _ClassVar[Capture.Start.Disk.FrameRate]
                FRAME_RATE_50: _ClassVar[Capture.Start.Disk.FrameRate]
                FRAME_RATE_59_94: _ClassVar[Capture.Start.Disk.FrameRate]
                FRAME_RATE_60: _ClassVar[Capture.Start.Disk.FrameRate]
            FRAME_RATE_UNKNOWN: Capture.Start.Disk.FrameRate
            FRAME_RATE_24: Capture.Start.Disk.FrameRate
            FRAME_RATE_25: Capture.Start.Disk.FrameRate
            FRAME_RATE_29_97: Capture.Start.Disk.FrameRate
            FRAME_RATE_30: Capture.Start.Disk.FrameRate
            FRAME_RATE_50: Capture.Start.Disk.FrameRate
            FRAME_RATE_59_94: Capture.Start.Disk.FrameRate
            FRAME_RATE_60: Capture.Start.Disk.FrameRate
            CODEC_FIELD_NUMBER: _ClassVar[int]
            FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
            RESOLUTION_FIELD_NUMBER: _ClassVar[int]
            STREAM_STARTED_FIELD_NUMBER: _ClassVar[int]
            VIDEO_BITRATE_FIELD_NUMBER: _ClassVar[int]
            codec: Capture.Start.Disk.Codec
            frame_rate: Capture.Start.Disk.FrameRate
            resolution: Capture.Resolution
            stream_started: bool
            video_bitrate: int
            def __init__(self, codec: _Optional[_Union[Capture.Start.Disk.Codec, str]] = ..., frame_rate: _Optional[_Union[Capture.Start.Disk.FrameRate, str]] = ..., resolution: _Optional[_Union[Capture.Resolution, _Mapping]] = ..., stream_started: bool = ..., video_bitrate: _Optional[int] = ...) -> None: ...
        class Resi(_message.Message):
            __slots__ = ("codec", "frame_rate", "resolution", "stream_started", "video_bitrate")
            class Codec(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                CODEC_UNKNOWN: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_AUTOMATIC: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_H264: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_H264_SOFTWARE: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_H265: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_H265_SOFTWARE: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_PRORES_422_PROXY: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_PRORES_422_LT: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_PRORES_422: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_PRORES_422_HQ: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_PRORES_4444: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_PRORES_4444_XQ: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_HAP: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_HAP_ALPHA: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_HAP_Q: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_HAP_Q_ALPHA: _ClassVar[Capture.Start.Resi.Codec]
                CODEC_NOTCH: _ClassVar[Capture.Start.Resi.Codec]
            CODEC_UNKNOWN: Capture.Start.Resi.Codec
            CODEC_AUTOMATIC: Capture.Start.Resi.Codec
            CODEC_H264: Capture.Start.Resi.Codec
            CODEC_H264_SOFTWARE: Capture.Start.Resi.Codec
            CODEC_H265: Capture.Start.Resi.Codec
            CODEC_H265_SOFTWARE: Capture.Start.Resi.Codec
            CODEC_PRORES_422_PROXY: Capture.Start.Resi.Codec
            CODEC_PRORES_422_LT: Capture.Start.Resi.Codec
            CODEC_PRORES_422: Capture.Start.Resi.Codec
            CODEC_PRORES_422_HQ: Capture.Start.Resi.Codec
            CODEC_PRORES_4444: Capture.Start.Resi.Codec
            CODEC_PRORES_4444_XQ: Capture.Start.Resi.Codec
            CODEC_HAP: Capture.Start.Resi.Codec
            CODEC_HAP_ALPHA: Capture.Start.Resi.Codec
            CODEC_HAP_Q: Capture.Start.Resi.Codec
            CODEC_HAP_Q_ALPHA: Capture.Start.Resi.Codec
            CODEC_NOTCH: Capture.Start.Resi.Codec
            class FrameRate(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
                __slots__ = ()
                FRAME_RATE_UNKNOWN: _ClassVar[Capture.Start.Resi.FrameRate]
                FRAME_RATE_24: _ClassVar[Capture.Start.Resi.FrameRate]
                FRAME_RATE_25: _ClassVar[Capture.Start.Resi.FrameRate]
                FRAME_RATE_29_97: _ClassVar[Capture.Start.Resi.FrameRate]
                FRAME_RATE_30: _ClassVar[Capture.Start.Resi.FrameRate]
                FRAME_RATE_50: _ClassVar[Capture.Start.Resi.FrameRate]
                FRAME_RATE_59_94: _ClassVar[Capture.Start.Resi.FrameRate]
                FRAME_RATE_60: _ClassVar[Capture.Start.Resi.FrameRate]
            FRAME_RATE_UNKNOWN: Capture.Start.Resi.FrameRate
            FRAME_RATE_24: Capture.Start.Resi.FrameRate
            FRAME_RATE_25: Capture.Start.Resi.FrameRate
            FRAME_RATE_29_97: Capture.Start.Resi.FrameRate
            FRAME_RATE_30: Capture.Start.Resi.FrameRate
            FRAME_RATE_50: Capture.Start.Resi.FrameRate
            FRAME_RATE_59_94: Capture.Start.Resi.FrameRate
            FRAME_RATE_60: Capture.Start.Resi.FrameRate
            CODEC_FIELD_NUMBER: _ClassVar[int]
            FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
            RESOLUTION_FIELD_NUMBER: _ClassVar[int]
            STREAM_STARTED_FIELD_NUMBER: _ClassVar[int]
            VIDEO_BITRATE_FIELD_NUMBER: _ClassVar[int]
            codec: Capture.Start.Resi.Codec
            frame_rate: Capture.Start.Resi.FrameRate
            resolution: Capture.Resolution
            stream_started: bool
            video_bitrate: int
            def __init__(self, codec: _Optional[_Union[Capture.Start.Resi.Codec, str]] = ..., frame_rate: _Optional[_Union[Capture.Start.Resi.FrameRate, str]] = ..., resolution: _Optional[_Union[Capture.Resolution, _Mapping]] = ..., stream_started: bool = ..., video_bitrate: _Optional[int] = ...) -> None: ...
        RTMP_FIELD_NUMBER: _ClassVar[int]
        DISK_FIELD_NUMBER: _ClassVar[int]
        RESI_FIELD_NUMBER: _ClassVar[int]
        rtmp: Capture.Start.RTMP
        disk: Capture.Start.Disk
        resi: Capture.Start.Resi
        def __init__(self, rtmp: _Optional[_Union[Capture.Start.RTMP, _Mapping]] = ..., disk: _Optional[_Union[Capture.Start.Disk, _Mapping]] = ..., resi: _Optional[_Union[Capture.Start.Resi, _Mapping]] = ...) -> None: ...
    START_FIELD_NUMBER: _ClassVar[int]
    start: Capture.Start
    def __init__(self, start: _Optional[_Union[Capture.Start, _Mapping]] = ...) -> None: ...
