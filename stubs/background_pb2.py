# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: background.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import color_pb2 as color__pb2
import graphicsData_pb2 as graphicsData__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10\x62\x61\x63kground.proto\x12\x07rv.data\x1a\x0b\x63olor.proto\x1a\x12graphicsData.proto\"y\n\nBackground\x12\x12\n\nis_enabled\x18\x03 \x01(\x08\x12\x1f\n\x05\x63olor\x18\x01 \x01(\x0b\x32\x0e.rv.data.ColorH\x00\x12.\n\x08gradient\x18\x02 \x01(\x0b\x32\x1a.rv.data.Graphics.GradientH\x00\x42\x06\n\x04\x46illb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'background_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_BACKGROUND']._serialized_start=62
  _globals['_BACKGROUND']._serialized_end=183
# @@protoc_insertion_point(module_scope)
