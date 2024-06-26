# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/smartwebsecurity/v1/security_profile.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n7yandex/cloud/smartwebsecurity/v1/security_profile.proto\x12 yandex.cloud.smartwebsecurity.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dyandex/cloud/validation.proto\"\x8f\x05\n\x0fSecurityProfile\x12\n\n\x02id\x18\x01 \x01(\t\x12\x11\n\tfolder_id\x18\x02 \x01(\t\x12\x10\n\x08\x63loud_id\x18\n \x01(\t\x12\x8a\x01\n\x06labels\x18\x03 \x03(\x0b\x32=.yandex.cloud.smartwebsecurity.v1.SecurityProfile.LabelsEntryB;\xf2\xc7\x31\x0b[-_0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x18\x12\x10[a-z][-_0-9a-z]*\x1a\x04\x31-63\x12\x38\n\x04name\x18\x04 \x01(\tB*\xe8\xc7\x31\x01\xf2\xc7\x31\x1a[a-zA-Z0-9][a-zA-Z0-9-_.]*\x8a\xc8\x31\x04\x31-50\x12\x1e\n\x0b\x64\x65scription\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05<=512\x12]\n\x0e\x64\x65\x66\x61ult_action\x18\x06 \x01(\x0e\x32?.yandex.cloud.smartwebsecurity.v1.SecurityProfile.DefaultActionB\x04\xe8\xc7\x31\x01\x12\x46\n\x0esecurity_rules\x18\x07 \x03(\x0b\x32..yandex.cloud.smartwebsecurity.v1.SecurityRule\x12.\n\ncreated_at\x18\x08 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x12\n\ncaptcha_id\x18\x0b \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"D\n\rDefaultAction\x12\x1e\n\x1a\x44\x45\x46\x41ULT_ACTION_UNSPECIFIED\x10\x00\x12\t\n\x05\x41LLOW\x10\x01\x12\x08\n\x04\x44\x45NY\x10\x02J\x04\x08\t\x10\n\"\x9b\x06\n\x0cSecurityRule\x12\x38\n\x04name\x18\x01 \x01(\tB*\xe8\xc7\x31\x01\xf2\xc7\x31\x1a[a-zA-Z0-9][a-zA-Z0-9-_.]*\x8a\xc8\x31\x04\x31-50\x12\x1e\n\x08priority\x18\x02 \x01(\x03\x42\x0c\xfa\xc7\x31\x08\x31-999999\x12\x0f\n\x07\x64ry_run\x18\x03 \x01(\x08\x12V\n\x0erule_condition\x18\x04 \x01(\x0b\x32<.yandex.cloud.smartwebsecurity.v1.SecurityRule.RuleConditionH\x00\x12Z\n\x10smart_protection\x18\x05 \x01(\x0b\x32>.yandex.cloud.smartwebsecurity.v1.SecurityRule.SmartProtectionH\x00\x12\x1e\n\x0b\x64\x65scription\x18\x07 \x01(\tB\t\x8a\xc8\x31\x05<=512\x1a\xdb\x01\n\rRuleCondition\x12S\n\x06\x61\x63tion\x18\x01 \x01(\x0e\x32\x43.yandex.cloud.smartwebsecurity.v1.SecurityRule.RuleCondition.Action\x12>\n\tcondition\x18\x02 \x01(\x0b\x32+.yandex.cloud.smartwebsecurity.v1.Condition\"5\n\x06\x41\x63tion\x12\x16\n\x12\x41\x43TION_UNSPECIFIED\x10\x00\x12\t\n\x05\x41LLOW\x10\x01\x12\x08\n\x04\x44\x45NY\x10\x02\x1a\xd5\x01\n\x0fSmartProtection\x12Q\n\x04mode\x18\x01 \x01(\x0e\x32\x43.yandex.cloud.smartwebsecurity.v1.SecurityRule.SmartProtection.Mode\x12>\n\tcondition\x18\x02 \x01(\x0b\x32+.yandex.cloud.smartwebsecurity.v1.Condition\"/\n\x04Mode\x12\x14\n\x10MODE_UNSPECIFIED\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x12\x07\n\x03\x41PI\x10\x02\x42\x10\n\x0erule_specifierJ\x04\x08\x06\x10\x07\"\xf9\r\n\tCondition\x12O\n\tauthority\x18\x01 \x01(\x0b\x32<.yandex.cloud.smartwebsecurity.v1.Condition.AuthorityMatcher\x12R\n\x0bhttp_method\x18\x02 \x01(\x0b\x32=.yandex.cloud.smartwebsecurity.v1.Condition.HttpMethodMatcher\x12R\n\x0brequest_uri\x18\x03 \x01(\x0b\x32=.yandex.cloud.smartwebsecurity.v1.Condition.RequestUriMatcher\x12T\n\x07headers\x18\x04 \x03(\x0b\x32\x39.yandex.cloud.smartwebsecurity.v1.Condition.HeaderMatcherB\x08\x82\xc8\x31\x04<=20\x12H\n\tsource_ip\x18\x05 \x01(\x0b\x32\x35.yandex.cloud.smartwebsecurity.v1.Condition.IpMatcher\x1a\xfc\x01\n\rStringMatcher\x12 \n\x0b\x65xact_match\x18\x01 \x01(\tB\t\x8a\xc8\x31\x05\x30-255H\x00\x12$\n\x0f\x65xact_not_match\x18\x02 \x01(\tB\t\x8a\xc8\x31\x05\x30-255H\x00\x12!\n\x0cprefix_match\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05\x30-255H\x00\x12%\n\x10prefix_not_match\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05\x30-255H\x00\x12%\n\x10pire_regex_match\x18\x05 \x01(\tB\t\x8a\xc8\x31\x05\x30-255H\x00\x12)\n\x14pire_regex_not_match\x18\x06 \x01(\tB\t\x8a\xc8\x31\x05\x30-255H\x00\x42\x07\n\x05match\x1an\n\x11HttpMethodMatcher\x12Y\n\x0chttp_methods\x18\x01 \x03(\x0b\x32\x39.yandex.cloud.smartwebsecurity.v1.Condition.StringMatcherB\x08\x82\xc8\x31\x04<=20\x1al\n\x10\x41uthorityMatcher\x12X\n\x0b\x61uthorities\x18\x01 \x03(\x0b\x32\x39.yandex.cloud.smartwebsecurity.v1.Condition.StringMatcherB\x08\x82\xc8\x31\x04<=20\x1a\xb1\x01\n\x11RequestUriMatcher\x12G\n\x04path\x18\x01 \x01(\x0b\x32\x39.yandex.cloud.smartwebsecurity.v1.Condition.StringMatcher\x12S\n\x07queries\x18\x02 \x03(\x0b\x32\x38.yandex.cloud.smartwebsecurity.v1.Condition.QueryMatcherB\x08\x82\xc8\x31\x04<=20\x1az\n\x0cQueryMatcher\x12\x1a\n\x03key\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x31-255\x12N\n\x05value\x18\x02 \x01(\x0b\x32\x39.yandex.cloud.smartwebsecurity.v1.Condition.StringMatcherB\x04\xe8\xc7\x31\x01\x1a|\n\rHeaderMatcher\x12\x1b\n\x04name\x18\x01 \x01(\tB\r\xe8\xc7\x31\x01\x8a\xc8\x31\x05\x31-255\x12N\n\x05value\x18\x02 \x01(\x0b\x32\x39.yandex.cloud.smartwebsecurity.v1.Condition.StringMatcherB\x04\xe8\xc7\x31\x01\x1a\xdf\x02\n\tIpMatcher\x12T\n\x0fip_ranges_match\x18\x01 \x01(\x0b\x32;.yandex.cloud.smartwebsecurity.v1.Condition.IpRangesMatcher\x12X\n\x13ip_ranges_not_match\x18\x02 \x01(\x0b\x32;.yandex.cloud.smartwebsecurity.v1.Condition.IpRangesMatcher\x12N\n\x0cgeo_ip_match\x18\x03 \x01(\x0b\x32\x38.yandex.cloud.smartwebsecurity.v1.Condition.GeoIpMatcher\x12R\n\x10geo_ip_not_match\x18\x04 \x01(\x0b\x32\x38.yandex.cloud.smartwebsecurity.v1.Condition.GeoIpMatcher\x1a\x31\n\x0fIpRangesMatcher\x12\x1e\n\tip_ranges\x18\x01 \x03(\tB\x0b\x82\xc8\x31\x07<=10000\x1a\x33\n\x0cGeoIpMatcher\x12#\n\tlocations\x18\x01 \x03(\tB\x10\x82\xc8\x31\x03>=1\x8a\xc8\x31\x01\x32\x90\xc8\x31\x01\x42}\n$yandex.cloud.api.smartwebsecurity.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/smartwebsecurity/v1;smartwebsecurityb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.smartwebsecurity.v1.security_profile_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n$yandex.cloud.api.smartwebsecurity.v1ZUgithub.com/yandex-cloud/go-genproto/yandex/cloud/smartwebsecurity/v1;smartwebsecurity'
  _SECURITYPROFILE_LABELSENTRY._options = None
  _SECURITYPROFILE_LABELSENTRY._serialized_options = b'8\001'
  _SECURITYPROFILE.fields_by_name['labels']._options = None
  _SECURITYPROFILE.fields_by_name['labels']._serialized_options = b'\362\3071\013[-_0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\030\022\020[a-z][-_0-9a-z]*\032\0041-63'
  _SECURITYPROFILE.fields_by_name['name']._options = None
  _SECURITYPROFILE.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\032[a-zA-Z0-9][a-zA-Z0-9-_.]*\212\3101\0041-50'
  _SECURITYPROFILE.fields_by_name['description']._options = None
  _SECURITYPROFILE.fields_by_name['description']._serialized_options = b'\212\3101\005<=512'
  _SECURITYPROFILE.fields_by_name['default_action']._options = None
  _SECURITYPROFILE.fields_by_name['default_action']._serialized_options = b'\350\3071\001'
  _SECURITYRULE.fields_by_name['name']._options = None
  _SECURITYRULE.fields_by_name['name']._serialized_options = b'\350\3071\001\362\3071\032[a-zA-Z0-9][a-zA-Z0-9-_.]*\212\3101\0041-50'
  _SECURITYRULE.fields_by_name['priority']._options = None
  _SECURITYRULE.fields_by_name['priority']._serialized_options = b'\372\3071\0101-999999'
  _SECURITYRULE.fields_by_name['description']._options = None
  _SECURITYRULE.fields_by_name['description']._serialized_options = b'\212\3101\005<=512'
  _CONDITION_STRINGMATCHER.fields_by_name['exact_match']._options = None
  _CONDITION_STRINGMATCHER.fields_by_name['exact_match']._serialized_options = b'\212\3101\0050-255'
  _CONDITION_STRINGMATCHER.fields_by_name['exact_not_match']._options = None
  _CONDITION_STRINGMATCHER.fields_by_name['exact_not_match']._serialized_options = b'\212\3101\0050-255'
  _CONDITION_STRINGMATCHER.fields_by_name['prefix_match']._options = None
  _CONDITION_STRINGMATCHER.fields_by_name['prefix_match']._serialized_options = b'\212\3101\0050-255'
  _CONDITION_STRINGMATCHER.fields_by_name['prefix_not_match']._options = None
  _CONDITION_STRINGMATCHER.fields_by_name['prefix_not_match']._serialized_options = b'\212\3101\0050-255'
  _CONDITION_STRINGMATCHER.fields_by_name['pire_regex_match']._options = None
  _CONDITION_STRINGMATCHER.fields_by_name['pire_regex_match']._serialized_options = b'\212\3101\0050-255'
  _CONDITION_STRINGMATCHER.fields_by_name['pire_regex_not_match']._options = None
  _CONDITION_STRINGMATCHER.fields_by_name['pire_regex_not_match']._serialized_options = b'\212\3101\0050-255'
  _CONDITION_HTTPMETHODMATCHER.fields_by_name['http_methods']._options = None
  _CONDITION_HTTPMETHODMATCHER.fields_by_name['http_methods']._serialized_options = b'\202\3101\004<=20'
  _CONDITION_AUTHORITYMATCHER.fields_by_name['authorities']._options = None
  _CONDITION_AUTHORITYMATCHER.fields_by_name['authorities']._serialized_options = b'\202\3101\004<=20'
  _CONDITION_REQUESTURIMATCHER.fields_by_name['queries']._options = None
  _CONDITION_REQUESTURIMATCHER.fields_by_name['queries']._serialized_options = b'\202\3101\004<=20'
  _CONDITION_QUERYMATCHER.fields_by_name['key']._options = None
  _CONDITION_QUERYMATCHER.fields_by_name['key']._serialized_options = b'\350\3071\001\212\3101\0051-255'
  _CONDITION_QUERYMATCHER.fields_by_name['value']._options = None
  _CONDITION_QUERYMATCHER.fields_by_name['value']._serialized_options = b'\350\3071\001'
  _CONDITION_HEADERMATCHER.fields_by_name['name']._options = None
  _CONDITION_HEADERMATCHER.fields_by_name['name']._serialized_options = b'\350\3071\001\212\3101\0051-255'
  _CONDITION_HEADERMATCHER.fields_by_name['value']._options = None
  _CONDITION_HEADERMATCHER.fields_by_name['value']._serialized_options = b'\350\3071\001'
  _CONDITION_IPRANGESMATCHER.fields_by_name['ip_ranges']._options = None
  _CONDITION_IPRANGESMATCHER.fields_by_name['ip_ranges']._serialized_options = b'\202\3101\007<=10000'
  _CONDITION_GEOIPMATCHER.fields_by_name['locations']._options = None
  _CONDITION_GEOIPMATCHER.fields_by_name['locations']._serialized_options = b'\202\3101\003>=1\212\3101\0012\220\3101\001'
  _CONDITION.fields_by_name['headers']._options = None
  _CONDITION.fields_by_name['headers']._serialized_options = b'\202\3101\004<=20'
  _globals['_SECURITYPROFILE']._serialized_start=158
  _globals['_SECURITYPROFILE']._serialized_end=813
  _globals['_SECURITYPROFILE_LABELSENTRY']._serialized_start=692
  _globals['_SECURITYPROFILE_LABELSENTRY']._serialized_end=737
  _globals['_SECURITYPROFILE_DEFAULTACTION']._serialized_start=739
  _globals['_SECURITYPROFILE_DEFAULTACTION']._serialized_end=807
  _globals['_SECURITYRULE']._serialized_start=816
  _globals['_SECURITYRULE']._serialized_end=1611
  _globals['_SECURITYRULE_RULECONDITION']._serialized_start=1152
  _globals['_SECURITYRULE_RULECONDITION']._serialized_end=1371
  _globals['_SECURITYRULE_RULECONDITION_ACTION']._serialized_start=1318
  _globals['_SECURITYRULE_RULECONDITION_ACTION']._serialized_end=1371
  _globals['_SECURITYRULE_SMARTPROTECTION']._serialized_start=1374
  _globals['_SECURITYRULE_SMARTPROTECTION']._serialized_end=1587
  _globals['_SECURITYRULE_SMARTPROTECTION_MODE']._serialized_start=1540
  _globals['_SECURITYRULE_SMARTPROTECTION_MODE']._serialized_end=1587
  _globals['_CONDITION']._serialized_start=1614
  _globals['_CONDITION']._serialized_end=3399
  _globals['_CONDITION_STRINGMATCHER']._serialized_start=2037
  _globals['_CONDITION_STRINGMATCHER']._serialized_end=2289
  _globals['_CONDITION_HTTPMETHODMATCHER']._serialized_start=2291
  _globals['_CONDITION_HTTPMETHODMATCHER']._serialized_end=2401
  _globals['_CONDITION_AUTHORITYMATCHER']._serialized_start=2403
  _globals['_CONDITION_AUTHORITYMATCHER']._serialized_end=2511
  _globals['_CONDITION_REQUESTURIMATCHER']._serialized_start=2514
  _globals['_CONDITION_REQUESTURIMATCHER']._serialized_end=2691
  _globals['_CONDITION_QUERYMATCHER']._serialized_start=2693
  _globals['_CONDITION_QUERYMATCHER']._serialized_end=2815
  _globals['_CONDITION_HEADERMATCHER']._serialized_start=2817
  _globals['_CONDITION_HEADERMATCHER']._serialized_end=2941
  _globals['_CONDITION_IPMATCHER']._serialized_start=2944
  _globals['_CONDITION_IPMATCHER']._serialized_end=3295
  _globals['_CONDITION_IPRANGESMATCHER']._serialized_start=3297
  _globals['_CONDITION_IPRANGESMATCHER']._serialized_end=3346
  _globals['_CONDITION_GEOIPMATCHER']._serialized_start=3348
  _globals['_CONDITION_GEOIPMATCHER']._serialized_end=3399
# @@protoc_insertion_point(module_scope)
