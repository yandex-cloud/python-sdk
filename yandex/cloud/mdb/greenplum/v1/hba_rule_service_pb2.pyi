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
import yandex.cloud.mdb.greenplum.v1.hba_rule_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class CreateHBARuleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    HBA_RULE_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Greenplum cluster.
    To get the Greenplum cluster ID use a [ClusterService.List] request.
    """
    @property
    def hba_rule(self) -> yandex.cloud.mdb.greenplum.v1.hba_rule_pb2.HBARule:
        """New hba rule for the cluster."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        hba_rule: yandex.cloud.mdb.greenplum.v1.hba_rule_pb2.HBARule | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["hba_rule", b"hba_rule"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "hba_rule", b"hba_rule"]) -> None: ...

global___CreateHBARuleRequest = CreateHBARuleRequest

@typing.final
class UpdateHBARuleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    HBA_RULE_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Greenplum cluster.
    To get the Greenplum cluster ID use a [ClusterService.List] request.
    """
    @property
    def hba_rule(self) -> yandex.cloud.mdb.greenplum.v1.hba_rule_pb2.HBARule:
        """Updated hba rule for the cluster."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        hba_rule: yandex.cloud.mdb.greenplum.v1.hba_rule_pb2.HBARule | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["hba_rule", b"hba_rule"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "hba_rule", b"hba_rule"]) -> None: ...

global___UpdateHBARuleRequest = UpdateHBARuleRequest

@typing.final
class DeleteHBARuleRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PRIORITY_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Greenplum cluster.
    To get the Greenplum cluster ID use a [ClusterService.List] request.
    """
    priority: builtins.int
    """Priority of the Greenplum cluster rule."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        priority: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "priority", b"priority"]) -> None: ...

global___DeleteHBARuleRequest = DeleteHBARuleRequest

@typing.final
class ListHBARulesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Greenplum cluster.
    To get the Greenplum cluster ID use a [ClusterService.List] request.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___ListHBARulesRequest = ListHBARulesRequest

@typing.final
class ListHBARulesAtRevisionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    REVISION_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Greenplum cluster.
    To get the Greenplum cluster ID use a [ClusterService.List] request.
    """
    revision: builtins.int
    """Cluster revision"""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        revision: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "revision", b"revision"]) -> None: ...

global___ListHBARulesAtRevisionRequest = ListHBARulesAtRevisionRequest

@typing.final
class ListHBARulesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HBA_RULES_FIELD_NUMBER: builtins.int
    @property
    def hba_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.greenplum.v1.hba_rule_pb2.HBARule]:
        """Requested list of hba rules for the cluster."""

    def __init__(
        self,
        *,
        hba_rules: collections.abc.Iterable[yandex.cloud.mdb.greenplum.v1.hba_rule_pb2.HBARule] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["hba_rules", b"hba_rules"]) -> None: ...

global___ListHBARulesResponse = ListHBARulesResponse

@typing.final
class BatchUpdateHBARulesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    HBA_RULES_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Greenplum cluster.
    To get the Greenplum cluster ID use a [ClusterService.List] request.
    """
    @property
    def hba_rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.mdb.greenplum.v1.hba_rule_pb2.HBARule]:
        """List of new hba rules for the cluster."""

    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        hba_rules: collections.abc.Iterable[yandex.cloud.mdb.greenplum.v1.hba_rule_pb2.HBARule] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "hba_rules", b"hba_rules"]) -> None: ...

global___BatchUpdateHBARulesRequest = BatchUpdateHBARulesRequest

@typing.final
class HBARulesMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Greenplum cluster which HBA rules was affected."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id"]) -> None: ...

global___HBARulesMetadata = HBARulesMetadata
