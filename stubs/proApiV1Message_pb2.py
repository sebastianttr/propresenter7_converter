# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proApiV1Message.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import proApiV1Identifier_pb2 as proApiV1Identifier__pb2
import proApiV1Timer_pb2 as proApiV1Timer__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15proApiV1Message.proto\x12\x07rv.data\x1a\x18proApiV1Identifier.proto\x1a\x13proApiV1Timer.proto\"\xc2\t\n\x0e\x41PI_v1_Message\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x0f\n\x07message\x18\x02 \x01(\t\x12;\n\x06tokens\x18\x03 \x03(\x0b\x32+.rv.data.API_v1_Message.API_v1_MessageToken\x12)\n\x05theme\x18\x04 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x1a\n\x12visible_on_network\x18\x05 \x01(\x08\x1a\xf2\x07\n\x13\x41PI_v1_MessageToken\x12\x0c\n\x04name\x18\x01 \x01(\t\x12L\n\x04text\x18\x02 \x01(\x0b\x32<.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_TextTokenH\x00\x12N\n\x05timer\x18\x03 \x01(\x0b\x32=.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_TimerTokenH\x00\x12N\n\x05\x63lock\x18\x04 \x01(\x0b\x32=.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_ClockTokenH\x00\x1a \n\x10\x41PI_v1_TextToken\x12\x0c\n\x04text\x18\x01 \x01(\t\x1a\xea\x02\n\x11\x41PI_v1_TimerToken\x12&\n\x02id\x18\x01 \x01(\x0b\x32\x1a.rv.data.API_v1_Identifier\x12\x16\n\x0e\x61llows_overrun\x18\x02 \x01(\x08\x12+\n\x06\x66ormat\x18\x06 \x01(\x0b\x32\x1b.rv.data.API_v1_TimerFormat\x12\x41\n\tcountdown\x18\x03 \x01(\x0b\x32,.rv.data.API_v1_Timer.API_v1_Timer_CountdownH\x00\x12P\n\x12\x63ount_down_to_time\x18\x04 \x01(\x0b\x32\x32.rv.data.API_v1_Timer.API_v1_Timer_CountdownToTimeH\x00\x12=\n\x07\x65lapsed\x18\x05 \x01(\x0b\x32*.rv.data.API_v1_Timer.API_v1_Timer_ElapsedH\x00\x42\x14\n\x12TimerConfiguration\x1a\xc2\x02\n\x11\x41PI_v1_ClockToken\x12\x63\n\x04\x64\x61te\x18\x01 \x01(\x0e\x32U.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat\x12\x63\n\x04time\x18\x02 \x01(\x0e\x32U.rv.data.API_v1_Message.API_v1_MessageToken.API_v1_ClockToken.API_v1_ClockTokenFormat\x12\x13\n\x0bis_24_hours\x18\x03 \x01(\x08\"N\n\x17\x41PI_v1_ClockTokenFormat\x12\x08\n\x04none\x10\x00\x12\t\n\x05short\x10\x01\x12\n\n\x06medium\x10\x02\x12\x08\n\x04long\x10\x03\x12\x08\n\x04\x66ull\x10\x04\x42\x0b\n\tTokenType\"\xc4\x06\n\x16\x41PI_v1_Message_Request\x12<\n\x08messages\x18\x01 \x01(\x0b\x32(.rv.data.API_v1_Message_Request.MessagesH\x00\x12G\n\x0e\x63reate_message\x18\x02 \x01(\x0b\x32-.rv.data.API_v1_Message_Request.CreateMessageH\x00\x12\x41\n\x0bget_message\x18\x03 \x01(\x0b\x32*.rv.data.API_v1_Message_Request.GetMessageH\x00\x12\x41\n\x0bput_message\x18\x04 \x01(\x0b\x32*.rv.data.API_v1_Message_Request.PutMessageH\x00\x12G\n\x0e\x64\x65lete_message\x18\x05 \x01(\x0b\x32-.rv.data.API_v1_Message_Request.DeleteMessageH\x00\x12I\n\x0ftrigger_message\x18\x06 \x01(\x0b\x32..rv.data.API_v1_Message_Request.TriggerMessageH\x00\x12\x45\n\rclear_message\x18\x07 \x01(\x0b\x32,.rv.data.API_v1_Message_Request.ClearMessageH\x00\x1a\n\n\x08Messages\x1a\x39\n\rCreateMessage\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.rv.data.API_v1_Message\x1a\x18\n\nGetMessage\x12\n\n\x02id\x18\x01 \x01(\t\x1a\x42\n\nPutMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12(\n\x07message\x18\x02 \x01(\x0b\x32\x17.rv.data.API_v1_Message\x1a\x1b\n\rDeleteMessage\x12\n\n\x02id\x18\x01 \x01(\t\x1aY\n\x0eTriggerMessage\x12\n\n\x02id\x18\x01 \x01(\t\x12;\n\x06tokens\x18\x02 \x03(\x0b\x32+.rv.data.API_v1_Message.API_v1_MessageToken\x1a\x1a\n\x0c\x43learMessage\x12\n\n\x02id\x18\x01 \x01(\tB\t\n\x07Request\"\xa9\x06\n\x17\x41PI_v1_Message_Response\x12=\n\x08messages\x18\x01 \x01(\x0b\x32).rv.data.API_v1_Message_Response.MessagesH\x00\x12H\n\x0e\x63reate_message\x18\x02 \x01(\x0b\x32..rv.data.API_v1_Message_Response.CreateMessageH\x00\x12\x42\n\x0bget_message\x18\x03 \x01(\x0b\x32+.rv.data.API_v1_Message_Response.GetMessageH\x00\x12\x42\n\x0bput_message\x18\x04 \x01(\x0b\x32+.rv.data.API_v1_Message_Response.PutMessageH\x00\x12H\n\x0e\x64\x65lete_message\x18\x05 \x01(\x0b\x32..rv.data.API_v1_Message_Response.DeleteMessageH\x00\x12J\n\x0ftrigger_message\x18\x06 \x01(\x0b\x32/.rv.data.API_v1_Message_Response.TriggerMessageH\x00\x12\x46\n\rclear_message\x18\x07 \x01(\x0b\x32-.rv.data.API_v1_Message_Response.ClearMessageH\x00\x1a\x35\n\x08Messages\x12)\n\x08messages\x18\x01 \x03(\x0b\x32\x17.rv.data.API_v1_Message\x1a\x39\n\rCreateMessage\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.rv.data.API_v1_Message\x1a\x36\n\nGetMessage\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.rv.data.API_v1_Message\x1a\x36\n\nPutMessage\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.rv.data.API_v1_Message\x1a\x0f\n\rDeleteMessage\x1a\x10\n\x0eTriggerMessage\x1a\x0e\n\x0c\x43learMessageB\n\n\x08Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proApiV1Message_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_API_V1_MESSAGE']._serialized_start=82
  _globals['_API_V1_MESSAGE']._serialized_end=1300
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN']._serialized_start=290
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN']._serialized_end=1300
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_TEXTTOKEN']._serialized_start=565
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_TEXTTOKEN']._serialized_end=597
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_TIMERTOKEN']._serialized_start=600
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_TIMERTOKEN']._serialized_end=962
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_CLOCKTOKEN']._serialized_start=965
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_CLOCKTOKEN']._serialized_end=1287
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_CLOCKTOKEN_API_V1_CLOCKTOKENFORMAT']._serialized_start=1209
  _globals['_API_V1_MESSAGE_API_V1_MESSAGETOKEN_API_V1_CLOCKTOKEN_API_V1_CLOCKTOKENFORMAT']._serialized_end=1287
  _globals['_API_V1_MESSAGE_REQUEST']._serialized_start=1303
  _globals['_API_V1_MESSAGE_REQUEST']._serialized_end=2139
  _globals['_API_V1_MESSAGE_REQUEST_MESSAGES']._serialized_start=1817
  _globals['_API_V1_MESSAGE_REQUEST_MESSAGES']._serialized_end=1827
  _globals['_API_V1_MESSAGE_REQUEST_CREATEMESSAGE']._serialized_start=1829
  _globals['_API_V1_MESSAGE_REQUEST_CREATEMESSAGE']._serialized_end=1886
  _globals['_API_V1_MESSAGE_REQUEST_GETMESSAGE']._serialized_start=1888
  _globals['_API_V1_MESSAGE_REQUEST_GETMESSAGE']._serialized_end=1912
  _globals['_API_V1_MESSAGE_REQUEST_PUTMESSAGE']._serialized_start=1914
  _globals['_API_V1_MESSAGE_REQUEST_PUTMESSAGE']._serialized_end=1980
  _globals['_API_V1_MESSAGE_REQUEST_DELETEMESSAGE']._serialized_start=1982
  _globals['_API_V1_MESSAGE_REQUEST_DELETEMESSAGE']._serialized_end=2009
  _globals['_API_V1_MESSAGE_REQUEST_TRIGGERMESSAGE']._serialized_start=2011
  _globals['_API_V1_MESSAGE_REQUEST_TRIGGERMESSAGE']._serialized_end=2100
  _globals['_API_V1_MESSAGE_REQUEST_CLEARMESSAGE']._serialized_start=2102
  _globals['_API_V1_MESSAGE_REQUEST_CLEARMESSAGE']._serialized_end=2128
  _globals['_API_V1_MESSAGE_RESPONSE']._serialized_start=2142
  _globals['_API_V1_MESSAGE_RESPONSE']._serialized_end=2951
  _globals['_API_V1_MESSAGE_RESPONSE_MESSAGES']._serialized_start=2664
  _globals['_API_V1_MESSAGE_RESPONSE_MESSAGES']._serialized_end=2717
  _globals['_API_V1_MESSAGE_RESPONSE_CREATEMESSAGE']._serialized_start=1829
  _globals['_API_V1_MESSAGE_RESPONSE_CREATEMESSAGE']._serialized_end=1886
  _globals['_API_V1_MESSAGE_RESPONSE_GETMESSAGE']._serialized_start=2778
  _globals['_API_V1_MESSAGE_RESPONSE_GETMESSAGE']._serialized_end=2832
  _globals['_API_V1_MESSAGE_RESPONSE_PUTMESSAGE']._serialized_start=2834
  _globals['_API_V1_MESSAGE_RESPONSE_PUTMESSAGE']._serialized_end=2888
  _globals['_API_V1_MESSAGE_RESPONSE_DELETEMESSAGE']._serialized_start=1982
  _globals['_API_V1_MESSAGE_RESPONSE_DELETEMESSAGE']._serialized_end=1997
  _globals['_API_V1_MESSAGE_RESPONSE_TRIGGERMESSAGE']._serialized_start=2011
  _globals['_API_V1_MESSAGE_RESPONSE_TRIGGERMESSAGE']._serialized_end=2027
  _globals['_API_V1_MESSAGE_RESPONSE_CLEARMESSAGE']._serialized_start=2102
  _globals['_API_V1_MESSAGE_RESPONSE_CLEARMESSAGE']._serialized_end=2116
# @@protoc_insertion_point(module_scope)
