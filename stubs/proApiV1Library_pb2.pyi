import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Library_Request(_message.Message):
    __slots__ = ("libraries", "library", "trigger")
    class Libraries(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class Library(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class Trigger(_message.Message):
        __slots__ = ("library_id", "presentation_id", "index")
        LIBRARY_ID_FIELD_NUMBER: _ClassVar[int]
        PRESENTATION_ID_FIELD_NUMBER: _ClassVar[int]
        INDEX_FIELD_NUMBER: _ClassVar[int]
        library_id: str
        presentation_id: str
        index: int
        def __init__(self, library_id: _Optional[str] = ..., presentation_id: _Optional[str] = ..., index: _Optional[int] = ...) -> None: ...
    LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_FIELD_NUMBER: _ClassVar[int]
    libraries: API_v1_Library_Request.Libraries
    library: API_v1_Library_Request.Library
    trigger: API_v1_Library_Request.Trigger
    def __init__(self, libraries: _Optional[_Union[API_v1_Library_Request.Libraries, _Mapping]] = ..., library: _Optional[_Union[API_v1_Library_Request.Library, _Mapping]] = ..., trigger: _Optional[_Union[API_v1_Library_Request.Trigger, _Mapping]] = ...) -> None: ...

class API_v1_Library_Response(_message.Message):
    __slots__ = ("libraries", "library", "triggger")
    class Libraries(_message.Message):
        __slots__ = ("libraries",)
        LIBRARIES_FIELD_NUMBER: _ClassVar[int]
        libraries: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        def __init__(self, libraries: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
    class Library(_message.Message):
        __slots__ = ("update_type", "items")
        class UpdateType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            all: _ClassVar[API_v1_Library_Response.Library.UpdateType]
            add: _ClassVar[API_v1_Library_Response.Library.UpdateType]
            remove: _ClassVar[API_v1_Library_Response.Library.UpdateType]
        all: API_v1_Library_Response.Library.UpdateType
        add: API_v1_Library_Response.Library.UpdateType
        remove: API_v1_Library_Response.Library.UpdateType
        UPDATE_TYPE_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        update_type: API_v1_Library_Response.Library.UpdateType
        items: _containers.RepeatedCompositeFieldContainer[_proApiV1Identifier_pb2.API_v1_Identifier]
        def __init__(self, update_type: _Optional[_Union[API_v1_Library_Response.Library.UpdateType, str]] = ..., items: _Optional[_Iterable[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]]] = ...) -> None: ...
    class Trigger(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    LIBRARIES_FIELD_NUMBER: _ClassVar[int]
    LIBRARY_FIELD_NUMBER: _ClassVar[int]
    TRIGGGER_FIELD_NUMBER: _ClassVar[int]
    libraries: API_v1_Library_Response.Libraries
    library: API_v1_Library_Response.Library
    triggger: API_v1_Library_Response.Trigger
    def __init__(self, libraries: _Optional[_Union[API_v1_Library_Response.Libraries, _Mapping]] = ..., library: _Optional[_Union[API_v1_Library_Response.Library, _Mapping]] = ..., triggger: _Optional[_Union[API_v1_Library_Response.Trigger, _Mapping]] = ...) -> None: ...
