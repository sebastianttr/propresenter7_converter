import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_Look(_message.Message):
    __slots__ = ("id", "screens")
    ID_FIELD_NUMBER: _ClassVar[int]
    SCREENS_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    screens: _containers.RepeatedCompositeFieldContainer[API_v1_Screen]
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., screens: _Optional[_Iterable[_Union[API_v1_Screen, _Mapping]]] = ...) -> None: ...

class API_v1_Screen(_message.Message):
    __slots__ = ("video_input", "media", "slide", "announcements", "props", "messages", "presentation", "mask")
    VIDEO_INPUT_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    SLIDE_FIELD_NUMBER: _ClassVar[int]
    ANNOUNCEMENTS_FIELD_NUMBER: _ClassVar[int]
    PROPS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    PRESENTATION_FIELD_NUMBER: _ClassVar[int]
    MASK_FIELD_NUMBER: _ClassVar[int]
    video_input: bool
    media: bool
    slide: bool
    announcements: bool
    props: bool
    messages: bool
    presentation: str
    mask: str
    def __init__(self, video_input: bool = ..., media: bool = ..., slide: bool = ..., announcements: bool = ..., props: bool = ..., messages: bool = ..., presentation: _Optional[str] = ..., mask: _Optional[str] = ...) -> None: ...

