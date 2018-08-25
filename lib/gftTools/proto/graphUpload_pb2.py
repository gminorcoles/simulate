# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: graphUpload.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from . import common_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='graphUpload.proto',
  package='com.gftchina.common.persistence.graphUpload',
  serialized_pb=_b('\n\x11graphUpload.proto\x12+com.gftchina.common.persistence.graphUpload\x1a\x0c\x63ommon.proto\")\n\x05Names\x12\x0f\n\x07\x63hinese\x18\x01 \x01(\t\x12\x0f\n\x07\x65nglish\x18\x02 \x01(\t\">\n\x10\x44omainPrimaryKey\x12\x0e\n\x06\x64omain\x18\x01 \x02(\t\x12\x1a\n\x12primaryKeyInDomain\x18\x02 \x02(\t\"\x8b\x01\n\nBusinessID\x12Y\n\x10\x64omainPrimaryKey\x18\x01 \x01(\x0b\x32=.com.gftchina.common.persistence.graphUpload.DomainPrimaryKeyH\x00\x12\r\n\x03url\x18\x02 \x01(\tH\x00\x12\r\n\x03gid\x18\x03 \x01(\tH\x00\x42\x04\n\x02ID\"b\n\x15PropertyContainerInfo\x12\x0c\n\x04type\x18\x01 \x02(\t\x12;\n\x05props\x18\x02 \x01(\x0b\x32,.com.gftchina.common.persistence.common.Meta\"\x95\x02\n\x08NodeInfo\x12Q\n\x05props\x18\x01 \x02(\x0b\x32\x42.com.gftchina.common.persistence.graphUpload.PropertyContainerInfo\x12K\n\nbusinessID\x18\x02 \x02(\x0b\x32\x37.com.gftchina.common.persistence.graphUpload.BusinessID\x12\x41\n\x05names\x18\x03 \x02(\x0b\x32\x32.com.gftchina.common.persistence.graphUpload.Names\x12\x0f\n\x07subType\x18\x04 \x01(\t\x12\x15\n\rbinaryContent\x18\x05 \x01(\x0c\"\xe6\x02\n\x08\x45\x64geInfo\x12Q\n\x05props\x18\x01 \x02(\x0b\x32\x42.com.gftchina.common.persistence.graphUpload.PropertyContainerInfo\x12L\n\x0bstartNodeID\x18\x02 \x02(\x0b\x32\x37.com.gftchina.common.persistence.graphUpload.BusinessID\x12J\n\tendNodeID\x18\x03 \x02(\x0b\x32\x37.com.gftchina.common.persistence.graphUpload.BusinessID\x12\x10\n\x06source\x18\x04 \x01(\t:\x00\x12\x10\n\x06target\x18\x05 \x01(\t:\x00\x12I\n\x07subType\x18\x06 \x01(\x0e\x32\x38.com.gftchina.common.persistence.graphUpload.EdgeSubType\"\x93\x01\n\x05Graph\x12\x44\n\x05nodes\x18\x01 \x03(\x0b\x32\x35.com.gftchina.common.persistence.graphUpload.NodeInfo\x12\x44\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\x35.com.gftchina.common.persistence.graphUpload.EdgeInfo\"\xac\x02\n\x12GraphUploadRequest\x12\x41\n\x05graph\x18\x01 \x02(\x0b\x32\x32.com.gftchina.common.persistence.graphUpload.Graph\x12\x11\n\tuploadTag\x18\x02 \x02(\t\x12_\n\x16nodeAction4Duplication\x18\x03 \x02(\x0e\x32?.com.gftchina.common.persistence.graphUpload.Action4Duplication\x12_\n\x16\x65\x64geAction4Duplication\x18\x04 \x02(\x0e\x32?.com.gftchina.common.persistence.graphUpload.Action4Duplication\"Z\n\x16UpdateResultStatistics\x12\x16\n\x0enumOfCreations\x18\x01 \x02(\x05\x12\x14\n\x0cnumOfUpdates\x18\x02 \x02(\x05\x12\x12\n\nnumOfSkips\x18\x03 \x02(\x05\"\x8f\x01\n\nFailedNode\x12\x43\n\x04node\x18\x01 \x02(\x0b\x32\x35.com.gftchina.common.persistence.graphUpload.NodeInfo\x12<\n\x05\x65rror\x18\x02 \x02(\x0b\x32-.com.gftchina.common.persistence.common.Error\"\x8f\x01\n\nFailedEdge\x12\x43\n\x04\x65\x64ge\x18\x01 \x02(\x0b\x32\x35.com.gftchina.common.persistence.graphUpload.EdgeInfo\x12<\n\x05\x65rror\x18\x02 \x02(\x0b\x32-.com.gftchina.common.persistence.common.Error\"l\n\x10NodeUploadResult\x12K\n\nbusinessID\x18\x01 \x02(\x0b\x32\x37.com.gftchina.common.persistence.graphUpload.BusinessID\x12\x0b\n\x03gid\x18\x02 \x02(\t\"\xec\x03\n\x13GraphUploadResponse\x12\x11\n\tuploadTag\x18\x01 \x02(\t\x12T\n\ruploadedNodes\x18\x02 \x03(\x0b\x32=.com.gftchina.common.persistence.graphUpload.NodeUploadResult\x12g\n\x1anodeUpdateResultStatistics\x18\x03 \x02(\x0b\x32\x43.com.gftchina.common.persistence.graphUpload.UpdateResultStatistics\x12g\n\x1a\x65\x64geUpdateResultStatistics\x18\x04 \x02(\x0b\x32\x43.com.gftchina.common.persistence.graphUpload.UpdateResultStatistics\x12L\n\x0b\x66\x61iledNodes\x18\x05 \x03(\x0b\x32\x37.com.gftchina.common.persistence.graphUpload.FailedNode\x12L\n\x0b\x66\x61iledEdges\x18\x06 \x03(\x0b\x32\x37.com.gftchina.common.persistence.graphUpload.FailedEdge*+\n\x0b\x45\x64geSubType\x12\x0c\n\x08PASS_REF\x10\x00\x12\x0e\n\nPASS_VALUE\x10\x01**\n\x12\x41\x63tion4Duplication\x12\x08\n\x04SKIP\x10\x00\x12\n\n\x06UPDATE\x10\x01')
  ,
  dependencies=[common_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_EDGESUBTYPE = _descriptor.EnumDescriptor(
  name='EdgeSubType',
  full_name='com.gftchina.common.persistence.graphUpload.EdgeSubType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PASS_REF', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PASS_VALUE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2512,
  serialized_end=2555,
)
_sym_db.RegisterEnumDescriptor(_EDGESUBTYPE)

EdgeSubType = enum_type_wrapper.EnumTypeWrapper(_EDGESUBTYPE)
_ACTION4DUPLICATION = _descriptor.EnumDescriptor(
  name='Action4Duplication',
  full_name='com.gftchina.common.persistence.graphUpload.Action4Duplication',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SKIP', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UPDATE', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=2557,
  serialized_end=2599,
)
_sym_db.RegisterEnumDescriptor(_ACTION4DUPLICATION)

Action4Duplication = enum_type_wrapper.EnumTypeWrapper(_ACTION4DUPLICATION)
PASS_REF = 0
PASS_VALUE = 1
SKIP = 0
UPDATE = 1



_NAMES = _descriptor.Descriptor(
  name='Names',
  full_name='com.gftchina.common.persistence.graphUpload.Names',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chinese', full_name='com.gftchina.common.persistence.graphUpload.Names.chinese', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='english', full_name='com.gftchina.common.persistence.graphUpload.Names.english', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=80,
  serialized_end=121,
)


_DOMAINPRIMARYKEY = _descriptor.Descriptor(
  name='DomainPrimaryKey',
  full_name='com.gftchina.common.persistence.graphUpload.DomainPrimaryKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domain', full_name='com.gftchina.common.persistence.graphUpload.DomainPrimaryKey.domain', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='primaryKeyInDomain', full_name='com.gftchina.common.persistence.graphUpload.DomainPrimaryKey.primaryKeyInDomain', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=123,
  serialized_end=185,
)


_BUSINESSID = _descriptor.Descriptor(
  name='BusinessID',
  full_name='com.gftchina.common.persistence.graphUpload.BusinessID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='domainPrimaryKey', full_name='com.gftchina.common.persistence.graphUpload.BusinessID.domainPrimaryKey', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='com.gftchina.common.persistence.graphUpload.BusinessID.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='com.gftchina.common.persistence.graphUpload.BusinessID.gid', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
      name='ID', full_name='com.gftchina.common.persistence.graphUpload.BusinessID.ID',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=188,
  serialized_end=327,
)


_PROPERTYCONTAINERINFO = _descriptor.Descriptor(
  name='PropertyContainerInfo',
  full_name='com.gftchina.common.persistence.graphUpload.PropertyContainerInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='com.gftchina.common.persistence.graphUpload.PropertyContainerInfo.type', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='props', full_name='com.gftchina.common.persistence.graphUpload.PropertyContainerInfo.props', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=329,
  serialized_end=427,
)


_NODEINFO = _descriptor.Descriptor(
  name='NodeInfo',
  full_name='com.gftchina.common.persistence.graphUpload.NodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='props', full_name='com.gftchina.common.persistence.graphUpload.NodeInfo.props', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='businessID', full_name='com.gftchina.common.persistence.graphUpload.NodeInfo.businessID', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='names', full_name='com.gftchina.common.persistence.graphUpload.NodeInfo.names', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subType', full_name='com.gftchina.common.persistence.graphUpload.NodeInfo.subType', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='binaryContent', full_name='com.gftchina.common.persistence.graphUpload.NodeInfo.binaryContent', index=4,
      number=5, type=12, cpp_type=9, label=1,
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
  serialized_start=430,
  serialized_end=707,
)


_EDGEINFO = _descriptor.Descriptor(
  name='EdgeInfo',
  full_name='com.gftchina.common.persistence.graphUpload.EdgeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='props', full_name='com.gftchina.common.persistence.graphUpload.EdgeInfo.props', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='startNodeID', full_name='com.gftchina.common.persistence.graphUpload.EdgeInfo.startNodeID', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='endNodeID', full_name='com.gftchina.common.persistence.graphUpload.EdgeInfo.endNodeID', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source', full_name='com.gftchina.common.persistence.graphUpload.EdgeInfo.source', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='com.gftchina.common.persistence.graphUpload.EdgeInfo.target', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=True, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subType', full_name='com.gftchina.common.persistence.graphUpload.EdgeInfo.subType', index=5,
      number=6, type=14, cpp_type=8, label=1,
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
  serialized_start=710,
  serialized_end=1068,
)


_GRAPH = _descriptor.Descriptor(
  name='Graph',
  full_name='com.gftchina.common.persistence.graphUpload.Graph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='com.gftchina.common.persistence.graphUpload.Graph.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edges', full_name='com.gftchina.common.persistence.graphUpload.Graph.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
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
  serialized_start=1071,
  serialized_end=1218,
)


_GRAPHUPLOADREQUEST = _descriptor.Descriptor(
  name='GraphUploadRequest',
  full_name='com.gftchina.common.persistence.graphUpload.GraphUploadRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadRequest.graph', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uploadTag', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadRequest.uploadTag', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodeAction4Duplication', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadRequest.nodeAction4Duplication', index=2,
      number=3, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edgeAction4Duplication', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadRequest.edgeAction4Duplication', index=3,
      number=4, type=14, cpp_type=8, label=2,
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
  serialized_start=1221,
  serialized_end=1521,
)


_UPDATERESULTSTATISTICS = _descriptor.Descriptor(
  name='UpdateResultStatistics',
  full_name='com.gftchina.common.persistence.graphUpload.UpdateResultStatistics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='numOfCreations', full_name='com.gftchina.common.persistence.graphUpload.UpdateResultStatistics.numOfCreations', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numOfUpdates', full_name='com.gftchina.common.persistence.graphUpload.UpdateResultStatistics.numOfUpdates', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='numOfSkips', full_name='com.gftchina.common.persistence.graphUpload.UpdateResultStatistics.numOfSkips', index=2,
      number=3, type=5, cpp_type=1, label=2,
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
  serialized_start=1523,
  serialized_end=1613,
)


_FAILEDNODE = _descriptor.Descriptor(
  name='FailedNode',
  full_name='com.gftchina.common.persistence.graphUpload.FailedNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='com.gftchina.common.persistence.graphUpload.FailedNode.node', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='com.gftchina.common.persistence.graphUpload.FailedNode.error', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=1616,
  serialized_end=1759,
)


_FAILEDEDGE = _descriptor.Descriptor(
  name='FailedEdge',
  full_name='com.gftchina.common.persistence.graphUpload.FailedEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='edge', full_name='com.gftchina.common.persistence.graphUpload.FailedEdge.edge', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='com.gftchina.common.persistence.graphUpload.FailedEdge.error', index=1,
      number=2, type=11, cpp_type=10, label=2,
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
  serialized_start=1762,
  serialized_end=1905,
)


_NODEUPLOADRESULT = _descriptor.Descriptor(
  name='NodeUploadResult',
  full_name='com.gftchina.common.persistence.graphUpload.NodeUploadResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='businessID', full_name='com.gftchina.common.persistence.graphUpload.NodeUploadResult.businessID', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gid', full_name='com.gftchina.common.persistence.graphUpload.NodeUploadResult.gid', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=1907,
  serialized_end=2015,
)


_GRAPHUPLOADRESPONSE = _descriptor.Descriptor(
  name='GraphUploadResponse',
  full_name='com.gftchina.common.persistence.graphUpload.GraphUploadResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uploadTag', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadResponse.uploadTag', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uploadedNodes', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadResponse.uploadedNodes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nodeUpdateResultStatistics', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadResponse.nodeUpdateResultStatistics', index=2,
      number=3, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='edgeUpdateResultStatistics', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadResponse.edgeUpdateResultStatistics', index=3,
      number=4, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failedNodes', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadResponse.failedNodes', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failedEdges', full_name='com.gftchina.common.persistence.graphUpload.GraphUploadResponse.failedEdges', index=5,
      number=6, type=11, cpp_type=10, label=3,
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
  serialized_start=2018,
  serialized_end=2510,
)

_BUSINESSID.fields_by_name['domainPrimaryKey'].message_type = _DOMAINPRIMARYKEY
_BUSINESSID.oneofs_by_name['ID'].fields.append(
  _BUSINESSID.fields_by_name['domainPrimaryKey'])
_BUSINESSID.fields_by_name['domainPrimaryKey'].containing_oneof = _BUSINESSID.oneofs_by_name['ID']
_BUSINESSID.oneofs_by_name['ID'].fields.append(
  _BUSINESSID.fields_by_name['url'])
_BUSINESSID.fields_by_name['url'].containing_oneof = _BUSINESSID.oneofs_by_name['ID']
_BUSINESSID.oneofs_by_name['ID'].fields.append(
  _BUSINESSID.fields_by_name['gid'])
_BUSINESSID.fields_by_name['gid'].containing_oneof = _BUSINESSID.oneofs_by_name['ID']
_PROPERTYCONTAINERINFO.fields_by_name['props'].message_type = common_pb2._META
_NODEINFO.fields_by_name['props'].message_type = _PROPERTYCONTAINERINFO
_NODEINFO.fields_by_name['businessID'].message_type = _BUSINESSID
_NODEINFO.fields_by_name['names'].message_type = _NAMES
_EDGEINFO.fields_by_name['props'].message_type = _PROPERTYCONTAINERINFO
_EDGEINFO.fields_by_name['startNodeID'].message_type = _BUSINESSID
_EDGEINFO.fields_by_name['endNodeID'].message_type = _BUSINESSID
_EDGEINFO.fields_by_name['subType'].enum_type = _EDGESUBTYPE
_GRAPH.fields_by_name['nodes'].message_type = _NODEINFO
_GRAPH.fields_by_name['edges'].message_type = _EDGEINFO
_GRAPHUPLOADREQUEST.fields_by_name['graph'].message_type = _GRAPH
_GRAPHUPLOADREQUEST.fields_by_name['nodeAction4Duplication'].enum_type = _ACTION4DUPLICATION
_GRAPHUPLOADREQUEST.fields_by_name['edgeAction4Duplication'].enum_type = _ACTION4DUPLICATION
_FAILEDNODE.fields_by_name['node'].message_type = _NODEINFO
_FAILEDNODE.fields_by_name['error'].message_type = common_pb2._ERROR
_FAILEDEDGE.fields_by_name['edge'].message_type = _EDGEINFO
_FAILEDEDGE.fields_by_name['error'].message_type = common_pb2._ERROR
_NODEUPLOADRESULT.fields_by_name['businessID'].message_type = _BUSINESSID
_GRAPHUPLOADRESPONSE.fields_by_name['uploadedNodes'].message_type = _NODEUPLOADRESULT
_GRAPHUPLOADRESPONSE.fields_by_name['nodeUpdateResultStatistics'].message_type = _UPDATERESULTSTATISTICS
_GRAPHUPLOADRESPONSE.fields_by_name['edgeUpdateResultStatistics'].message_type = _UPDATERESULTSTATISTICS
_GRAPHUPLOADRESPONSE.fields_by_name['failedNodes'].message_type = _FAILEDNODE
_GRAPHUPLOADRESPONSE.fields_by_name['failedEdges'].message_type = _FAILEDEDGE
DESCRIPTOR.message_types_by_name['Names'] = _NAMES
DESCRIPTOR.message_types_by_name['DomainPrimaryKey'] = _DOMAINPRIMARYKEY
DESCRIPTOR.message_types_by_name['BusinessID'] = _BUSINESSID
DESCRIPTOR.message_types_by_name['PropertyContainerInfo'] = _PROPERTYCONTAINERINFO
DESCRIPTOR.message_types_by_name['NodeInfo'] = _NODEINFO
DESCRIPTOR.message_types_by_name['EdgeInfo'] = _EDGEINFO
DESCRIPTOR.message_types_by_name['Graph'] = _GRAPH
DESCRIPTOR.message_types_by_name['GraphUploadRequest'] = _GRAPHUPLOADREQUEST
DESCRIPTOR.message_types_by_name['UpdateResultStatistics'] = _UPDATERESULTSTATISTICS
DESCRIPTOR.message_types_by_name['FailedNode'] = _FAILEDNODE
DESCRIPTOR.message_types_by_name['FailedEdge'] = _FAILEDEDGE
DESCRIPTOR.message_types_by_name['NodeUploadResult'] = _NODEUPLOADRESULT
DESCRIPTOR.message_types_by_name['GraphUploadResponse'] = _GRAPHUPLOADRESPONSE
DESCRIPTOR.enum_types_by_name['EdgeSubType'] = _EDGESUBTYPE
DESCRIPTOR.enum_types_by_name['Action4Duplication'] = _ACTION4DUPLICATION

Names = _reflection.GeneratedProtocolMessageType('Names', (_message.Message,), dict(
  DESCRIPTOR = _NAMES,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.Names)
  ))
