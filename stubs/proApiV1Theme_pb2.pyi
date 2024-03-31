import proApiV1Color_pb2 as _proApiV1Color_pb2
import proApiV1Identifier_pb2 as _proApiV1Identifier_pb2
import proApiV1Size_pb2 as _proApiV1Size_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class API_v1_ThemeGroup(_message.Message):
    __slots__ = ("id", "groups", "themes")
    ID_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    THEMES_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    groups: _containers.RepeatedCompositeFieldContainer[API_v1_ThemeGroup]
    themes: _containers.RepeatedCompositeFieldContainer[API_v1_Theme]
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., groups: _Optional[_Iterable[_Union[API_v1_ThemeGroup, _Mapping]]] = ..., themes: _Optional[_Iterable[_Union[API_v1_Theme, _Mapping]]] = ...) -> None: ...

class API_v1_Theme(_message.Message):
    __slots__ = ("id", "slides")
    ID_FIELD_NUMBER: _ClassVar[int]
    SLIDES_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    slides: _containers.RepeatedCompositeFieldContainer[API_v1_ThemeSlide]
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., slides: _Optional[_Iterable[_Union[API_v1_ThemeSlide, _Mapping]]] = ...) -> None: ...

class API_v1_ThemeSlide(_message.Message):
    __slots__ = ("id", "size", "background")
    ID_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_FIELD_NUMBER: _ClassVar[int]
    id: _proApiV1Identifier_pb2.API_v1_Identifier
    size: _proApiV1Size_pb2.API_v1_Size
    background: _proApiV1Color_pb2.API_v1_Color
    def __init__(self, id: _Optional[_Union[_proApiV1Identifier_pb2.API_v1_Identifier, _Mapping]] = ..., size: _Optional[_Union[_proApiV1Size_pb2.API_v1_Size, _Mapping]] = ..., background: _Optional[_Union[_proApiV1Color_pb2.API_v1_Color, _Mapping]] = ...) -> None: ...

