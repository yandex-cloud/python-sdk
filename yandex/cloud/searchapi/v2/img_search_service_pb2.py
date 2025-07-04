# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: yandex/cloud/searchapi/v2/img_search_service.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'yandex/cloud/searchapi/v2/img_search_service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from yandex.cloud import validation_pb2 as yandex_dot_cloud_dot_validation__pb2
from yandex.cloud.searchapi.v2 import search_query_pb2 as yandex_dot_cloud_dot_searchapi_dot_v2_dot_search__query__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n2yandex/cloud/searchapi/v2/img_search_service.proto\x12\x19yandex.cloud.searchapi.v2\x1a\x1dyandex/cloud/validation.proto\x1a,yandex/cloud/searchapi/v2/search_query.proto\x1a\x1cgoogle/api/annotations.proto\"\x80\x08\n\tImageSpec\x12@\n\x06\x66ormat\x18\x01 \x01(\x0e\x32\x30.yandex.cloud.searchapi.v2.ImageSpec.ImageFormat\x12<\n\x04size\x18\x02 \x01(\x0e\x32..yandex.cloud.searchapi.v2.ImageSpec.ImageSize\x12J\n\x0borientation\x18\x03 \x01(\x0e\x32\x35.yandex.cloud.searchapi.v2.ImageSpec.ImageOrientation\x12>\n\x05\x63olor\x18\x04 \x01(\x0e\x32/.yandex.cloud.searchapi.v2.ImageSpec.ImageColor\"n\n\x0bImageFormat\x12\x1c\n\x18IMAGE_FORMAT_UNSPECIFIED\x10\x00\x12\x15\n\x11IMAGE_FORMAT_JPEG\x10\x01\x12\x14\n\x10IMAGE_FORMAT_GIF\x10\x02\x12\x14\n\x10IMAGE_FORMAT_PNG\x10\x03\"\x95\x01\n\x10ImageOrientation\x12!\n\x1dIMAGE_ORIENTATION_UNSPECIFIED\x10\x00\x12\x1e\n\x1aIMAGE_ORIENTATION_VERTICAL\x10\x01\x12 \n\x1cIMAGE_ORIENTATION_HORIZONTAL\x10\x02\x12\x1c\n\x18IMAGE_ORIENTATION_SQUARE\x10\x03\"\xb2\x01\n\tImageSize\x12\x1a\n\x16IMAGE_SIZE_UNSPECIFIED\x10\x00\x12\x17\n\x13IMAGE_SIZE_ENORMOUS\x10\x01\x12\x14\n\x10IMAGE_SIZE_LARGE\x10\x02\x12\x15\n\x11IMAGE_SIZE_MEDIUM\x10\x03\x12\x14\n\x10IMAGE_SIZE_SMALL\x10\x04\x12\x13\n\x0fIMAGE_SIZE_TINY\x10\x05\x12\x18\n\x14IMAGE_SIZE_WALLPAPER\x10\x06\"\xa9\x02\n\nImageColor\x12\x1b\n\x17IMAGE_COLOR_UNSPECIFIED\x10\x00\x12\x15\n\x11IMAGE_COLOR_COLOR\x10\x01\x12\x19\n\x15IMAGE_COLOR_GRAYSCALE\x10\x02\x12\x13\n\x0fIMAGE_COLOR_RED\x10\x03\x12\x16\n\x12IMAGE_COLOR_ORANGE\x10\x04\x12\x16\n\x12IMAGE_COLOR_YELLOW\x10\x05\x12\x15\n\x11IMAGE_COLOR_GREEN\x10\x06\x12\x14\n\x10IMAGE_COLOR_CYAN\x10\x07\x12\x14\n\x10IMAGE_COLOR_BLUE\x10\x08\x12\x16\n\x12IMAGE_COLOR_VIOLET\x10\t\x12\x15\n\x11IMAGE_COLOR_WHITE\x10\n\x12\x15\n\x11IMAGE_COLOR_BLACK\x10\x0b\"\xf6\x01\n\x12ImageSearchRequest\x12;\n\x05query\x18\x01 \x01(\x0b\x32&.yandex.cloud.searchapi.v2.SearchQueryB\x04\xe8\xc7\x31\x01\x12\x38\n\nimage_spec\x18\x02 \x01(\x0b\x32$.yandex.cloud.searchapi.v2.ImageSpec\x12\x0c\n\x04site\x18\x03 \x01(\t\x12\x1f\n\x0c\x64ocs_on_page\x18\x04 \x01(\x03\x42\t\xfa\xc7\x31\x05\x31-100\x12\x1b\n\tfolder_id\x18\x05 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\nuser_agent\x18\x06 \x01(\tB\t\x8a\xc8\x31\x05<=200\"-\n\x13ImageSearchResponse\x12\x16\n\x08raw_data\x18\x01 \x01(\x0c\x42\x04\xe8\xc7\x31\x01\"\x9a\x02\n\x19ImageSearchByImageRequest\x12\x18\n\x04site\x18\x01 \x01(\tB\n\x8a\xc8\x31\x06<=1024\x12\x1b\n\tfolder_id\x18\x02 \x01(\tB\x08\x8a\xc8\x31\x04<=50\x12\x1d\n\x03url\x18\x03 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=1024H\x00\x12!\n\x04\x64\x61ta\x18\x04 \x01(\x0c\x42\x11\xe8\xc7\x31\x01\x8a\xc8\x31\t<=3145728H\x00\x12\x1c\n\x02id\x18\x05 \x01(\tB\x0e\xe8\xc7\x31\x01\x8a\xc8\x31\x06<=1024H\x00\x12\x15\n\x04page\x18\x06 \x01(\x03\x42\x07\xfa\xc7\x31\x03>=0\x12\x46\n\x0b\x66\x61mily_mode\x18\x07 \x01(\x0e\x32\x31.yandex.cloud.searchapi.v2.SearchQuery.FamilyModeB\x07\n\x05image\"\xda\x02\n\x1aImageSearchByImageResponse\x12O\n\x06images\x18\x01 \x03(\x0b\x32?.yandex.cloud.searchapi.v2.ImageSearchByImageResponse.ImageInfo\x12\x0c\n\x04page\x18\x02 \x01(\x03\x12\x10\n\x08max_page\x18\x03 \x01(\x03\x12\n\n\x02id\x18\x04 \x01(\t\x1a\xbe\x01\n\tImageInfo\x12\x0b\n\x03url\x18\x01 \x01(\t\x12@\n\x06\x66ormat\x18\x02 \x01(\x0e\x32\x30.yandex.cloud.searchapi.v2.ImageSpec.ImageFormat\x12\r\n\x05width\x18\x03 \x01(\x03\x12\x0e\n\x06height\x18\x04 \x01(\x03\x12\x0f\n\x07passage\x18\x05 \x01(\t\x12\x0c\n\x04host\x18\x06 \x01(\t\x12\x12\n\npage_title\x18\x07 \x01(\t\x12\x10\n\x08page_url\x18\x08 \x01(\t2\xc0\x02\n\x12ImageSearchService\x12\x84\x01\n\x06Search\x12-.yandex.cloud.searchapi.v2.ImageSearchRequest\x1a..yandex.cloud.searchapi.v2.ImageSearchResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v2/image/search:\x01*\x12\xa2\x01\n\rSearchByImage\x12\x34.yandex.cloud.searchapi.v2.ImageSearchByImageRequest\x1a\x35.yandex.cloud.searchapi.v2.ImageSearchByImageResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v2/image/search_by_image:\x01*Be\n\x1ayandex.cloud.api.search.v2ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/searchapi/v2;searchapib\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'yandex.cloud.searchapi.v2.img_search_service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\032yandex.cloud.api.search.v2ZGgithub.com/yandex-cloud/go-genproto/yandex/cloud/searchapi/v2;searchapi'
  _globals['_IMAGESEARCHREQUEST'].fields_by_name['query']._loaded_options = None
  _globals['_IMAGESEARCHREQUEST'].fields_by_name['query']._serialized_options = b'\350\3071\001'
  _globals['_IMAGESEARCHREQUEST'].fields_by_name['docs_on_page']._loaded_options = None
  _globals['_IMAGESEARCHREQUEST'].fields_by_name['docs_on_page']._serialized_options = b'\372\3071\0051-100'
  _globals['_IMAGESEARCHREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_IMAGESEARCHREQUEST'].fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_IMAGESEARCHREQUEST'].fields_by_name['user_agent']._loaded_options = None
  _globals['_IMAGESEARCHREQUEST'].fields_by_name['user_agent']._serialized_options = b'\212\3101\005<=200'
  _globals['_IMAGESEARCHRESPONSE'].fields_by_name['raw_data']._loaded_options = None
  _globals['_IMAGESEARCHRESPONSE'].fields_by_name['raw_data']._serialized_options = b'\350\3071\001'
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['site']._loaded_options = None
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['site']._serialized_options = b'\212\3101\006<=1024'
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['folder_id']._loaded_options = None
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['folder_id']._serialized_options = b'\212\3101\004<=50'
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['url']._loaded_options = None
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['url']._serialized_options = b'\350\3071\001\212\3101\006<=1024'
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['data']._loaded_options = None
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['data']._serialized_options = b'\350\3071\001\212\3101\t<=3145728'
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['id']._loaded_options = None
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['id']._serialized_options = b'\350\3071\001\212\3101\006<=1024'
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['page']._loaded_options = None
  _globals['_IMAGESEARCHBYIMAGEREQUEST'].fields_by_name['page']._serialized_options = b'\372\3071\003>=0'
  _globals['_IMAGESEARCHSERVICE'].methods_by_name['Search']._loaded_options = None
  _globals['_IMAGESEARCHSERVICE'].methods_by_name['Search']._serialized_options = b'\202\323\344\223\002\025\"\020/v2/image/search:\001*'
  _globals['_IMAGESEARCHSERVICE'].methods_by_name['SearchByImage']._loaded_options = None
  _globals['_IMAGESEARCHSERVICE'].methods_by_name['SearchByImage']._serialized_options = b'\202\323\344\223\002\036\"\031/v2/image/search_by_image:\001*'
  _globals['_IMAGESPEC']._serialized_start=189
  _globals['_IMAGESPEC']._serialized_end=1213
  _globals['_IMAGESPEC_IMAGEFORMAT']._serialized_start=470
  _globals['_IMAGESPEC_IMAGEFORMAT']._serialized_end=580
  _globals['_IMAGESPEC_IMAGEORIENTATION']._serialized_start=583
  _globals['_IMAGESPEC_IMAGEORIENTATION']._serialized_end=732
  _globals['_IMAGESPEC_IMAGESIZE']._serialized_start=735
  _globals['_IMAGESPEC_IMAGESIZE']._serialized_end=913
  _globals['_IMAGESPEC_IMAGECOLOR']._serialized_start=916
  _globals['_IMAGESPEC_IMAGECOLOR']._serialized_end=1213
  _globals['_IMAGESEARCHREQUEST']._serialized_start=1216
  _globals['_IMAGESEARCHREQUEST']._serialized_end=1462
  _globals['_IMAGESEARCHRESPONSE']._serialized_start=1464
  _globals['_IMAGESEARCHRESPONSE']._serialized_end=1509
  _globals['_IMAGESEARCHBYIMAGEREQUEST']._serialized_start=1512
  _globals['_IMAGESEARCHBYIMAGEREQUEST']._serialized_end=1794
  _globals['_IMAGESEARCHBYIMAGERESPONSE']._serialized_start=1797
  _globals['_IMAGESEARCHBYIMAGERESPONSE']._serialized_end=2143
  _globals['_IMAGESEARCHBYIMAGERESPONSE_IMAGEINFO']._serialized_start=1953
  _globals['_IMAGESEARCHBYIMAGERESPONSE_IMAGEINFO']._serialized_end=2143
  _globals['_IMAGESEARCHSERVICE']._serialized_start=2146
  _globals['_IMAGESEARCHSERVICE']._serialized_end=2466
# @@protoc_insertion_point(module_scope)
