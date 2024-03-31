from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Miscellaneous_Request(_message.Message):
    __slots__ = ("find_my_mouse",)
    class FindMyMouse(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    FIND_MY_MOUSE_FIELD_NUMBER: _ClassVar[int]
    find_my_mouse: API_v1_Miscellaneous_Request.FindMyMouse
    def __init__(self, find_my_mouse: _Optional[_Union[API_v1_Miscellaneous_Request.FindMyMouse, _Mapping]] = ...) -> None: ...

class API_v1_Miscellaneous_Response(_message.Message):
    __slots__ = ("find_my_mouse",)
    class FindMyMouse(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    FIND_MY_MOUSE_FIELD_NUMBER: _ClassVar[int]
    find_my_mouse: API_v1_Miscellaneous_Response.FindMyMouse
    def __init__(self, find_my_mouse: _Optional[_Union[API_v1_Miscellaneous_Response.FindMyMouse, _Mapping]] = ...) -> None: ...
