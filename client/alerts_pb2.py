# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: alerts.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='alerts.proto',
  package='pb',
  syntax='proto3',
  serialized_options=b'Z\003/pb',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0c\x61lerts.proto\x12\x02pb\" \n\x0c\x41lertRequest\x12\x10\n\x08\x63\x61meraId\x18\x01 \x01(\t\" \n\rAlertResponse\x12\x0f\n\x07\x61lerted\x18\x01 \x01(\x08\x32:\n\x08\x41lerting\x12.\n\x05\x41lert\x12\x10.pb.AlertRequest\x1a\x11.pb.AlertResponse\"\x00\x42\x05Z\x03/pbb\x06proto3'
)




_ALERTREQUEST = _descriptor.Descriptor(
  name='AlertRequest',
  full_name='pb.AlertRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='cameraId', full_name='pb.AlertRequest.cameraId', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=52,
)


_ALERTRESPONSE = _descriptor.Descriptor(
  name='AlertResponse',
  full_name='pb.AlertResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='alerted', full_name='pb.AlertResponse.alerted', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=54,
  serialized_end=86,
)

DESCRIPTOR.message_types_by_name['AlertRequest'] = _ALERTREQUEST
DESCRIPTOR.message_types_by_name['AlertResponse'] = _ALERTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AlertRequest = _reflection.GeneratedProtocolMessageType('AlertRequest', (_message.Message,), {
  'DESCRIPTOR' : _ALERTREQUEST,
  '__module__' : 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:pb.AlertRequest)
  })
_sym_db.RegisterMessage(AlertRequest)

AlertResponse = _reflection.GeneratedProtocolMessageType('AlertResponse', (_message.Message,), {
  'DESCRIPTOR' : _ALERTRESPONSE,
  '__module__' : 'alerts_pb2'
  # @@protoc_insertion_point(class_scope:pb.AlertResponse)
  })
_sym_db.RegisterMessage(AlertResponse)


DESCRIPTOR._options = None

_ALERTING = _descriptor.ServiceDescriptor(
  name='Alerting',
  full_name='pb.Alerting',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=88,
  serialized_end=146,
  methods=[
  _descriptor.MethodDescriptor(
    name='Alert',
    full_name='pb.Alerting.Alert',
    index=0,
    containing_service=None,
    input_type=_ALERTREQUEST,
    output_type=_ALERTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ALERTING)

DESCRIPTOR.services_by_name['Alerting'] = _ALERTING

# @@protoc_insertion_point(module_scope)