_sym_db.RegisterMessage(Names)

DomainPrimaryKey = _reflection.GeneratedProtocolMessageType('DomainPrimaryKey', (_message.Message,), dict(
  DESCRIPTOR = _DOMAINPRIMARYKEY,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.DomainPrimaryKey)
  ))
_sym_db.RegisterMessage(DomainPrimaryKey)

BusinessID = _reflection.GeneratedProtocolMessageType('BusinessID', (_message.Message,), dict(
  DESCRIPTOR = _BUSINESSID,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.BusinessID)
  ))
_sym_db.RegisterMessage(BusinessID)

PropertyContainerInfo = _reflection.GeneratedProtocolMessageType('PropertyContainerInfo', (_message.Message,), dict(
  DESCRIPTOR = _PROPERTYCONTAINERINFO,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.PropertyContainerInfo)
  ))
_sym_db.RegisterMessage(PropertyContainerInfo)

NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFO,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.NodeInfo)
  ))
_sym_db.RegisterMessage(NodeInfo)

EdgeInfo = _reflection.GeneratedProtocolMessageType('EdgeInfo', (_message.Message,), dict(
  DESCRIPTOR = _EDGEINFO,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.EdgeInfo)
  ))
_sym_db.RegisterMessage(EdgeInfo)

Graph = _reflection.GeneratedProtocolMessageType('Graph', (_message.Message,), dict(
  DESCRIPTOR = _GRAPH,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.Graph)
  ))
