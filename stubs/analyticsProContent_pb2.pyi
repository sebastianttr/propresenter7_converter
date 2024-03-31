from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProContent(_message.Message):
    __slots__ = ("media_bin", "download")
    class ViewMediaBin(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Download(_message.Message):
        __slots__ = ("is_retry",)
        IS_RETRY_FIELD_NUMBER: _ClassVar[int]
        is_retry: bool
        def __init__(self, is_retry: bool = ...) -> None: ...
    MEDIA_BIN_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    media_bin: ProContent.ViewMediaBin
    download: ProContent.Download
    def __init__(self, media_bin: _Optional[_Union[ProContent.ViewMediaBin, _Mapping]] = ..., download: _Optional[_Union[ProContent.Download, _Mapping]] = ...) -> None: ...
