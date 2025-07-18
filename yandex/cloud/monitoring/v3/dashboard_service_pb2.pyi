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
import yandex.cloud.monitoring.v3.dashboard_pb2
import yandex.cloud.monitoring.v3.link_item_pb2
import yandex.cloud.monitoring.v3.parametrization_pb2
import yandex.cloud.monitoring.v3.timeline_pb2
import yandex.cloud.monitoring.v3.widget_pb2
import yandex.cloud.operation.operation_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetDashboardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DASHBOARD_ID_FIELD_NUMBER: builtins.int
    dashboard_id: builtins.str
    """Required. Dashboard ID."""
    def __init__(
        self,
        *,
        dashboard_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dashboard_id", b"dashboard_id"]) -> None: ...

global___GetDashboardRequest = GetDashboardRequest

@typing.final
class ListDashboardsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    FOLDER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    SELECTORS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Required. Folder ID."""
    page_size: builtins.int
    """The maximum number of dashboards to return.
    If unspecified, at most 100 dashboards will be returned.
    The maximum value is 1000; values above 1000 will be coerced to 1000.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set `page_token` to the
    [ListDashboardResponse.next_page_token] returned by a previous list request.
    """
    filter: builtins.str
    """Text substring to find in any of dashboard fields: id, name, etc
    result will include dashboards that meet BOTH filter and selector (see below) criteria
    """
    selectors: builtins.str
    """Selector string to match dashboard fields:
    id, name, description, managed_by, etc, format: FIELDNAME PREDICATE VALUE, FIELDNAME PREDICATE VALUE, ...
    and dashboard labels, format: labels.KEY PREDICATE VALUE, labels.KEY PREDICATE VALUE, ...
    supports GLOB and regex expressions
    dashboard must meet ALL tokens in selector string
    example: name = "New", description = "*new*", labels.key != "bad"
    """
    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
        selectors: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["container", b"container", "folder_id", b"folder_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["container", b"container", "filter", b"filter", "folder_id", b"folder_id", "page_size", b"page_size", "page_token", b"page_token", "selectors", b"selectors"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["container", b"container"]) -> typing.Literal["folder_id"] | None: ...

global___ListDashboardsRequest = ListDashboardsRequest

@typing.final
class ListDashboardsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DASHBOARDS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """Token to retrieve the next page of results, or empty if there are no more results in the list."""
    @property
    def dashboards(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.monitoring.v3.dashboard_pb2.Dashboard]:
        """List of dashboards."""

    def __init__(
        self,
        *,
        dashboards: collections.abc.Iterable[yandex.cloud.monitoring.v3.dashboard_pb2.Dashboard] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dashboards", b"dashboards", "next_page_token", b"next_page_token"]) -> None: ...

global___ListDashboardsResponse = ListDashboardsResponse

@typing.final
class CreateDashboardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    FOLDER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    WIDGETS_FIELD_NUMBER: builtins.int
    PARAMETRIZATION_FIELD_NUMBER: builtins.int
    MANAGED_BY_FIELD_NUMBER: builtins.int
    MANAGED_LINK_FIELD_NUMBER: builtins.int
    TIMELINE_FIELD_NUMBER: builtins.int
    LINKS_FIELD_NUMBER: builtins.int
    folder_id: builtins.str
    """Required. Folder ID."""
    name: builtins.str
    """Required. Dashboard name."""
    description: builtins.str
    """Dashboard description."""
    title: builtins.str
    """Dashboard title."""
    managed_by: builtins.str
    """Entity that controls dashboard
    Must match the regular expression "[\\w \\-]{1,100}"
    """
    managed_link: builtins.str
    """Information about entity that controls dashboard
    Must be valid URI
    """
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs."""

    @property
    def widgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.monitoring.v3.widget_pb2.Widget]:
        """List of dashboard widgets."""

    @property
    def parametrization(self) -> yandex.cloud.monitoring.v3.parametrization_pb2.Parametrization:
        """Dashboard parametrization."""

    @property
    def timeline(self) -> yandex.cloud.monitoring.v3.timeline_pb2.Timeline:
        """Refresh and time window settings"""

    @property
    def links(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.monitoring.v3.link_item_pb2.LinkItem]:
        """Dashboard links"""

    def __init__(
        self,
        *,
        folder_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        title: builtins.str = ...,
        widgets: collections.abc.Iterable[yandex.cloud.monitoring.v3.widget_pb2.Widget] | None = ...,
        parametrization: yandex.cloud.monitoring.v3.parametrization_pb2.Parametrization | None = ...,
        managed_by: builtins.str = ...,
        managed_link: builtins.str = ...,
        timeline: yandex.cloud.monitoring.v3.timeline_pb2.Timeline | None = ...,
        links: collections.abc.Iterable[yandex.cloud.monitoring.v3.link_item_pb2.LinkItem] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["container", b"container", "folder_id", b"folder_id", "parametrization", b"parametrization", "timeline", b"timeline"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["container", b"container", "description", b"description", "folder_id", b"folder_id", "labels", b"labels", "links", b"links", "managed_by", b"managed_by", "managed_link", b"managed_link", "name", b"name", "parametrization", b"parametrization", "timeline", b"timeline", "title", b"title", "widgets", b"widgets"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["container", b"container"]) -> typing.Literal["folder_id"] | None: ...

global___CreateDashboardRequest = CreateDashboardRequest

@typing.final
class CreateDashboardMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DASHBOARD_ID_FIELD_NUMBER: builtins.int
    dashboard_id: builtins.str
    """Dashboard ID."""
    def __init__(
        self,
        *,
        dashboard_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dashboard_id", b"dashboard_id"]) -> None: ...

global___CreateDashboardMetadata = CreateDashboardMetadata

@typing.final
class UpdateDashboardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class LabelsEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: builtins.str
        value: builtins.str
        def __init__(
            self,
            *,
            key: builtins.str = ...,
            value: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["key", b"key", "value", b"value"]) -> None: ...

    DASHBOARD_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    TITLE_FIELD_NUMBER: builtins.int
    WIDGETS_FIELD_NUMBER: builtins.int
    PARAMETRIZATION_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    MANAGED_BY_FIELD_NUMBER: builtins.int
    MANAGED_LINK_FIELD_NUMBER: builtins.int
    TIMELINE_FIELD_NUMBER: builtins.int
    LINKS_FIELD_NUMBER: builtins.int
    dashboard_id: builtins.str
    """Required. Dashboard ID."""
    name: builtins.str
    """Required. Dashboard name."""
    description: builtins.str
    """Dashboard description."""
    title: builtins.str
    """Dashboard title."""
    etag: builtins.str
    """The current etag of the dashboard."""
    managed_by: builtins.str
    """Entity that controls dashboard
    Must match the regular expression "[\\w \\-]{1,100}"
    """
    managed_link: builtins.str
    """Information about entity that controls dashboard
    Must be valid URI
    """
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Resource labels as `key:value` pairs.

        Existing set of `labels` is completely replaced by the provided set.
        """

    @property
    def widgets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.monitoring.v3.widget_pb2.Widget]:
        """List of dashboard widgets."""

    @property
    def parametrization(self) -> yandex.cloud.monitoring.v3.parametrization_pb2.Parametrization:
        """Dashboard parametrization."""

    @property
    def timeline(self) -> yandex.cloud.monitoring.v3.timeline_pb2.Timeline:
        """Refresh and time window settings"""

    @property
    def links(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.monitoring.v3.link_item_pb2.LinkItem]:
        """Dashboard links"""

    def __init__(
        self,
        *,
        dashboard_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        title: builtins.str = ...,
        widgets: collections.abc.Iterable[yandex.cloud.monitoring.v3.widget_pb2.Widget] | None = ...,
        parametrization: yandex.cloud.monitoring.v3.parametrization_pb2.Parametrization | None = ...,
        etag: builtins.str = ...,
        managed_by: builtins.str = ...,
        managed_link: builtins.str = ...,
        timeline: yandex.cloud.monitoring.v3.timeline_pb2.Timeline | None = ...,
        links: collections.abc.Iterable[yandex.cloud.monitoring.v3.link_item_pb2.LinkItem] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["parametrization", b"parametrization", "timeline", b"timeline"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["dashboard_id", b"dashboard_id", "description", b"description", "etag", b"etag", "labels", b"labels", "links", b"links", "managed_by", b"managed_by", "managed_link", b"managed_link", "name", b"name", "parametrization", b"parametrization", "timeline", b"timeline", "title", b"title", "widgets", b"widgets"]) -> None: ...

global___UpdateDashboardRequest = UpdateDashboardRequest

@typing.final
class UpdateDashboardMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DASHBOARD_ID_FIELD_NUMBER: builtins.int
    dashboard_id: builtins.str
    """Dashboard ID."""
    def __init__(
        self,
        *,
        dashboard_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dashboard_id", b"dashboard_id"]) -> None: ...

global___UpdateDashboardMetadata = UpdateDashboardMetadata

@typing.final
class DeleteDashboardRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DASHBOARD_ID_FIELD_NUMBER: builtins.int
    ETAG_FIELD_NUMBER: builtins.int
    dashboard_id: builtins.str
    """Required. Dashboard ID."""
    etag: builtins.str
    """The current etag of the dashboard."""
    def __init__(
        self,
        *,
        dashboard_id: builtins.str = ...,
        etag: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dashboard_id", b"dashboard_id", "etag", b"etag"]) -> None: ...

global___DeleteDashboardRequest = DeleteDashboardRequest

@typing.final
class DeleteDashboardMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DASHBOARD_ID_FIELD_NUMBER: builtins.int
    dashboard_id: builtins.str
    """Dashboard ID."""
    def __init__(
        self,
        *,
        dashboard_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dashboard_id", b"dashboard_id"]) -> None: ...

global___DeleteDashboardMetadata = DeleteDashboardMetadata

@typing.final
class ListDashboardOperationsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DASHBOARD_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    dashboard_id: builtins.str
    """ID of the dashboard to list operations for."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size], the service returns a [ListDashboardOperationsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListDashboardOperationsResponse.next_page_token] returned by a previous list request.
    """
    def __init__(
        self,
        *,
        dashboard_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["dashboard_id", b"dashboard_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListDashboardOperationsRequest = ListDashboardOperationsRequest

@typing.final
class ListDashboardOperationsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPERATIONS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListDashboardOperationsRequest.page_size], use the [next_page_token] as the value
    for the [ListDashboardOperationsRequest.page_token] query parameter in the next list request.
    Each subsequent list request will have its own [next_page_token] to continue paging through the results.
    """
    @property
    def operations(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.operation.operation_pb2.Operation]:
        """List of operations for the specified dashboard."""

    def __init__(
        self,
        *,
        operations: collections.abc.Iterable[yandex.cloud.operation.operation_pb2.Operation] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "operations", b"operations"]) -> None: ...

global___ListDashboardOperationsResponse = ListDashboardOperationsResponse

@typing.final
class ListDashboardLabelNamesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    SELECTORS_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    text: builtins.str
    """Contains substring of name(aka key). All label names containing this string will be returned"""
    selectors: builtins.str
    """Filters alerts by this selectors."""
    page_size: builtins.int
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        text: builtins.str = ...,
        selectors: builtins.str = ...,
        page_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["page_size", b"page_size", "project_id", b"project_id", "selectors", b"selectors", "text", b"text"]) -> None: ...

global___ListDashboardLabelNamesRequest = ListDashboardLabelNamesRequest

@typing.final
class ListDashboardLabelNamesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LABEL_NAMES_FIELD_NUMBER: builtins.int
    TRUNCATED_FIELD_NUMBER: builtins.int
    truncated: builtins.bool
    @property
    def label_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        label_names: collections.abc.Iterable[builtins.str] | None = ...,
        truncated: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["label_names", b"label_names", "truncated", b"truncated"]) -> None: ...

