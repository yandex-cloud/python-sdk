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
import yandex.cloud.mdb.postgresql.v1.backup_retention_policy_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ListBackupRetentionPoliciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the PostgreSQL cluster.
    To get the PostgreSQL cluster ID use a [ClusterService.List] request.
    """
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListBackupRetentionPoliciesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token]
    to the [ListBackupRetentionPoliciesResponse.next_page_token] returned by the previous list request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListBackupRetentionPoliciesRequest = ListBackupRetentionPoliciesRequest

@typing.final
class ListBackupRetentionPoliciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListBackupRetentionPoliciesRequest.page_size], use the [next_page_token] as the value
    for the [ListBackupRetentionPoliciesRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def policies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.postgresql.v1.backup_retention_policy_pb2.BackupRetentionPolicy]:
        """List of [BackupRetentionPolicy] associated with the cluster."""

    def __init__(
        self,
        *,
        policies: collections.abc.Iterable[yandex.cloud.mdb.postgresql.v1.backup_retention_policy_pb2.BackupRetentionPolicy] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "policies", b"policies"]) -> None: ...

global___ListBackupRetentionPoliciesResponse = ListBackupRetentionPoliciesResponse

@typing.final
class CreateBackupRetentionPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    CRON_FIELD_NUMBER: builtins.int
    RETAIN_FOR_DAYS_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    POLICY_NAME_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the PostgreSQL cluster.
    To get the PostgreSQL cluster ID use a [ClusterService.List] request.
    """
    retain_for_days: builtins.int
    """Retention duration."""
    description: builtins.str
    """Policy description."""
    policy_name: builtins.str
    """Required. Policy name."""
    @property
    def cron(self) -> yandex.cloud.mdb.postgresql.v1.backup_retention_policy_pb2.CronTab:
        """CronTab schedule."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        cron: yandex.cloud.mdb.postgresql.v1.backup_retention_policy_pb2.CronTab | None = ...,
        retain_for_days: builtins.int = ...,
        description: builtins.str = ...,
        policy_name: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cron", b"cron"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "cron", b"cron", "description", b"description", "policy_name", b"policy_name", "retain_for_days", b"retain_for_days"]) -> None: ...

global___CreateBackupRetentionPolicyRequest = CreateBackupRetentionPolicyRequest

@typing.final
class CreateBackupRetentionPolicyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_FIELD_NUMBER: builtins.int
    @property
    def policy(self) -> yandex.cloud.mdb.postgresql.v1.backup_retention_policy_pb2.BackupRetentionPolicy:
        """Newly created [BackupRetentionPolicy]."""

    def __init__(
        self,
        *,
        policy: yandex.cloud.mdb.postgresql.v1.backup_retention_policy_pb2.BackupRetentionPolicy | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["policy", b"policy"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["policy", b"policy"]) -> None: ...

global___CreateBackupRetentionPolicyResponse = CreateBackupRetentionPolicyResponse

@typing.final
class DeleteBackupRetentionPolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    POLICY_ID_FIELD_NUMBER: builtins.int
    CLUSTER_ID_FIELD_NUMBER: builtins.int
    policy_id: builtins.str
    """Unique identifier for the [BackupRetentionPolicy]."""
    cluster_id: builtins.str
    """ID of the PostgreSQL cluster.
    To get the PostgreSQL cluster ID use a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        policy_id: builtins.str = ...,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "policy_id", b"policy_id"]) -> None: ...

global___DeleteBackupRetentionPolicyRequest = DeleteBackupRetentionPolicyRequest

@typing.final
class DeleteBackupRetentionPolicyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteBackupRetentionPolicyResponse = DeleteBackupRetentionPolicyResponse
