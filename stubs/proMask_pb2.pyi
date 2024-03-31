import slide_pb2 as _slide_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ProMask(_message.Message):
    __slots__ = ("base_slide", "name")
    BASE_SLIDE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    base_slide: _slide_pb2.Slide
    name: str
    def __init__(self, base_slide: _Optional[_Union[_slide_pb2.Slide, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class MaskCollection(_message.Message):
    __slots__ = ("collection",)
    COLLECTION_FIELD_NUMBER: _ClassVar[int]
    collection: _containers.RepeatedCompositeFieldContainer[ProMask]
    def __init__(self, collection: _Optional[_Iterable[_Union[ProMask, _Mapping]]] = ...) -> None: ...