class API_v1_Looks_Request(_message.Message):
    __slots__ = ("looks", "create_look", "get_current_look", "put_current_look", "get_look", "put_look", "delete_look", "trigger_look")
    class Looks(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class CreateLook(_message.Message):
        __slots__ = ("look",)
        LOOK_FIELD_NUMBER: _ClassVar[int]
        look: API_v1_Look
        def __init__(self, look: _Optional[_Union[API_v1_Look, _Mapping]] = ...) -> None: ...
    class GetCurrentLook(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class PutCurrentLook(_message.Message):
        __slots__ = ("look",)
        LOOK_FIELD_NUMBER: _ClassVar[int]
        look: API_v1_Look
        def __init__(self, look: _Optional[_Union[API_v1_Look, _Mapping]] = ...) -> None: ...
    class GetLook(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PutLook(_message.Message):
        __slots__ = ("id", "look")
        ID_FIELD_NUMBER: _ClassVar[int]
        LOOK_FIELD_NUMBER: _ClassVar[int]
        id: str
        look: API_v1_Look
        def __init__(self, id: _Optional[str] = ..., look: _Optional[_Union[API_v1_Look, _Mapping]] = ...) -> None: ...
    class DeleteLook(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class TriggerLook(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    LOOKS_FIELD_NUMBER: _ClassVar[int]
    CREATE_LOOK_FIELD_NUMBER: _ClassVar[int]
    GET_CURRENT_LOOK_FIELD_NUMBER: _ClassVar[int]
    PUT_CURRENT_LOOK_FIELD_NUMBER: _ClassVar[int]
    GET_LOOK_FIELD_NUMBER: _ClassVar[int]
    PUT_LOOK_FIELD_NUMBER: _ClassVar[int]
    DELETE_LOOK_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_LOOK_FIELD_NUMBER: _ClassVar[int]
    looks: API_v1_Looks_Request.Looks
    create_look: API_v1_Looks_Request.CreateLook
    get_current_look: API_v1_Looks_Request.GetCurrentLook
    put_current_look: API_v1_Looks_Request.PutCurrentLook
    get_look: API_v1_Looks_Request.GetLook
    put_look: API_v1_Looks_Request.PutLook
    delete_look: API_v1_Looks_Request.DeleteLook
    trigger_look: API_v1_Looks_Request.TriggerLook
    def __init__(self, looks: _Optional[_Union[API_v1_Looks_Request.Looks, _Mapping]] = ..., create_look: _Optional[_Union[API_v1_Looks_Request.CreateLook, _Mapping]] = ..., get_current_look: _Optional[_Union[API_v1_Looks_Request.GetCurrentLook, _Mapping]] = ..., put_current_look: _Optional[_Union[API_v1_Looks_Request.PutCurrentLook, _Mapping]] = ..., get_look: _Optional[_Union[API_v1_Looks_Request.GetLook, _Mapping]] = ..., put_look: _Optional[_Union[API_v1_Looks_Request.PutLook, _Mapping]] = ..., delete_look: _Optional[_Union[API_v1_Looks_Request.DeleteLook, _Mapping]] = ..., trigger_look: _Optional[_Union[API_v1_Looks_Request.TriggerLook, _Mapping]] = ...) -> None: ...

class API_v1_Looks_Response(_message.Message):
    __slots__ = ("looks", "create_look", "get_current_look", "put_current_look", "get_look", "put_look", "delete_look", "trigger_look")
    class Looks(_message.Message):
        __slots__ = ("looks",)
        LOOKS_FIELD_NUMBER: _ClassVar[int]
        looks: _containers.RepeatedCompositeFieldContainer[API_v1_Look]
        def __init__(self, looks: _Optional[_Iterable[_Union[API_v1_Look, _Mapping]]] = ...) -> None: ...
    class CreateLook(_message.Message):
        __slots__ = ("look",)
        LOOK_FIELD_NUMBER: _ClassVar[int]
        look: API_v1_Look
        def __init__(self, look: _Optional[_Union[API_v1_Look, _Mapping]] = ...) -> None: ...
    class GetCurrentLook(_message.Message):
        __slots__ = ("look",)
        LOOK_FIELD_NUMBER: _ClassVar[int]
        look: API_v1_Look
        def __init__(self, look: _Optional[_Union[API_v1_Look, _Mapping]] = ...) -> None: ...
    class PutCurrentLook(_message.Message):
        __slots__ = ("look",)
        LOOK_FIELD_NUMBER: _ClassVar[int]
        look: API_v1_Look
        def __init__(self, look: _Optional[_Union[API_v1_Look, _Mapping]] = ...) -> None: ...
    class GetLook(_message.Message):
        __slots__ = ("look",)
        LOOK_FIELD_NUMBER: _ClassVar[int]
        look: API_v1_Look
        def __init__(self, look: _Optional[_Union[API_v1_Look, _Mapping]] = ...) -> None: ...
    class PutLook(_message.Message):
        __slots__ = ("look",)
        LOOK_FIELD_NUMBER: _ClassVar[int]
        look: API_v1_Look
        def __init__(self, look: _Optional[_Union[API_v1_Look, _Mapping]] = ...) -> None: ...
    class DeleteLook(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class TriggerLook(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    LOOKS_FIELD_NUMBER: _ClassVar[int]
    CREATE_LOOK_FIELD_NUMBER: _ClassVar[int]
    GET_CURRENT_LOOK_FIELD_NUMBER: _ClassVar[int]
    PUT_CURRENT_LOOK_FIELD_NUMBER: _ClassVar[int]
    GET_LOOK_FIELD_NUMBER: _ClassVar[int]
    PUT_LOOK_FIELD_NUMBER: _ClassVar[int]
    DELETE_LOOK_FIELD_NUMBER: _ClassVar[int]
    TRIGGER_LOOK_FIELD_NUMBER: _ClassVar[int]
    looks: API_v1_Looks_Response.Looks
    create_look: API_v1_Looks_Response.CreateLook
    get_current_look: API_v1_Looks_Response.GetCurrentLook
    put_current_look: API_v1_Looks_Response.PutCurrentLook
    get_look: API_v1_Looks_Response.GetLook
    put_look: API_v1_Looks_Response.PutLook
    delete_look: API_v1_Looks_Response.DeleteLook
    trigger_look: API_v1_Looks_Response.TriggerLook
    def __init__(self, looks: _Optional[_Union[API_v1_Looks_Response.Looks, _Mapping]] = ..., create_look: _Optional[_Union[API_v1_Looks_Response.CreateLook, _Mapping]] = ..., get_current_look: _Optional[_Union[API_v1_Looks_Response.GetCurrentLook, _Mapping]] = ..., put_current_look: _Optional[_Union[API_v1_Looks_Response.PutCurrentLook, _Mapping]] = ..., get_look: _Optional[_Union[API_v1_Looks_Response.GetLook, _Mapping]] = ..., put_look: _Optional[_Union[API_v1_Looks_Response.PutLook, _Mapping]] = ..., delete_look: _Optional[_Union[API_v1_Looks_Response.DeleteLook, _Mapping]] = ..., trigger_look: _Optional[_Union[API_v1_Looks_Response.TriggerLook, _Mapping]] = ...) -> None: ...
