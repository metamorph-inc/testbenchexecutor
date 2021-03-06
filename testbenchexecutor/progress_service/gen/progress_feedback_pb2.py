# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: progress_feedback.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='progress_feedback.proto',
  package='progress_feedback',
  syntax='proto3',
  serialized_options=b'\252\002(JobManagerFramework.ProgressFeedback.Gen',
  serialized_pb=b'\n\x17progress_feedback.proto\x12\x11progress_feedback\"c\n\x0eProgressUpdate\x12\x0e\n\x06job_id\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x18\n\x10\x63urrent_progress\x18\x03 \x01(\x11\x12\x16\n\x0etotal_progress\x18\x04 \x01(\x11\"\x10\n\x0eProgressResult2l\n\x10ProgressFeedback\x12X\n\x0eUpdateProgress\x12!.progress_feedback.ProgressUpdate\x1a!.progress_feedback.ProgressResult\"\x00\x42+\xaa\x02(JobManagerFramework.ProgressFeedback.Genb\x06proto3'
)




_PROGRESSUPDATE = _descriptor.Descriptor(
  name='ProgressUpdate',
  full_name='progress_feedback.ProgressUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job_id', full_name='progress_feedback.ProgressUpdate.job_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='message', full_name='progress_feedback.ProgressUpdate.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_progress', full_name='progress_feedback.ProgressUpdate.current_progress', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_progress', full_name='progress_feedback.ProgressUpdate.total_progress', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=46,
  serialized_end=145,
)


_PROGRESSRESULT = _descriptor.Descriptor(
  name='ProgressResult',
  full_name='progress_feedback.ProgressResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
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
  serialized_start=147,
  serialized_end=163,
)

DESCRIPTOR.message_types_by_name['ProgressUpdate'] = _PROGRESSUPDATE
DESCRIPTOR.message_types_by_name['ProgressResult'] = _PROGRESSRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ProgressUpdate = _reflection.GeneratedProtocolMessageType('ProgressUpdate', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSUPDATE,
  '__module__' : 'progress_feedback_pb2'
  # @@protoc_insertion_point(class_scope:progress_feedback.ProgressUpdate)
  })
_sym_db.RegisterMessage(ProgressUpdate)

ProgressResult = _reflection.GeneratedProtocolMessageType('ProgressResult', (_message.Message,), {
  'DESCRIPTOR' : _PROGRESSRESULT,
  '__module__' : 'progress_feedback_pb2'
  # @@protoc_insertion_point(class_scope:progress_feedback.ProgressResult)
  })
_sym_db.RegisterMessage(ProgressResult)


DESCRIPTOR._options = None

_PROGRESSFEEDBACK = _descriptor.ServiceDescriptor(
  name='ProgressFeedback',
  full_name='progress_feedback.ProgressFeedback',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=165,
  serialized_end=273,
  methods=[
  _descriptor.MethodDescriptor(
    name='UpdateProgress',
    full_name='progress_feedback.ProgressFeedback.UpdateProgress',
    index=0,
    containing_service=None,
    input_type=_PROGRESSUPDATE,
    output_type=_PROGRESSRESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROGRESSFEEDBACK)

DESCRIPTOR.services_by_name['ProgressFeedback'] = _PROGRESSFEEDBACK

# @@protoc_insertion_point(module_scope)