global___ListDashboardLabelNamesResponse = ListDashboardLabelNamesResponse

@typing.final
class ListDashboardLabelValuesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    SELECTORS_FIELD_NUMBER: builtins.int
    LABEL_NAME_FIELD_NUMBER: builtins.int
    TEXT_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    selectors: builtins.str
    """Filters alerts by this selectors."""
    label_name: builtins.str
    """Contains full name (aka key), for which existing values are gathered."""
    text: builtins.str
    """Contains substring of value. All label values containing this string will be returned"""
    page_size: builtins.int
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        selectors: builtins.str = ...,
        label_name: builtins.str = ...,
        text: builtins.str = ...,
        page_size: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["label_name", b"label_name", "page_size", b"page_size", "project_id", b"project_id", "selectors", b"selectors", "text", b"text"]) -> None: ...

global___ListDashboardLabelValuesRequest = ListDashboardLabelValuesRequest

@typing.final
class ListDashboardLabelValuesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LABEL_VALUES_FIELD_NUMBER: builtins.int
    TRUNCATED_FIELD_NUMBER: builtins.int
    truncated: builtins.bool
    @property
    def label_values(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]: ...
    def __init__(
        self,
        *,
        label_values: collections.abc.Iterable[builtins.str] | None = ...,
        truncated: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["label_values", b"label_values", "truncated", b"truncated"]) -> None: ...

global___ListDashboardLabelValuesResponse = ListDashboardLabelValuesResponse
