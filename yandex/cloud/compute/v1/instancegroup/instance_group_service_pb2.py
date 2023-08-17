# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/compute/v1/instancegroup/instance_group_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import field_mask_pb2 as google_dot_protobuf_dot_field__mask__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.access import access_pb2 as yandex_dot_cloud_dot_access_dot_access__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.compute.v1.instancegroup import instance_group_pb2 as yandex_dot_cloud_dot_compute_dot_v1_dot_instancegroup_dot_instance__group__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\nByandex/cloud/compute/v1/instancegroup/instance_group_service.proto\x12%yandex.cloud.compute.v1.instancegroup\x1a google/protobuf/field_mask.proto\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/access/access.proto\x1a yandex/cloud/api/operation.proto\x1a:yandex/cloud/compute/v1/instancegroup/instance_group.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\"J\n#ResumeInstanceGroupProcessesRequest\x12#\n\x11instance_group_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"?\n\"ResumeInstanceGroupProcessMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"I\n\"PauseInstanceGroupProcessesRequest\x12#\n\x11instance_group_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\">\n!PauseInstanceGroupProcessMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"\x8a\x01\n\x17GetInstanceGroupRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x46\n\x04view\x18\x02 \x01(\x0e\x32\x38.yandex.cloud.compute.v1.instancegroup.InstanceGroupView\"\xc6\x08\n\x1a\x43reateInstanceGroupRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\xa2\x01\n\x06labels\x18\x05 \x03(\x0b\x32M.yandex.cloud.compute.v1.instancegroup.CreateInstanceGroupRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12X\n\x11instance_template\x18\x06 \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.InstanceTemplateB\x04\xe8\xc7\x31\x01\x12N\n\x0cscale_policy\x18\x07 \x01(\x0b\x32\x32.yandex.cloud.compute.v1.instancegroup.ScalePolicyB\x04\xe8\xc7\x31\x01\x12P\n\rdeploy_policy\x18\x08 \x01(\x0b\x32\x33.yandex.cloud.compute.v1.instancegroup.DeployPolicyB\x04\xe8\xc7\x31\x01\x12X\n\x11\x61llocation_policy\x18\t \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.AllocationPolicyB\x04\xe8\xc7\x31\x01\x12S\n\x12load_balancer_spec\x18\n \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.LoadBalancerSpec\x12S\n\x12health_checks_spec\x18\x0b \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.HealthChecksSpec\x12\x1a\n\x12service_account_id\x18\x0c \x01(\t\x12\x42\n\tvariables\x18\r \x03(\x0b\x32/.yandex.cloud.compute.v1.instancegroup.Variable\x12\x1b\n\x13\x64\x65letion_protection\x18\x0e \x01(\x08\x12j\n\x1e\x61pplication_load_balancer_spec\x18\x0f \x01(\x0b\x32\x42.yandex.cloud.compute.v1.instancegroup.ApplicationLoadBalancerSpec\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"m\n\"CreateInstanceGroupFromYamlRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12.\n\x13instance_group_yaml\x18\x02 \x01(\tB\x11\xe8\xc7\x31\x01\x8a\xc8\x31\t<=1048576\"B\n\x1b\x43reateInstanceGroupMetadata\x12#\n\x11instance_group_id\x18\x01 \x01(\tB\x08\x8a\xc8\x31\x04<=50\"\x87\t\n\x1aUpdateInstanceGroupRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12/\n\x0bupdate_mask\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.FieldMask\x12\x32\n\x04name\x18\x03 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x04 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\xa2\x01\n\x06labels\x18\x05 \x03(\x0b\x32M.yandex.cloud.compute.v1.instancegroup.UpdateInstanceGroupRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12X\n\x11instance_template\x18\x06 \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.InstanceTemplateB\x04\xe8\xc7\x31\x01\x12N\n\x0cscale_policy\x18\x07 \x01(\x0b\x32\x32.yandex.cloud.compute.v1.instancegroup.ScalePolicyB\x04\xe8\xc7\x31\x01\x12P\n\rdeploy_policy\x18\x08 \x01(\x0b\x32\x33.yandex.cloud.compute.v1.instancegroup.DeployPolicyB\x04\xe8\xc7\x31\x01\x12X\n\x11\x61llocation_policy\x18\t \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.AllocationPolicyB\x04\xe8\xc7\x31\x01\x12S\n\x12health_checks_spec\x18\x0b \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.HealthChecksSpec\x12\x1a\n\x12service_account_id\x18\x0c \x01(\t\x12S\n\x12load_balancer_spec\x18\x0e \x01(\x0b\x32\x37.yandex.cloud.compute.v1.instancegroup.LoadBalancerSpec\x12\x42\n\tvariables\x18\x0f \x03(\x0b\x32/.yandex.cloud.compute.v1.instancegroup.Variable\x12\x1b\n\x13\x64\x65letion_protection\x18\x10 \x01(\x08\x12j\n\x1e\x61pplication_load_balancer_spec\x18\x11 \x01(\x0b\x32\x42.yandex.cloud.compute.v1.instancegroup.ApplicationLoadBalancerSpec\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"}\n\"UpdateInstanceGroupFromYamlRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12.\n\x13instance_group_yaml\x18\x02 \x01(\tB\x11\xe8\xc7\x31\x01\x8a\xc8\x31\t<=1048576\"8\n\x1bUpdateInstanceGroupMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"D\n\x19StartInstanceGroupRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"7\n\x1aStartInstanceGroupMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"C\n\x18StopInstanceGroupRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"6\n\x19StopInstanceGroupMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"^\n\x15RollingRestartRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\x14managed_instance_ids\x18\x02 \x03(\t\"3\n\x16RollingRestartMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"_\n\x16RollingRecreateRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1c\n\x14managed_instance_ids\x18\x02 \x03(\t\"4\n\x17RollingRecreateMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"E\n\x1a\x44\x65leteInstanceGroupRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"8\n\x1b\x44\x65leteInstanceGroupMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"4\n\x17\x44\x65leteInstancesMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"2\n\x15StopInstancesMetadata\x12\x19\n\x11instance_group_id\x18\x01 \x01(\t\"\xd7\x01\n\x19ListInstanceGroupsRequest\x12\x17\n\tfolder_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x46\n\x04view\x18\x05 \x01(\x0e\x32\x38.yandex.cloud.compute.v1.instancegroup.InstanceGroupView\"\x84\x01\n\x1aListInstanceGroupsResponse\x12M\n\x0finstance_groups\x18\x01 \x03(\x0b\x32\x34.yandex.cloud.compute.v1.instancegroup.InstanceGroup\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa7\x01\n!ListInstanceGroupInstancesRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"\x88\x01\n\"ListInstanceGroupInstancesResponse\x12I\n\tinstances\x18\x01 \x03(\x0b\x32\x36.yandex.cloud.compute.v1.instancegroup.ManagedInstance\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x88\x01\n\x16\x44\x65leteInstancesRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12-\n\x14managed_instance_ids\x18\x02 \x03(\tB\x0f\x82\xc8\x31\x03>=1\x8a\xc8\x31\x04<=50\x12\x16\n\x0e\x63reate_another\x18\x03 \x01(\x08\"n\n\x14StopInstancesRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12-\n\x14managed_instance_ids\x18\x02 \x03(\tB\x0f\x82\xc8\x31\x03>=1\x8a\xc8\x31\x04<=50\"\xa8\x01\n\"ListInstanceGroupOperationsRequest\x12\'\n\x11instance_group_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"u\n#ListInstanceGroupOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\xa0\x01\n\"ListInstanceGroupLogRecordsRequest\x12\x1f\n\x11instance_group_id\x18\x01 \x01(\tB\x04\xe8\xc7\x31\x01\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06\x30-1000\x12\x1e\n\npage_token\x18\x03 \x01(\tB\n\x8a\xc8\x31\x06<=1000\x12\x1a\n\x06\x66ilter\x18\x04 \x01(\tB\n\x8a\xc8\x31\x06<=1000\"\x85\x01\n#ListInstanceGroupLogRecordsResponse\x12\x45\n\x0blog_records\x18\x01 \x03(\x0b\x32\x30.yandex.cloud.compute.v1.instancegroup.LogRecord\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t*(\n\x11InstanceGroupView\x12\t\n\x05\x42\x41SIC\x10\x00\x12\x08\n\x04\x46ULL\x10\x01\x32\x84$\n\x14InstanceGroupService\x12\xb3\x01\n\x03Get\x12>.yandex.cloud.compute.v1.instancegroup.GetInstanceGroupRequest\x1a\x34.yandex.cloud.compute.v1.instancegroup.InstanceGroup\"6\x82\xd3\xe4\x93\x02\x30\x12./compute/v1/instanceGroups/{instance_group_id}\x12\xaf\x01\n\x04List\x12@.yandex.cloud.compute.v1.instancegroup.ListInstanceGroupsRequest\x1a\x41.yandex.cloud.compute.v1.instancegroup.ListInstanceGroupsResponse\"\"\x82\xd3\xe4\x93\x02\x1c\x12\x1a/compute/v1/instanceGroups\x12\xc5\x01\n\x06\x43reate\x12\x41.yandex.cloud.compute.v1.instancegroup.CreateInstanceGroupRequest\x1a!.yandex.cloud.operation.Operation\"U\xb2\xd2*,\n\x1b\x43reateInstanceGroupMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x1f\"\x1a/compute/v1/instanceGroups:\x01*\x12\xda\x01\n\x0e\x43reateFromYaml\x12I.yandex.cloud.compute.v1.instancegroup.CreateInstanceGroupFromYamlRequest\x1a!.yandex.cloud.operation.Operation\"Z\xb2\xd2*,\n\x1b\x43reateInstanceGroupMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02$\"\x1f/compute/v1/instanceGroups:yaml:\x01*\x12\xd9\x01\n\x06Update\x12\x41.yandex.cloud.compute.v1.instancegroup.UpdateInstanceGroupRequest\x1a!.yandex.cloud.operation.Operation\"i\xb2\xd2*,\n\x1bUpdateInstanceGroupMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x33\x32./compute/v1/instanceGroups/{instance_group_id}:\x01*\x12\xee\x01\n\x0eUpdateFromYaml\x12I.yandex.cloud.compute.v1.instancegroup.UpdateInstanceGroupFromYamlRequest\x1a!.yandex.cloud.operation.Operation\"n\xb2\xd2*,\n\x1bUpdateInstanceGroupMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x38\x32\x33/compute/v1/instanceGroups/{instance_group_id}:yaml:\x01*\x12\xd5\x01\n\x04Stop\x12?.yandex.cloud.compute.v1.instancegroup.StopInstanceGroupRequest\x1a!.yandex.cloud.operation.Operation\"i\xb2\xd2**\n\x19StopInstanceGroupMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x35\"3/compute/v1/instanceGroups/{instance_group_id}:stop\x12\xe6\x01\n\x0eRollingRestart\x12<.yandex.cloud.compute.v1.instancegroup.RollingRestartRequest\x1a!.yandex.cloud.operation.Operation\"s\xb2\xd2*\'\n\x16RollingRestartMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x42\"=/compute/v1/instanceGroups/{instance_group_id}:rollingRestart:\x01*\x12\xea\x01\n\x0fRollingRecreate\x12=.yandex.cloud.compute.v1.instancegroup.RollingRecreateRequest\x1a!.yandex.cloud.operation.Operation\"u\xb2\xd2*(\n\x17RollingRecreateMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x43\">/compute/v1/instanceGroups/{instance_group_id}:rollingRecreate:\x01*\x12\xd9\x01\n\x05Start\x12@.yandex.cloud.compute.v1.instancegroup.StartInstanceGroupRequest\x1a!.yandex.cloud.operation.Operation\"k\xb2\xd2*+\n\x1aStartInstanceGroupMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x36\"4/compute/v1/instanceGroups/{instance_group_id}:start\x12\xde\x01\n\x06\x44\x65lete\x12\x41.yandex.cloud.compute.v1.instancegroup.DeleteInstanceGroupRequest\x1a!.yandex.cloud.operation.Operation\"n\xb2\xd2*4\n\x1b\x44\x65leteInstanceGroupMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x30*./compute/v1/instanceGroups/{instance_group_id}\x12\xe6\x01\n\rListInstances\x12H.yandex.cloud.compute.v1.instancegroup.ListInstanceGroupInstancesRequest\x1aI.yandex.cloud.compute.v1.instancegroup.ListInstanceGroupInstancesResponse\"@\x82\xd3\xe4\x93\x02:\x12\x38/compute/v1/instanceGroups/{instance_group_id}/instances\x12\xa1\x01\n\x0f\x44\x65leteInstances\x12=.yandex.cloud.compute.v1.instancegroup.DeleteInstancesRequest\x1a!.yandex.cloud.operation.Operation\",\xb2\xd2*(\n\x17\x44\x65leteInstancesMetadata\x12\rInstanceGroup\x12\x9b\x01\n\rStopInstances\x12;.yandex.cloud.compute.v1.instancegroup.StopInstancesRequest\x1a!.yandex.cloud.operation.Operation\"*\xb2\xd2*&\n\x15StopInstancesMetadata\x12\rInstanceGroup\x12\xea\x01\n\x0eListOperations\x12I.yandex.cloud.compute.v1.instancegroup.ListInstanceGroupOperationsRequest\x1aJ.yandex.cloud.compute.v1.instancegroup.ListInstanceGroupOperationsResponse\"A\x82\xd3\xe4\x93\x02;\x12\x39/compute/v1/instanceGroups/{instance_group_id}/operations\x12\xe4\x01\n\x0eListLogRecords\x12I.yandex.cloud.compute.v1.instancegroup.ListInstanceGroupLogRecordsRequest\x1aJ.yandex.cloud.compute.v1.instancegroup.ListInstanceGroupLogRecordsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/compute/v1/instanceGroups/{instance_group_id}:logs\x12\xba\x01\n\x12ListAccessBindings\x12..yandex.cloud.access.ListAccessBindingsRequest\x1a/.yandex.cloud.access.ListAccessBindingsResponse\"C\x82\xd3\xe4\x93\x02=\x12;/compute/v1/instanceGroups/{resource_id}:listAccessBindings\x12\xea\x01\n\x11SetAccessBindings\x12-.yandex.cloud.access.SetAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x82\x01\xb2\xd2*9\n access.SetAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02?\":/compute/v1/instanceGroups/{resource_id}:setAccessBindings:\x01*\x12\xf6\x01\n\x14UpdateAccessBindings\x12\x30.yandex.cloud.access.UpdateAccessBindingsRequest\x1a!.yandex.cloud.operation.Operation\"\x88\x01\xb2\xd2*<\n#access.UpdateAccessBindingsMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02\x42\"=/compute/v1/instanceGroups/{resource_id}:updateAccessBindings:\x01*\x12\x83\x02\n\x0fResumeProcesses\x12J.yandex.cloud.compute.v1.instancegroup.ResumeInstanceGroupProcessesRequest\x1a!.yandex.cloud.operation.Operation\"\x80\x01\xb2\xd2*3\n\"ResumeInstanceGroupProcessMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x43\">/compute/v1/instanceGroups/{instance_group_id}:resumeProcesses:\x01*\x12\xfe\x01\n\x0ePauseProcesses\x12I.yandex.cloud.compute.v1.instancegroup.PauseInstanceGroupProcessesRequest\x1a!.yandex.cloud.operation.Operation\"~\xb2\xd2*2\n!PauseInstanceGroupProcessMetadata\x12\rInstanceGroup\x82\xd3\xe4\x93\x02\x42\"=/compute/v1/instanceGroups/{instance_group_id}:pauseProcesses:\x01*B\x84\x01\n)yandex.cloud.api.compute.v1.instancegroupZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1/instancegroup;instancegroupb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.compute.v1.instancegroup.instance_group_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n)yandex.cloud.api.compute.v1.instancegroupZWgithub.com/yandex-cloud/go-genproto/yandex/cloud/compute/v1/instancegroup;instancegroup'
  _RESUMEINSTANCEGROUPPROCESSESREQUEST.fields_by_name['instance_group_id']._options = None
  _RESUMEINSTANCEGROUPPROCESSESREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\212\3101\004<=50'
  _PAUSEINSTANCEGROUPPROCESSESREQUEST.fields_by_name['instance_group_id']._options = None
  _PAUSEINSTANCEGROUPPROCESSESREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\212\3101\004<=50'
  _GETINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._options = None
  _GETINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _CREATEINSTANCEGROUPREQUEST_LABELSENTRY._options = None
  _CREATEINSTANCEGROUPREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['folder_id']._options = None
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['name']._options = None
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['description']._options = None
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['labels']._options = None
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['instance_template']._options = None
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['instance_template']._serialized_options = b'\350\3071\001'
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['scale_policy']._options = None
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['scale_policy']._serialized_options = b'\350\3071\001'
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['deploy_policy']._options = None
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['deploy_policy']._serialized_options = b'\350\3071\001'
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['allocation_policy']._options = None
  _CREATEINSTANCEGROUPREQUEST.fields_by_name['allocation_policy']._serialized_options = b'\350\3071\001'
  _CREATEINSTANCEGROUPFROMYAMLREQUEST.fields_by_name['folder_id']._options = None
  _CREATEINSTANCEGROUPFROMYAMLREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _CREATEINSTANCEGROUPFROMYAMLREQUEST.fields_by_name['instance_group_yaml']._options = None
  _CREATEINSTANCEGROUPFROMYAMLREQUEST.fields_by_name['instance_group_yaml']._serialized_options = b'\350\3071\001\212\3101\t<=1048576'
  _CREATEINSTANCEGROUPMETADATA.fields_by_name['instance_group_id']._options = None
  _CREATEINSTANCEGROUPMETADATA.fields_by_name['instance_group_id']._serialized_options = b'\212\3101\004<=50'
  _UPDATEINSTANCEGROUPREQUEST_LABELSENTRY._options = None
  _UPDATEINSTANCEGROUPREQUEST_LABELSENTRY._serialized_options = b'8\001'
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._options = None
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['name']._options = None
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['description']._options = None
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['labels']._options = None
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['instance_template']._options = None
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['instance_template']._serialized_options = b'\350\3071\001'
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['scale_policy']._options = None
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['scale_policy']._serialized_options = b'\350\3071\001'
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['deploy_policy']._options = None
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['deploy_policy']._serialized_options = b'\350\3071\001'
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['allocation_policy']._options = None
  _UPDATEINSTANCEGROUPREQUEST.fields_by_name['allocation_policy']._serialized_options = b'\350\3071\001'
  _UPDATEINSTANCEGROUPFROMYAMLREQUEST.fields_by_name['instance_group_id']._options = None
  _UPDATEINSTANCEGROUPFROMYAMLREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _UPDATEINSTANCEGROUPFROMYAMLREQUEST.fields_by_name['instance_group_yaml']._options = None
  _UPDATEINSTANCEGROUPFROMYAMLREQUEST.fields_by_name['instance_group_yaml']._serialized_options = b'\350\3071\001\212\3101\t<=1048576'
  _STARTINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._options = None
  _STARTINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _STOPINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._options = None
  _STOPINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ROLLINGRESTARTREQUEST.fields_by_name['instance_group_id']._options = None
  _ROLLINGRESTARTREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _ROLLINGRECREATEREQUEST.fields_by_name['instance_group_id']._options = None
  _ROLLINGRECREATEREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._options = None
  _DELETEINSTANCEGROUPREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTINSTANCEGROUPSREQUEST.fields_by_name['folder_id']._options = None
  _LISTINSTANCEGROUPSREQUEST.fields_by_name['folder_id']._serialized_options = b'\350\3071\001'
  _LISTINSTANCEGROUPSREQUEST.fields_by_name['page_size']._options = None
  _LISTINSTANCEGROUPSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTINSTANCEGROUPSREQUEST.fields_by_name['page_token']._options = None
  _LISTINSTANCEGROUPSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=1000'
  _LISTINSTANCEGROUPSREQUEST.fields_by_name['filter']._options = None
  _LISTINSTANCEGROUPSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTINSTANCEGROUPINSTANCESREQUEST.fields_by_name['instance_group_id']._options = None
  _LISTINSTANCEGROUPINSTANCESREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTINSTANCEGROUPINSTANCESREQUEST.fields_by_name['page_size']._options = None
  _LISTINSTANCEGROUPINSTANCESREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _LISTINSTANCEGROUPINSTANCESREQUEST.fields_by_name['page_token']._options = None
  _LISTINSTANCEGROUPINSTANCESREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=1000'
  _LISTINSTANCEGROUPINSTANCESREQUEST.fields_by_name['filter']._options = None
  _LISTINSTANCEGROUPINSTANCESREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _DELETEINSTANCESREQUEST.fields_by_name['instance_group_id']._options = None
  _DELETEINSTANCESREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _DELETEINSTANCESREQUEST.fields_by_name['managed_instance_ids']._options = None
  _DELETEINSTANCESREQUEST.fields_by_name['managed_instance_ids']._serialized_options = b'\202\3101\003>=1\212\3101\004<=50'
  _STOPINSTANCESREQUEST.fields_by_name['instance_group_id']._options = None
  _STOPINSTANCESREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _STOPINSTANCESREQUEST.fields_by_name['managed_instance_ids']._options = None
  _STOPINSTANCESREQUEST.fields_by_name['managed_instance_ids']._serialized_options = b'\202\3101\003>=1\212\3101\004<=50'
  _LISTINSTANCEGROUPOPERATIONSREQUEST.fields_by_name['instance_group_id']._options = None
  _LISTINSTANCEGROUPOPERATIONSREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _LISTINSTANCEGROUPOPERATIONSREQUEST.fields_by_name['page_size']._options = None
  _LISTINSTANCEGROUPOPERATIONSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTINSTANCEGROUPOPERATIONSREQUEST.fields_by_name['page_token']._options = None
  _LISTINSTANCEGROUPOPERATIONSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=1000'
  _LISTINSTANCEGROUPOPERATIONSREQUEST.fields_by_name['filter']._options = None
  _LISTINSTANCEGROUPOPERATIONSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _LISTINSTANCEGROUPLOGRECORDSREQUEST.fields_by_name['instance_group_id']._options = None
  _LISTINSTANCEGROUPLOGRECORDSREQUEST.fields_by_name['instance_group_id']._serialized_options = b'\350\3071\001'
  _LISTINSTANCEGROUPLOGRECORDSREQUEST.fields_by_name['page_size']._options = None
  _LISTINSTANCEGROUPLOGRECORDSREQUEST.fields_by_name['page_size']._serialized_options = b'\372\3071\0060-1000'
  _LISTINSTANCEGROUPLOGRECORDSREQUEST.fields_by_name['page_token']._options = None
  _LISTINSTANCEGROUPLOGRECORDSREQUEST.fields_by_name['page_token']._serialized_options = b'\212\3101\006<=1000'
  _LISTINSTANCEGROUPLOGRECORDSREQUEST.fields_by_name['filter']._options = None
  _LISTINSTANCEGROUPLOGRECORDSREQUEST.fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _INSTANCEGROUPSERVICE.methods_by_name['Get']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['Get']._serialized_options = b'\202\323\344\223\0020\022./compute/v1/instanceGroups/{instance_group_id}'
  _INSTANCEGROUPSERVICE.methods_by_name['List']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['List']._serialized_options = b'\202\323\344\223\002\034\022\032/compute/v1/instanceGroups'
  _INSTANCEGROUPSERVICE.methods_by_name['Create']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['Create']._serialized_options = b'\262\322*,\n\033CreateInstanceGroupMetadata\022\rInstanceGroup\202\323\344\223\002\037\"\032/compute/v1/instanceGroups:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['CreateFromYaml']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['CreateFromYaml']._serialized_options = b'\262\322*,\n\033CreateInstanceGroupMetadata\022\rInstanceGroup\202\323\344\223\002$\"\037/compute/v1/instanceGroups:yaml:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['Update']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['Update']._serialized_options = b'\262\322*,\n\033UpdateInstanceGroupMetadata\022\rInstanceGroup\202\323\344\223\00232./compute/v1/instanceGroups/{instance_group_id}:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['UpdateFromYaml']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['UpdateFromYaml']._serialized_options = b'\262\322*,\n\033UpdateInstanceGroupMetadata\022\rInstanceGroup\202\323\344\223\002823/compute/v1/instanceGroups/{instance_group_id}:yaml:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['Stop']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['Stop']._serialized_options = b'\262\322**\n\031StopInstanceGroupMetadata\022\rInstanceGroup\202\323\344\223\0025\"3/compute/v1/instanceGroups/{instance_group_id}:stop'
  _INSTANCEGROUPSERVICE.methods_by_name['RollingRestart']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['RollingRestart']._serialized_options = b'\262\322*\'\n\026RollingRestartMetadata\022\rInstanceGroup\202\323\344\223\002B\"=/compute/v1/instanceGroups/{instance_group_id}:rollingRestart:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['RollingRecreate']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['RollingRecreate']._serialized_options = b'\262\322*(\n\027RollingRecreateMetadata\022\rInstanceGroup\202\323\344\223\002C\">/compute/v1/instanceGroups/{instance_group_id}:rollingRecreate:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['Start']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['Start']._serialized_options = b'\262\322*+\n\032StartInstanceGroupMetadata\022\rInstanceGroup\202\323\344\223\0026\"4/compute/v1/instanceGroups/{instance_group_id}:start'
  _INSTANCEGROUPSERVICE.methods_by_name['Delete']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['Delete']._serialized_options = b'\262\322*4\n\033DeleteInstanceGroupMetadata\022\025google.protobuf.Empty\202\323\344\223\0020*./compute/v1/instanceGroups/{instance_group_id}'
  _INSTANCEGROUPSERVICE.methods_by_name['ListInstances']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['ListInstances']._serialized_options = b'\202\323\344\223\002:\0228/compute/v1/instanceGroups/{instance_group_id}/instances'
  _INSTANCEGROUPSERVICE.methods_by_name['DeleteInstances']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['DeleteInstances']._serialized_options = b'\262\322*(\n\027DeleteInstancesMetadata\022\rInstanceGroup'
  _INSTANCEGROUPSERVICE.methods_by_name['StopInstances']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['StopInstances']._serialized_options = b'\262\322*&\n\025StopInstancesMetadata\022\rInstanceGroup'
  _INSTANCEGROUPSERVICE.methods_by_name['ListOperations']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\002;\0229/compute/v1/instanceGroups/{instance_group_id}/operations'
  _INSTANCEGROUPSERVICE.methods_by_name['ListLogRecords']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['ListLogRecords']._serialized_options = b'\202\323\344\223\0025\0223/compute/v1/instanceGroups/{instance_group_id}:logs'
  _INSTANCEGROUPSERVICE.methods_by_name['ListAccessBindings']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['ListAccessBindings']._serialized_options = b'\202\323\344\223\002=\022;/compute/v1/instanceGroups/{resource_id}:listAccessBindings'
  _INSTANCEGROUPSERVICE.methods_by_name['SetAccessBindings']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['SetAccessBindings']._serialized_options = b'\262\322*9\n access.SetAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002?\":/compute/v1/instanceGroups/{resource_id}:setAccessBindings:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['UpdateAccessBindings']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['UpdateAccessBindings']._serialized_options = b'\262\322*<\n#access.UpdateAccessBindingsMetadata\022\025google.protobuf.Empty\202\323\344\223\002B\"=/compute/v1/instanceGroups/{resource_id}:updateAccessBindings:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['ResumeProcesses']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['ResumeProcesses']._serialized_options = b'\262\322*3\n\"ResumeInstanceGroupProcessMetadata\022\rInstanceGroup\202\323\344\223\002C\">/compute/v1/instanceGroups/{instance_group_id}:resumeProcesses:\001*'
  _INSTANCEGROUPSERVICE.methods_by_name['PauseProcesses']._options = None
  _INSTANCEGROUPSERVICE.methods_by_name['PauseProcesses']._serialized_options = b'\262\322*2\n!PauseInstanceGroupProcessMetadata\022\rInstanceGroup\202\323\344\223\002B\"=/compute/v1/instanceGroups/{instance_group_id}:pauseProcesses:\001*'
  _globals['_INSTANCEGROUPVIEW']._serialized_start=5705
  _globals['_INSTANCEGROUPVIEW']._serialized_end=5745
  _globals['_RESUMEINSTANCEGROUPPROCESSESREQUEST']._serialized_start=372
  _globals['_RESUMEINSTANCEGROUPPROCESSESREQUEST']._serialized_end=446
  _globals['_RESUMEINSTANCEGROUPPROCESSMETADATA']._serialized_start=448
  _globals['_RESUMEINSTANCEGROUPPROCESSMETADATA']._serialized_end=511
  _globals['_PAUSEINSTANCEGROUPPROCESSESREQUEST']._serialized_start=513
  _globals['_PAUSEINSTANCEGROUPPROCESSESREQUEST']._serialized_end=586
  _globals['_PAUSEINSTANCEGROUPPROCESSMETADATA']._serialized_start=588
  _globals['_PAUSEINSTANCEGROUPPROCESSMETADATA']._serialized_end=650
  _globals['_GETINSTANCEGROUPREQUEST']._serialized_start=653
  _globals['_GETINSTANCEGROUPREQUEST']._serialized_end=791
  _globals['_CREATEINSTANCEGROUPREQUEST']._serialized_start=794
  _globals['_CREATEINSTANCEGROUPREQUEST']._serialized_end=1888
  _globals['_CREATEINSTANCEGROUPREQUEST_LABELSENTRY']._serialized_start=1843
  _globals['_CREATEINSTANCEGROUPREQUEST_LABELSENTRY']._serialized_end=1888
  _globals['_CREATEINSTANCEGROUPFROMYAMLREQUEST']._serialized_start=1890
  _globals['_CREATEINSTANCEGROUPFROMYAMLREQUEST']._serialized_end=1999
  _globals['_CREATEINSTANCEGROUPMETADATA']._serialized_start=2001
  _globals['_CREATEINSTANCEGROUPMETADATA']._serialized_end=2067
  _globals['_UPDATEINSTANCEGROUPREQUEST']._serialized_start=2070
  _globals['_UPDATEINSTANCEGROUPREQUEST']._serialized_end=3229
  _globals['_UPDATEINSTANCEGROUPREQUEST_LABELSENTRY']._serialized_start=1843
  _globals['_UPDATEINSTANCEGROUPREQUEST_LABELSENTRY']._serialized_end=1888
  _globals['_UPDATEINSTANCEGROUPFROMYAMLREQUEST']._serialized_start=3231
  _globals['_UPDATEINSTANCEGROUPFROMYAMLREQUEST']._serialized_end=3356
  _globals['_UPDATEINSTANCEGROUPMETADATA']._serialized_start=3358
  _globals['_UPDATEINSTANCEGROUPMETADATA']._serialized_end=3414
  _globals['_STARTINSTANCEGROUPREQUEST']._serialized_start=3416
  _globals['_STARTINSTANCEGROUPREQUEST']._serialized_end=3484
  _globals['_STARTINSTANCEGROUPMETADATA']._serialized_start=3486
  _globals['_STARTINSTANCEGROUPMETADATA']._serialized_end=3541
  _globals['_STOPINSTANCEGROUPREQUEST']._serialized_start=3543
  _globals['_STOPINSTANCEGROUPREQUEST']._serialized_end=3610
  _globals['_STOPINSTANCEGROUPMETADATA']._serialized_start=3612
  _globals['_STOPINSTANCEGROUPMETADATA']._serialized_end=3666
  _globals['_ROLLINGRESTARTREQUEST']._serialized_start=3668
  _globals['_ROLLINGRESTARTREQUEST']._serialized_end=3762
  _globals['_ROLLINGRESTARTMETADATA']._serialized_start=3764
  _globals['_ROLLINGRESTARTMETADATA']._serialized_end=3815
  _globals['_ROLLINGRECREATEREQUEST']._serialized_start=3817
  _globals['_ROLLINGRECREATEREQUEST']._serialized_end=3912
  _globals['_ROLLINGRECREATEMETADATA']._serialized_start=3914
  _globals['_ROLLINGRECREATEMETADATA']._serialized_end=3966
  _globals['_DELETEINSTANCEGROUPREQUEST']._serialized_start=3968
  _globals['_DELETEINSTANCEGROUPREQUEST']._serialized_end=4037
  _globals['_DELETEINSTANCEGROUPMETADATA']._serialized_start=4039
  _globals['_DELETEINSTANCEGROUPMETADATA']._serialized_end=4095
  _globals['_DELETEINSTANCESMETADATA']._serialized_start=4097
  _globals['_DELETEINSTANCESMETADATA']._serialized_end=4149
  _globals['_STOPINSTANCESMETADATA']._serialized_start=4151
  _globals['_STOPINSTANCESMETADATA']._serialized_end=4201
  _globals['_LISTINSTANCEGROUPSREQUEST']._serialized_start=4204
  _globals['_LISTINSTANCEGROUPSREQUEST']._serialized_end=4419
  _globals['_LISTINSTANCEGROUPSRESPONSE']._serialized_start=4422
  _globals['_LISTINSTANCEGROUPSRESPONSE']._serialized_end=4554
  _globals['_LISTINSTANCEGROUPINSTANCESREQUEST']._serialized_start=4557
  _globals['_LISTINSTANCEGROUPINSTANCESREQUEST']._serialized_end=4724
  _globals['_LISTINSTANCEGROUPINSTANCESRESPONSE']._serialized_start=4727
  _globals['_LISTINSTANCEGROUPINSTANCESRESPONSE']._serialized_end=4863
  _globals['_DELETEINSTANCESREQUEST']._serialized_start=4866
  _globals['_DELETEINSTANCESREQUEST']._serialized_end=5002
  _globals['_STOPINSTANCESREQUEST']._serialized_start=5004
  _globals['_STOPINSTANCESREQUEST']._serialized_end=5114
  _globals['_LISTINSTANCEGROUPOPERATIONSREQUEST']._serialized_start=5117
  _globals['_LISTINSTANCEGROUPOPERATIONSREQUEST']._serialized_end=5285
  _globals['_LISTINSTANCEGROUPOPERATIONSRESPONSE']._serialized_start=5287
  _globals['_LISTINSTANCEGROUPOPERATIONSRESPONSE']._serialized_end=5404
  _globals['_LISTINSTANCEGROUPLOGRECORDSREQUEST']._serialized_start=5407
  _globals['_LISTINSTANCEGROUPLOGRECORDSREQUEST']._serialized_end=5567
  _globals['_LISTINSTANCEGROUPLOGRECORDSRESPONSE']._serialized_start=5570
  _globals['_LISTINSTANCEGROUPLOGRECORDSRESPONSE']._serialized_end=5703
  _globals['_INSTANCEGROUPSERVICE']._serialized_start=5748
  _globals['_INSTANCEGROUPSERVICE']._serialized_end=10360
# @@protoc_insertion_point(module_scope)
