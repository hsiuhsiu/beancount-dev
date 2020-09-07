# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: returns_config.proto

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
  name='returns_config.proto',
  package='beancount.returns',
  syntax='proto2',
  serialized_pb=_b('\n\x14returns_config.proto\x12\x11\x62\x65\x61ncount.returns\"t\n\x06\x43onfig\x12\x38\n\x0binvestments\x18\x01 \x01(\x0b\x32#.beancount.returns.InvestmentConfig\x12\x30\n\x07reports\x18\x02 \x01(\x0b\x32\x1f.beancount.returns.ReportConfig\"E\n\x10InvestmentConfig\x12\x31\n\ninvestment\x18\x01 \x03(\x0b\x32\x1d.beancount.returns.Investment\">\n\x0cReportConfig\x12.\n\x06report\x18\x01 \x03(\x0b\x32\x1e.beancount.returns.ReportGroup\"\x7f\n\nInvestment\x12\x10\n\x08\x63urrency\x18\x01 \x01(\t\x12\x15\n\rasset_account\x18\x02 \x01(\t\x12\x19\n\x11\x64ividend_accounts\x18\x03 \x03(\t\x12\x16\n\x0ematch_accounts\x18\x04 \x03(\t\x12\x15\n\rcash_accounts\x18\x05 \x03(\t\"0\n\x0bReportGroup\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x13\n\x0binvestments\x18\x02 \x03(\t')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONFIG = _descriptor.Descriptor(
  name='Config',
  full_name='beancount.returns.Config',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='investments', full_name='beancount.returns.Config.investments', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reports', full_name='beancount.returns.Config.reports', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=43,
  serialized_end=159,
)


_INVESTMENTCONFIG = _descriptor.Descriptor(
  name='InvestmentConfig',
  full_name='beancount.returns.InvestmentConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='investment', full_name='beancount.returns.InvestmentConfig.investment', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=161,
  serialized_end=230,
)


_REPORTCONFIG = _descriptor.Descriptor(
  name='ReportConfig',
  full_name='beancount.returns.ReportConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='report', full_name='beancount.returns.ReportConfig.report', index=0,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=232,
  serialized_end=294,
)


_INVESTMENT = _descriptor.Descriptor(
  name='Investment',
  full_name='beancount.returns.Investment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='currency', full_name='beancount.returns.Investment.currency', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='asset_account', full_name='beancount.returns.Investment.asset_account', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dividend_accounts', full_name='beancount.returns.Investment.dividend_accounts', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='match_accounts', full_name='beancount.returns.Investment.match_accounts', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cash_accounts', full_name='beancount.returns.Investment.cash_accounts', index=4,
      number=5, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=296,
  serialized_end=423,
)


_REPORTGROUP = _descriptor.Descriptor(
  name='ReportGroup',
  full_name='beancount.returns.ReportGroup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='beancount.returns.ReportGroup.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='investments', full_name='beancount.returns.ReportGroup.investments', index=1,
      number=2, type=9, cpp_type=9, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=425,
  serialized_end=473,
)

_CONFIG.fields_by_name['investments'].message_type = _INVESTMENTCONFIG
_CONFIG.fields_by_name['reports'].message_type = _REPORTCONFIG
_INVESTMENTCONFIG.fields_by_name['investment'].message_type = _INVESTMENT
_REPORTCONFIG.fields_by_name['report'].message_type = _REPORTGROUP
DESCRIPTOR.message_types_by_name['Config'] = _CONFIG
DESCRIPTOR.message_types_by_name['InvestmentConfig'] = _INVESTMENTCONFIG
DESCRIPTOR.message_types_by_name['ReportConfig'] = _REPORTCONFIG
DESCRIPTOR.message_types_by_name['Investment'] = _INVESTMENT
DESCRIPTOR.message_types_by_name['ReportGroup'] = _REPORTGROUP

Config = _reflection.GeneratedProtocolMessageType('Config', (_message.Message,), dict(
  DESCRIPTOR = _CONFIG,
  __module__ = 'returns_config_pb2'
  # @@protoc_insertion_point(class_scope:beancount.returns.Config)
  ))
_sym_db.RegisterMessage(Config)

InvestmentConfig = _reflection.GeneratedProtocolMessageType('InvestmentConfig', (_message.Message,), dict(
  DESCRIPTOR = _INVESTMENTCONFIG,
  __module__ = 'returns_config_pb2'
  # @@protoc_insertion_point(class_scope:beancount.returns.InvestmentConfig)
  ))
_sym_db.RegisterMessage(InvestmentConfig)

ReportConfig = _reflection.GeneratedProtocolMessageType('ReportConfig', (_message.Message,), dict(
  DESCRIPTOR = _REPORTCONFIG,
  __module__ = 'returns_config_pb2'
  # @@protoc_insertion_point(class_scope:beancount.returns.ReportConfig)
  ))
_sym_db.RegisterMessage(ReportConfig)

Investment = _reflection.GeneratedProtocolMessageType('Investment', (_message.Message,), dict(
  DESCRIPTOR = _INVESTMENT,
  __module__ = 'returns_config_pb2'
  # @@protoc_insertion_point(class_scope:beancount.returns.Investment)
  ))
_sym_db.RegisterMessage(Investment)

ReportGroup = _reflection.GeneratedProtocolMessageType('ReportGroup', (_message.Message,), dict(
  DESCRIPTOR = _REPORTGROUP,
  __module__ = 'returns_config_pb2'
  # @@protoc_insertion_point(class_scope:beancount.returns.ReportGroup)
  ))
_sym_db.RegisterMessage(ReportGroup)


# @@protoc_insertion_point(module_scope)
