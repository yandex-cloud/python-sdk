# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/datasphere/v2/community_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.datasphere.v2 import community_pb2 as yandex_dot_cloud_dot_datasphere_dot_v2_dot_community__pb2
from yandex.cloud.datasphere.v2 import resource_types_pb2 as yandex_dot_cloud_dot_datasphere_dot_v2_dot_resource__types__pb2
from yandex.cloud.datasphere.v2 import restrictions_pb2 as yandex_dot_cloud_dot_datasphere_dot_v2_dot_restrictions__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/datasphere/v2/community_service.proto\x12\x1ayandex.cloud.datasphere.v2\x1a\x1cgoogle/api/annotations.proto\x1a\x1bgoogle/protobuf/empty.proto\x1a google/protobuf/field_mask.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a&yandex/cloud/operation/operation.proto\x1a*yandex/cloud/datasphere/v2/community.proto\x1a/yandex/cloud/datasphere/v2/resource_types.proto\x1a-yandex/cloud/datasphere/v2/restrictions.proto\"\xca\x02\n\x16\x43reateCommunityRequest\x12J\n\x04name\x18\x01 \x01(\tB<\xf2\xc7\x31\x30[a-zA-Z0-9\xd0\x81\xd1\x91\xd0\x90-\xd1\x8f]\\S{1,61}[a-zA-Z0-9\xd0\x81\xd1\x91\xd0\x90-\xd1\x8f]\x8a\xc8\x31\x04<=63\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x1d\n\x0forganization_id\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1a\n\x12\x62illing_account_id\x18\x04 \x01(\t\x12N\n\x06labels\x18\x05 \x03(\x0b\x32>.yandex.cloud.datasphere.v2.CreateCommunityRequest.LabelsEntry\x12\x15\n\x07zone_id\x18\x06 \x01(\tB\x04\xe8\xc7\x31\x01\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"/\n\x17\x43reateCommunityMetadata\x12\x14\n\x0c\x63ommunity_id\x18\x01 \x01(\t\"1\n\x13GetCommunityRequest\x12\x1a\n\x0c\x63ommunity_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"\x87\x02\n\x16UpdateCommunityRequest\x12\x1a\n\x0c\x63ommunity_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x04 \x01(\t\x12N\n\x06labels\x18\x05 \x03(\x0b\x32>.yandex.cloud.datasphere.v2.UpdateCommunityRequest.LabelsEntry\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"/\n\x17UpdateCommunityMetadata\x12\x14\n\x0c\x63ommunity_id\x18\x01 \x01(\t\"4\n\x16\x44\x65leteCommunityRequest\x12\x1a\n\x0c\x63ommunity_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"/\n\x17\x44\x65leteCommunityMetadata\x12\x14\n\x0c\x63ommunity_id\x18\x01 \x01(\t\"\xb3\x01\n\x16ListCommunitiesRequest\x12\x11\n\tpage_size\x18\x01 \x01(\x03\x12\x12\n\npage_token\x18\x02 \x01(\t\x12#\n\x1bname_or_description_pattern\x18\x03 \x01(\t\x12\x13\n\x0bowned_by_id\x18\x05 \x01(\t\x12\x13\n\x0blist_public\x18\x06 \x01(\x08\x12\x1d\n\x0forganization_id\x18\x07 \x01(\tB\x04\xe8\xc7\x31\x01J\x04\x08\x04\x10\x05\"n\n\x17ListCommunitiesResponse\x12:\n\x0b\x63ommunities\x18\x01 \x03(\x0b\x32%.yandex.cloud.datasphere.v2.Community\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\":\n\"SetCommunityAccessBindingsMetadata\x12\x14\n\x0c\x63ommunity_id\x18\x01 \x01(\t\"=\n%UpdateCommunityAccessBindingsMetadata\x12\x14\n\x0c\x63ommunity_id\x18\x01 \x01(\t\"\xa3\x01\n\x1b\x41\x64\x64\x43ommunityResourceRequest\x12\"\n\x0c\x63ommunity_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x45\n\rresource_type\x18\x02 \x01(\x0e\x32(.yandex.cloud.datasphere.v2.ResourceTypeB\x04\xe8\xc7\x31\x01\x12\x19\n\x0bresource_id\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01\"\xa6\x01\n\x1eRemoveCommunityResourceRequest\x12\"\n\x0c\x63ommunity_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x45\n\rresource_type\x18\x02 \x01(\x0e\x32(.yandex.cloud.datasphere.v2.ResourceTypeB\x04\xe8\xc7\x31\x01\x12\x19\n\x0bresource_id\x18\x03 \x01(\tB\x04\xe8\xc7\x31\x01\"=\n\x1fGetCommunityRestrictionsRequest\x12\x1a\n\x0c\x63ommunity_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\"|\n\x1fSetCommunityRestrictionsRequest\x12\x1a\n\x0c\x63ommunity_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12=\n\x0crestrictions\x18\x02 \x03(\x0b\x32\'.yandex.cloud.datasphere.v2.Restriction2\xe6\x13\n\x10\x43ommunityService\x12\xae\x01\n\x06\x43reate\x12\x32.yandex.cloud.datasphere.v2.CreateCommunityRequest\x1a!.yandex.cloud.operation.Operation\"M\xb2\xd2*$\n\x17\x43reateCommunityMetadata\x12\tCommunity\x82\xd3\xe4\x93\x02\x1f\"\x1a/datasphere/v2/communities:\x01*\x12\x90\x01\n\x03Get\x12/.yandex.cloud.datasphere.v2.GetCommunityRequest\x1a%.yandex.cloud.datasphere.v2.Community\"1\x82\xd3\xe4\x93\x02+\x12)/datasphere/v2/communities/{community_id}\x12\xbd\x01\n\x06Update\x12\x32.yandex.cloud.datasphere.v2.UpdateCommunityRequest\x1a!.yandex.cloud.operation.Operation\"\\\xb2\xd2*$\n\x17UpdateCommunityMetadata\x12\tCommunity\x82\xd3\xe4\x93\x02.2)/datasphere/v2/communities/{community_id}:\x01*\x12\xc6\x01\n\x06\x44\x65lete\x12\x32.yandex.cloud.datasphere.v2.DeleteCommunityRequest\x1a!.yandex.cloud.operation.Operation\"e\xb2\xd2*0\n\x17\x44\x65leteCommunityMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02+*)/datasphere/v2/communities/{community_id}\x12\x93\x01\n\x04List\x12\x32.yandex.cloud.datasphere.v2.ListCommunitiesRequest\x1a\x33.yandex.cloud.datasphere.v2.ListCommunitiesResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/datasphere/v2/communities\x12\xb6\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"?\x82\xd3\xe4\x93\x02\x39\x12\x37/datasphere/v2/communities/{resource_id}:accessBindings\x12\xec\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x84\x01\xb2\xd2*;\n\"SetCommunityAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02?\":/datasphere/v2/communities/{resource_id}:setAccessBindings:\x01*\x12\xf8\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x8a\x01\xb2\xd2*>\n%UpdateCommunityAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x42\x32=/datasphere/v2/communities/{resource_id}:updateAccessBindings:\x01*\x12\xc5\x01\n\x0b\x41\x64\x64Resource\x12\x37.yandex.cloud.datasphere.v2.AddCommunityResourceRequest\x1a!.yandex.cloud.operation.Operation\"Z\xb2\xd2*\x17\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x39\"4/datasphere/v2/communities/{resource_id}:addResource:\x01*\x12\xce\x01\n\x0eRemoveResource\x12:.yandex.cloud.datasphere.v2.RemoveCommunityResourceRequest\x1a!.yandex.cloud.operation.Operation\"]\xb2\xd2*\x17\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02<\"7/datasphere/v2/communities/{resource_id}:removeResource:\x01*\x12\x9b\x01\n\x13GetRestrictionsMeta\x12\x16.google.protobuf.Empty\x1a\x37.yandex.cloud.datasphere.v2.GetRestrictionsMetaResponse\"3\x82\xd3\xe4\x93\x02-\x12+/datasphere/v2/communities/restrictionsMeta\x12\xc0\x01\n\x0fGetRestrictions\x12;.yandex.cloud.datasphere.v2.GetCommunityRestrictionsRequest\x1a\x30.yandex.cloud.datasphere.v2.RestrictionsResponse\">\x82\xd3\xe4\x93\x02\x38\x12\x36/datasphere/v2/communities/{community_id}:restrictions\x12\xd1\x01\n\x0fSetRestrictions\x12;.yandex.cloud.datasphere.v2.SetCommunityRestrictionsRequest\x1a!.yandex.cloud.operation.Operation\"^\xb2\xd2*\x16\x12\x14RestrictionsResponse\x82\xd3\xe4\x93\x02>\"9/datasphere/v2/communities/{community_id}:setRestrictions:\x01*Bk\n\x1eyandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphereb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.datasphere.v2.community_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\036yandex.cloud.api.datasphere.v2ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/datasphere/v2;datasphere'
  _CREATECOMMUNITYREQUEST_LABELSENTRY._options = None
  _CREATECOMMUNITYREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATECOMMUNITYREQUEST.fields_by_name['name']._options = None
  _CREATECOMMUNITYREQUEST.fields_by_name['name']._serialized_options = b'\362\30710[a-zA-Z0-9\320\201\321\221\320\220-\321\217]\\S{1,61}[a-zA-Z0-9\320\201\321\221\320\220-\321\217]\212\3101\004<=63'
  _CREATECOMMUNITYREQUEST.fields_by_name['organization_id']._options = None
  _CREATECOMMUNITYREQUEST.fields_by_name['organization_id']._serialized_options = b'\350\3071\001'
  _CREATECOMMUNITYREQUEST.fields_by_name['zone_id']._options = None
  _CREATECOMMUNITYREQUEST.fields_by_name['zone_id']._serialized_options = b'\350\3071\001'
  _GETCOMMUNITYREQUEST.fields_by_name['community_id']._options = None
  _GETCOMMUNITYREQUEST.fields_by_name['community_id']._serialized_options = b'\350\3071\001'
  _UPDATECOMMUNITYREQUEST_LABELSENTRY._options = None
  _UPDATECOMMUNITYREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATECOMMUNITYREQUEST.fields_by_name['community_id']._options = None
  _UPDATECOMMUNITYREQUEST.fields_by_name['community_id']._serialized_options = b'\350\3071\001'
  _DELETECOMMUNITYREQUEST.fields_by_name['community_id']._options = None
  _DELETECOMMUNITYREQUEST.fields_by_name['community_id']._serialized_options = b'\350\3071\001'
  _LISTCOMMUNITIESREQUEST.fields_by_name['organization_id']._options = None
  _LISTCOMMUNITIESREQUEST.fields_by_name['organization_id']._serialized_options = b'\350\3071\001'
  _ADDCOMMUNITYRESOURCEREQUEST.fields_by_name['community_id']._options = None
  _ADDCOMMUNITYRESOURCEREQUEST.fields_by_name['community_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ADDCOMMUNITYRESOURCEREQUEST.fields_by_name['resource_type']._options = None
  _ADDCOMMUNITYRESOURCEREQUEST.fields_by_name['resource_type']._serialized_options = b'\350\3071\001'
  _ADDCOMMUNITYRESOURCEREQUEST.fields_by_name['resource_id']._options = None
  _ADDCOMMUNITYRESOURCEREQUEST.fields_by_name['resource_id']._serialized_options = b'\350\3071\001'
  _REMOVECOMMUNITYRESOURCEREQUEST.fields_by_name['community_id']._options = None
  _REMOVECOMMUNITYRESOURCEREQUEST.fields_by_name['community_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _REMOVECOMMUNITYRESOURCEREQUEST.fields_by_name['resource_type']._options = None
  _REMOVECOMMUNITYRESOURCEREQUEST.fields_by_name['resource_type']._serialized_options = b'\350\3071\001'
  _REMOVECOMMUNITYRESOURCEREQUEST.fields_by_name['resource_id']._options = None
  _REMOVECOMMUNITYRESOURCEREQUEST.fields_by_name['resource_id']._serialized_options = b'\350\3071\001'
  _GETCOMMUNITYRESTRICTIONSREQUEST.fields_by_name['community_id']._options = None
  _GETCOMMUNITYRESTRICTIONSREQUEST.fields_by_name['community_id']._serialized_options = b'\350\3071\001'
  _SETCOMMUNITYRESTRICTIONSREQUEST.fields_by_name['community_id']._options = None
  _SETCOMMUNITYRESTRICTIONSREQUEST.fields_by_name['community_id']._serialized_options = b'\350\3071\001'
  _COMMUNITYSERVICE.methods_by_name['Create']._options = None
  _COMMUNITYSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*$\n\027CreateCommunityMetadata\022\tCommunity\202\323\344\223\002\037\"\032/datasphere/v2/communities:\001*'
  _COMMUNITYSERVICE.methods_by_name['Get']._options = None
  _COMMUNITYSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\002+\022)/datasphere/v2/communities/{community_id}'
  _COMMUNITYSERVICE.methods_by_name['Update']._options = None
  _COMMUNITYSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*$\n\027UpdateCommunityMetadata\022\tCommunity\202\323\344\223\002.2)/datasphere/v2/communities/{community_id}:\001*'
  _COMMUNITYSERVICE.methods_by_name['Delete']._options = None
  _COMMUNITYSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*0\n\027DeleteCommunityMetadata\022\025google.protobuf.Empty\202\323\344\223\002+*)/datasphere/v2/communities/{community_id}'
  _COMMUNITYSERVICE.methods_by_name['List']._options = None
  _COMMUNITYSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\034\022\032/datasphere/v2/communities'
  _COMMUNITYSERVICE.methods_by_name['ListAccessBindings']._options = None
  _COMMUNITYSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\0029\0227/datasphere/v2/communities/{resource_id}:accessBindings'
  _COMMUNITYSERVICE.methods_by_name['SetAccessBindings']._options = None
  _COMMUNITYSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*;\n\"SetCommunityAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002?\":/datasphere/v2/communities/{resource_id}:setAccessBindings:\001*'
  _COMMUNITYSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _COMMUNITYSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*>\n%UpdateCommunityAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002B2=/datasphere/v2/communities/{resource_id}:updateAccessBindings:\001*'
  _COMMUNITYSERVICE.methods_by_name['AddResource']._options = None
  _COMMUNITYSERVICE.methods_by_name['AddResource']._serialized_options = b'\262\322*\027\022\025google.protobuf.Empty\202\323\344\223\0029\"4/datasphere/v2/communities/{resource_id}:addResource:\001*'
  _COMMUNITYSERVICE.methods_by_name['RemoveResource']._options = None
  _COMMUNITYSERVICE.methods_by_name['RemoveResource']._serialized_options = b'\262\322*\027\022\025google.protobuf.Empty\202\323\344\223\002<\"7/datasphere/v2/communities/{resource_id}:removeResource:\001*'
  _COMMUNITYSERVICE.methods_by_name['GetRestrictionsMeta']._options = None
  _COMMUNITYSERVICE.methods_by_name['GetRestrictionsMeta']._serialized_options = b'\202\323\344\223\002-\022+/datasphere/v2/communities/restrictionsMeta'
  _COMMUNITYSERVICE.methods_by_name['GetRestrictions']._options = None
  _COMMUNITYSERVICE.methods_by_name['GetRestrictions']._serialized_options = b'\202\323\344\223\0028\0226/datasphere/v2/communities/{community_id}:restrictions'
  _COMMUNITYSERVICE.methods_by_name['SetRestrictions']._options = None
  _COMMUNITYSERVICE.methods_by_name['SetRestrictions']._serialized_options = b'\262\322*\026\022\024RestrictionsResponse\202\323\344\223\002>\"9/datasphere/v2/communities/{community_id}:setRestrictions:\001*'
  _globals['_CREATECOMMUNITYREQUEST']._serialized_start=455
  _globals['_CREATECOMMUNITYREQUEST']._serialized_end=785
  _globals['_CREATECOMMUNITYREQUEST_LABELSENTRY']._serialized_start=740
  _globals['_CREATECOMMUNITYREQUEST_LABELSENTRY']._serialized_end=785
  _globals['_CREATECOMMUNITYMETADATA']._serialized_start=787
  _globals['_CREATECOMMUNITYMETADATA']._serialized_end=834
  _globals['_GETCOMMUNITYREQUEST']._serialized_start=836
  _globals['_GETCOMMUNITYREQUEST']._serialized_end=885
  _globals['_UPDATECOMMUNITYREQUEST']._serialized_start=888
  _globals['_UPDATECOMMUNITYREQUEST']._serialized_end=1151
  _globals['_UPDATECOMMUNITYREQUEST_LABELSENTRY']._serialized_start=740
  _globals['_UPDATECOMMUNITYREQUEST_LABELSENTRY']._serialized_end=785
  _globals['_UPDATECOMMUNITYMETADATA']._serialized_start=1153
  _globals['_UPDATECOMMUNITYMETADATA']._serialized_end=1200
  _globals['_DELETECOMMUNITYREQUEST']._serialized_start=1202
  _globals['_DELETECOMMUNITYREQUEST']._serialized_end=1254
  _globals['_DELETECOMMUNITYMETADATA']._serialized_start=1256
  _globals['_DELETECOMMUNITYMETADATA']._serialized_end=1303
  _globals['_LISTCOMMUNITIESREQUEST']._serialized_start=1306
  _globals['_LISTCOMMUNITIESREQUEST']._serialized_end=1485
  _globals['_LISTCOMMUNITIESRESPONSE']._serialized_start=1487
  _globals['_LISTCOMMUNITIESRESPONSE']._serialized_end=1597
  _globals['_SETCOMMUNITYACCESSBINDINGSMETADATA']._serialized_start=1599
  _globals['_SETCOMMUNITYACCESSBINDINGSMETADATA']._serialized_end=1657
  _globals['_UPDATECOMMUNITYACCESSBINDINGSMETADATA']._serialized_start=1659
  _globals['_UPDATECOMMUNITYACCESSBINDINGSMETADATA']._serialized_end=1720
  _globals['_ADDCOMMUNITYRESOURCEREQUEST']._serialized_start=1723
  _globals['_ADDCOMMUNITYRESOURCEREQUEST']._serialized_end=1886
  _globals['_REMOVECOMMUNITYRESOURCEREQUEST']._serialized_start=1889
  _globals['_REMOVECOMMUNITYRESOURCEREQUEST']._serialized_end=2055
  _globals['_GETCOMMUNITYRESTRICTIONSREQUEST']._serialized_start=2057
  _globals['_GETCOMMUNITYRESTRICTIONSREQUEST']._serialized_end=2118
  _globals['_SETCOMMUNITYRESTRICTIONSREQUEST']._serialized_start=2120
  _globals['_SETCOMMUNITYRESTRICTIONSREQUEST']._serialized_end=2244
  _globals['_COMMUNITYSERVICE']._serialized_start=2247
  _globals['_COMMUNITYSERVICE']._serialized_end=4781
# @@protoc_insertion_point(module_scope)
