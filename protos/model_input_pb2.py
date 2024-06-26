# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/model_input.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/model_input.proto',
  package='protos',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18protos/model_input.proto\x12\x06protos\"\x9a\x02\n\x0bModel_input\x12\x10\n\x08pca_temp\x18\x01 \x01(\x05\x12\x1a\n\x0bstd_feature\x18\x02 \x02(\x08:\x05\x66\x61lse\x12\x18\n\tstd_label\x18\x03 \x02(\x08:\x05\x66\x61lse\x12\x17\n\x08mv_label\x18\x04 \x02(\x08:\x05\x66\x61lse\x12\x16\n\x07mv_temp\x18\x05 \x02(\x08:\x05\x66\x61lse\x12\x12\n\x07mv_coef\x18\x06 \x02(\x05:\x01\x35\x12\x11\n\ttsne_temp\x18\x07 \x01(\x05\x12,\n\x14parametric_tsne_temp\x18\x08 \x01(\x0b\x32\x0e.protos.P_tSNE\x12\x1b\n\x0cshuffle_bool\x18\t \x02(\x08:\x05\x66\x61lse\x12 \n\x11\x62\x61tch_offset_bool\x18\n \x02(\x08:\x05\x66\x61lse\"\xff\x02\n\x06P_tSNE\x12\x0f\n\x07tar_num\x18\x01 \x02(\x05\x12\x12\n\niter_times\x18\x02 \x02(\x05\x12\x11\n\tbatch_num\x18\x03 \x02(\x05\x12\x14\n\x0crestore_path\x18\x04 \x01(\t\x12\x1b\n\x0c\x62ool_fit_lab\x18\x05 \x02(\x08:\x05\x66\x61lse\x12 \n\x11\x62ool_remain_ori_F\x18\x06 \x02(\x08:\x05\x66\x61lse\x12\x1d\n\x12smoothing_var_coef\x18\x07 \x02(\x02:\x01\x30\x12\x1e\n\x0f\x62ool_leaky_rely\x18\x08 \x02(\x08:\x05\x66\x61lse\x12\x16\n\x0especific_label\x18\t \x01(\t\x12-\n\x10specific_feature\x18\n \x01(\x0b\x32\x13.protos.string_list\x12\x1b\n\x0c\x62ool_kill_OF\x18\x0b \x02(\x08:\x05\x66\x61lse\x12\x15\n\rspecific_file\x18\x0c \x01(\t\x12\x13\n\x08GPU_code\x18\r \x02(\t:\x01\x31\x12\x19\n\x0cGPU_fraction\x18\x0e \x02(\x02:\x03\x30.1\"\x1b\n\x0bstring_list\x12\x0c\n\x04keys\x18\x01 \x03(\t'
)




_MODEL_INPUT = _descriptor.Descriptor(
  name='Model_input',
  full_name='protos.Model_input',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='pca_temp', full_name='protos.Model_input.pca_temp', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='std_feature', full_name='protos.Model_input.std_feature', index=1,
      number=2, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='std_label', full_name='protos.Model_input.std_label', index=2,
      number=3, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mv_label', full_name='protos.Model_input.mv_label', index=3,
      number=4, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mv_temp', full_name='protos.Model_input.mv_temp', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mv_coef', full_name='protos.Model_input.mv_coef', index=5,
      number=6, type=5, cpp_type=1, label=2,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='tsne_temp', full_name='protos.Model_input.tsne_temp', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='parametric_tsne_temp', full_name='protos.Model_input.parametric_tsne_temp', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='shuffle_bool', full_name='protos.Model_input.shuffle_bool', index=8,
      number=9, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_offset_bool', full_name='protos.Model_input.batch_offset_bool', index=9,
      number=10, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
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
  serialized_start=37,
  serialized_end=319,
)


_P_TSNE = _descriptor.Descriptor(
  name='P_tSNE',
  full_name='protos.P_tSNE',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='tar_num', full_name='protos.P_tSNE.tar_num', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='iter_times', full_name='protos.P_tSNE.iter_times', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='batch_num', full_name='protos.P_tSNE.batch_num', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='restore_path', full_name='protos.P_tSNE.restore_path', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_fit_lab', full_name='protos.P_tSNE.bool_fit_lab', index=4,
      number=5, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_remain_ori_F', full_name='protos.P_tSNE.bool_remain_ori_F', index=5,
      number=6, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='smoothing_var_coef', full_name='protos.P_tSNE.smoothing_var_coef', index=6,
      number=7, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_leaky_rely', full_name='protos.P_tSNE.bool_leaky_rely', index=7,
      number=8, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specific_label', full_name='protos.P_tSNE.specific_label', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specific_feature', full_name='protos.P_tSNE.specific_feature', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bool_kill_OF', full_name='protos.P_tSNE.bool_kill_OF', index=10,
      number=11, type=8, cpp_type=7, label=2,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='specific_file', full_name='protos.P_tSNE.specific_file', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='GPU_code', full_name='protos.P_tSNE.GPU_code', index=12,
      number=13, type=9, cpp_type=9, label=2,
      has_default_value=True, default_value=b"1".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='GPU_fraction', full_name='protos.P_tSNE.GPU_fraction', index=13,
      number=14, type=2, cpp_type=6, label=2,
      has_default_value=True, default_value=float(0.1),
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
  serialized_start=322,
  serialized_end=705,
)


_STRING_LIST = _descriptor.Descriptor(
  name='string_list',
  full_name='protos.string_list',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='keys', full_name='protos.string_list.keys', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=707,
  serialized_end=734,
)

_MODEL_INPUT.fields_by_name['parametric_tsne_temp'].message_type = _P_TSNE
_P_TSNE.fields_by_name['specific_feature'].message_type = _STRING_LIST
DESCRIPTOR.message_types_by_name['Model_input'] = _MODEL_INPUT
DESCRIPTOR.message_types_by_name['P_tSNE'] = _P_TSNE
DESCRIPTOR.message_types_by_name['string_list'] = _STRING_LIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Model_input = _reflection.GeneratedProtocolMessageType('Model_input', (_message.Message,), {
  'DESCRIPTOR' : _MODEL_INPUT,
  '__module__' : 'protos.model_input_pb2'
  # @@protoc_insertion_point(class_scope:protos.Model_input)
  })
_sym_db.RegisterMessage(Model_input)

P_tSNE = _reflection.GeneratedProtocolMessageType('P_tSNE', (_message.Message,), {
  'DESCRIPTOR' : _P_TSNE,
  '__module__' : 'protos.model_input_pb2'
  # @@protoc_insertion_point(class_scope:protos.P_tSNE)
  })
_sym_db.RegisterMessage(P_tSNE)

string_list = _reflection.GeneratedProtocolMessageType('string_list', (_message.Message,), {
  'DESCRIPTOR' : _STRING_LIST,
  '__module__' : 'protos.model_input_pb2'
  # @@protoc_insertion_point(class_scope:protos.string_list)
  })
_sym_db.RegisterMessage(string_list)


# @@protoc_insertion_point(module_scope)
