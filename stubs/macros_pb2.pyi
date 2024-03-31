import action_pb2 as _action_pb2
import applicationInfo_pb2 as _applicationInfo_pb2
import color_pb2 as _color_pb2
import uuid_pb2 as _uuid_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MacrosDocument(_message.Message):
    __slots__ = ("application_info", "macros", "macro_collections")
    class Macro(_message.Message):
        __slots__ = ("uuid", "name", "color", "actions", "trigger_on_startup", "image_type", "image_data")
        class ImageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            ImageTypeDefault: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeOne: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeTwo: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeThree: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeFour: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeFive: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeSix: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeSeven: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeEight: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeNine: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeZero: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeArrow: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeAudio: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeBell: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeBulb: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeCloud: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeCupcake: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeExclamation: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeFlask: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeFlower: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeGlasses: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeHashtag: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeHat: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeHeart: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeMegaphone: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeMessage: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypePaperclip: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypePlay: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeSlide: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeStar: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeSun: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeSunglasses: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeTarget: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeTimer: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeVideoInput: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeXClear: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterA: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterB: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterC: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterD: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterE: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterF: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterG: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterH: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterI: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterJ: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterK: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterL: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterM: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterN: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterO: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterP: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterQ: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterR: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterS: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterT: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterU: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterV: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterW: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterX: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterY: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeLetterZ: _ClassVar[MacrosDocument.Macro.ImageType]
            ImageTypeCustom: _ClassVar[MacrosDocument.Macro.ImageType]
        ImageTypeDefault: MacrosDocument.Macro.ImageType
        ImageTypeOne: MacrosDocument.Macro.ImageType
        ImageTypeTwo: MacrosDocument.Macro.ImageType
        ImageTypeThree: MacrosDocument.Macro.ImageType
        ImageTypeFour: MacrosDocument.Macro.ImageType
        ImageTypeFive: MacrosDocument.Macro.ImageType
        ImageTypeSix: MacrosDocument.Macro.ImageType
        ImageTypeSeven: MacrosDocument.Macro.ImageType
        ImageTypeEight: MacrosDocument.Macro.ImageType
        ImageTypeNine: MacrosDocument.Macro.ImageType
        ImageTypeZero: MacrosDocument.Macro.ImageType
        ImageTypeArrow: MacrosDocument.Macro.ImageType
        ImageTypeAudio: MacrosDocument.Macro.ImageType
        ImageTypeBell: MacrosDocument.Macro.ImageType
        ImageTypeBulb: MacrosDocument.Macro.ImageType
        ImageTypeCloud: MacrosDocument.Macro.ImageType
        ImageTypeCupcake: MacrosDocument.Macro.ImageType
        ImageTypeExclamation: MacrosDocument.Macro.ImageType
        ImageTypeFlask: MacrosDocument.Macro.ImageType
        ImageTypeFlower: MacrosDocument.Macro.ImageType
        ImageTypeGlasses: MacrosDocument.Macro.ImageType
        ImageTypeHashtag: MacrosDocument.Macro.ImageType
        ImageTypeHat: MacrosDocument.Macro.ImageType
        ImageTypeHeart: MacrosDocument.Macro.ImageType
        ImageTypeMegaphone: MacrosDocument.Macro.ImageType
        ImageTypeMessage: MacrosDocument.Macro.ImageType
        ImageTypePaperclip: MacrosDocument.Macro.ImageType
        ImageTypePlay: MacrosDocument.Macro.ImageType
        ImageTypeSlide: MacrosDocument.Macro.ImageType
        ImageTypeStar: MacrosDocument.Macro.ImageType
        ImageTypeSun: MacrosDocument.Macro.ImageType
        ImageTypeSunglasses: MacrosDocument.Macro.ImageType
        ImageTypeTarget: MacrosDocument.Macro.ImageType
        ImageTypeTimer: MacrosDocument.Macro.ImageType
        ImageTypeVideoInput: MacrosDocument.Macro.ImageType
        ImageTypeXClear: MacrosDocument.Macro.ImageType
        ImageTypeLetterA: MacrosDocument.Macro.ImageType
        ImageTypeLetterB: MacrosDocument.Macro.ImageType
        ImageTypeLetterC: MacrosDocument.Macro.ImageType
        ImageTypeLetterD: MacrosDocument.Macro.ImageType
        ImageTypeLetterE: MacrosDocument.Macro.ImageType
        ImageTypeLetterF: MacrosDocument.Macro.ImageType
        ImageTypeLetterG: MacrosDocument.Macro.ImageType
        ImageTypeLetterH: MacrosDocument.Macro.ImageType
        ImageTypeLetterI: MacrosDocument.Macro.ImageType
        ImageTypeLetterJ: MacrosDocument.Macro.ImageType
        ImageTypeLetterK: MacrosDocument.Macro.ImageType
        ImageTypeLetterL: MacrosDocument.Macro.ImageType
        ImageTypeLetterM: MacrosDocument.Macro.ImageType
        ImageTypeLetterN: MacrosDocument.Macro.ImageType
        ImageTypeLetterO: MacrosDocument.Macro.ImageType
        ImageTypeLetterP: MacrosDocument.Macro.ImageType
        ImageTypeLetterQ: MacrosDocument.Macro.ImageType
        ImageTypeLetterR: MacrosDocument.Macro.ImageType
        ImageTypeLetterS: MacrosDocument.Macro.ImageType
        ImageTypeLetterT: MacrosDocument.Macro.ImageType
        ImageTypeLetterU: MacrosDocument.Macro.ImageType
        ImageTypeLetterV: MacrosDocument.Macro.ImageType
        ImageTypeLetterW: MacrosDocument.Macro.ImageType
        ImageTypeLetterX: MacrosDocument.Macro.ImageType
        ImageTypeLetterY: MacrosDocument.Macro.ImageType
        ImageTypeLetterZ: MacrosDocument.Macro.ImageType
        ImageTypeCustom: MacrosDocument.Macro.ImageType
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        COLOR_FIELD_NUMBER: _ClassVar[int]
        ACTIONS_FIELD_NUMBER: _ClassVar[int]
        TRIGGER_ON_STARTUP_FIELD_NUMBER: _ClassVar[int]
        IMAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
        IMAGE_DATA_FIELD_NUMBER: _ClassVar[int]
        uuid: _uuid_pb2.UUID
        name: str
        color: _color_pb2.Color
        actions: _containers.RepeatedCompositeFieldContainer[_action_pb2.Action]
        trigger_on_startup: bool
        image_type: MacrosDocument.Macro.ImageType
        image_data: bytes
        def __init__(self, uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., color: _Optional[_Union[_color_pb2.Color, _Mapping]] = ..., actions: _Optional[_Iterable[_Union[_action_pb2.Action, _Mapping]]] = ..., trigger_on_startup: bool = ..., image_type: _Optional[_Union[MacrosDocument.Macro.ImageType, str]] = ..., image_data: _Optional[bytes] = ...) -> None: ...
    class MacroCollection(_message.Message):
        __slots__ = ("uuid", "name", "items")
        class Item(_message.Message):
            __slots__ = ("macro_id",)
            MACRO_ID_FIELD_NUMBER: _ClassVar[int]
            macro_id: _uuid_pb2.UUID
            def __init__(self, macro_id: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ...) -> None: ...
        UUID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ITEMS_FIELD_NUMBER: _ClassVar[int]
        uuid: _uuid_pb2.UUID
        name: str
        items: _containers.RepeatedCompositeFieldContainer[MacrosDocument.MacroCollection.Item]
        def __init__(self, uuid: _Optional[_Union[_uuid_pb2.UUID, _Mapping]] = ..., name: _Optional[str] = ..., items: _Optional[_Iterable[_Union[MacrosDocument.MacroCollection.Item, _Mapping]]] = ...) -> None: ...
    APPLICATION_INFO_FIELD_NUMBER: _ClassVar[int]
    MACROS_FIELD_NUMBER: _ClassVar[int]
    MACRO_COLLECTIONS_FIELD_NUMBER: _ClassVar[int]
    application_info: _applicationInfo_pb2.ApplicationInfo
    macros: _containers.RepeatedCompositeFieldContainer[MacrosDocument.Macro]
    macro_collections: _containers.RepeatedCompositeFieldContainer[MacrosDocument.MacroCollection]
    def __init__(self, application_info: _Optional[_Union[_applicationInfo_pb2.ApplicationInfo, _Mapping]] = ..., macros: _Optional[_Iterable[_Union[MacrosDocument.Macro, _Mapping]]] = ..., macro_collections: _Optional[_Iterable[_Union[MacrosDocument.MacroCollection, _Mapping]]] = ...) -> None: ...
