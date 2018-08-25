# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: CalcOutput.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import status_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='CalcOutput.proto',
  package='com.gftchina.common.calcProtocol',
  serialized_pb=_b('\n\x10\x43\x61lcOutput.proto\x12 com.gftchina.common.calcProtocol\x1a\x0cstatus.proto\"\'\n\x07\x62inData\x12\r\n\x05_type\x18\x01 \x02(\x05\x12\r\n\x05_data\x18\x02 \x01(\x0c\"n\n\tvalueType\x12\n\n\x02_o\x18\x01 \x03(\t\x12\n\n\x02_t\x18\x02 \x03(\x04\x12\x0c\n\x04_val\x18\x03 \x03(\x01\x12;\n\x08_binData\x18\x04 \x03(\x0b\x32).com.gftchina.common.calcProtocol.binData\"\xb3\x02\n\x10outputStatistics\x12\x1d\n\x15_statistics_time_cost\x18\x01 \x01(\x05\x12\x14\n\x0c_j_row_count\x18\x02 \x01(\x05\x12@\n\x0c_j_freq_type\x18\x03 \x01(\x0e\x32*.com.gftchina.common.calcProtocol.freqType\x12\x17\n\x0f_j_unique_o_cnt\x18\x04 \x01(\x05\x12\x10\n\x08_j_min_t\x18\x05 \x01(\x04\x12\x10\n\x08_j_max_t\x18\x06 \x01(\x04\x12\x15\n\r_j_v_fullness\x18\x07 \x01(\x01\x12\x17\n\x0f_j_integer_flag\x18\x08 \x01(\x05\x12\x17\n\x0f_j_non_zero_cnt\x18\t \x01(\x05\x12\x10\n\x08_j_min_v\x18\n \x01(\x01\x12\x10\n\x08_j_max_v\x18\x0b \x01(\x01\"N\n\x0cotvCountInfo\x12\x0e\n\x06_o_cnt\x18\x01 \x02(\x05\x12\x0e\n\x06_t_cnt\x18\x02 \x02(\x05\x12\x0e\n\x06_v_cnt\x18\x03 \x02(\x05\x12\x0e\n\x06_b_cnt\x18\x04 \x02(\x05\"\xa3\x01\n\x11\x66ullStatisticInfo\x12\x0c\n\x04_gid\x18\x01 \x03(\t\x12>\n\x06otvCnt\x18\x02 \x02(\x0b\x32..com.gftchina.common.calcProtocol.otvCountInfo\x12@\n\x04stat\x18\x03 \x01(\x0b\x32\x32.com.gftchina.common.calcProtocol.outputStatistics\"\xf2\x02\n\noutputItem\x12\x0e\n\x06_o_cnt\x18\x01 \x02(\x05\x12\x0e\n\x06_t_cnt\x18\x02 \x02(\x05\x12\x0e\n\x06_v_cnt\x18\x03 \x02(\x05\x12\r\n\x05_name\x18\x04 \x01(\t\x12\x0f\n\x07_o_meta\x18\x05 \x03(\t\x12\x0f\n\x07_t_meta\x18\x06 \x03(\t\x12\x0f\n\x07_v_meta\x18\x07 \x03(\t\x12:\n\x05_vals\x18\x08 \x03(\x0b\x32+.com.gftchina.common.calcProtocol.valueType\x12\x10\n\x08_o_label\x18\t \x03(\t\x12\x10\n\x08_t_label\x18\n \x03(\t\x12\x10\n\x08_v_label\x18\x0b \x03(\t\x12\x10\n\x08_bin_cnt\x18\x0c \x01(\x05\x12\x11\n\t_bin_meta\x18\r \x03(\t\x12\x12\n\n_bin_label\x18\x0e \x03(\t\x12G\n\x0b_statistics\x18\x14 \x01(\x0b\x32\x32.com.gftchina.common.calcProtocol.outputStatistics\"\x9f\x01\n\x0bInstrOutput\x12\x0b\n\x03_fi\x18\x01 \x02(\t\x12\x0c\n\x04_idx\x18\x02 \x02(\x05\x12>\n\x08_outputs\x18\x03 \x03(\x0b\x32,.com.gftchina.common.calcProtocol.outputItem\x12\x0f\n\x07_dup_fi\x18\x04 \x03(\t\x12\x10\n\x08_dup_idx\x18\x05 \x03(\x05\x12\x12\n\n_calc_cost\x18\n \x01(\x05')
  ,
  dependencies=[status_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_BINDATA = _descriptor.Descriptor(
  name='binData',
  full_name='com.gftchina.common.calcProtocol.binData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_type', full_name='com.gftchina.common.calcProtocol.binData._type', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_data', full_name='com.gftchina.common.calcProtocol.binData._data', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=107,
)


_VALUETYPE = _descriptor.Descriptor(
  name='valueType',
  full_name='com.gftchina.common.calcProtocol.valueType',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_o', full_name='com.gftchina.common.calcProtocol.valueType._o', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_t', full_name='com.gftchina.common.calcProtocol.valueType._t', index=1,
      number=2, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_val', full_name='com.gftchina.common.calcProtocol.valueType._val', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_binData', full_name='com.gftchina.common.calcProtocol.valueType._binData', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=109,
  serialized_end=219,
)


_OUTPUTSTATISTICS = _descriptor.Descriptor(
  name='outputStatistics',
  full_name='com.gftchina.common.calcProtocol.outputStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_statistics_time_cost', full_name='com.gftchina.common.calcProtocol.outputStatistics._statistics_time_cost', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_row_count', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_row_count', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_freq_type', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_freq_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_unique_o_cnt', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_unique_o_cnt', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_min_t', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_min_t', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_max_t', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_max_t', index=5,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_v_fullness', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_v_fullness', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_integer_flag', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_integer_flag', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_non_zero_cnt', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_non_zero_cnt', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_min_v', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_min_v', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_j_max_v', full_name='com.gftchina.common.calcProtocol.outputStatistics._j_max_v', index=10,
      number=11, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=222,
  serialized_end=529,
)


_OTVCOUNTINFO = _descriptor.Descriptor(
  name='otvCountInfo',
  full_name='com.gftchina.common.calcProtocol.otvCountInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_o_cnt', full_name='com.gftchina.common.calcProtocol.otvCountInfo._o_cnt', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_t_cnt', full_name='com.gftchina.common.calcProtocol.otvCountInfo._t_cnt', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_v_cnt', full_name='com.gftchina.common.calcProtocol.otvCountInfo._v_cnt', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_b_cnt', full_name='com.gftchina.common.calcProtocol.otvCountInfo._b_cnt', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=531,
  serialized_end=609,
)


_FULLSTATISTICINFO = _descriptor.Descriptor(
  name='fullStatisticInfo',
  full_name='com.gftchina.common.calcProtocol.fullStatisticInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_gid', full_name='com.gftchina.common.calcProtocol.fullStatisticInfo._gid', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='otvCnt', full_name='com.gftchina.common.calcProtocol.fullStatisticInfo.otvCnt', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stat', full_name='com.gftchina.common.calcProtocol.fullStatisticInfo.stat', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=612,
  serialized_end=775,
)


_OUTPUTITEM = _descriptor.Descriptor(
  name='outputItem',
  full_name='com.gftchina.common.calcProtocol.outputItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_o_cnt', full_name='com.gftchina.common.calcProtocol.outputItem._o_cnt', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_t_cnt', full_name='com.gftchina.common.calcProtocol.outputItem._t_cnt', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_v_cnt', full_name='com.gftchina.common.calcProtocol.outputItem._v_cnt', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_name', full_name='com.gftchina.common.calcProtocol.outputItem._name', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_o_meta', full_name='com.gftchina.common.calcProtocol.outputItem._o_meta', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_t_meta', full_name='com.gftchina.common.calcProtocol.outputItem._t_meta', index=5,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_v_meta', full_name='com.gftchina.common.calcProtocol.outputItem._v_meta', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_vals', full_name='com.gftchina.common.calcProtocol.outputItem._vals', index=7,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_o_label', full_name='com.gftchina.common.calcProtocol.outputItem._o_label', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_t_label', full_name='com.gftchina.common.calcProtocol.outputItem._t_label', index=9,
      number=10, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_v_label', full_name='com.gftchina.common.calcProtocol.outputItem._v_label', index=10,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_bin_cnt', full_name='com.gftchina.common.calcProtocol.outputItem._bin_cnt', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_bin_meta', full_name='com.gftchina.common.calcProtocol.outputItem._bin_meta', index=12,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_bin_label', full_name='com.gftchina.common.calcProtocol.outputItem._bin_label', index=13,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_statistics', full_name='com.gftchina.common.calcProtocol.outputItem._statistics', index=14,
      number=20, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=778,
  serialized_end=1148,
)


_INSTROUTPUT = _descriptor.Descriptor(
  name='InstrOutput',
  full_name='com.gftchina.common.calcProtocol.InstrOutput',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_fi', full_name='com.gftchina.common.calcProtocol.InstrOutput._fi', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_idx', full_name='com.gftchina.common.calcProtocol.InstrOutput._idx', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_outputs', full_name='com.gftchina.common.calcProtocol.InstrOutput._outputs', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_dup_fi', full_name='com.gftchina.common.calcProtocol.InstrOutput._dup_fi', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_dup_idx', full_name='com.gftchina.common.calcProtocol.InstrOutput._dup_idx', index=4,
      number=5, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='_calc_cost', full_name='com.gftchina.common.calcProtocol.InstrOutput._calc_cost', index=5,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1151,
  serialized_end=1310,
)

_VALUETYPE.fields_by_name['_binData'].message_type = _BINDATA
_OUTPUTSTATISTICS.fields_by_name['_j_freq_type'].enum_type = status_pb2._FREQTYPE
_FULLSTATISTICINFO.fields_by_name['otvCnt'].message_type = _OTVCOUNTINFO
_FULLSTATISTICINFO.fields_by_name['stat'].message_type = _OUTPUTSTATISTICS
_OUTPUTITEM.fields_by_name['_vals'].message_type = _VALUETYPE
_OUTPUTITEM.fields_by_name['_statistics'].message_type = _OUTPUTSTATISTICS
_INSTROUTPUT.fields_by_name['_outputs'].message_type = _OUTPUTITEM
DESCRIPTOR.message_types_by_name['binData'] = _BINDATA
DESCRIPTOR.message_types_by_name['valueType'] = _VALUETYPE
DESCRIPTOR.message_types_by_name['outputStatistics'] = _OUTPUTSTATISTICS
DESCRIPTOR.message_types_by_name['otvCountInfo'] = _OTVCOUNTINFO
DESCRIPTOR.message_types_by_name['fullStatisticInfo'] = _FULLSTATISTICINFO
DESCRIPTOR.message_types_by_name['outputItem'] = _OUTPUTITEM
DESCRIPTOR.message_types_by_name['InstrOutput'] = _INSTROUTPUT

binData = _reflection.GeneratedProtocolMessageType('binData', (_message.Message,), dict(
  DESCRIPTOR = _BINDATA,
  __module__ = 'CalcOutput_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.calcProtocol.binData)
  ))
_sym_db.RegisterMessage(binData)

valueType = _reflection.GeneratedProtocolMessageType('valueType', (_message.Message,), dict(
  DESCRIPTOR = _VALUETYPE,
  __module__ = 'CalcOutput_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.calcProtocol.valueType)
  ))
_sym_db.RegisterMessage(valueType)

outputStatistics = _reflection.GeneratedProtocolMessageType('outputStatistics', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTSTATISTICS,
  __module__ = 'CalcOutput_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.calcProtocol.outputStatistics)
  ))
