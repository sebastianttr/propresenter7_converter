import uuid_pb2 as _uuid_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CollectionElementType(_message.Message):
    __slots__ = ("parameter_uuid", "parameter_name", "parent_collection")
    PARAMETER_UUID_FIELD_NUMBER: _ClassVar[int]
    PARAMETER_NAME_FIELD_NUMBER: _ClassVar[int]
    PARENT_COLLECTION_FIELD_NUMBER: _ClassVar[int]
    parameter_uuid: _uuid_pb2.UUID
    parameter_name: str
    parent_collection: CollectionElementType
    def __init__(self, parameter_uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., parameter_name: _Optional[str] = ..., parent_collection: _Optional[_Union[CollectionElementType, _Mapping]] = ...) -> None: ...
