# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pythonLibInspect.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='pythonLibInspect.proto',
  package='com.gftchina.common.persistence.pythonlib',
  serialized_pb=_b('\n\x16pythonLibInspect.proto\x12)com.gftchina.common.persistence.pythonlib\"\x91\x01\n\x05value\x12\x15\n\x0b\x62oolean_val\x18\x01 \x01(\x08H\x00\x12\x11\n\x07str_val\x18\x02 \x01(\tH\x00\x12\x11\n\x07int_val\x18\x03 \x01(\x03H\x00\x12\x13\n\tfloat_val\x18\x04 \x01(\x01H\x00\x12\x11\n\x07is_none\x18\x05 \x01(\x08H\x00\x12\x14\n\nother_type\x18\x06 \x01(\tH\x00\x42\r\n\x0bunion_value\">\n\x0ereference_info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\x05\x12\x10\n\x08showname\x18\x03 \x02(\t\"y\n\x0bscalar_info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0b\n\x03\x64oc\x18\x02 \x01(\t\x12\x10\n\x08\x63omments\x18\x03 \x01(\t\x12=\n\x03val\x18\x04 \x02(\x0b\x32\x30.com.gftchina.common.persistence.pythonlib.value\"{\n\tparameter\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0b\n\x03idx\x18\x02 \x01(\x05\x12\x0c\n\x04type\x18\x03 \x01(\x05\x12\x45\n\x0b\x64\x65\x66\x61ult_val\x18\x04 \x01(\x0b\x32\x30.com.gftchina.common.persistence.pythonlib.value\"P\n\tsignature\x12\x43\n\x05paras\x18\x01 \x03(\x0b\x32\x34.com.gftchina.common.persistence.pythonlib.parameter\"\x99\x01\n\rfunction_info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08\x63omments\x18\x02 \x01(\t\x12\x0b\n\x03\x64oc\x18\x03 \x01(\t\x12\x42\n\x04sign\x18\x04 \x01(\x0b\x32\x34.com.gftchina.common.persistence.pythonlib.signature\x12\x17\n\x0fis_bound_method\x18\x05 \x02(\x08\"\x81\x03\n\nclass_info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08\x63omments\x18\x02 \x01(\t\x12\x0b\n\x03\x64oc\x18\x03 \x01(\t\x12I\n\tenum_defs\x18\x04 \x03(\x0b\x32\x36.com.gftchina.common.persistence.pythonlib.scalar_info\x12I\n\x07methods\x18\x05 \x03(\x0b\x32\x38.com.gftchina.common.persistence.pythonlib.function_info\x12J\n\x0bsub_classes\x18\x06 \x03(\x0b\x32\x35.com.gftchina.common.persistence.pythonlib.class_info\x12M\n\nreferences\x18\x07 \x03(\x0b\x32\x39.com.gftchina.common.persistence.pythonlib.reference_info\x12\x15\n\rsuper_classes\x18\x08 \x03(\t\"\x9d\x04\n\x0bmodule_info\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x10\n\x08\x63omments\x18\x02 \x01(\t\x12\x0b\n\x03\x64oc\x18\x03 \x01(\t\x12I\n\tenum_defs\x18\x04 \x03(\x0b\x32\x36.com.gftchina.common.persistence.pythonlib.scalar_info\x12G\n\x05\x66uncs\x18\x05 \x03(\x0b\x32\x38.com.gftchina.common.persistence.pythonlib.function_info\x12I\n\nclass_defs\x18\x06 \x03(\x0b\x32\x35.com.gftchina.common.persistence.pythonlib.class_info\x12K\n\x0bsub_modules\x18\x07 \x03(\x0b\x32\x36.com.gftchina.common.persistence.pythonlib.module_info\x12\x11\n\tfile_name\x18\x08 \x01(\t\x12\x15\n\rfrom_packages\x18\t \x03(\t\x12\x0f\n\x07version\x18\n \x01(\t\x12M\n\nreferences\x18\x0b \x03(\x0b\x32\x39.com.gftchina.common.persistence.pythonlib.reference_info\x12\x10\n\x08showname\x18\x0c \x01(\t\x12\x19\n\x11owner_folder_name\x18\r \x01(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_VALUE = _descriptor.Descriptor(
  name='value',
  full_name='com.gftchina.common.persistence.pythonlib.value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='boolean_val', full_name='com.gftchina.common.persistence.pythonlib.value.boolean_val', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_val', full_name='com.gftchina.common.persistence.pythonlib.value.str_val', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='int_val', full_name='com.gftchina.common.persistence.pythonlib.value.int_val', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_val', full_name='com.gftchina.common.persistence.pythonlib.value.float_val', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_none', full_name='com.gftchina.common.persistence.pythonlib.value.is_none', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='other_type', full_name='com.gftchina.common.persistence.pythonlib.value.other_type', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
    _descriptor.OneofDescriptor(
      name='union_value', full_name='com.gftchina.common.persistence.pythonlib.value.union_value',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=70,
  serialized_end=215,
)


_REFERENCE_INFO = _descriptor.Descriptor(
  name='reference_info',
  full_name='com.gftchina.common.persistence.pythonlib.reference_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.gftchina.common.persistence.pythonlib.reference_info.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.gftchina.common.persistence.pythonlib.reference_info.type', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='showname', full_name='com.gftchina.common.persistence.pythonlib.reference_info.showname', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=217,
  serialized_end=279,
)


_SCALAR_INFO = _descriptor.Descriptor(
  name='scalar_info',
  full_name='com.gftchina.common.persistence.pythonlib.scalar_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.gftchina.common.persistence.pythonlib.scalar_info.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc', full_name='com.gftchina.common.persistence.pythonlib.scalar_info.doc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comments', full_name='com.gftchina.common.persistence.pythonlib.scalar_info.comments', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='val', full_name='com.gftchina.common.persistence.pythonlib.scalar_info.val', index=3,
      number=4, type=11, cpp_type=10, label=2,
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
  serialized_start=281,
  serialized_end=402,
)


_PARAMETER = _descriptor.Descriptor(
  name='parameter',
  full_name='com.gftchina.common.persistence.pythonlib.parameter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.gftchina.common.persistence.pythonlib.parameter.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='idx', full_name='com.gftchina.common.persistence.pythonlib.parameter.idx', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='com.gftchina.common.persistence.pythonlib.parameter.type', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_val', full_name='com.gftchina.common.persistence.pythonlib.parameter.default_val', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=404,
  serialized_end=527,
)


_SIGNATURE = _descriptor.Descriptor(
  name='signature',
  full_name='com.gftchina.common.persistence.pythonlib.signature',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='paras', full_name='com.gftchina.common.persistence.pythonlib.signature.paras', index=0,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=529,
  serialized_end=609,
)


_FUNCTION_INFO = _descriptor.Descriptor(
  name='function_info',
  full_name='com.gftchina.common.persistence.pythonlib.function_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.gftchina.common.persistence.pythonlib.function_info.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comments', full_name='com.gftchina.common.persistence.pythonlib.function_info.comments', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc', full_name='com.gftchina.common.persistence.pythonlib.function_info.doc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sign', full_name='com.gftchina.common.persistence.pythonlib.function_info.sign', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_bound_method', full_name='com.gftchina.common.persistence.pythonlib.function_info.is_bound_method', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=False, default_value=False,
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
  serialized_end=765,
)


_CLASS_INFO = _descriptor.Descriptor(
  name='class_info',
  full_name='com.gftchina.common.persistence.pythonlib.class_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.gftchina.common.persistence.pythonlib.class_info.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comments', full_name='com.gftchina.common.persistence.pythonlib.class_info.comments', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc', full_name='com.gftchina.common.persistence.pythonlib.class_info.doc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enum_defs', full_name='com.gftchina.common.persistence.pythonlib.class_info.enum_defs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='methods', full_name='com.gftchina.common.persistence.pythonlib.class_info.methods', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_classes', full_name='com.gftchina.common.persistence.pythonlib.class_info.sub_classes', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='references', full_name='com.gftchina.common.persistence.pythonlib.class_info.references', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='super_classes', full_name='com.gftchina.common.persistence.pythonlib.class_info.super_classes', index=7,
      number=8, type=9, cpp_type=9, label=3,
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
  serialized_start=768,
  serialized_end=1153,
)


_MODULE_INFO = _descriptor.Descriptor(
  name='module_info',
  full_name='com.gftchina.common.persistence.pythonlib.module_info',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='com.gftchina.common.persistence.pythonlib.module_info.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='comments', full_name='com.gftchina.common.persistence.pythonlib.module_info.comments', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='doc', full_name='com.gftchina.common.persistence.pythonlib.module_info.doc', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enum_defs', full_name='com.gftchina.common.persistence.pythonlib.module_info.enum_defs', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='funcs', full_name='com.gftchina.common.persistence.pythonlib.module_info.funcs', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_defs', full_name='com.gftchina.common.persistence.pythonlib.module_info.class_defs', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_modules', full_name='com.gftchina.common.persistence.pythonlib.module_info.sub_modules', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='file_name', full_name='com.gftchina.common.persistence.pythonlib.module_info.file_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_packages', full_name='com.gftchina.common.persistence.pythonlib.module_info.from_packages', index=8,
      number=9, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='com.gftchina.common.persistence.pythonlib.module_info.version', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='references', full_name='com.gftchina.common.persistence.pythonlib.module_info.references', index=10,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='showname', full_name='com.gftchina.common.persistence.pythonlib.module_info.showname', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner_folder_name', full_name='com.gftchina.common.persistence.pythonlib.module_info.owner_folder_name', index=12,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=1156,
  serialized_end=1697,
)

_VALUE.oneofs_by_name['union_value'].fields.append(
  _VALUE.fields_by_name['boolean_val'])
_VALUE.fields_by_name['boolean_val'].containing_oneof = _VALUE.oneofs_by_name['union_value']
_VALUE.oneofs_by_name['union_value'].fields.append(
  _VALUE.fields_by_name['str_val'])
_VALUE.fields_by_name['str_val'].containing_oneof = _VALUE.oneofs_by_name['union_value']
_VALUE.oneofs_by_name['union_value'].fields.append(
  _VALUE.fields_by_name['int_val'])
_VALUE.fields_by_name['int_val'].containing_oneof = _VALUE.oneofs_by_name['union_value']
_VALUE.oneofs_by_name['union_value'].fields.append(
  _VALUE.fields_by_name['float_val'])
_VALUE.fields_by_name['float_val'].containing_oneof = _VALUE.oneofs_by_name['union_value']
_VALUE.oneofs_by_name['union_value'].fields.append(
  _VALUE.fields_by_name['is_none'])
_VALUE.fields_by_name['is_none'].containing_oneof = _VALUE.oneofs_by_name['union_value']
_VALUE.oneofs_by_name['union_value'].fields.append(
  _VALUE.fields_by_name['other_type'])
_VALUE.fields_by_name['other_type'].containing_oneof = _VALUE.oneofs_by_name['union_value']
_SCALAR_INFO.fields_by_name['val'].message_type = _VALUE
_PARAMETER.fields_by_name['default_val'].message_type = _VALUE
_SIGNATURE.fields_by_name['paras'].message_type = _PARAMETER
_FUNCTION_INFO.fields_by_name['sign'].message_type = _SIGNATURE
_CLASS_INFO.fields_by_name['enum_defs'].message_type = _SCALAR_INFO
_CLASS_INFO.fields_by_name['methods'].message_type = _FUNCTION_INFO
_CLASS_INFO.fields_by_name['sub_classes'].message_type = _CLASS_INFO
_CLASS_INFO.fields_by_name['references'].message_type = _REFERENCE_INFO
_MODULE_INFO.fields_by_name['enum_defs'].message_type = _SCALAR_INFO
_MODULE_INFO.fields_by_name['funcs'].message_type = _FUNCTION_INFO
_MODULE_INFO.fields_by_name['class_defs'].message_type = _CLASS_INFO
_MODULE_INFO.fields_by_name['sub_modules'].message_type = _MODULE_INFO
_MODULE_INFO.fields_by_name['references'].message_type = _REFERENCE_INFO
DESCRIPTOR.message_types_by_name['value'] = _VALUE
DESCRIPTOR.message_types_by_name['reference_info'] = _REFERENCE_INFO
DESCRIPTOR.message_types_by_name['scalar_info'] = _SCALAR_INFO
DESCRIPTOR.message_types_by_name['parameter'] = _PARAMETER
DESCRIPTOR.message_types_by_name['signature'] = _SIGNATURE
DESCRIPTOR.message_types_by_name['function_info'] = _FUNCTION_INFO
DESCRIPTOR.message_types_by_name['class_info'] = _CLASS_INFO
DESCRIPTOR.message_types_by_name['module_info'] = _MODULE_INFO

value = _reflection.GeneratedProtocolMessageType('value', (_message.Message,), dict(
  DESCRIPTOR = _VALUE,
  __module__ = 'pythonLibInspect_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.pythonlib.value)
  ))
_sym_db.RegisterMessage(value)

reference_info = _reflection.GeneratedProtocolMessageType('reference_info', (_message.Message,), dict(
  DESCRIPTOR = _REFERENCE_INFO,
  __module__ = 'pythonLibInspect_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.pythonlib.reference_info)
  ))
_sym_db.RegisterMessage(reference_info)

scalar_info = _reflection.GeneratedProtocolMessageType('scalar_info', (_message.Message,), dict(
  DESCRIPTOR = _SCALAR_INFO,
  __module__ = 'pythonLibInspect_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.pythonlib.scalar_info)
  ))
_sym_db.RegisterMessage(scalar_info)

parameter = _reflection.GeneratedProtocolMessageType('parameter', (_message.Message,), dict(
  DESCRIPTOR = _PARAMETER,
  __module__ = 'pythonLibInspect_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.pythonlib.parameter)
  ))
_sym_db.RegisterMessage(parameter)

signature = _reflection.GeneratedProtocolMessageType('signature', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATURE,
  __module__ = 'pythonLibInspect_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.pythonlib.signature)
  ))
_sym_db.RegisterMessage(signature)

function_info = _reflection.GeneratedProtocolMessageType('function_info', (_message.Message,), dict(
  DESCRIPTOR = _FUNCTION_INFO,
  __module__ = 'pythonLibInspect_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.pythonlib.function_info)
  ))
_sym_db.RegisterMessage(function_info)

class_info = _reflection.GeneratedProtocolMessageType('class_info', (_message.Message,), dict(
  DESCRIPTOR = _CLASS_INFO,
  __module__ = 'pythonLibInspect_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.pythonlib.class_info)
  ))
_sym_db.RegisterMessage(class_info)

module_info = _reflection.GeneratedProtocolMessageType('module_info', (_message.Message,), dict(
  DESCRIPTOR = _MODULE_INFO,
  __module__ = 'pythonLibInspect_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.pythonlib.module_info)
  ))
_sym_db.RegisterMessage(module_info)


# @@protoc_insertion_point(module_scope)