_sym_db.RegisterMessage(Graph)

GraphUploadRequest = _reflection.GeneratedProtocolMessageType('GraphUploadRequest', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHUPLOADREQUEST,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.GraphUploadRequest)
  ))
_sym_db.RegisterMessage(GraphUploadRequest)

UpdateResultStatistics = _reflection.GeneratedProtocolMessageType('UpdateResultStatistics', (_message.Message,), dict(
  DESCRIPTOR = _UPDATERESULTSTATISTICS,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.UpdateResultStatistics)
  ))
_sym_db.RegisterMessage(UpdateResultStatistics)

FailedNode = _reflection.GeneratedProtocolMessageType('FailedNode', (_message.Message,), dict(
  DESCRIPTOR = _FAILEDNODE,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.FailedNode)
  ))
_sym_db.RegisterMessage(FailedNode)

FailedEdge = _reflection.GeneratedProtocolMessageType('FailedEdge', (_message.Message,), dict(
  DESCRIPTOR = _FAILEDEDGE,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.FailedEdge)
  ))
_sym_db.RegisterMessage(FailedEdge)

NodeUploadResult = _reflection.GeneratedProtocolMessageType('NodeUploadResult', (_message.Message,), dict(
  DESCRIPTOR = _NODEUPLOADRESULT,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.NodeUploadResult)
  ))
_sym_db.RegisterMessage(NodeUploadResult)

GraphUploadResponse = _reflection.GeneratedProtocolMessageType('GraphUploadResponse', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHUPLOADRESPONSE,
  __module__ = 'graphUpload_pb2'
  # @@protoc_insertion_point(class_scope:com.gftchina.common.persistence.graphUpload.GraphUploadResponse)
  ))
_sym_db.RegisterMessage(GraphUploadResponse)


# @@protoc_insertion_point(module_scope)
