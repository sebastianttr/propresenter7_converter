from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WHMStore(_message.Message):
    __slots__ = ("view_store", "download")
    class ViewStore(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Download(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    VIEW_STORE_FIELD_NUMBER: _ClassVar[int]
    DOWNLOAD_FIELD_NUMBER: _ClassVar[int]
    view_store: WHMStore.ViewStore
    download: WHMStore.Download
    def __init__(self, view_store: _Optional[_Union[WHMStore.ViewStore, _Mapping]] = ..., download: _Optional[_Union[WHMStore.Download, _Mapping]] = ...) -> None: ...
