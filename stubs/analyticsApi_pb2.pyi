from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API(_message.Message):
    __slots__ = ("message_received",)
    class MessageReceived(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    MESSAGE_RECEIVED_FIELD_NUMBER: _ClassVar[int]
    message_received: API.MessageReceived
    def __init__(self, message_received: _Optional[_Union[API.MessageReceived, _Mapping]] = ...) -> None: ...
