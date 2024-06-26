# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: clearGroups.proto
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
import color_pb2 as color__pb2
import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x63learGroups.proto\x12\x07rv.data\x1a\x0c\x61\x63tion.proto\x1a\x15\x61pplicationInfo.proto\x1a\x0b\x63olor.proto\x1a\nuuid.proto\"\xae\n\n\x13\x43learGroupsDocument\x12\x32\n\x10\x61pplication_info\x18\x01 \x01(\x0b\x32\x18.rv.data.ApplicationInfo\x12\x37\n\x06groups\x18\x02 \x03(\x0b\x32\'.rv.data.ClearGroupsDocument.ClearGroup\x1a\xa9\t\n\nClearGroup\x12\x1b\n\x04uuid\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x30\n\rlayer_targets\x18\x03 \x03(\x0b\x32\x19.rv.data.Action.ClearType\x12\x1c\n\x14is_hidden_in_preview\x18\x04 \x01(\x08\x12\x12\n\nimage_data\x18\x05 \x01(\x0c\x12\x45\n\nimage_type\x18\x06 \x01(\x0e\x32\x31.rv.data.ClearGroupsDocument.ClearGroup.ImageType\x12\x16\n\x0eis_icon_tinted\x18\x07 \x01(\x08\x12\'\n\x0ficon_tint_color\x18\x08 \x01(\x0b\x32\x0e.rv.data.Color\x12T\n\x10timeline_targets\x18\t \x03(\x0e\x32:.rv.data.ClearGroupsDocument.ClearGroup.ContentDestination\x12%\n\x1d\x63lear_presentation_next_slide\x18\n \x01(\x08\"\xa9\x05\n\tImageType\x12\x13\n\x0fImageTypeCustom\x10\x00\x12\x10\n\x0cImageTypeOne\x10\x01\x12\x10\n\x0cImageTypeTwo\x10\x02\x12\x12\n\x0eImageTypeThree\x10\x03\x12\x11\n\rImageTypeFour\x10\x04\x12\x11\n\rImageTypeFive\x10\x05\x12\x10\n\x0cImageTypeSix\x10\x06\x12\x12\n\x0eImageTypeSeven\x10\x07\x12\x12\n\x0eImageTypeEight\x10\x08\x12\x11\n\rImageTypeNine\x10\t\x12\x11\n\rImageTypeZero\x10\n\x12\x10\n\x0cImageTypeAll\x10\x0b\x12\x15\n\x11ImageTypeMegahorn\x10\x0c\x12\x11\n\rImageTypePlay\x10\r\x12\x11\n\rImageTypeBulb\x10\x0e\x12\x17\n\x13ImageTypeSunglasses\x10\x0f\x12\x12\n\x0eImageTypeArrow\x10\x10\x12\x13\n\x0fImageTypeTarget\x10\x11\x12\x11\n\rImageTypeStar\x10\x12\x12\x10\n\x0cImageTypeSun\x10\x13\x12\x11\n\rImageTypeBell\x10\x14\x12\x16\n\x12ImageTypePaperclip\x10\x15\x12\x12\n\x0eImageTypeFlask\x10\x16\x12\x17\n\x13ImageTypeEyeglasses\x10\x17\x12\x14\n\x10ImageTypeCupcake\x10\x18\x12\x12\n\x0eImageTypeSlide\x10\x19\x12\x10\n\x0cImageTypeHat\x10\x1a\x12\x13\n\x0fImageTypeFlower\x10\x1b\x12\x12\n\x0eImageTypeHeart\x10\x1c\x12\x14\n\x10ImageTypeMessage\x10\x1d\x12\x12\n\x0eImageTypeAudio\x10\x1e\x12\x12\n\x0eImageTypeCloud\x10\x1f\x12\x18\n\x14ImageTypeExclamation\x10 \"[\n\x12\x43ontentDestination\x12\x1e\n\x1a\x43ONTENT_DESTINATION_GLOBAL\x10\x00\x12%\n!CONTENT_DESTINATION_ANNOUNCEMENTS\x10\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'clearGroups_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_CLEARGROUPSDOCUMENT']._serialized_start=93
  _globals['_CLEARGROUPSDOCUMENT']._serialized_end=1419
  _globals['_CLEARGROUPSDOCUMENT_CLEARGROUP']._serialized_start=226
  _globals['_CLEARGROUPSDOCUMENT_CLEARGROUP']._serialized_end=1419
  _globals['_CLEARGROUPSDOCUMENT_CLEARGROUP_IMAGETYPE']._serialized_start=645
  _globals['_CLEARGROUPSDOCUMENT_CLEARGROUP_IMAGETYPE']._serialized_end=1326
  _globals['_CLEARGROUPSDOCUMENT_CLEARGROUP_CONTENTDESTINATION']._serialized_start=1328
  _globals['_CLEARGROUPSDOCUMENT_CLEARGROUP_CONTENTDESTINATION']._serialized_end=1419
# @@protoc_insertion_point(module_scope)
