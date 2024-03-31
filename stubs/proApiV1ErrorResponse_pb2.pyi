from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Error_Response(_message.Message):
    __slots__ = ("error",)
    class API_v1_Error_Type(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        NOT_FOUND: _ClassVar[API_v1_Error_Response.API_v1_Error_Type]
        BAD_REQUEST: _ClassVar[API_v1_Error_Response.API_v1_Error_Type]
        INTERNAL_ERROR: _ClassVar[API_v1_Error_Response.API_v1_Error_Type]
        UNAUTHORIZED: _ClassVar[API_v1_Error_Response.API_v1_Error_Type]
    NOT_FOUND: API_v1_Error_Response.API_v1_Error_Type
    BAD_REQUEST: API_v1_Error_Response.API_v1_Error_Type
    INTERNAL_ERROR: API_v1_Error_Response.API_v1_Error_Type
    UNAUTHORIZED: API_v1_Error_Response.API_v1_Error_Type
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: API_v1_Error_Response.API_v1_Error_Type
    def __init__(self, error: _Optional[_Union[API_v1_Error_Response.API_v1_Error_Type, str]] = ...) -> None: ...
