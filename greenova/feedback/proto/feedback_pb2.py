# pylint: skip-file
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: feedback.proto
# Protobuf Python Version: 6.30.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    6,
    30,
    2,
    '',
    'feedback.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0e\x66\x65\x65\x64\x62\x61\x63k.proto\x12\x08\x66\x65\x65\x64\x62\x61\x63k\"\xda\x08\n\x0e\x42ugReportProto\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x1b\n\x13\x61pplication_version\x18\x04 \x01(\t\x12\x18\n\x10operating_system\x18\x05 \x01(\t\x12\x0f\n\x07\x62rowser\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x65vice_type\x18\x07 \x01(\t\x12\x1a\n\x12steps_to_reproduce\x18\x08 \x01(\t\x12\x19\n\x11\x65xpected_behavior\x18\t \x01(\t\x12\x17\n\x0f\x61\x63tual_behavior\x18\n \x01(\t\x12\x16\n\x0e\x65rror_messages\x18\x0b \x01(\t\x12\x14\n\x0ctrace_report\x18\x0c \x01(\t\x12\x35\n\tfrequency\x18\r \x01(\x0e\x32\".feedback.BugReportProto.Frequency\x12:\n\x0fimpact_severity\x18\x0e \x01(\x0e\x32!.feedback.BugReportProto.Severity\x12\x39\n\x0e\x61\x64min_severity\x18\x0f \x01(\x0e\x32!.feedback.BugReportProto.Severity\x12\x13\n\x0buser_impact\x18\x10 \x01(\t\x12\x13\n\x0bworkarounds\x18\x11 \x01(\t\x12\x1b\n\x13\x61\x64\x64itional_comments\x18\x12 \x01(\t\x12\x0f\n\x07user_id\x18\x13 \x01(\x05\x12\x10\n\x08username\x18\x14 \x01(\t\x12\x12\n\ncreated_at\x18\x15 \x01(\x03\x12\x12\n\nupdated_at\x18\x16 \x01(\x03\x12\x18\n\x10github_issue_url\x18\x17 \x01(\t\x12/\n\x06status\x18\x18 \x01(\x0e\x32\x1f.feedback.BugReportProto.Status\x12\x15\n\radmin_comment\x18\x19 \x01(\t\"\x90\x01\n\tFrequency\x12!\n\x1d\x46REQUENCY_UNKNOWN_UNSPECIFIED\x10\x00\x12\x14\n\x10\x46REQUENCY_ALWAYS\x10\x01\x12\x18\n\x14\x46REQUENCY_FREQUENTLY\x10\x02\x12\x1a\n\x16\x46REQUENCY_OCCASIONALLY\x10\x03\x12\x14\n\x10\x46REQUENCY_RARELY\x10\x04\"\x7f\n\x08Severity\x12\"\n\x1eSEVERITY_UNDEFINED_UNSPECIFIED\x10\x00\x12\x10\n\x0cSEVERITY_LOW\x10\x01\x12\x13\n\x0fSEVERITY_MEDIUM\x10\x02\x12\x11\n\rSEVERITY_HIGH\x10\x03\x12\x15\n\x11SEVERITY_CRITICAL\x10\x04\"\x86\x01\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x0f\n\x0bSTATUS_OPEN\x10\x01\x12\x16\n\x12STATUS_IN_PROGRESS\x10\x02\x12\x13\n\x0fSTATUS_RESOLVED\x10\x03\x12\x11\n\rSTATUS_CLOSED\x10\x04\x12\x13\n\x0fSTATUS_REJECTED\x10\x05\"@\n\x13\x42ugReportCollection\x12)\n\x07reports\x18\x01 \x03(\x0b\x32\x18.feedback.BugReportProtob\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'feedback_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals['_BUGREPORTPROTO']._serialized_start = 29
    _globals['_BUGREPORTPROTO']._serialized_end = 1143
    _globals['_BUGREPORTPROTO_FREQUENCY']._serialized_start = 733
    _globals['_BUGREPORTPROTO_FREQUENCY']._serialized_end = 877
    _globals['_BUGREPORTPROTO_SEVERITY']._serialized_start = 879
    _globals['_BUGREPORTPROTO_SEVERITY']._serialized_end = 1006
    _globals['_BUGREPORTPROTO_STATUS']._serialized_start = 1009
    _globals['_BUGREPORTPROTO_STATUS']._serialized_end = 1143
    _globals['_BUGREPORTCOLLECTION']._serialized_start = 1145
    _globals['_BUGREPORTCOLLECTION']._serialized_end = 1209
# @@protoc_insertion_point(module_scope)
