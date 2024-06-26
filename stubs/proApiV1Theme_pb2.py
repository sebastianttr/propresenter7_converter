# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proApiV1Theme.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proApiV1Color_pb2 as proApiV1Color__pb2
import proApiV1Identifier_pb2 as proApiV1Identifier__pb2
import proApiV1Size_pb2 as proApiV1Size__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13proApiV1Theme.proto\x12\x07rv.data\x1a\x13proApiV1Color.proto\x1a\x18proApiV1Identifier.proto\x1a\x12proApiV1Size.proto\"\x8e\x01\n\x11\x41PI_v1_ThemeGroup\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12*\n\x06groups\x18\x02 \x03(\x0b\x32\x1a.rv.data.API_v1_ThemeGroup\x12%\n\x06themes\x18\x03 \x03(\x0b\x32\x15.rv.data.API_v1_Theme\"b\n\x0c\x41PI_v1_Theme\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12*\n\x06slides\x18\x02 \x03(\x0b\x32\x1a.rv.data.API_v1_ThemeSlide\"\x8a\x01\n\x11\x41PI_v1_ThemeSlide\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\"\n\x04size\x18\x02 \x01(\x0b\x32\x14.rv.data.API_v1_Size\x12)\n\nbackground\x18\x03 \x01(\x0b\x32\x15.rv.data.API_v1_Color\"\xb2\x08\n\x14\x41PI_v1_Theme_Request\x12\x37\n\x07get_all\x18\x01 \x01(\x0b\x32$.rv.data.API_v1_Theme_Request.GetAllH\x00\x12;\n\tget_theme\x18\x02 \x01(\x0b\x32&.rv.data.API_v1_Theme_Request.GetThemeH\x00\x12\x41\n\x0c\x64\x65lete_theme\x18\x03 \x01(\x0b\x32).rv.data.API_v1_Theme_Request.DeleteThemeH\x00\x12\x44\n\x0eget_theme_name\x18\x04 \x01(\x0b\x32*.rv.data.API_v1_Theme_Request.GetThemeNameH\x00\x12\x44\n\x0eput_theme_name\x18\x05 \x01(\x0b\x32*.rv.data.API_v1_Theme_Request.PutThemeNameH\x00\x12\x46\n\x0fget_theme_slide\x18\x06 \x01(\x0b\x32+.rv.data.API_v1_Theme_Request.GetThemeSlideH\x00\x12\x46\n\x0fput_theme_slide\x18\x07 \x01(\x0b\x32+.rv.data.API_v1_Theme_Request.PutThemeSlideH\x00\x12L\n\x12\x64\x65lete_theme_slide\x18\x08 \x01(\x0b\x32..rv.data.API_v1_Theme_Request.DeleteThemeSlideH\x00\x12Y\n\x19get_theme_slide_thumbnail\x18\t \x01(\x0b\x32\x34.rv.data.API_v1_Theme_Request.GetThemeSlideThumbnailH\x00\x1a\x08\n\x06GetAll\x1a\x16\n\x08GetTheme\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x19\n\x0b\x44\x65leteTheme\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x1a\n\x0cGetThemeName\x12\n\n\x02id\x18\x01 \x01(\t\x1a(\n\x0cPutThemeName\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x1a\x30\n\rGetThemeSlide\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0btheme_slide\x18\x02 \x01(\t\x1a[\n\rPutThemeSlide\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0btheme_slide\x18\x02 \x01(\t\x12)\n\x05slide\x18\x03 \x01(\x0b\x32\x1a.rv.data.API_v1_ThemeSlide\x1a\x33\n\x10\x44\x65leteThemeSlide\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0btheme_slide\x18\x02 \x01(\t\x1aJ\n\x16GetThemeSlideThumbnail\x12\n\n\x02id\x18\x01 \x01(\t\x12\x13\n\x0btheme_slide\x18\x02 \x01(\t\x12\x0f\n\x07quality\x18\x03 \x01(\x05\x42\t\n\x07Request\"\xbd\x08\n\x15\x41PI_v1_Theme_Response\x12\x38\n\x07get_all\x18\x01 \x01(\x0b\x32%.rv.data.API_v1_Theme_Response.GetAllH\x00\x12<\n\tget_theme\x18\x02 \x01(\x0b\x32\'.rv.data.API_v1_Theme_Response.GetThemeH\x00\x12\x42\n\x0c\x64\x65lete_theme\x18\x03 \x01(\x0b\x32*.rv.data.API_v1_Theme_Response.DeleteThemeH\x00\x12\x45\n\x0eget_theme_name\x18\x04 \x01(\x0b\x32+.rv.data.API_v1_Theme_Response.GetThemeNameH\x00\x12\x45\n\x0eput_theme_name\x18\x05 \x01(\x0b\x32+.rv.data.API_v1_Theme_Response.PutThemeNameH\x00\x12G\n\x0fget_theme_slide\x18\x06 \x01(\x0b\x32,.rv.data.API_v1_Theme_Response.GetThemeSlideH\x00\x12G\n\x0fput_theme_slide\x18\x07 \x01(\x0b\x32,.rv.data.API_v1_Theme_Response.PutThemeSlideH\x00\x12M\n\x12\x64\x65lete_theme_slide\x18\x08 \x01(\x0b\x32/.rv.data.API_v1_Theme_Response.DeleteThemeSlideH\x00\x12Z\n\x19get_theme_slide_thumbnail\x18\t \x01(\x0b\x32\x35.rv.data.API_v1_Theme_Response.GetThemeSlideThumbnailH\x00\x1a[\n\x06GetAll\x12*\n\x06groups\x18\x01 \x03(\x0b\x32\x1a.rv.data.API_v1_ThemeGroup\x12%\n\x06themes\x18\x02 \x03(\x0b\x32\x15.rv.data.API_v1_Theme\x1ah\n\x08GetTheme\x12&\n\x05theme\x18\x01 \x01(\x0b\x32\x15.rv.data.API_v1_ThemeH\x00\x12+\n\x05group\x18\x02 \x01(\x0b\x32\x1a.rv.data.API_v1_ThemeGroupH\x00\x42\x07\n\x05Value\x1a\r\n\x0b\x44\x65leteTheme\x1a\x1c\n\x0cGetThemeName\x12\x0c\n\x04name\x18\x01 \x01(\t\x1a\x0e\n\x0cPutThemeName\x1a@\n\rGetThemeSlide\x12/\n\x0btheme_slide\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_ThemeSlide\x1a\x0f\n\rPutThemeSlide\x1a\x12\n\x10\x44\x65leteThemeSlide\x1a&\n\x16GetThemeSlideThumbnail\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x42\n\n\x08Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Theme_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_API_V1_THEMEGROUP']._serialized_start=100
  _globals['_API_V1_THEMEGROUP']._serialized_end=242
  _globals['_API_V1_THEME']._serialized_start=244
  _globals['_API_V1_THEME']._serialized_end=342
  _globals['_API_V1_THEMESLIDE']._serialized_start=345
  _globals['_API_V1_THEMESLIDE']._serialized_end=483
  _globals['_API_V1_THEME_REQUEST']._serialized_start=486
  _globals['_API_V1_THEME_REQUEST']._serialized_end=1560
  _globals['_API_V1_THEME_REQUEST_GETALL']._serialized_start=1148
  _globals['_API_V1_THEME_REQUEST_GETALL']._serialized_end=1156
  _globals['_API_V1_THEME_REQUEST_GETTHEME']._serialized_start=1158
  _globals['_API_V1_THEME_REQUEST_GETTHEME']._serialized_end=1180
  _globals['_API_V1_THEME_REQUEST_DELETETHEME']._serialized_start=1182
  _globals['_API_V1_THEME_REQUEST_DELETETHEME']._serialized_end=1207
  _globals['_API_V1_THEME_REQUEST_GETTHEMENAME']._serialized_start=1209
  _globals['_API_V1_THEME_REQUEST_GETTHEMENAME']._serialized_end=1235
  _globals['_API_V1_THEME_REQUEST_PUTTHEMENAME']._serialized_start=1237
  _globals['_API_V1_THEME_REQUEST_PUTTHEMENAME']._serialized_end=1277
  _globals['_API_V1_THEME_REQUEST_GETTHEMESLIDE']._serialized_start=1279
  _globals['_API_V1_THEME_REQUEST_GETTHEMESLIDE']._serialized_end=1327
  _globals['_API_V1_THEME_REQUEST_PUTTHEMESLIDE']._serialized_start=1329
  _globals['_API_V1_THEME_REQUEST_PUTTHEMESLIDE']._serialized_end=1420
  _globals['_API_V1_THEME_REQUEST_DELETETHEMESLIDE']._serialized_start=1422
  _globals['_API_V1_THEME_REQUEST_DELETETHEMESLIDE']._serialized_end=1473
  _globals['_API_V1_THEME_REQUEST_GETTHEMESLIDETHUMBNAIL']._serialized_start=1475
  _globals['_API_V1_THEME_REQUEST_GETTHEMESLIDETHUMBNAIL']._serialized_end=1549
  _globals['_API_V1_THEME_RESPONSE']._serialized_start=1563
  _globals['_API_V1_THEME_RESPONSE']._serialized_end=2648
  _globals['_API_V1_THEME_RESPONSE_GETALL']._serialized_start=2235
  _globals['_API_V1_THEME_RESPONSE_GETALL']._serialized_end=2326
  _globals['_API_V1_THEME_RESPONSE_GETTHEME']._serialized_start=2328
  _globals['_API_V1_THEME_RESPONSE_GETTHEME']._serialized_end=2432
  _globals['_API_V1_THEME_RESPONSE_DELETETHEME']._serialized_start=1182
  _globals['_API_V1_THEME_RESPONSE_DELETETHEME']._serialized_end=1195
  _globals['_API_V1_THEME_RESPONSE_GETTHEMENAME']._serialized_start=2449
  _globals['_API_V1_THEME_RESPONSE_GETTHEMENAME']._serialized_end=2477
  _globals['_API_V1_THEME_RESPONSE_PUTTHEMENAME']._serialized_start=1237
  _globals['_API_V1_THEME_RESPONSE_PUTTHEMENAME']._serialized_end=1251
  _globals['_API_V1_THEME_RESPONSE_GETTHEMESLIDE']._serialized_start=2495
  _globals['_API_V1_THEME_RESPONSE_GETTHEMESLIDE']._serialized_end=2559
  _globals['_API_V1_THEME_RESPONSE_PUTTHEMESLIDE']._serialized_start=1329
  _globals['_API_V1_THEME_RESPONSE_PUTTHEMESLIDE']._serialized_end=1344
  _globals['_API_V1_THEME_RESPONSE_DELETETHEMESLIDE']._serialized_start=1422
  _globals['_API_V1_THEME_RESPONSE_DELETETHEMESLIDE']._serialized_end=1440
  _globals['_API_V1_THEME_RESPONSE_GETTHEMESLIDETHUMBNAIL']._serialized_start=2598
  _globals['_API_V1_THEME_RESPONSE_GETTHEMESLIDETHUMBNAIL']._serialized_end=2636
# @@protoc_insertion_point(module_scope)
