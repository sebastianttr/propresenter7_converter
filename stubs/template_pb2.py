# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: template.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import action_pb2 as action__pb2
import applicationInfo_pb2 as applicationInfo__pb2
import slide_pb2 as slide__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0etemplate.proto\x12\x07rv.data\x1a\x0c\x61\x63tion.proto\x1a\x15\x61pplicationInfo.proto\x1a\x0bslide.proto\"\xd0\x01\n\x08Template\x1a[\n\x05Slide\x12\"\n\nbase_slide\x18\x01 \x01(\x0b\x32\x0e.rv.data.Slide\x12\x0c\n\x04name\x18\x02 \x01(\t\x12 \n\x07\x61\x63tions\x18\x03 \x03(\x0b\x32\x0f.rv.data.Action\x1ag\n\x08\x44ocument\x12\x32\n\x10\x61pplication_info\x18\x01 \x01(\x0b\x32\x18.rv.data.ApplicationInfo\x12\'\n\x06slides\x18\x03 \x03(\x0b\x32\x17.rv.data.Template.Slideb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'template_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TEMPLATE']._serialized_start=78
  _globals['_TEMPLATE']._serialized_end=286
  _globals['_TEMPLATE_SLIDE']._serialized_start=90
  _globals['_TEMPLATE_SLIDE']._serialized_end=181
  _globals['_TEMPLATE_DOCUMENT']._serialized_start=183
  _globals['_TEMPLATE_DOCUMENT']._serialized_end=286
# @@protoc_insertion_point(module_scope)
