# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proCoreTestPatterns.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import testPattern_pb2 as testPattern__pb2
import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19proCoreTestPatterns.proto\x12\x07rv.data\x1a\x11testPattern.proto\x1a\nuuid.proto\"\xb0\x03\n\x12TestPatternRequest\x12\x45\n\x0fget_definitions\x18\x01 \x01(\x0b\x32*.rv.data.TestPatternRequest.GetDefinitionsH\x00\x12\x36\n\x11set_current_state\x18\x02 \x01(\x0b\x32\x19.rv.data.TestPatternStateH\x00\x12H\n\x11get_current_state\x18\x03 \x01(\x0b\x32+.rv.data.TestPatternRequest.GetCurrentStateH\x00\x12\x41\n\rget_thumbnail\x18\x04 \x01(\x0b\x32(.rv.data.TestPatternRequest.GetThumbnailH\x00\x1a\x10\n\x0eGetDefinitions\x1a\x11\n\x0fGetCurrentState\x1a^\n\x0cGetThumbnail\x12/\n\x07pattern\x18\x01 \x01(\x0b\x32\x1e.rv.data.TestPatternDefinition\x12\r\n\x05width\x18\x02 \x01(\x05\x12\x0e\n\x06height\x18\x03 \x01(\x05\x42\t\n\x07Request\"\xe8\x02\n\x13TestPatternResponse\x12\x46\n\x0fget_definitions\x18\x01 \x01(\x0b\x32+.rv.data.TestPatternResponse.GetDefinitionsH\x00\x12\x36\n\x11get_current_state\x18\x02 \x01(\x0b\x32\x19.rv.data.TestPatternStateH\x00\x12\x42\n\rget_thumbnail\x18\x03 \x01(\x0b\x32).rv.data.TestPatternResponse.GetThumbnailH\x00\x1a\x42\n\x0eGetDefinitions\x12\x30\n\x08patterns\x18\x01 \x03(\x0b\x32\x1e.rv.data.TestPatternDefinition\x1a=\n\x0cGetThumbnail\x12\x1e\n\x07pattern\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\r\n\x05image\x18\x02 \x01(\x0c\x42\n\n\x08Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proCoreTestPatterns_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TESTPATTERNREQUEST']._serialized_start=70
  _globals['_TESTPATTERNREQUEST']._serialized_end=502
  _globals['_TESTPATTERNREQUEST_GETDEFINITIONS']._serialized_start=360
  _globals['_TESTPATTERNREQUEST_GETDEFINITIONS']._serialized_end=376
  _globals['_TESTPATTERNREQUEST_GETCURRENTSTATE']._serialized_start=378
  _globals['_TESTPATTERNREQUEST_GETCURRENTSTATE']._serialized_end=395
  _globals['_TESTPATTERNREQUEST_GETTHUMBNAIL']._serialized_start=397
  _globals['_TESTPATTERNREQUEST_GETTHUMBNAIL']._serialized_end=491
  _globals['_TESTPATTERNRESPONSE']._serialized_start=505
  _globals['_TESTPATTERNRESPONSE']._serialized_end=865
  _globals['_TESTPATTERNRESPONSE_GETDEFINITIONS']._serialized_start=724
  _globals['_TESTPATTERNRESPONSE_GETDEFINITIONS']._serialized_end=790
  _globals['_TESTPATTERNRESPONSE_GETTHUMBNAIL']._serialized_start=792
  _globals['_TESTPATTERNRESPONSE_GETTHUMBNAIL']._serialized_end=853
# @@protoc_insertion_point(module_scope)