_sym_db.RegisterMessage(outputStatistics)

otvCountInfo = _reflection.GeneratedProtocolMessageType('otvCountInfo', (_message.Message,), dict(
  DESCRIPTOR = _OTVCOUNTINFO,
  __module__ = 'CalcOutput_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.calcProtocol.otvCountInfo)
  ))
_sym_db.RegisterMessage(otvCountInfo)

fullStatisticInfo = _reflection.GeneratedProtocolMessageType('fullStatisticInfo', (_message.Message,), dict(
  DESCRIPTOR = _FULLSTATISTICINFO,
  __module__ = 'CalcOutput_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.calcProtocol.fullStatisticInfo)
  ))
_sym_db.RegisterMessage(fullStatisticInfo)

outputItem = _reflection.GeneratedProtocolMessageType('outputItem', (_message.Message,), dict(
  DESCRIPTOR = _OUTPUTITEM,
  __module__ = 'CalcOutput_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.calcProtocol.outputItem)
  ))
_sym_db.RegisterMessage(outputItem)

InstrOutput = _reflection.GeneratedProtocolMessageType('InstrOutput', (_message.Message,), dict(
  DESCRIPTOR = _INSTROUTPUT,
  __module__ = 'CalcOutput_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.calcProtocol.InstrOutput)
  ))
_sym_db.RegisterMessage(InstrOutput)


# @@protoc_insertion_point(module_scope)
