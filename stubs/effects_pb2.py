# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: effects.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import color_pb2 as color__pb2
import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\reffects.proto\x12\x07rv.data\x1a\x0b\x63olor.proto\x1a\nuuid.proto\"\xe7\x0b\n\x06\x45\x66\x66\x65\x63t\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0f\n\x07\x65nabled\x18\x02 \x01(\x08\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x11\n\trender_id\x18\x04 \x01(\t\x12\x1c\n\x14\x62\x65havior_description\x18\x05 \x01(\t\x12\x10\n\x08\x63\x61tegory\x18\x06 \x01(\t\x12\x31\n\tvariables\x18\x07 \x03(\x0b\x32\x1e.rv.data.Effect.EffectVariable\x1a\xd3\t\n\x0e\x45\x66\x66\x65\x63tVariable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x37\n\x03int\x18\x03 \x01(\x0b\x32(.rv.data.Effect.EffectVariable.EffectIntH\x00\x12;\n\x05\x66loat\x18\x04 \x01(\x0b\x32*.rv.data.Effect.EffectVariable.EffectFloatH\x00\x12;\n\x05\x63olor\x18\x05 \x01(\x0b\x32*.rv.data.Effect.EffectVariable.EffectColorH\x00\x12\x43\n\tdirection\x18\x06 \x01(\x0b\x32..rv.data.Effect.EffectVariable.EffectDirectionH\x00\x12=\n\x06\x64ouble\x18\x07 \x01(\x0b\x32+.rv.data.Effect.EffectVariable.EffectDoubleH\x00\x1aK\n\tEffectInt\x12\r\n\x05value\x18\x01 \x01(\x05\x12\x15\n\rdefault_value\x18\x02 \x01(\x05\x12\x0b\n\x03min\x18\x03 \x01(\x05\x12\x0b\n\x03max\x18\x04 \x01(\x05\x1aM\n\x0b\x45\x66\x66\x65\x63tFloat\x12\r\n\x05value\x18\x01 \x01(\x02\x12\x15\n\rdefault_value\x18\x02 \x01(\x02\x12\x0b\n\x03min\x18\x03 \x01(\x02\x12\x0b\n\x03max\x18\x04 \x01(\x02\x1aN\n\x0c\x45\x66\x66\x65\x63tDouble\x12\r\n\x05value\x18\x01 \x01(\x01\x12\x15\n\rdefault_value\x18\x02 \x01(\x01\x12\x0b\n\x03min\x18\x03 \x01(\x01\x12\x0b\n\x03max\x18\x04 \x01(\x01\x1aS\n\x0b\x45\x66\x66\x65\x63tColor\x12\x1d\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x0e.rv.data.Color\x12%\n\rdefault_color\x18\x02 \x01(\x0b\x32\x0e.rv.data.Color\x1a\x9d\x04\n\x0f\x45\x66\x66\x65\x63tDirection\x12Q\n\tdirection\x18\x01 \x01(\x0e\x32>.rv.data.Effect.EffectVariable.EffectDirection.EffectDirection\x12Y\n\x11\x64\x65\x66\x61ult_direction\x18\x02 \x01(\x0e\x32>.rv.data.Effect.EffectVariable.EffectDirection.EffectDirection\x12\x1c\n\x14\x61vailable_directions\x18\x03 \x01(\r\"\xbd\x02\n\x0f\x45\x66\x66\x65\x63tDirection\x12\x19\n\x15\x45\x46\x46\x45\x43T_DIRECTION_NONE\x10\x00\x12\x1d\n\x19\x45\x46\x46\x45\x43T_DIRECTION_TOP_LEFT\x10\x01\x12\x18\n\x14\x45\x46\x46\x45\x43T_DIRECTION_TOP\x10\x02\x12\x1e\n\x1a\x45\x46\x46\x45\x43T_DIRECTION_TOP_RIGHT\x10\x04\x12\x19\n\x15\x45\x46\x46\x45\x43T_DIRECTION_LEFT\x10\x08\x12\x1b\n\x17\x45\x46\x46\x45\x43T_DIRECTION_CENTER\x10\x10\x12\x1a\n\x16\x45\x46\x46\x45\x43T_DIRECTION_RIGHT\x10 \x12 \n\x1c\x45\x46\x46\x45\x43T_DIRECTION_BOTTOM_LEFT\x10@\x12\x1c\n\x17\x45\x46\x46\x45\x43T_DIRECTION_BOTTOM\x10\x80\x01\x12\"\n\x1d\x45\x46\x46\x45\x43T_DIRECTION_BOTTOM_RIGHT\x10\x80\x02\x42\x06\n\x04Type\x1aU\n\x06Preset\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12 \n\x07\x65\x66\x66\x65\x63ts\x18\x03 \x03(\x0b\x32\x0f.rv.data.Effect\"\xc3\x01\n\nTransition\x12\x10\n\x08\x64uration\x18\x01 \x01(\x01\x12$\n\rfavorite_uuid\x18\x02 \x01(\x0b\x32\r.rv.data.UUID\x12\x1f\n\x06\x65\x66\x66\x65\x63t\x18\x03 \x01(\x0b\x32\x0f.rv.data.Effect\x1a\\\n\x06Preset\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\ntransition\x18\x03 \x01(\x0b\x32\x13.rv.data.Transitionb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'effects_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_EFFECT']._serialized_start=52
  _globals['_EFFECT']._serialized_end=1563
  _globals['_EFFECT_EFFECTVARIABLE']._serialized_start=241
  _globals['_EFFECT_EFFECTVARIABLE']._serialized_end=1476
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTINT']._serialized_start=605
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTINT']._serialized_end=680
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTFLOAT']._serialized_start=682
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTFLOAT']._serialized_end=759
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTDOUBLE']._serialized_start=761
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTDOUBLE']._serialized_end=839
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTCOLOR']._serialized_start=841
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTCOLOR']._serialized_end=924
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTDIRECTION']._serialized_start=927
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTDIRECTION']._serialized_end=1468
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTDIRECTION_EFFECTDIRECTION']._serialized_start=1151
  _globals['_EFFECT_EFFECTVARIABLE_EFFECTDIRECTION_EFFECTDIRECTION']._serialized_end=1468
  _globals['_EFFECT_PRESET']._serialized_start=1478
  _globals['_EFFECT_PRESET']._serialized_end=1563
  _globals['_TRANSITION']._serialized_start=1566
  _globals['_TRANSITION']._serialized_end=1761
  _globals['_TRANSITION_PRESET']._serialized_start=1669
  _globals['_TRANSITION_PRESET']._serialized_end=1761
# @@protoc_insertion_point(module_scope)
