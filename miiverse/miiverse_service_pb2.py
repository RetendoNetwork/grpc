# -*- coding: utf-8 -*-
# Auto-generated Protocol Buffers code. Note: Do not edit manually.
# source: miiverse_service.proto

"""Protobuf code with modifications for clarity and reuse."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_sym_db = _symbol_database.Default()

# Import statement from another proto file, required for dependency
from . import smm_request_post_id_rpc_pb2 as smm_rpc_proto

# Descriptor initialization with serialized data for compatibility
DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x16miiverse_service.proto\x12\x08miiverse\x1a\x1dsmm_request_post_id_rpc.proto2g\n\x08Miiverse\x12[\n\x10SMMRequestPostId\x12!.miiverse.SMMRequestPostIdRequest\x1a\".miiverse.SMMRequestPostIdResponse\"\x00\x42\x12Z\x10./;grpc_miiverseb\x06proto3'
)

# Building message and enum descriptors for global use
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'miiverse_service_pb2', globals())

# Check for use of C Descriptors (if applicable)
if _descriptor._USE_C_DESCRIPTORS == False:
    DESCRIPTOR._options = None
    DESCRIPTOR._serialized_options = b'Z\020./;grpc_miiverse'
    _MIIVERSE._serialized_start = 67
    _MIIVERSE._serialized_end = 170

# @@protoc_insertion_point(module_scope)
