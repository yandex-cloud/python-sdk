"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import google.protobuf.timestamp_pb2
import typing
import yandex.cloud.containerregistry.v1.image_pb2
import yandex.cloud.containerregistry.v1.lifecycle_policy_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetLifecyclePolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy."""
    def __init__(
        self,
        *,
        lifecycle_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lifecycle_policy_id", b"lifecycle_policy_id"]) -> None: ...

global___GetLifecyclePolicyRequest = GetLifecyclePolicyRequest

@typing.final
class ListLifecyclePoliciesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REGISTRY_ID_FIELD_NUMBER: builtins.int
    REPOSITORY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    registry_id: builtins.str
    """ID of the lifecycle policy."""
    repository_id: builtins.str
    """Repository of the lifecycle policy."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns 
    a [ListLifecyclePoliciesResponse.next_page_token] that can be used to get the next page of results in subsequent list requests.
    Default value: 100.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListLifecyclePoliciesResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters lifecycle policy resources listed in the response.

    The expression must specify:
    1. The field name. Currently you can use filtering only on [LifecyclePolicy.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    order_by: builtins.str
    """Sorting the list by [LifecyclePolicy.name], [LifecyclePolicy.created_at] and [LifecyclePolicy.status] fields.
    The default sorting order is ascending.
    """
    def __init__(
        self,
        *,
        registry_id: builtins.str = ...,
        repository_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
        order_by: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["id", b"id", "registry_id", b"registry_id", "repository_id", b"repository_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "id", b"id", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token", "registry_id", b"registry_id", "repository_id", b"repository_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["id", b"id"]) -> typing.Literal["registry_id", "repository_id"] | None: ...

global___ListLifecyclePoliciesRequest = ListLifecyclePoliciesRequest

@typing.final
class ListLifecyclePoliciesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICIES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListLifecyclePoliciesRequest.page_size], use `next_page_token` as the value
    for the [ListLifecyclePoliciesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def lifecycle_policies(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy]:
        """List of lifecycle policies."""

    def __init__(
        self,
        *,
        lifecycle_policies: collections.abc.Iterable[yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lifecycle_policies", b"lifecycle_policies", "next_page_token", b"next_page_token"]) -> None: ...

global___ListLifecyclePoliciesResponse = ListLifecyclePoliciesResponse

@typing.final
class CreateLifecyclePolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REPOSITORY_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    repository_id: builtins.str
    """ID of the lifecycle policy repository."""
    name: builtins.str
    """Name of lifecycle policy."""
    description: builtins.str
    """Description of lifecycle policy."""
    status: yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy.Status.ValueType
    """Status of the lifecycle policy."""
    @property
    def rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecycleRule]:
        """The rules of the lifecycle policy."""

    def __init__(
        self,
        *,
        repository_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        status: yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy.Status.ValueType = ...,
        rules: collections.abc.Iterable[yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecycleRule] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "name", b"name", "repository_id", b"repository_id", "rules", b"rules", "status", b"status"]) -> None: ...

global___CreateLifecyclePolicyRequest = CreateLifecyclePolicyRequest

@typing.final
class UpdateLifecyclePolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    RULES_FIELD_NUMBER: builtins.int
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy."""
    name: builtins.str
    """Name of lifecycle policy."""
    description: builtins.str
    """Description of lifecycle policy."""
    status: yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy.Status.ValueType
    """Status of the lifecycle policy."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the lifecycle policy resource are going to be updated."""

    @property
    def rules(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecycleRule]:
        """The rules of the lifecycle policy."""

    def __init__(
        self,
        *,
        lifecycle_policy_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        status: yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecyclePolicy.Status.ValueType = ...,
        rules: collections.abc.Iterable[yandex.cloud.containerregistry.v1.lifecycle_policy_pb2.LifecycleRule] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "lifecycle_policy_id", b"lifecycle_policy_id", "name", b"name", "rules", b"rules", "status", b"status", "update_mask", b"update_mask"]) -> None: ...

global___UpdateLifecyclePolicyRequest = UpdateLifecyclePolicyRequest

@typing.final
class DeleteLifecyclePolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy."""
    def __init__(
        self,
        *,
        lifecycle_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lifecycle_policy_id", b"lifecycle_policy_id"]) -> None: ...

global___DeleteLifecyclePolicyRequest = DeleteLifecyclePolicyRequest

@typing.final
class CreateLifecyclePolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy resource that is being created."""
    def __init__(
        self,
        *,
        lifecycle_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lifecycle_policy_id", b"lifecycle_policy_id"]) -> None: ...

global___CreateLifecyclePolicyMetadata = CreateLifecyclePolicyMetadata

@typing.final
class UpdateLifecyclePolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy resource that is being updated."""
    def __init__(
        self,
        *,
        lifecycle_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lifecycle_policy_id", b"lifecycle_policy_id"]) -> None: ...

global___UpdateLifecyclePolicyMetadata = UpdateLifecyclePolicyMetadata

@typing.final
class DeleteLifecyclePolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy resource that is being deleted."""
    def __init__(
        self,
        *,
        lifecycle_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lifecycle_policy_id", b"lifecycle_policy_id"]) -> None: ...

global___DeleteLifecyclePolicyMetadata = DeleteLifecyclePolicyMetadata

@typing.final
class DryRunLifecyclePolicyRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy."""
    def __init__(
        self,
        *,
        lifecycle_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["lifecycle_policy_id", b"lifecycle_policy_id"]) -> None: ...

global___DryRunLifecyclePolicyRequest = DryRunLifecyclePolicyRequest

@typing.final
class DryRunLifecyclePolicyMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRY_RUN_LIFECYCLE_POLICY_RESULT_ID_FIELD_NUMBER: builtins.int
    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    dry_run_lifecycle_policy_result_id: builtins.str
    """ID of the dry run result of the lifecycle policy."""
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy."""
    def __init__(
        self,
        *,
        dry_run_lifecycle_policy_result_id: builtins.str = ...,
        lifecycle_policy_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dry_run_lifecycle_policy_result_id", b"dry_run_lifecycle_policy_result_id", "lifecycle_policy_id", b"lifecycle_policy_id"]) -> None: ...

global___DryRunLifecyclePolicyMetadata = DryRunLifecyclePolicyMetadata

@typing.final
class DryRunLifecyclePolicyResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRY_RUN_LIFECYCLE_POLICY_RESULT_ID_FIELD_NUMBER: builtins.int
    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    RUN_AT_FIELD_NUMBER: builtins.int
    AFFECTED_IMAGES_COUNT_FIELD_NUMBER: builtins.int
    dry_run_lifecycle_policy_result_id: builtins.str
    """ID of the dry run result of the lifecycle policy."""
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy."""
    affected_images_count: builtins.int
    """Count of affected images."""
    @property
    def run_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Time of the getting result."""

    def __init__(
        self,
        *,
        dry_run_lifecycle_policy_result_id: builtins.str = ...,
        lifecycle_policy_id: builtins.str = ...,
        run_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        affected_images_count: builtins.int = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["run_at", b"run_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["affected_images_count", b"affected_images_count", "dry_run_lifecycle_policy_result_id", b"dry_run_lifecycle_policy_result_id", "lifecycle_policy_id", b"lifecycle_policy_id", "run_at", b"run_at"]) -> None: ...

global___DryRunLifecyclePolicyResult = DryRunLifecyclePolicyResult

@typing.final
class GetDryRunLifecyclePolicyResultRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRY_RUN_LIFECYCLE_POLICY_RESULT_ID_FIELD_NUMBER: builtins.int
    dry_run_lifecycle_policy_result_id: builtins.str
    """ID of the dry run result of the lifecycle policy."""
    def __init__(
        self,
        *,
        dry_run_lifecycle_policy_result_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dry_run_lifecycle_policy_result_id", b"dry_run_lifecycle_policy_result_id"]) -> None: ...

global___GetDryRunLifecyclePolicyResultRequest = GetDryRunLifecyclePolicyResultRequest

@typing.final
class ListDryRunLifecyclePolicyResultsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIFECYCLE_POLICY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    lifecycle_policy_id: builtins.str
    """ID of the lifecycle policy."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns 
    a [ListDryRunLifecyclePolicyResultsResponse.next_page_token] that can be used to get 
    the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListDryRunLifecyclePolicyResultsResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters dry run results listed in the response.

    The expression must specify:
    1. The field name. Currently you can use filtering only on [LifecyclePolicy.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    order_by: builtins.str
    """Sorting the list by [DryRunLifecyclePolicyResult.run_at] and [DryRunLifecyclePolicyResult.affected_images_count] fields.
    The default sorting order is ascending.
    """
    def __init__(
        self,
        *,
        lifecycle_policy_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
        order_by: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "lifecycle_policy_id", b"lifecycle_policy_id", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDryRunLifecyclePolicyResultsRequest = ListDryRunLifecyclePolicyResultsRequest

@typing.final
class ListDryRunLifecyclePolicyResultsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRY_RUN_LIFECYCLE_POLICY_RESULTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListDryRunLifecyclePolicyResultsRequest.page_size] use `next_page_token` as the value
    for the [ListDryRunLifecyclePolicyResultsRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def dry_run_lifecycle_policy_results(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___DryRunLifecyclePolicyResult]:
        """List of results of dry runs of a lifecycle policy."""

    def __init__(
        self,
        *,
        dry_run_lifecycle_policy_results: collections.abc.Iterable[global___DryRunLifecyclePolicyResult] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dry_run_lifecycle_policy_results", b"dry_run_lifecycle_policy_results", "next_page_token", b"next_page_token"]) -> None: ...

global___ListDryRunLifecyclePolicyResultsResponse = ListDryRunLifecyclePolicyResultsResponse

@typing.final
class ListDryRunLifecyclePolicyResultAffectedImagesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DRY_RUN_LIFECYCLE_POLICY_RESULT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    ORDER_BY_FIELD_NUMBER: builtins.int
    dry_run_lifecycle_policy_result_id: builtins.str
    """ID of the dry run result of the lifecycle policy"""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than `page_size`, the service returns a [ListDryRunLifecyclePolicyResultAffectedImagesResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListDryRunLifecyclePolicyResultAffectedImagesResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """A filter expression that filters affected images listed in the response.

    The expression must specify:
    1. The field name. Currently you can use filtering only on [LifecyclePolicy.name] field.
    2. An `=` operator.
    3. The value in double quotes (`"`). Must be 3-63 characters long and match the regular expression `[a-z][-a-z0-9]{1,61}[a-z0-9]`.
    """
    order_by: builtins.str
    """Sorting the list by [LifecyclePolicy.name] and [LifecyclePolicy.created_at] fields.
    The default sorting order is ascending.
    """
    def __init__(
        self,
        *,
        dry_run_lifecycle_policy_result_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
        order_by: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dry_run_lifecycle_policy_result_id", b"dry_run_lifecycle_policy_result_id", "filter", b"filter", "order_by", b"order_by", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDryRunLifecyclePolicyResultAffectedImagesRequest = ListDryRunLifecyclePolicyResultAffectedImagesRequest

@typing.final
class ListDryRunLifecyclePolicyResultAffectedImagesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    AFFECTED_IMAGES_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token for getting the next page of the list. If the number of results is greater than
    the specified [ListDryRunLifecyclePolicyResultAffectedImagesRequest.page_size], use `next_page_token` as the value
    for the [ListDryRunLifecyclePolicyResultAffectedImagesRequest.page_token] parameter in the next list request.

    Each subsequent page will have its own `next_page_token` to continue paging through the results.
    """
    @property
    def affected_images(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.containerregistry.v1.image_pb2.Image]:
        """List of affected images."""

    def __init__(
        self,
        *,
        affected_images: collections.abc.Iterable[yandex.cloud.containerregistry.v1.image_pb2.Image] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["affected_images", b"affected_images", "next_page_token", b"next_page_token"]) -> None: ...

global___ListDryRunLifecyclePolicyResultAffectedImagesResponse = ListDryRunLifecyclePolicyResultAffectedImagesResponse