class API_v1_Theme_Request(_message.Message):
    __slots__ = ("get_all", "get_theme", "delete_theme", "get_theme_name", "put_theme_name", "get_theme_slide", "put_theme_slide", "delete_theme_slide", "get_theme_slide_thumbnail")
    class GetAll(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetTheme(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class DeleteTheme(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class GetThemeName(_message.Message):
        __slots__ = ("id",)
        ID_FIELD_NUMBER: _ClassVar[int]
        id: str
        def __init__(self, id: _Optional[str] = ...) -> None: ...
    class PutThemeName(_message.Message):
        __slots__ = ("id", "name")
        ID_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        id: str
        name: str
        def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...
    class GetThemeSlide(_message.Message):
        __slots__ = ("id", "theme_slide")
        ID_FIELD_NUMBER: _ClassVar[int]
        THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        id: str
        theme_slide: str
        def __init__(self, id: _Optional[str] = ..., theme_slide: _Optional[str] = ...) -> None: ...
    class PutThemeSlide(_message.Message):
        __slots__ = ("id", "theme_slide", "slide")
        ID_FIELD_NUMBER: _ClassVar[int]
        THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        SLIDE_FIELD_NUMBER: _ClassVar[int]
        id: str
        theme_slide: str
        slide: API_v1_ThemeSlide
        def __init__(self, id: _Optional[str] = ..., theme_slide: _Optional[str] = ..., slide: _Optional[_Union[API_v1_ThemeSlide, _Mapping]] = ...) -> None: ...
    class DeleteThemeSlide(_message.Message):
        __slots__ = ("id", "theme_slide")
        ID_FIELD_NUMBER: _ClassVar[int]
        THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        id: str
        theme_slide: str
        def __init__(self, id: _Optional[str] = ..., theme_slide: _Optional[str] = ...) -> None: ...
    class GetThemeSlideThumbnail(_message.Message):
        __slots__ = ("id", "theme_slide", "quality")
        ID_FIELD_NUMBER: _ClassVar[int]
        THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        QUALITY_FIELD_NUMBER: _ClassVar[int]
        id: str
        theme_slide: str
        quality: int
        def __init__(self, id: _Optional[str] = ..., theme_slide: _Optional[str] = ..., quality: _Optional[int] = ...) -> None: ...
    GET_ALL_FIELD_NUMBER: _ClassVar[int]
    GET_THEME_FIELD_NUMBER: _ClassVar[int]
    DELETE_THEME_FIELD_NUMBER: _ClassVar[int]
    GET_THEME_NAME_FIELD_NUMBER: _ClassVar[int]
    PUT_THEME_NAME_FIELD_NUMBER: _ClassVar[int]
    GET_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
    PUT_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
    DELETE_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
    GET_THEME_SLIDE_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    get_all: API_v1_Theme_Request.GetAll
    get_theme: API_v1_Theme_Request.GetTheme
    delete_theme: API_v1_Theme_Request.DeleteTheme
    get_theme_name: API_v1_Theme_Request.GetThemeName
    put_theme_name: API_v1_Theme_Request.PutThemeName
    get_theme_slide: API_v1_Theme_Request.GetThemeSlide
    put_theme_slide: API_v1_Theme_Request.PutThemeSlide
    delete_theme_slide: API_v1_Theme_Request.DeleteThemeSlide
    get_theme_slide_thumbnail: API_v1_Theme_Request.GetThemeSlideThumbnail
    def __init__(self, get_all: _Optional[_Union[API_v1_Theme_Request.GetAll, _Mapping]] = ..., get_theme: _Optional[_Union[API_v1_Theme_Request.GetTheme, _Mapping]] = ..., delete_theme: _Optional[_Union[API_v1_Theme_Request.DeleteTheme, _Mapping]] = ..., get_theme_name: _Optional[_Union[API_v1_Theme_Request.GetThemeName, _Mapping]] = ..., put_theme_name: _Optional[_Union[API_v1_Theme_Request.PutThemeName, _Mapping]] = ..., get_theme_slide: _Optional[_Union[API_v1_Theme_Request.GetThemeSlide, _Mapping]] = ..., put_theme_slide: _Optional[_Union[API_v1_Theme_Request.PutThemeSlide, _Mapping]] = ..., delete_theme_slide: _Optional[_Union[API_v1_Theme_Request.DeleteThemeSlide, _Mapping]] = ..., get_theme_slide_thumbnail: _Optional[_Union[API_v1_Theme_Request.GetThemeSlideThumbnail, _Mapping]] = ...) -> None: ...

class API_v1_Theme_Response(_message.Message):
    __slots__ = ("get_all", "get_theme", "delete_theme", "get_theme_name", "put_theme_name", "get_theme_slide", "put_theme_slide", "delete_theme_slide", "get_theme_slide_thumbnail")
    class GetAll(_message.Message):
        __slots__ = ("groups", "themes")
        GROUPS_FIELD_NUMBER: _ClassVar[int]
        THEMES_FIELD_NUMBER: _ClassVar[int]
        groups: _containers.RepeatedCompositeFieldContainer[API_v1_ThemeGroup]
        themes: _containers.RepeatedCompositeFieldContainer[API_v1_Theme]
        def __init__(self, groups: _Optional[_Iterable[_Union[API_v1_ThemeGroup, _Mapping]]] = ..., themes: _Optional[_Iterable[_Union[API_v1_Theme, _Mapping]]] = ...) -> None: ...
    class GetTheme(_message.Message):
        __slots__ = ("theme", "group")
        THEME_FIELD_NUMBER: _ClassVar[int]
        GROUP_FIELD_NUMBER: _ClassVar[int]
        theme: API_v1_Theme
        group: API_v1_ThemeGroup
        def __init__(self, theme: _Optional[_Union[API_v1_Theme, _Mapping]] = ..., group: _Optional[_Union[API_v1_ThemeGroup, _Mapping]] = ...) -> None: ...
    class DeleteTheme(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetThemeName(_message.Message):
        __slots__ = ("name",)
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class PutThemeName(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetThemeSlide(_message.Message):
        __slots__ = ("theme_slide",)
        THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
        theme_slide: API_v1_ThemeSlide
        def __init__(self, theme_slide: _Optional[_Union[API_v1_ThemeSlide, _Mapping]] = ...) -> None: ...
    class PutThemeSlide(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class DeleteThemeSlide(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    class GetThemeSlideThumbnail(_message.Message):
        __slots__ = ("data",)
        DATA_FIELD_NUMBER: _ClassVar[int]
        data: bytes
        def __init__(self, data: _Optional[bytes] = ...) -> None: ...
    GET_ALL_FIELD_NUMBER: _ClassVar[int]
    GET_THEME_FIELD_NUMBER: _ClassVar[int]
    DELETE_THEME_FIELD_NUMBER: _ClassVar[int]
    GET_THEME_NAME_FIELD_NUMBER: _ClassVar[int]
    PUT_THEME_NAME_FIELD_NUMBER: _ClassVar[int]
    GET_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
    PUT_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
    DELETE_THEME_SLIDE_FIELD_NUMBER: _ClassVar[int]
    GET_THEME_SLIDE_THUMBNAIL_FIELD_NUMBER: _ClassVar[int]
    get_all: API_v1_Theme_Response.GetAll
    get_theme: API_v1_Theme_Response.GetTheme
    delete_theme: API_v1_Theme_Response.DeleteTheme
    get_theme_name: API_v1_Theme_Response.GetThemeName
    put_theme_name: API_v1_Theme_Response.PutThemeName
    get_theme_slide: API_v1_Theme_Response.GetThemeSlide
    put_theme_slide: API_v1_Theme_Response.PutThemeSlide
    delete_theme_slide: API_v1_Theme_Response.DeleteThemeSlide
    get_theme_slide_thumbnail: API_v1_Theme_Response.GetThemeSlideThumbnail
    def __init__(self, get_all: _Optional[_Union[API_v1_Theme_Response.GetAll, _Mapping]] = ..., get_theme: _Optional[_Union[API_v1_Theme_Response.GetTheme, _Mapping]] = ..., delete_theme: _Optional[_Union[API_v1_Theme_Response.DeleteTheme, _Mapping]] = ..., get_theme_name: _Optional[_Union[API_v1_Theme_Response.GetThemeName, _Mapping]] = ..., put_theme_name: _Optional[_Union[API_v1_Theme_Response.PutThemeName, _Mapping]] = ..., get_theme_slide: _Optional[_Union[API_v1_Theme_Response.GetThemeSlide, _Mapping]] = ..., put_theme_slide: _Optional[_Union[API_v1_Theme_Response.PutThemeSlide, _Mapping]] = ..., delete_theme_slide: _Optional[_Union[API_v1_Theme_Response.DeleteThemeSlide, _Mapping]] = ..., get_theme_slide_thumbnail: _Optional[_Union[API_v1_Theme_Response.GetThemeSlideThumbnail, _Mapping]] = ...) -> None: ...
