import url_pb2 as _url_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FileProperties(_message.Message):
    __slots__ = ("local_url", "remote_properties")
    class RemoteProperties(_message.Message):
        __slots__ = ("procontent",)
        class ProContent(_message.Message):
            __slots__ = ("download_identifier",)
            DOWNLOAD_IDENTIFIER_FIELD_NUMBER: _ClassVar[int]
            download_identifier: str
            def __init__(self, download_identifier: _Optional[str] = ...) -> None: ...
        PROCONTENT_FIELD_NUMBER: _ClassVar[int]
        procontent: FileProperties.RemoteProperties.ProContent
        def __init__(self, procontent: _Optional[_Union[FileProperties.RemoteProperties.ProContent, _Mapping]] = ...) -> None: ...
    LOCAL_URL_FIELD_NUMBER: _ClassVar[int]
    REMOTE_PROPERTIES_FIELD_NUMBER: _ClassVar[int]
    local_url: _url_pb2.URL
    remote_properties: FileProperties.RemoteProperties
    def __init__(self, local_url: _Optional[_Union[_url_pb2.URL, _Mapping]] = ..., remote_properties: _Optional[_Union[FileProperties.RemoteProperties, _Mapping]] = ...) -> None: ...
