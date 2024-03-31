# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/act_function.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/act_function.proto',
  package='protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x19protos/act_function.proto\x12\x06protos\"\x90\x02\n\x08\x41\x63t_func\x12\x1a\n\x04relu\x18\x01 \x01(\x0b\x32\x0c.protos.RELU\x12&\n\nleaky_relu\x18\x02 \x01(\x0b\x32\x12.protos.Leaky_relu\x12 \n\x07sigmoid\x18\x03 \x01(\x0b\x32\x0f.protos.Sigmoid\x12\x1a\n\x04tanh\x18\x04 \x01(\x0b\x32\x0c.protos.Tanh\x12\"\n\x08gaussian\x18\x05 \x01(\x0b\x32\x10.protos.Gaussian\x12$\n\tpiecewise\x18\x06 \x01(\x0b\x32\x11.protos.Piecewise\x12\x1c\n\x05relu6\x18\x07 \x01(\x0b\x32\r.protos.Relu6\x12\x1a\n\x04silu\x18\x08 \x01(\x0b\x32\x0c.protos.Silu\"\x06\n\x04RELU\" \n\nLeaky_relu\x12\x12\n\x05\x61lpha\x18\x01 \x02(\x02:\x03\x30.2\"\t\n\x07Sigmoid\"\x06\n\x04Tanh\"\x1c\n\x08Gaussian\x12\x10\n\x05sigma\x18\x01 \x02(\x02:\x01\x31\"/\n\tPiecewise\x12\x10\n\x05lower\x18\x01 \x02(\x02:\x01\x30\x12\x10\n\x05upper\x18\x02 \x02(\x02:\x01\x36\"\x07\n\x05Relu6\"\x17\n\x04Silu\x12\x0f\n\x04\x62\x65ta\x18\x01 \x02(\x02:\x01\x31'
)




_ACT_FUNC = _descriptor.Descriptor(
  name='Act_func',
  full_name='protos.Act_func',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='relu', full_name='protos.Act_func.relu', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='leaky_relu', full_name='protos.Act_func.leaky_relu', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sigmoid', full_name='protos.Act_func.sigmoid', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tanh', full_name='protos.Act_func.tanh', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='gaussian', full_name='protos.Act_func.gaussian', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='piecewise', full_name='protos.Act_func.piecewise', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='relu6', full_name='protos.Act_func.relu6', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='silu', full_name='protos.Act_func.silu', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=310,
)


_RELU = _descriptor.Descriptor(
  name='RELU',
  full_name='protos.RELU',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=312,
  serialized_end=318,
)


_LEAKY_RELU = _descriptor.Descriptor(
  name='Leaky_relu',
  full_name='protos.Leaky_relu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alpha', full_name='protos.Leaky_relu.alpha', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.2),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=320,
  serialized_end=352,
)


_SIGMOID = _descriptor.Descriptor(
  name='Sigmoid',
  full_name='protos.Sigmoid',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=363,
)


_TANH = _descriptor.Descriptor(
  name='Tanh',
  full_name='protos.Tanh',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=365,
  serialized_end=371,
)


_GAUSSIAN = _descriptor.Descriptor(
  name='Gaussian',
  full_name='protos.Gaussian',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sigma', full_name='protos.Gaussian.sigma', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=401,
)


_PIECEWISE = _descriptor.Descriptor(
  name='Piecewise',
  full_name='protos.Piecewise',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='lower', full_name='protos.Piecewise.lower', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='upper', full_name='protos.Piecewise.upper', index=1,
      number=2, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(6),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=403,
  serialized_end=450,
)


_RELU6 = _descriptor.Descriptor(
  name='Relu6',
  full_name='protos.Relu6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=452,
  serialized_end=459,
)


_SILU = _descriptor.Descriptor(
  name='Silu',
  full_name='protos.Silu',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='beta', full_name='protos.Silu.beta', index=0,
      number=1, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=461,
  serialized_end=484,
)

_ACT_FUNC.fields_by_name['relu'].message_type = _RELU
_ACT_FUNC.fields_by_name['leaky_relu'].message_type = _LEAKY_RELU
_ACT_FUNC.fields_by_name['sigmoid'].message_type = _SIGMOID
_ACT_FUNC.fields_by_name['tanh'].message_type = _TANH
_ACT_FUNC.fields_by_name['gaussian'].message_type = _GAUSSIAN
_ACT_FUNC.fields_by_name['piecewise'].message_type = _PIECEWISE
_ACT_FUNC.fields_by_name['relu6'].message_type = _RELU6
_ACT_FUNC.fields_by_name['silu'].message_type = _SILU
DESCRIPTOR.message_types_by_name['Act_func'] = _ACT_FUNC
DESCRIPTOR.message_types_by_name['RELU'] = _RELU
DESCRIPTOR.message_types_by_name['Leaky_relu'] = _LEAKY_RELU
DESCRIPTOR.message_types_by_name['Sigmoid'] = _SIGMOID
DESCRIPTOR.message_types_by_name['Tanh'] = _TANH
DESCRIPTOR.message_types_by_name['Gaussian'] = _GAUSSIAN
DESCRIPTOR.message_types_by_name['Piecewise'] = _PIECEWISE
DESCRIPTOR.message_types_by_name['Relu6'] = _RELU6
DESCRIPTOR.message_types_by_name['Silu'] = _SILU
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Act_func = _reflection.GeneratedProtocolMessageType('Act_func', (_message.Message,), {
  'DESCRIPTOR' : _ACT_FUNC,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.Act_func)
  })
_sym_db.RegisterMessage(Act_func)

RELU = _reflection.GeneratedProtocolMessageType('RELU', (_message.Message,), {
  'DESCRIPTOR' : _RELU,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.RELU)
  })
_sym_db.RegisterMessage(RELU)

Leaky_relu = _reflection.GeneratedProtocolMessageType('Leaky_relu', (_message.Message,), {
  'DESCRIPTOR' : _LEAKY_RELU,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.Leaky_relu)
  })
_sym_db.RegisterMessage(Leaky_relu)

Sigmoid = _reflection.GeneratedProtocolMessageType('Sigmoid', (_message.Message,), {
  'DESCRIPTOR' : _SIGMOID,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.Sigmoid)
  })
_sym_db.RegisterMessage(Sigmoid)

Tanh = _reflection.GeneratedProtocolMessageType('Tanh', (_message.Message,), {
  'DESCRIPTOR' : _TANH,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.Tanh)
  })
_sym_db.RegisterMessage(Tanh)

Gaussian = _reflection.GeneratedProtocolMessageType('Gaussian', (_message.Message,), {
  'DESCRIPTOR' : _GAUSSIAN,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.Gaussian)
  })
_sym_db.RegisterMessage(Gaussian)

Piecewise = _reflection.GeneratedProtocolMessageType('Piecewise', (_message.Message,), {
  'DESCRIPTOR' : _PIECEWISE,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.Piecewise)
  })
_sym_db.RegisterMessage(Piecewise)

Relu6 = _reflection.GeneratedProtocolMessageType('Relu6', (_message.Message,), {
  'DESCRIPTOR' : _RELU6,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.Relu6)
  })
_sym_db.RegisterMessage(Relu6)

Silu = _reflection.GeneratedProtocolMessageType('Silu', (_message.Message,), {
  'DESCRIPTOR' : _SILU,
  '__module__' : 'protos.act_function_pb2'
  # @@protoc_insertion_point(class_scope:protos.Silu)
  })
_sym_db.RegisterMessage(Silu)


# @@protoc_insertion_point(module_scope)
