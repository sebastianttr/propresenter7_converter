# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proApiV1Stage.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proApiV1Identifier_pb2 as proApiV1Identifier__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proApiV1Stage.proto\x12\x07rv.data\x1a\x18proApiV1Identifier.proto\"\xaf\x01\n\x15\x41PI_v1_StageLayoutMap\x12\x35\n\x07\x65ntries\x18\x01 \x03(\x0b\x32$.rv.data.API_v1_StageLayoutMap.Entry\x1a_\n\x05\x45ntry\x12*\n\x06screen\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12*\n\x06layout\x18\x02 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\"\xeb\x08\n\x14\x41PI_v1_Stage_Request\x12\x44\n\x0eget_layout_map\x18\x01 \x01(\x0b\x32*.rv.data.API_v1_Stage_Request.GetLayoutMapH\x00\x12\x44\n\x0eset_layout_map\x18\x02 \x01(\x0b\x32*.rv.data.API_v1_Stage_Request.SetLayoutMapH\x00\x12?\n\x0bget_message\x18\x03 \x01(\x0b\x32(.rv.data.API_v1_Stage_Request.GetMessageH\x00\x12?\n\x0bput_message\x18\x04 \x01(\x0b\x32(.rv.data.API_v1_Stage_Request.PutMessageH\x00\x12\x45\n\x0e\x64\x65lete_message\x18\x05 \x01(\x0b\x32+.rv.data.API_v1_Stage_Request.DeleteMessageH\x00\x12?\n\x0bget_screens\x18\x06 \x01(\x0b\x32(.rv.data.API_v1_Stage_Request.GetScreensH\x00\x12J\n\x11get_screen_layout\x18\x07 \x01(\x0b\x32-.rv.data.API_v1_Stage_Request.GetScreenLayoutH\x00\x12J\n\x11set_screen_layout\x18\x08 \x01(\x0b\x32-.rv.data.API_v1_Stage_Request.SetScreenLayoutH\x00\x12?\n\x0bget_layouts\x18\t \x01(\x0b\x32(.rv.data.API_v1_Stage_Request.GetLayoutsH\x00\x12\x43\n\rdelete_layout\x18\n \x01(\x0b\x32*.rv.data.API_v1_Stage_Request.DeleteLayoutH\x00\x12P\n\x14get_layout_thumbnail\x18\x0b \x01(\x0b\x32\x30.rv.data.API_v1_Stage_Request.GetLayoutThumbnailH\x00\x1a\x0e\n\x0cGetLayoutMap\x1a;\n\x0cSetLayoutMap\x12+\n\x03map\x18\x01 \x01(\x0b\x32\x1e.rv.data.API_v1_StageLayoutMap\x1a\x0c\n\nGetMessage\x1a\x1d\n\nPutMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x1a\x0f\n\rDeleteMessage\x1a\x0c\n\nGetScreens\x1a\x1d\n\x0fGetScreenLayout\x12\n\n\x02id\x18\x01 \x01(\t\x1a-\n\x0fSetScreenLayout\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06layout\x18\x02 \x01(\t\x1a\x0c\n\nGetLayouts\x1a\x1a\n\x0c\x44\x65leteLayout\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x31\n\x12GetLayoutThumbnail\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07quality\x18\x02 \x01(\x05\x42\t\n\x07Request\"\x80\n\n\x15\x41PI_v1_Stage_Response\x12\x45\n\x0eget_layout_map\x18\x01 \x01(\x0b\x32+.rv.data.API_v1_Stage_Response.GetLayoutMapH\x00\x12\x45\n\x0eset_layout_map\x18\x02 \x01(\x0b\x32+.rv.data.API_v1_Stage_Response.SetLayoutMapH\x00\x12@\n\x0bget_message\x18\x03 \x01(\x0b\x32).rv.data.API_v1_Stage_Response.GetMessageH\x00\x12@\n\x0bput_message\x18\x04 \x01(\x0b\x32).rv.data.API_v1_Stage_Response.PutMessageH\x00\x12\x46\n\x0e\x64\x65lete_message\x18\x05 \x01(\x0b\x32,.rv.data.API_v1_Stage_Response.DeleteMessageH\x00\x12@\n\x0bget_screens\x18\x06 \x01(\x0b\x32).rv.data.API_v1_Stage_Response.GetScreensH\x00\x12K\n\x11get_screen_layout\x18\x07 \x01(\x0b\x32..rv.data.API_v1_Stage_Response.GetScreenLayoutH\x00\x12K\n\x11set_screen_layout\x18\x08 \x01(\x0b\x32..rv.data.API_v1_Stage_Response.SetScreenLayoutH\x00\x12@\n\x0bget_layouts\x18\t \x01(\x0b\x32).rv.data.API_v1_Stage_Response.GetLayoutsH\x00\x12\x44\n\rdelete_layout\x18\n \x01(\x0b\x32+.rv.data.API_v1_Stage_Response.DeleteLayoutH\x00\x12Q\n\x14get_layout_thumbnail\x18\x0b \x01(\x0b\x32\x31.rv.data.API_v1_Stage_Response.GetLayoutThumbnailH\x00\x1a;\n\x0cGetLayoutMap\x12+\n\x03map\x18\x01 \x01(\x0b\x32\x1e.rv.data.API_v1_StageLayoutMap\x1a\x0e\n\x0cSetLayoutMap\x1a\x1d\n\nGetMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\x1a\x0c\n\nPutMessage\x1a\x0f\n\rDeleteMessage\x1a\x39\n\nGetScreens\x12+\n\x07screens\x18\x01 \x03(\x0b\x32\x1a.rv.data.API_v1_Identifier\x1a\x39\n\x0fGetScreenLayout\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x1a\x11\n\x0fSetScreenLayout\x1a\x81\x01\n\nGetLayouts\x12\x41\n\x07layouts\x18\x01 \x03(\x0b\x32\x30.rv.data.API_v1_Stage_Response.GetLayouts.Layout\x1a\x30\n\x06Layout\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x1a\x0e\n\x0c\x44\x65leteLayout\x1a\"\n\x12GetLayoutThumbnail\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x42\n\n\x08Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Stage_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_API_V1_STAGELAYOUTMAP']._serialized_start=59
  _globals['_API_V1_STAGELAYOUTMAP']._serialized_end=234
  _globals['_API_V1_STAGELAYOUTMAP_ENTRY']._serialized_start=139
  _globals['_API_V1_STAGELAYOUTMAP_ENTRY']._serialized_end=234
  _globals['_API_V1_STAGE_REQUEST']._serialized_start=237
  _globals['_API_V1_STAGE_REQUEST']._serialized_end=1368
  _globals['_API_V1_STAGE_REQUEST_GETLAYOUTMAP']._serialized_start=1035
  _globals['_API_V1_STAGE_REQUEST_GETLAYOUTMAP']._serialized_end=1049
  _globals['_API_V1_STAGE_REQUEST_SETLAYOUTMAP']._serialized_start=1051
  _globals['_API_V1_STAGE_REQUEST_SETLAYOUTMAP']._serialized_end=1110
  _globals['_API_V1_STAGE_REQUEST_GETMESSAGE']._serialized_start=1112
  _globals['_API_V1_STAGE_REQUEST_GETMESSAGE']._serialized_end=1124
  _globals['_API_V1_STAGE_REQUEST_PUTMESSAGE']._serialized_start=1126
  _globals['_API_V1_STAGE_REQUEST_PUTMESSAGE']._serialized_end=1155
  _globals['_API_V1_STAGE_REQUEST_DELETEMESSAGE']._serialized_start=1157
  _globals['_API_V1_STAGE_REQUEST_DELETEMESSAGE']._serialized_end=1172
  _globals['_API_V1_STAGE_REQUEST_GETSCREENS']._serialized_start=1174
  _globals['_API_V1_STAGE_REQUEST_GETSCREENS']._serialized_end=1186
  _globals['_API_V1_STAGE_REQUEST_GETSCREENLAYOUT']._serialized_start=1188
  _globals['_API_V1_STAGE_REQUEST_GETSCREENLAYOUT']._serialized_end=1217
  _globals['_API_V1_STAGE_REQUEST_SETSCREENLAYOUT']._serialized_start=1219
  _globals['_API_V1_STAGE_REQUEST_SETSCREENLAYOUT']._serialized_end=1264
  _globals['_API_V1_STAGE_REQUEST_GETLAYOUTS']._serialized_start=1266
  _globals['_API_V1_STAGE_REQUEST_GETLAYOUTS']._serialized_end=1278
  _globals['_API_V1_STAGE_REQUEST_DELETELAYOUT']._serialized_start=1280
  _globals['_API_V1_STAGE_REQUEST_DELETELAYOUT']._serialized_end=1306
  _globals['_API_V1_STAGE_REQUEST_GETLAYOUTTHUMBNAIL']._serialized_start=1308
  _globals['_API_V1_STAGE_REQUEST_GETLAYOUTTHUMBNAIL']._serialized_end=1357
  _globals['_API_V1_STAGE_RESPONSE']._serialized_start=1371
  _globals['_API_V1_STAGE_RESPONSE']._serialized_end=2651
  _globals['_API_V1_STAGE_RESPONSE_GETLAYOUTMAP']._serialized_start=2181
  _globals['_API_V1_STAGE_RESPONSE_GETLAYOUTMAP']._serialized_end=2240
  _globals['_API_V1_STAGE_RESPONSE_SETLAYOUTMAP']._serialized_start=1051
  _globals['_API_V1_STAGE_RESPONSE_SETLAYOUTMAP']._serialized_end=1065
  _globals['_API_V1_STAGE_RESPONSE_GETMESSAGE']._serialized_start=2258
  _globals['_API_V1_STAGE_RESPONSE_GETMESSAGE']._serialized_end=2287
  _globals['_API_V1_STAGE_RESPONSE_PUTMESSAGE']._serialized_start=1126
  _globals['_API_V1_STAGE_RESPONSE_PUTMESSAGE']._serialized_end=1138
  _globals['_API_V1_STAGE_RESPONSE_DELETEMESSAGE']._serialized_start=1157
  _globals['_API_V1_STAGE_RESPONSE_DELETEMESSAGE']._serialized_end=1172
  _globals['_API_V1_STAGE_RESPONSE_GETSCREENS']._serialized_start=2320
  _globals['_API_V1_STAGE_RESPONSE_GETSCREENS']._serialized_end=2377
  _globals['_API_V1_STAGE_RESPONSE_GETSCREENLAYOUT']._serialized_start=2379
  _globals['_API_V1_STAGE_RESPONSE_GETSCREENLAYOUT']._serialized_end=2436
  _globals['_API_V1_STAGE_RESPONSE_SETSCREENLAYOUT']._serialized_start=1219
  _globals['_API_V1_STAGE_RESPONSE_SETSCREENLAYOUT']._serialized_end=1236
  _globals['_API_V1_STAGE_RESPONSE_GETLAYOUTS']._serialized_start=2458
  _globals['_API_V1_STAGE_RESPONSE_GETLAYOUTS']._serialized_end=2587
  _globals['_API_V1_STAGE_RESPONSE_GETLAYOUTS_LAYOUT']._serialized_start=2539
  _globals['_API_V1_STAGE_RESPONSE_GETLAYOUTS_LAYOUT']._serialized_end=2587
  _globals['_API_V1_STAGE_RESPONSE_DELETELAYOUT']._serialized_start=1280
  _globals['_API_V1_STAGE_RESPONSE_DELETELAYOUT']._serialized_end=1294
  _globals['_API_V1_STAGE_RESPONSE_GETLAYOUTTHUMBNAIL']._serialized_start=2605
  _globals['_API_V1_STAGE_RESPONSE_GETLAYOUTTHUMBNAIL']._serialized_end=2639
# @@protoc_insertion_point(module_scope)
