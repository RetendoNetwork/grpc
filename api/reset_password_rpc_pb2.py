# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: reset_password_rpc.proto
# Protobuf Python Version: 5.28.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    1,
    '',
    'reset_password_rpc.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18reset_password_rpc.proto\x12\x03\x61pi\"Q\n\x14ResetPasswordRequest\x12\x10\n\x08password\x18\x01 \x01(\t\x12\x18\n\x10password_confirm\x18\x02 \x01(\t\x12\r\n\x05token\x18\x03 \x01(\tB\rZ\x0b./;grpc_apib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'reset_password_rpc_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'Z\013./;grpc_api'
  _globals['_RESETPASSWORDREQUEST']._serialized_start=33
  _globals['_RESETPASSWORDREQUEST']._serialized_end=114
# @@protoc_insertion_point(module_scope)
