# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: config/appconfig.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from config import acipherinfo_pb2 as config_dot_acipherinfo__pb2
from config import devcommon_pb2 as config_dot_devcommon__pb2
from config import storage_pb2 as config_dot_storage__pb2
from config import vm_pb2 as config_dot_vm__pb2
from config import netconfig_pb2 as config_dot_netconfig__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='config/appconfig.proto',
  package='',
  syntax='proto3',
  serialized_options=_b('\n\025org.lfedge.eve.configZ$github.com/lf-edge/eve/api/go/config'),
  serialized_pb=_b('\n\x16\x63onfig/appconfig.proto\x1a\x18\x63onfig/acipherinfo.proto\x1a\x16\x63onfig/devcommon.proto\x1a\x14\x63onfig/storage.proto\x1a\x0f\x63onfig/vm.proto\x1a\x16\x63onfig/netconfig.proto\"2\n\x0eInstanceOpsCmd\x12\x0f\n\x07\x63ounter\x18\x02 \x01(\r\x12\x0f\n\x07opsTime\x18\x04 \x01(\t\"\x80\x03\n\x11\x41ppInstanceConfig\x12\'\n\x0euuidandversion\x18\x01 \x01(\x0b\x32\x0f.UUIDandVersion\x12\x13\n\x0b\x64isplayname\x18\x02 \x01(\t\x12!\n\x0e\x66ixedresources\x18\x03 \x01(\x0b\x32\t.VmConfig\x12\x16\n\x06\x64rives\x18\x04 \x03(\x0b\x32\x06.Drive\x12\x10\n\x08\x61\x63tivate\x18\x05 \x01(\x08\x12#\n\ninterfaces\x18\x06 \x03(\x0b\x32\x0f.NetworkAdapter\x12\x1a\n\x08\x61\x64\x61pters\x18\x07 \x03(\x0b\x32\x08.Adapter\x12 \n\x07restart\x18\t \x01(\x0b\x32\x0f.InstanceOpsCmd\x12\x1e\n\x05purge\x18\n \x01(\x0b\x32\x0f.InstanceOpsCmd\x12\x10\n\x08userData\x18\x0b \x01(\t\x12\x15\n\rremoteConsole\x18\x0c \x01(\x08\x12 \n\ncipherData\x18\r \x01(\x0b\x32\x0c.CipherBlock\x12\x12\n\nvolumeRefs\x18\x0e \x03(\tB=\n\x15org.lfedge.eve.configZ$github.com/lf-edge/eve/api/go/configb\x06proto3')
  ,
  dependencies=[config_dot_acipherinfo__pb2.DESCRIPTOR,config_dot_devcommon__pb2.DESCRIPTOR,config_dot_storage__pb2.DESCRIPTOR,config_dot_vm__pb2.DESCRIPTOR,config_dot_netconfig__pb2.DESCRIPTOR,])




_INSTANCEOPSCMD = _descriptor.Descriptor(
  name='InstanceOpsCmd',
  full_name='InstanceOpsCmd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='counter', full_name='InstanceOpsCmd.counter', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='opsTime', full_name='InstanceOpsCmd.opsTime', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=189,
)


_APPINSTANCECONFIG = _descriptor.Descriptor(
  name='AppInstanceConfig',
  full_name='AppInstanceConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='uuidandversion', full_name='AppInstanceConfig.uuidandversion', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='displayname', full_name='AppInstanceConfig.displayname', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fixedresources', full_name='AppInstanceConfig.fixedresources', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='drives', full_name='AppInstanceConfig.drives', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activate', full_name='AppInstanceConfig.activate', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interfaces', full_name='AppInstanceConfig.interfaces', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='adapters', full_name='AppInstanceConfig.adapters', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='restart', full_name='AppInstanceConfig.restart', index=7,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='purge', full_name='AppInstanceConfig.purge', index=8,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='userData', full_name='AppInstanceConfig.userData', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remoteConsole', full_name='AppInstanceConfig.remoteConsole', index=10,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cipherData', full_name='AppInstanceConfig.cipherData', index=11,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='volumeRefs', full_name='AppInstanceConfig.volumeRefs', index=12,
      number=14, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=192,
  serialized_end=576,
)

_APPINSTANCECONFIG.fields_by_name['uuidandversion'].message_type = config_dot_devcommon__pb2._UUIDANDVERSION
_APPINSTANCECONFIG.fields_by_name['fixedresources'].message_type = config_dot_vm__pb2._VMCONFIG
_APPINSTANCECONFIG.fields_by_name['drives'].message_type = config_dot_storage__pb2._DRIVE
_APPINSTANCECONFIG.fields_by_name['interfaces'].message_type = config_dot_netconfig__pb2._NETWORKADAPTER
_APPINSTANCECONFIG.fields_by_name['adapters'].message_type = config_dot_devcommon__pb2._ADAPTER
_APPINSTANCECONFIG.fields_by_name['restart'].message_type = _INSTANCEOPSCMD
_APPINSTANCECONFIG.fields_by_name['purge'].message_type = _INSTANCEOPSCMD
_APPINSTANCECONFIG.fields_by_name['cipherData'].message_type = config_dot_acipherinfo__pb2._CIPHERBLOCK
DESCRIPTOR.message_types_by_name['InstanceOpsCmd'] = _INSTANCEOPSCMD
DESCRIPTOR.message_types_by_name['AppInstanceConfig'] = _APPINSTANCECONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InstanceOpsCmd = _reflection.GeneratedProtocolMessageType('InstanceOpsCmd', (_message.Message,), dict(
  DESCRIPTOR = _INSTANCEOPSCMD,
  __module__ = 'config.appconfig_pb2'
  # @@protoc_insertion_point(class_scope:InstanceOpsCmd)
  ))
_sym_db.RegisterMessage(InstanceOpsCmd)

AppInstanceConfig = _reflection.GeneratedProtocolMessageType('AppInstanceConfig', (_message.Message,), dict(
  DESCRIPTOR = _APPINSTANCECONFIG,
  __module__ = 'config.appconfig_pb2'
  # @@protoc_insertion_point(class_scope:AppInstanceConfig)
  ))
_sym_db.RegisterMessage(AppInstanceConfig)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
