# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: yandex/cloud/monitoring/v3/dashboard_service.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from yandex.cloud.api import operation_pb2 as yandex_dot_cloud_dot_api_dot_operation__pb2
from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.monitoring.v3 import dashboard_pb2 as yandex_dot_cloud_dot_monitoring_dot_v3_dot_dashboard__pb2
from yandex.cloud.monitoring.v3 import parametrization_pb2 as yandex_dot_cloud_dot_monitoring_dot_v3_dot_parametrization__pb2
from yandex.cloud.monitoring.v3 import widget_pb2 as yandex_dot_cloud_dot_monitoring_dot_v3_dot_widget__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/monitoring/v3/dashboard_service.proto\x12\x1ayandex.cloud.monitoring.v3\x1a\x1cgoogle/api/annotations.proto\x1a yandex/cloud/api/operation.proto\x1a&yandex/cloud/operation/operation.proto\x1a\x1dyandex/cloud/validation.proto\x1a*yandex/cloud/monitoring/v3/dashboard.proto\x1a\x30yandex/cloud/monitoring/v3/parametrization.proto\x1a\'yandex/cloud/monitoring/v3/widget.proto\"9\n\x13GetDashboardRequest\x12\"\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\"\xa1\x01\n\x15ListDashboardsRequest\x12!\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50H\x00\x12\x1d\n\tpage_size\x18\x13 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x14 \x01(\tB\t\x8a\xc8\x31\x05<=100\x12\x1a\n\x06\x66ilter\x18\x15 \x01(\tB\n\x8a\xc8\x31\x06<=1000B\x0b\n\tcontainer\"l\n\x16ListDashboardsResponse\x12\x39\n\ndashboards\x18\x01 \x03(\x0b\x32%.yandex.cloud.monitoring.v3.Dashboard\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t\"\x9b\x04\n\x16\x43reateDashboardRequest\x12!\n\tfolder_id\x18\x02 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50H\x00\x12\x32\n\x04name\x18\x13 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x14 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x93\x01\n\x06labels\x18\x15 \x03(\x0b\x32>.yandex.cloud.monitoring.v3.CreateDashboardRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\r\n\x05title\x18\x16 \x01(\t\x12\x33\n\x07widgets\x18\x17 \x03(\x0b\x32\".yandex.cloud.monitoring.v3.Widget\x12\x44\n\x0fparametrization\x18\x18 \x01(\x0b\x32+.yandex.cloud.monitoring.v3.Parametrization\x12\x12\n\nmanaged_by\x18\x1a \x01(\t\x12\x14\n\x0cmanaged_link\x18\x1b \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x42\x0b\n\tcontainerJ\x04\x08\x19\x10\x1a\"/\n\x17\x43reateDashboardMetadata\x12\x14\n\x0c\x64\x61shboard_id\x18\x01 \x01(\t\"\x9d\x04\n\x16UpdateDashboardRequest\x12\"\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x32\n\x04name\x18\x02 \x01(\tB$\xf2\xc7\x31 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?\x12\x1e\n\x0b\x64\x65scription\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=256\x12\x93\x01\n\x06labels\x18\x04 \x03(\x0b\x32>.yandex.cloud.monitoring.v3.UpdateDashboardRequest.LabelsEntryBC\xf2\xc7\x31\x0f[-_./\\@0-9a-z]*\x82\xc8\x31\x04<=64\x8a\xc8\x31\x04<=63\xb2\xc8\x31\x1c\x12\x14[a-z][-_./\\@0-9a-z]*\x1a\x04\x31-63\x12\r\n\x05title\x18\x05 \x01(\t\x12\x33\n\x07widgets\x18\x06 \x03(\x0b\x32\".yandex.cloud.monitoring.v3.Widget\x12\x44\n\x0fparametrization\x18\x07 \x01(\x0b\x32+.yandex.cloud.monitoring.v3.Parametrization\x12\x0c\n\x04\x65tag\x18\x08 \x01(\t\x12\x12\n\nmanaged_by\x18\x1a \x01(\t\x12\x14\n\x0cmanaged_link\x18\x1b \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01J\x04\x08\t\x10\x1a\"/\n\x17UpdateDashboardMetadata\x12\x14\n\x0c\x64\x61shboard_id\x18\x01 \x01(\t\"J\n\x16\x44\x65leteDashboardRequest\x12\"\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x0c\n\x04\x65tag\x18\x02 \x01(\t\"/\n\x17\x44\x65leteDashboardMetadata\x12\x14\n\x0c\x64\x61shboard_id\x18\x01 \x01(\t\"\x82\x01\n\x1eListDashboardOperationsRequest\x12\"\n\x0c\x64\x61shboard_id\x18\x01 \x01(\tB\x0c\xe8\xc7\x31\x01\x8a\xc8\x31\x04<=50\x12\x1d\n\tpage_size\x18\x02 \x01(\x03\x42\n\xfa\xc7\x31\x06<=1000\x12\x1d\n\npage_token\x18\x03 \x01(\tB\t\x8a\xc8\x31\x05<=100\"q\n\x1fListDashboardOperationsResponse\x12\x35\n\noperations\x18\x01 \x03(\x0b\x32!.yandex.cloud.operation.Operation\x12\x17\n\x0fnext_page_token\x18\x02 \x01(\t2\xb7\x08\n\x10\x44\x61shboardService\x12\x8f\x01\n\x03Get\x12/.yandex.cloud.monitoring.v3.GetDashboardRequest\x1a%.yandex.cloud.monitoring.v3.Dashboard\"0\x82\xd3\xe4\x93\x02*\x12(/monitoring/v3/dashboards/{dashboard_id}\x12\x90\x01\n\x04List\x12\x31.yandex.cloud.monitoring.v3.ListDashboardsRequest\x1a\x32.yandex.cloud.monitoring.v3.ListDashboardsResponse\"!\x82\xd3\xe4\x93\x02\x1b\x12\x19/monitoring/v3/dashboards\x12\xad\x01\n\x06\x43reate\x12\x32.yandex.cloud.monitoring.v3.CreateDashboardRequest\x1a!.yandex.cloud.operation.Operation\"L\xb2\xd2*$\n\x17\x43reateDashboardMetadata\x12\tDashboard\x82\xd3\xe4\x93\x02\x1e\"\x19/monitoring/v3/dashboards:\x01*\x12\xbc\x01\n\x06Update\x12\x32.yandex.cloud.monitoring.v3.UpdateDashboardRequest\x1a!.yandex.cloud.operation.Operation\"[\xb2\xd2*$\n\x17UpdateDashboardMetadata\x12\tDashboard\x82\xd3\xe4\x93\x02-2(/monitoring/v3/dashboards/{dashboard_id}:\x01*\x12\xc5\x01\n\x06\x44\x65lete\x12\x32.yandex.cloud.monitoring.v3.DeleteDashboardRequest\x1a!.yandex.cloud.operation.Operation\"d\xb2\xd2*0\n\x17\x44\x65leteDashboardMetadata\x12\x15google.protobuf.Empty\x82\xd3\xe4\x93\x02**(/monitoring/v3/dashboards/{dashboard_id}\x12\xc6\x01\n\x0eListOperations\x12:.yandex.cloud.monitoring.v3.ListDashboardOperationsRequest\x1a;.yandex.cloud.monitoring.v3.ListDashboardOperationsResponse\";\x82\xd3\xe4\x93\x02\x35\x12\x33/monitoring/v3/dashboards/{dashboard_id}/operationsBk\n\x1eyandex.cloud.api.monitoring.v3ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/monitoring/v3;monitoringb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.monitoring.v3.dashboard_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\036yandex.cloud.api.monitoring.v3ZIgithub.com/yandex-cloud/go-genproto/yandex/cloud/monitoring/v3;monitoring'
  _globals['_GETDASHBOARDREQUEST'].fields_by_name['dashboard_id']._loaded_options = None
  _globals['_GETDASHBOARDREQUEST'].fields_by_name['dashboard_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['filter']._loaded_options = None
  _globals['_LISTDASHBOARDSREQUEST'].fields_by_name['filter']._serialized_options = b'\212\3101\006<=1000'
  _globals['_CREATEDASHBOARDREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_CREATEDASHBOARDREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['folder_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_CREATEDASHBOARDREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_UPDATEDASHBOARDREQUEST_LABELSENTRY']._loaded_options = None
  _globals['_UPDATEDASHBOARDREQUEST_LABELSENTRY']._serialized_options = b'8\001'
  _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['dashboard_id']._loaded_options = None
  _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['dashboard_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['name']._loaded_options = None
  _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['name']._serialized_options = b'\362\3071 |[a-z]([-a-z0-9]{0,61}[a-z0-9])?'
  _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['description']._loaded_options = None
  _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['description']._serialized_options = b'\212\3101\005<=256'
  _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['labels']._loaded_options = None
  _globals['_UPDATEDASHBOARDREQUEST'].fields_by_name['labels']._serialized_options = b'\362\3071\017[-_./\\@0-9a-z]*\202\3101\004<=64\212\3101\004<=63\262\3101\034\022\024[a-z][-_./\\@0-9a-z]*\032\0041-63'
  _globals['_DELETEDASHBOARDREQUEST'].fields_by_name['dashboard_id']._loaded_options = None
  _globals['_DELETEDASHBOARDREQUEST'].fields_by_name['dashboard_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDASHBOARDOPERATIONSREQUEST'].fields_by_name['dashboard_id']._loaded_options = None
  _globals['_LISTDASHBOARDOPERATIONSREQUEST'].fields_by_name['dashboard_id']._serialized_options = b'\350\3071\001\212\3101\004<=50'
  _globals['_LISTDASHBOARDOPERATIONSREQUEST'].fields_by_name['page_size']._loaded_options = None
  _globals['_LISTDASHBOARDOPERATIONSREQUEST'].fields_by_name['page_size']._serialized_options = b'\372\3071\006<=1000'
  _globals['_LISTDASHBOARDOPERATIONSREQUEST'].fields_by_name['page_token']._loaded_options = None
  _globals['_LISTDASHBOARDOPERATIONSREQUEST'].fields_by_name['page_token']._serialized_options = b'\212\3101\005<=100'
  _globals['_DASHBOARDSERVICE'].methods_by_name['Get']._loaded_options = None
  _globals['_DASHBOARDSERVICE'].methods_by_name['Get']._serialized_options = b'\202\323\344\223\002*\022(/monitoring/v3/dashboards/{dashboard_id}'
  _globals['_DASHBOARDSERVICE'].methods_by_name['List']._loaded_options = None
  _globals['_DASHBOARDSERVICE'].methods_by_name['List']._serialized_options = b'\202\323\344\223\002\033\022\031/monitoring/v3/dashboards'
  _globals['_DASHBOARDSERVICE'].methods_by_name['Create']._loaded_options = None
  _globals['_DASHBOARDSERVICE'].methods_by_name['Create']._serialized_options = b'\262\322*$\n\027CreateDashboardMetadata\022\tDashboard\202\323\344\223\002\036\"\031/monitoring/v3/dashboards:\001*'
  _globals['_DASHBOARDSERVICE'].methods_by_name['Update']._loaded_options = None
  _globals['_DASHBOARDSERVICE'].methods_by_name['Update']._serialized_options = b'\262\322*$\n\027UpdateDashboardMetadata\022\tDashboard\202\323\344\223\002-2(/monitoring/v3/dashboards/{dashboard_id}:\001*'
  _globals['_DASHBOARDSERVICE'].methods_by_name['Delete']._loaded_options = None
  _globals['_DASHBOARDSERVICE'].methods_by_name['Delete']._serialized_options = b'\262\322*0\n\027DeleteDashboardMetadata\022\025google.protobuf.Empty\202\323\344\223\002**(/monitoring/v3/dashboards/{dashboard_id}'
  _globals['_DASHBOARDSERVICE'].methods_by_name['ListOperations']._loaded_options = None
  _globals['_DASHBOARDSERVICE'].methods_by_name['ListOperations']._serialized_options = b'\202\323\344\223\0025\0223/monitoring/v3/dashboards/{dashboard_id}/operations'
  _globals['_GETDASHBOARDREQUEST']._serialized_start=352
  _globals['_GETDASHBOARDREQUEST']._serialized_end=409
  _globals['_LISTDASHBOARDSREQUEST']._serialized_start=412
  _globals['_LISTDASHBOARDSREQUEST']._serialized_end=573
  _globals['_LISTDASHBOARDSRESPONSE']._serialized_start=575
  _globals['_LISTDASHBOARDSRESPONSE']._serialized_end=683
  _globals['_CREATEDASHBOARDREQUEST']._serialized_start=686
  _globals['_CREATEDASHBOARDREQUEST']._serialized_end=1225
  _globals['_CREATEDASHBOARDREQUEST_LABELSENTRY']._serialized_start=1161
  _globals['_CREATEDASHBOARDREQUEST_LABELSENTRY']._serialized_end=1206
  _globals['_CREATEDASHBOARDMETADATA']._serialized_start=1227
  _globals['_CREATEDASHBOARDMETADATA']._serialized_end=1274
  _globals['_UPDATEDASHBOARDREQUEST']._serialized_start=1277
  _globals['_UPDATEDASHBOARDREQUEST']._serialized_end=1818
  _globals['_UPDATEDASHBOARDREQUEST_LABELSENTRY']._serialized_start=1161
  _globals['_UPDATEDASHBOARDREQUEST_LABELSENTRY']._serialized_end=1206
  _globals['_UPDATEDASHBOARDMETADATA']._serialized_start=1820
  _globals['_UPDATEDASHBOARDMETADATA']._serialized_end=1867
  _globals['_DELETEDASHBOARDREQUEST']._serialized_start=1869
  _globals['_DELETEDASHBOARDREQUEST']._serialized_end=1943
  _globals['_DELETEDASHBOARDMETADATA']._serialized_start=1945
  _globals['_DELETEDASHBOARDMETADATA']._serialized_end=1992
  _globals['_LISTDASHBOARDOPERATIONSREQUEST']._serialized_start=1995
  _globals['_LISTDASHBOARDOPERATIONSREQUEST']._serialized_end=2125
  _globals['_LISTDASHBOARDOPERATIONSRESPONSE']._serialized_start=2127
  _globals['_LISTDASHBOARDOPERATIONSRESPONSE']._serialized_end=2240
  _globals['_DASHBOARDSERVICE']._serialized_start=2243
  _globals['_DASHBOARDSERVICE']._serialized_end=3322
# @@protoc_insertion_point(module_scope)
