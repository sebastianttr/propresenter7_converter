# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proApiV1Library.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proApiV1Identifier_pb2 as proApiV1Identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proApiV1Library.proto\x12\x07rv.data\x1a\x18proApiV1Identifier.proto\"\xc6\x02\n\x16\x41PI_v1_Library_Request\x12>\n\tlibraries\x18\x01 \x01(\x0b\x32).rv.data.API_v1_Library_Request.LibrariesH\x00\x12:\n\x07library\x18\x02 \x01(\x0b\x32\'.rv.data.API_v1_Library_Request.LibraryH\x00\x12:\n\x07trigger\x18\x03 \x01(\x0b\x32\'.rv.data.API_v1_Library_Request.TriggerH\x00\x1a\x0b\n\tLibraries\x1a\x15\n\x07Library\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x45\n\x07Trigger\x12\x12\n\nlibrary_id\x18\x01 \x01(\t\x12\x17\n\x0fpresentation_id\x18\x02 \x01(\t\x12\r\n\x05index\x18\x03 \x01(\rB\t\n\x07Request\"\xd5\x03\n\x17\x41PI_v1_Library_Response\x12?\n\tlibraries\x18\x01 \x01(\x0b\x32*.rv.data.API_v1_Library_Response.LibrariesH\x00\x12;\n\x07library\x18\x02 \x01(\x0b\x32(.rv.data.API_v1_Library_Response.LibraryH\x00\x12<\n\x08triggger\x18\x03 \x01(\x0b\x32(.rv.data.API_v1_Library_Response.TriggerH\x00\x1a:\n\tLibraries\x12-\n\tlibraries\x18\x01 \x03(\x0b\x32\x1a.rv.data.API_v1_Identifier\x1a\xaa\x01\n\x07Library\x12H\n\x0bupdate_type\x18\x01 \x01(\x0e\x32\x33.rv.data.API_v1_Library_Response.Library.UpdateType\x12)\n\x05items\x18\x02 \x03(\x0b\x32\x1a.rv.data.API_v1_Identifier\"*\n\nUpdateType\x12\x07\n\x03\x61ll\x10\x00\x12\x07\n\x03\x61\x64\x64\x10\x01\x12\n\n\x06remove\x10\x02\x1a\t\n\x07TriggerB\n\n\x08Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Library_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_API_V1_LIBRARY_REQUEST']._serialized_start=61
  _globals['_API_V1_LIBRARY_REQUEST']._serialized_end=387
  _globals['_API_V1_LIBRARY_REQUEST_LIBRARIES']._serialized_start=271
  _globals['_API_V1_LIBRARY_REQUEST_LIBRARIES']._serialized_end=282
  _globals['_API_V1_LIBRARY_REQUEST_LIBRARY']._serialized_start=284
  _globals['_API_V1_LIBRARY_REQUEST_LIBRARY']._serialized_end=305
  _globals['_API_V1_LIBRARY_REQUEST_TRIGGER']._serialized_start=307
  _globals['_API_V1_LIBRARY_REQUEST_TRIGGER']._serialized_end=376
  _globals['_API_V1_LIBRARY_RESPONSE']._serialized_start=390
  _globals['_API_V1_LIBRARY_RESPONSE']._serialized_end=859
  _globals['_API_V1_LIBRARY_RESPONSE_LIBRARIES']._serialized_start=605
  _globals['_API_V1_LIBRARY_RESPONSE_LIBRARIES']._serialized_end=663
  _globals['_API_V1_LIBRARY_RESPONSE_LIBRARY']._serialized_start=666
  _globals['_API_V1_LIBRARY_RESPONSE_LIBRARY']._serialized_end=836
  _globals['_API_V1_LIBRARY_RESPONSE_LIBRARY_UPDATETYPE']._serialized_start=794
  _globals['_API_V1_LIBRARY_RESPONSE_LIBRARY_UPDATETYPE']._serialized_end=836
  _globals['_API_V1_LIBRARY_RESPONSE_TRIGGER']._serialized_start=307
  _globals['_API_V1_LIBRARY_RESPONSE_TRIGGER']._serialized_end=316
# @@protoc_insertion_point(module_scope)
