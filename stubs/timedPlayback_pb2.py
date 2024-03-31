# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timedPlayback.proto
# Protobuf Python Version: 4.25.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import action_pb2 as action__pb2
import cue_pb2 as cue__pb2
import presentation_pb2 as presentation__pb2
import uuid_pb2 as uuid__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13timedPlayback.proto\x12\x07rv.data\x1a\x0c\x61\x63tion.proto\x1a\tcue.proto\x1a\x12presentation.proto\x1a\nuuid.proto\"\xa0\x02\n\rTriggerSource\x12:\n\x10library_location\x18\x01 \x01(\x0b\x32\x1e.rv.data.TriggerSource.LibraryH\x00\x12<\n\x11playlist_location\x18\x02 \x01(\x0b\x32\x1f.rv.data.TriggerSource.PlaylistH\x00\x1a\x32\n\x07Library\x12\x0c\n\x04path\x18\x01 \x01(\t\x12\x19\n\x11presentation_name\x18\x02 \x01(\t\x1aU\n\x08Playlist\x12!\n\nidentifier\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12&\n\x0fitem_identifier\x18\x02 \x01(\x0b\x32\r.rv.data.UUIDB\n\n\x08Location\"\xc5\x11\n\rTimedPlayback\x12\x31\n\x08sequence\x18\x01 \x01(\x0b\x32\x1f.rv.data.TimedPlayback.Sequence\x12-\n\x06timing\x18\x02 \x01(\x0b\x32\x1d.rv.data.TimedPlayback.Timing\x1a\xac\x05\n\x08Sequence\x12>\n\x08sequence\x18\x01 \x03(\x0b\x32,.rv.data.TimedPlayback.Sequence.SequenceItem\x12O\n\x13\x63ontent_destination\x18\x02 \x01(\x0e\x32\x32.rv.data.TimedPlayback.Sequence.ContentDestination\x12+\n\x0cpresentation\x18\x03 \x01(\x0b\x32\x15.rv.data.Presentation\x1a\x84\x03\n\x0cSequenceItem\x12!\n\nidentifier\x18\x01 \x01(\x0b\x32\r.rv.data.UUID\x12\x0c\n\x04time\x18\x02 \x01(\x01\x12.\n\x0etrigger_source\x18\x03 \x01(\x0b\x32\x16.rv.data.TriggerSource\x12\\\n\x13\x63ontent_destination\x18\x04 \x01(\x0e\x32?.rv.data.TimedPlayback.Sequence.SequenceItem.ContentDestination\x12\x10\n\x08\x65nd_time\x18\x07 \x01(\x01\x12\x1b\n\x03\x63ue\x18\x05 \x01(\x0b\x32\x0c.rv.data.CueH\x00\x12!\n\x06\x61\x63tion\x18\x06 \x01(\x0b\x32\x0f.rv.data.ActionH\x00\"[\n\x12\x43ontentDestination\x12\x1e\n\x1a\x43ONTENT_DESTINATION_GLOBAL\x10\x00\x12%\n!CONTENT_DESTINATION_ANNOUNCEMENTS\x10\x01\x42\x06\n\x04Item\"[\n\x12\x43ontentDestination\x12\x1e\n\x1a\x43ONTENT_DESTINATION_GLOBAL\x10\x00\x12%\n!CONTENT_DESTINATION_ANNOUNCEMENTS\x10\x01\x1a\x9d\x04\n\x06Timing\x12G\n\x0flayer_transport\x18\x01 \x01(\x0b\x32,.rv.data.TimedPlayback.Timing.LayerTransportH\x00\x12\x45\n\x0esmpte_timecode\x18\x02 \x01(\x0b\x32+.rv.data.TimedPlayback.Timing.SMPTETimecodeH\x00\x12:\n\x08internal\x18\x03 \x01(\x0b\x32&.rv.data.TimedPlayback.Timing.InternalH\x00\x1a\x1f\n\x0eLayerTransport\x12\r\n\x05layer\x18\x01 \x01(\x05\x1a\xe8\x01\n\rSMPTETimecode\x12\x19\n\x11\x64\x65vice_identifier\x18\x01 \x01(\t\x12\x0f\n\x07\x63hannel\x18\x02 \x01(\x05\x12\x42\n\x06\x66ormat\x18\x03 \x01(\x0e\x32\x32.rv.data.TimedPlayback.Timing.SMPTETimecode.Format\x12\x0e\n\x06offset\x18\x04 \x01(\x01\"W\n\x06\x46ormat\x12\x11\n\rFORMAT_24_FPS\x10\x00\x12\x11\n\rFORMAT_25_FPS\x10\x01\x12\x14\n\x10\x46ORMAT_29_97_FPS\x10\x02\x12\x11\n\rFORMAT_30_FPS\x10\x03\x1a\x31\n\x08Internal\x12\x10\n\x08\x64uration\x18\x01 \x01(\x01\x12\x13\n\x0bshould_loop\x18\x02 \x01(\x08\x42\x08\n\x06Source\x1a\x82\x07\n\x06Update\x12\x32\n\x04play\x18\x01 \x01(\x0b\x32\".rv.data.TimedPlayback.Update.PlayH\x00\x12\x36\n\x06record\x18\x02 \x01(\x0b\x32$.rv.data.TimedPlayback.Update.RecordH\x00\x12\x34\n\x05pause\x18\x03 \x01(\x0b\x32#.rv.data.TimedPlayback.Update.PauseH\x00\x12\x34\n\x05reset\x18\x04 \x01(\x0b\x32#.rv.data.TimedPlayback.Update.ResetH\x00\x12@\n\x0cjump_to_time\x18\x05 \x01(\x0b\x32(.rv.data.TimedPlayback.Update.JumpToTimeH\x00\x12?\n\x0bstart_scrub\x18\x06 \x01(\x0b\x32(.rv.data.TimedPlayback.Update.StartScrubH\x00\x12;\n\tend_scrub\x18\x07 \x01(\x0b\x32&.rv.data.TimedPlayback.Update.EndScrubH\x00\x12:\n\x08\x64uration\x18\x08 \x01(\x0b\x32&.rv.data.TimedPlayback.Update.DurationH\x00\x12\x32\n\x04loop\x18\t \x01(\x0b\x32\".rv.data.TimedPlayback.Update.LoopH\x00\x12:\n\x0fupdate_sequence\x18\n \x01(\x0b\x32\x1f.rv.data.TimedPlayback.SequenceH\x00\x12\x45\n\x0emonitor_source\x18\x0b \x01(\x0b\x32+.rv.data.TimedPlayback.Update.MonitorSourceH\x00\x1a\x06\n\x04Play\x1a\x1e\n\x06Record\x12\x14\n\x0cis_recording\x18\x01 \x01(\x08\x1a\x07\n\x05Pause\x1a\x07\n\x05Reset\x1a\x1a\n\nJumpToTime\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a\x1a\n\nStartScrub\x12\x0c\n\x04time\x18\x01 \x01(\x01\x1a\x18\n\x08\x45ndScrub\x12\x0c\n\x04time\x18\x02 \x01(\x01\x1a\x1c\n\x08\x44uration\x12\x10\n\x08\x64uration\x18\x01 \x01(\x01\x1a\x14\n\x04Loop\x12\x0c\n\x04loop\x18\x01 \x01(\x08\x1a\x1f\n\rMonitorSource\x12\x0e\n\x06\x65nable\x18\x01 \x01(\x08\x42\x0c\n\nActionTypeb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'timedPlayback_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRIGGERSOURCE']._serialized_start=90
  _globals['_TRIGGERSOURCE']._serialized_end=378
  _globals['_TRIGGERSOURCE_LIBRARY']._serialized_start=229
  _globals['_TRIGGERSOURCE_LIBRARY']._serialized_end=279
  _globals['_TRIGGERSOURCE_PLAYLIST']._serialized_start=281
  _globals['_TRIGGERSOURCE_PLAYLIST']._serialized_end=366
  _globals['_TIMEDPLAYBACK']._serialized_start=381
  _globals['_TIMEDPLAYBACK']._serialized_end=2626
  _globals['_TIMEDPLAYBACK_SEQUENCE']._serialized_start=497
  _globals['_TIMEDPLAYBACK_SEQUENCE']._serialized_end=1181
  _globals['_TIMEDPLAYBACK_SEQUENCE_SEQUENCEITEM']._serialized_start=700
  _globals['_TIMEDPLAYBACK_SEQUENCE_SEQUENCEITEM']._serialized_end=1088
  _globals['_TIMEDPLAYBACK_SEQUENCE_SEQUENCEITEM_CONTENTDESTINATION']._serialized_start=989
  _globals['_TIMEDPLAYBACK_SEQUENCE_SEQUENCEITEM_CONTENTDESTINATION']._serialized_end=1080
  _globals['_TIMEDPLAYBACK_SEQUENCE_CONTENTDESTINATION']._serialized_start=989
  _globals['_TIMEDPLAYBACK_SEQUENCE_CONTENTDESTINATION']._serialized_end=1080
  _globals['_TIMEDPLAYBACK_TIMING']._serialized_start=1184
  _globals['_TIMEDPLAYBACK_TIMING']._serialized_end=1725
  _globals['_TIMEDPLAYBACK_TIMING_LAYERTRANSPORT']._serialized_start=1398
  _globals['_TIMEDPLAYBACK_TIMING_LAYERTRANSPORT']._serialized_end=1429
  _globals['_TIMEDPLAYBACK_TIMING_SMPTETIMECODE']._serialized_start=1432
  _globals['_TIMEDPLAYBACK_TIMING_SMPTETIMECODE']._serialized_end=1664
  _globals['_TIMEDPLAYBACK_TIMING_SMPTETIMECODE_FORMAT']._serialized_start=1577
  _globals['_TIMEDPLAYBACK_TIMING_SMPTETIMECODE_FORMAT']._serialized_end=1664
  _globals['_TIMEDPLAYBACK_TIMING_INTERNAL']._serialized_start=1666
  _globals['_TIMEDPLAYBACK_TIMING_INTERNAL']._serialized_end=1715
  _globals['_TIMEDPLAYBACK_UPDATE']._serialized_start=1728
  _globals['_TIMEDPLAYBACK_UPDATE']._serialized_end=2626
  _globals['_TIMEDPLAYBACK_UPDATE_PLAY']._serialized_start=2389
  _globals['_TIMEDPLAYBACK_UPDATE_PLAY']._serialized_end=2395
  _globals['_TIMEDPLAYBACK_UPDATE_RECORD']._serialized_start=2397
  _globals['_TIMEDPLAYBACK_UPDATE_RECORD']._serialized_end=2427
  _globals['_TIMEDPLAYBACK_UPDATE_PAUSE']._serialized_start=2429
  _globals['_TIMEDPLAYBACK_UPDATE_PAUSE']._serialized_end=2436
  _globals['_TIMEDPLAYBACK_UPDATE_RESET']._serialized_start=2438
  _globals['_TIMEDPLAYBACK_UPDATE_RESET']._serialized_end=2445
  _globals['_TIMEDPLAYBACK_UPDATE_JUMPTOTIME']._serialized_start=2447
  _globals['_TIMEDPLAYBACK_UPDATE_JUMPTOTIME']._serialized_end=2473
  _globals['_TIMEDPLAYBACK_UPDATE_STARTSCRUB']._serialized_start=2475
  _globals['_TIMEDPLAYBACK_UPDATE_STARTSCRUB']._serialized_end=2501
  _globals['_TIMEDPLAYBACK_UPDATE_ENDSCRUB']._serialized_start=2503
  _globals['_TIMEDPLAYBACK_UPDATE_ENDSCRUB']._serialized_end=2527
  _globals['_TIMEDPLAYBACK_UPDATE_DURATION']._serialized_start=2529
  _globals['_TIMEDPLAYBACK_UPDATE_DURATION']._serialized_end=2557
  _globals['_TIMEDPLAYBACK_UPDATE_LOOP']._serialized_start=2559
  _globals['_TIMEDPLAYBACK_UPDATE_LOOP']._serialized_end=2579
  _globals['_TIMEDPLAYBACK_UPDATE_MONITORSOURCE']._serialized_start=2581
  _globals['_TIMEDPLAYBACK_UPDATE_MONITORSOURCE']._serialized_end=2612
# @@protoc_insertion_point(module_scope)
