import graphicsData_pb2 as _graphicsData_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class IdentificationOverlay(_message.Message):
    __slots__ = ("screen_name", "outputs")
    class Output(_message.Message):
        __slots__ = ("x", "y", "width", "height", "name", "frame_rate")
        X_FIELD_NUMBER: _ClassVar[int]
        Y_FIELD_NUMBER: _ClassVar[int]
        WIDTH_FIELD_NUMBER: _ClassVar[int]
        HEIGHT_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        FRAME_RATE_FIELD_NUMBER: _ClassVar[int]
        x: int
        y: int
        width: int
        height: int
        name: str
        frame_rate: float
        def __init__(self, x: _Optional[int] = ..., y: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., name: _Optional[str] = ..., frame_rate: _Optional[float] = ...) -> None: ...
    SCREEN_NAME_FIELD_NUMBER: _ClassVar[int]
    OUTPUTS_FIELD_NUMBER: _ClassVar[int]
    screen_name: str
    outputs: _containers.RepeatedCompositeFieldContainer[IdentificationOverlay.Output]
    def __init__(self, screen_name: _Optional[str] = ..., outputs: _Optional[_Iterable[_Union[IdentificationOverlay.Output, _Mapping]]] = ...) -> None: ...

class LayerIdentificationOverlay(_message.Message):
    __slots__ = ("layer", "layer_name")
    class Layer(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        LAYER_VIDEO_INPUT: _ClassVar[LayerIdentificationOverlay.Layer]
        LAYER_MEDIA: _ClassVar[LayerIdentificationOverlay.Layer]
        LAYER_PRESENTATION: _ClassVar[LayerIdentificationOverlay.Layer]
        LAYER_ANNOUNCEMENTS: _ClassVar[LayerIdentificationOverlay.Layer]
        LAYER_PROPS: _ClassVar[LayerIdentificationOverlay.Layer]
        LAYER_MESSAGES: _ClassVar[LayerIdentificationOverlay.Layer]
    LAYER_VIDEO_INPUT: LayerIdentificationOverlay.Layer
    LAYER_MEDIA: LayerIdentificationOverlay.Layer
    LAYER_PRESENTATION: LayerIdentificationOverlay.Layer
    LAYER_ANNOUNCEMENTS: LayerIdentificationOverlay.Layer
    LAYER_PROPS: LayerIdentificationOverlay.Layer
    LAYER_MESSAGES: LayerIdentificationOverlay.Layer
    LAYER_FIELD_NUMBER: _ClassVar[int]
    LAYER_NAME_FIELD_NUMBER: _ClassVar[int]
    layer: LayerIdentificationOverlay.Layer
    layer_name: str
    def __init__(self, layer: _Optional[_Union[LayerIdentificationOverlay.Layer, str]] = ..., layer_name: _Optional[str] = ...) -> None: ...

class TextLayer(_message.Message):
    __slots__ = ("composite", "media", "cut_out", "background_effect")
    class Composite(_message.Message):
        __slots__ = ()
        def __init__(self) -> None: ...
    COMPOSITE_FIELD_NUMBER: _ClassVar[int]
    MEDIA_FIELD_NUMBER: _ClassVar[int]
    CUT_OUT_FIELD_NUMBER: _ClassVar[int]
    BACKGROUND_EFFECT_FIELD_NUMBER: _ClassVar[int]
    composite: TextLayer.Composite
    media: _graphicsData_pb2.Media
    cut_out: _graphicsData_pb2.Graphics.Text.CutOutFill
    background_effect: _graphicsData_pb2.Graphics.BackgroundEffect
    def __init__(self, composite: _Optional[_Union[TextLayer.Composite, _Mapping]] = ..., media: _Optional[_Union[_graphicsData_pb2.Media, _Mapping]] = ..., cut_out: _Optional[_Union[_graphicsData_pb2.Graphics.Text.CutOutFill, _Mapping]] = ..., background_effect: _Optional[_Union[_graphicsData_pb2.Graphics.BackgroundEffect, _Mapping]] = ...) -> None: ...
