# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: templateIdentification.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1ctemplateIdentification.proto\x12\x07rv.data\x1a\nuuid.proto\"\x8f\x01\n\x16TemplateIdentification\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12!\n\nslide_uuid\x18\x03 \x01(\x0b\x32\r.rv.data.UUID\x12\x12\n\nslide_name\x18\x04 \x01(\t\x12\x13\n\x0bslide_index\x18\x05 \x01(\rb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'templateIdentification_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TEMPLATEIDENTIFICATION']._serialized_start=54
  _globals['_TEMPLATEIDENTIFICATION']._serialized_end=197
# @@protoc_insertion_point(module_scope)
