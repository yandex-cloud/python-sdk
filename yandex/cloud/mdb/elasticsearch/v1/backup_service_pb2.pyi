"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import yandex.cloud.mdb.elasticsearch.v1.backup_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetBackupRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUP_ID_FIELD_NUMBER: builtins.int
    backup_id: builtins.str
    """Required. ID of the backup to return."""
    def __init__(
        self,
        *,
        backup_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["backup_id", b"backup_id"]) -> None: ...

global___GetBackupRequest = GetBackupRequest

@typing.final
class ListBackupsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Required. ID of the folder to list backups in."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a `next_page_token` that can be used
    to get the next page of results in subsequent ListBackups requests.
    Acceptable values are 0 to 1000, inclusive. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set `page_token` to the `next_page_token` returned by a previous ListBackups
    request to get the next page of results.
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListBackupsRequest = ListBackupsRequest

@typing.final
class ListBackupsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    BACKUPS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for ListBackups requests,
    if the number of results is larger than `page_size` specified in the request.
    To get the next page, specify the value of `next_page_token` as a value for
    the `page_token` parameter in the next ListBackups request. Subsequent ListBackups
    requests will have their own `next_page_token` to continue paging through the results.
    """
    @property
    def backups(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.elasticsearch.v1.backup_pb2.Backup]:
        """Requested list of backups."""

    def __init__(
        self,
        *,
        backups: collections.abc.Iterable[yandex.cloud.mdb.elasticsearch.v1.backup_pb2.Backup] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["backups", b"backups", "next_page_token", b"next_page_token"]) -> None: ...

global___ListBackupsResponse = ListBackupsResponse
