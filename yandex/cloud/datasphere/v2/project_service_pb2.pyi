"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.struct_pb2
import google.protobuf.timestamp_pb2
import google.protobuf.wrappers_pb2
import sys
import typing
import yandex.cloud.datasphere.v2.project_pb2
import yandex.cloud.datasphere.v2.resource_types_pb2
import yandex.cloud.datasphere.v2.restrictions_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ExecutionStatus:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ExecutionStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ExecutionStatus.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    EXECUTION_STATUS_UNSPECIFIED: _ExecutionStatus.ValueType  # 0
    OK: _ExecutionStatus.ValueType  # 1
    """Execution finished successfully."""
    ERROR: _ExecutionStatus.ValueType  # 2
    """Execution ended with error."""
    ABORTED: _ExecutionStatus.ValueType  # 3
    """Execution was aborted."""

class ExecutionStatus(_ExecutionStatus, metaclass=_ExecutionStatusEnumTypeWrapper): ...

EXECUTION_STATUS_UNSPECIFIED: ExecutionStatus.ValueType  # 0
OK: ExecutionStatus.ValueType  # 1
"""Execution finished successfully."""
ERROR: ExecutionStatus.ValueType  # 2
"""Execution ended with error."""
ABORTED: ExecutionStatus.ValueType  # 3
"""Execution was aborted."""
global___ExecutionStatus = ExecutionStatus

@typing.final
class CreateProjectRequest(google.protobuf.message.Message):
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

    COMMUNITY_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    community_id: builtins.str
    """ID of the community to create a project in."""
    name: builtins.str
    """Name of the project. 0-63 characters long."""
    description: builtins.str
    """Description of the project. 0-256 characters long."""
    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels of the project."""

    @property
    def settings(self) -> yandex.cloud.datasphere.v2.project_pb2.Project.Settings:
        """Settings of the project."""

    @property
    def limits(self) -> yandex.cloud.datasphere.v2.project_pb2.Project.Limits:
        """Limits of the project."""

    def __init__(
        self,
        *,
        community_id: builtins.str = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        settings: yandex.cloud.datasphere.v2.project_pb2.Project.Settings | None = ...,
        limits: yandex.cloud.datasphere.v2.project_pb2.Project.Limits | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["limits", b"limits", "settings", b"settings"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["community_id", b"community_id", "description", b"description", "labels", b"labels", "limits", b"limits", "name", b"name", "settings", b"settings"]) -> None: ...

global___CreateProjectRequest = CreateProjectRequest

@typing.final
class CreateProjectMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project that is being created."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___CreateProjectMetadata = CreateProjectMetadata

@typing.final
class UpdateProjectRequest(google.protobuf.message.Message):
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

    PROJECT_ID_FIELD_NUMBER: builtins.int
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESCRIPTION_FIELD_NUMBER: builtins.int
    LABELS_FIELD_NUMBER: builtins.int
    SETTINGS_FIELD_NUMBER: builtins.int
    LIMITS_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the Project resource to update.
    To get the project ID use a [ProjectService.List] request.
    """
    name: builtins.str
    """Name of the project. 0-63 characters long."""
    description: builtins.str
    """Description of the project. 0-256 characters long."""
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask:
        """Field mask that specifies which fields of the Project resource are going to be updated."""

    @property
    def labels(self) -> google.protobuf.internal.containers.ScalarMap[builtins.str, builtins.str]:
        """Labels of the project."""

    @property
    def settings(self) -> yandex.cloud.datasphere.v2.project_pb2.Project.Settings:
        """Settings of the project."""

    @property
    def limits(self) -> yandex.cloud.datasphere.v2.project_pb2.Project.Limits:
        """Limits of the project."""

    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        update_mask: google.protobuf.field_mask_pb2.FieldMask | None = ...,
        name: builtins.str = ...,
        description: builtins.str = ...,
        labels: collections.abc.Mapping[builtins.str, builtins.str] | None = ...,
        settings: yandex.cloud.datasphere.v2.project_pb2.Project.Settings | None = ...,
        limits: yandex.cloud.datasphere.v2.project_pb2.Project.Limits | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["limits", b"limits", "settings", b"settings", "update_mask", b"update_mask"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["description", b"description", "labels", b"labels", "limits", b"limits", "name", b"name", "project_id", b"project_id", "settings", b"settings", "update_mask", b"update_mask"]) -> None: ...

global___UpdateProjectRequest = UpdateProjectRequest

@typing.final
class UpdateProjectMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project that is being updated."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___UpdateProjectMetadata = UpdateProjectMetadata

@typing.final
class DeleteProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the Project resource to delete.
    To get the project ID use a [ProjectService.List] request.
    """
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___DeleteProjectRequest = DeleteProjectRequest

@typing.final
class DeleteProjectMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project that is being deleted."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___DeleteProjectMetadata = DeleteProjectMetadata

@typing.final
class OpenProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the Project resource to open.
    To get the project ID use a [ProjectService.List] request.
    """
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___OpenProjectRequest = OpenProjectRequest

@typing.final
class OpenProjectMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _OpenProjectStatus:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _OpenProjectStatusEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[OpenProjectMetadata._OpenProjectStatus.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        OPEN_PROJECT_STATUS_UNSPECIFIED: OpenProjectMetadata._OpenProjectStatus.ValueType  # 0
        OPEN_PROJECT_STATUS_CLOSING_IDE: OpenProjectMetadata._OpenProjectStatus.ValueType  # 1
        """Closing previous IDE instance."""
        OPEN_PROJECT_STATUS_UNZIPPING_PROJECT: OpenProjectMetadata._OpenProjectStatus.ValueType  # 2
        """Unzipping project."""
        OPEN_PROJECT_STATUS_ALLOCATING_VM: OpenProjectMetadata._OpenProjectStatus.ValueType  # 3
        """Allocating VM for the project."""
        OPEN_PROJECT_STATUS_ALLOCATING_RESOURCES: OpenProjectMetadata._OpenProjectStatus.ValueType  # 4
        """Allocating resources for the project."""
        OPEN_PROJECT_STATUS_STARTING_IDE: OpenProjectMetadata._OpenProjectStatus.ValueType  # 5
        """Starting IDE."""
        OPEN_PROJECT_STATUS_APPLYING_CHECKPOINT: OpenProjectMetadata._OpenProjectStatus.ValueType  # 6
        """Applying checkpoint to project."""
        OPEN_PROJECT_STATUS_UNKNOWN: OpenProjectMetadata._OpenProjectStatus.ValueType  # 7
        """Unknown open project status."""

    class OpenProjectStatus(_OpenProjectStatus, metaclass=_OpenProjectStatusEnumTypeWrapper): ...
    OPEN_PROJECT_STATUS_UNSPECIFIED: OpenProjectMetadata.OpenProjectStatus.ValueType  # 0
    OPEN_PROJECT_STATUS_CLOSING_IDE: OpenProjectMetadata.OpenProjectStatus.ValueType  # 1
    """Closing previous IDE instance."""
    OPEN_PROJECT_STATUS_UNZIPPING_PROJECT: OpenProjectMetadata.OpenProjectStatus.ValueType  # 2
    """Unzipping project."""
    OPEN_PROJECT_STATUS_ALLOCATING_VM: OpenProjectMetadata.OpenProjectStatus.ValueType  # 3
    """Allocating VM for the project."""
    OPEN_PROJECT_STATUS_ALLOCATING_RESOURCES: OpenProjectMetadata.OpenProjectStatus.ValueType  # 4
    """Allocating resources for the project."""
    OPEN_PROJECT_STATUS_STARTING_IDE: OpenProjectMetadata.OpenProjectStatus.ValueType  # 5
    """Starting IDE."""
    OPEN_PROJECT_STATUS_APPLYING_CHECKPOINT: OpenProjectMetadata.OpenProjectStatus.ValueType  # 6
    """Applying checkpoint to project."""
    OPEN_PROJECT_STATUS_UNKNOWN: OpenProjectMetadata.OpenProjectStatus.ValueType  # 7
    """Unknown open project status."""

    PROJECT_ID_FIELD_NUMBER: builtins.int
    STATUS_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project that is being opened."""
    status: global___OpenProjectMetadata.OpenProjectStatus.ValueType
    """Project opening status."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        status: global___OpenProjectMetadata.OpenProjectStatus.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id", "status", b"status"]) -> None: ...

global___OpenProjectMetadata = OpenProjectMetadata

@typing.final
class OpenProjectResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_URL_FIELD_NUMBER: builtins.int
    SESSION_TOKEN_FIELD_NUMBER: builtins.int
    project_url: builtins.str
    """URL of the project that is being opened.
    Make GET request to [project_url] with sessionToken query parameter equals to [session_token]
    or POST request to [project_url] with sessionToken body parameter equals to [session_token]
    to fetch DataSphere web interface.
    """
    session_token: builtins.str
    """Session token of the project that is being opened."""
    def __init__(
        self,
        *,
        project_url: builtins.str = ...,
        session_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_url", b"project_url", "session_token", b"session_token"]) -> None: ...

global___OpenProjectResponse = OpenProjectResponse

@typing.final
class GetProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the Project resource to return.
    To get the project ID use a [ProjectService.List] request.
    """
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___GetProjectRequest = GetProjectRequest

@typing.final
class ListProjectsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    COMMUNITY_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    PROJECT_NAME_PATTERN_FIELD_NUMBER: builtins.int
    OWNED_BY_ID_FIELD_NUMBER: builtins.int
    community_id: builtins.str
    """ID of the community to list projects in."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListProjectsResponse.next_page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListProjectsResponse.next_page_token] returned by a previous list request.
    """
    project_name_pattern: builtins.str
    """Name pattern to filter projects that are returned.
    Only projects with names matching the pattern will be returned.
    """
    owned_by_id: builtins.str
    """User ID to filter projects that are returned.
    Only projects that are owned by specified user will be returned.
    """
    def __init__(
        self,
        *,
        community_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        project_name_pattern: builtins.str = ...,
        owned_by_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["community_id", b"community_id", "owned_by_id", b"owned_by_id", "page_size", b"page_size", "page_token", b"page_token", "project_name_pattern", b"project_name_pattern"]) -> None: ...

global___ListProjectsRequest = ListProjectsRequest

@typing.final
class ListProjectsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECTS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListProjectsRequest.page_size], use
    the [next_page_token] as the value
    for the [ListProjectsRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [next_page_token] to continue paging through the results.
    """
    @property
    def projects(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.project_pb2.Project]:
        """List of Project resources."""

    def __init__(
        self,
        *,
        projects: collections.abc.Iterable[yandex.cloud.datasphere.v2.project_pb2.Project] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["next_page_token", b"next_page_token", "projects", b"projects"]) -> None: ...

global___ListProjectsResponse = ListProjectsResponse

@typing.final
class GetUnitBalanceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project to return the unit balance for."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___GetUnitBalanceRequest = GetUnitBalanceRequest

@typing.final
class GetUnitBalanceResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    UNIT_BALANCE_FIELD_NUMBER: builtins.int
    @property
    def unit_balance(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of units available to the project."""

    def __init__(
        self,
        *,
        unit_balance: google.protobuf.wrappers_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["unit_balance", b"unit_balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["unit_balance", b"unit_balance"]) -> None: ...

global___GetUnitBalanceResponse = GetUnitBalanceResponse

@typing.final
class SetUnitBalanceRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    UNIT_BALANCE_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project to set the unit balance for."""
    @property
    def unit_balance(self) -> google.protobuf.wrappers_pb2.Int64Value:
        """The number of units available to the project."""

    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        unit_balance: google.protobuf.wrappers_pb2.Int64Value | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["unit_balance", b"unit_balance"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id", "unit_balance", b"unit_balance"]) -> None: ...

global___SetUnitBalanceRequest = SetUnitBalanceRequest

@typing.final
class SetUnitBalanceMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project which unit balance is set."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___SetUnitBalanceMetadata = SetUnitBalanceMetadata

@typing.final
class ProjectExecutionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    NOTEBOOK_ID_FIELD_NUMBER: builtins.int
    CELL_ID_FIELD_NUMBER: builtins.int
    INPUT_VARIABLES_FIELD_NUMBER: builtins.int
    OUTPUT_VARIABLE_NAMES_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project to execute notebook/cell in."""
    notebook_id: builtins.str
    """The path to the executable notebook in the project storage. The maximum string length is 200 characters.

    To get the path, right-click on the notebook in JupyterLab and select `Copy path`.
    """
    cell_id: builtins.str
    """ID of the cell to execute.
    Deprecated
    """
    @property
    def input_variables(self) -> google.protobuf.struct_pb2.Struct:
        """Values of input variables."""

    @property
    def output_variable_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of output variables."""

    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        notebook_id: builtins.str = ...,
        cell_id: builtins.str = ...,
        input_variables: google.protobuf.struct_pb2.Struct | None = ...,
        output_variable_names: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cell_id", b"cell_id", "input_variables", b"input_variables", "notebook_id", b"notebook_id", "target", b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cell_id", b"cell_id", "input_variables", b"input_variables", "notebook_id", b"notebook_id", "output_variable_names", b"output_variable_names", "project_id", b"project_id", "target", b"target"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["target", b"target"]) -> typing.Literal["notebook_id", "cell_id"] | None: ...

global___ProjectExecutionRequest = ProjectExecutionRequest

@typing.final
class ProjectExecutionMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    NOTEBOOK_ID_FIELD_NUMBER: builtins.int
    CELL_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project in which notebook is being executed."""
    notebook_id: builtins.str
    """ID of the notebook that is being executed"""
    cell_id: builtins.str
    """ID of the cell that is being executed"""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        notebook_id: builtins.str = ...,
        cell_id: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["cell_id", b"cell_id", "notebook_id", b"notebook_id", "target", b"target"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cell_id", b"cell_id", "notebook_id", b"notebook_id", "project_id", b"project_id", "target", b"target"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["target", b"target"]) -> typing.Literal["notebook_id", "cell_id"] | None: ...

global___ProjectExecutionMetadata = ProjectExecutionMetadata

@typing.final
class ProjectExecutionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CHECKPOINT_ID_FIELD_NUMBER: builtins.int
    OUTPUT_VARIABLES_FIELD_NUMBER: builtins.int
    EXECUTION_STATUS_FIELD_NUMBER: builtins.int
    checkpoint_id: builtins.str
    """ID of the checkpoint resulting from the execution.
    <project_id>/checkpoint/<uuid>
    """
    execution_status: global___ExecutionStatus.ValueType
    """Execution final status."""
    @property
    def output_variables(self) -> google.protobuf.struct_pb2.Struct:
        """Values of output variables resulting from the execution."""

    def __init__(
        self,
        *,
        checkpoint_id: builtins.str = ...,
        output_variables: google.protobuf.struct_pb2.Struct | None = ...,
        execution_status: global___ExecutionStatus.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["output_variables", b"output_variables"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["checkpoint_id", b"checkpoint_id", "execution_status", b"execution_status", "output_variables", b"output_variables"]) -> None: ...

global___ProjectExecutionResponse = ProjectExecutionResponse

@typing.final
class CellOutputsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    CELL_ID_FIELD_NUMBER: builtins.int
    CHECKPOINT_ID_FIELD_NUMBER: builtins.int
    START_AT_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project to return cell outputs for."""
    cell_id: builtins.str
    """ID of the cell to return outputs for."""
    checkpoint_id: builtins.str
    """ID of the checkpoint to return cell outputs for."""
    @property
    def start_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Timestamp from which to return outputs."""

    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        cell_id: builtins.str = ...,
        checkpoint_id: builtins.str = ...,
        start_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["start_at", b"start_at"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cell_id", b"cell_id", "checkpoint_id", b"checkpoint_id", "project_id", b"project_id", "start_at", b"start_at"]) -> None: ...

global___CellOutputsRequest = CellOutputsRequest

@typing.final
class CellOutputsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OUTPUTS_FIELD_NUMBER: builtins.int
    @property
    def outputs(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """List of outputs."""

    def __init__(
        self,
        *,
        outputs: collections.abc.Iterable[builtins.str] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["outputs", b"outputs"]) -> None: ...

global___CellOutputsResponse = CellOutputsResponse

@typing.final
class GetStateVariablesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    NOTEBOOK_ID_FIELD_NUMBER: builtins.int
    VARIABLE_NAMES_FIELD_NUMBER: builtins.int
    CHECKPOINT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project, for which to return state variables."""
    notebook_id: builtins.str
    """ID of the notebook, for which to return state variables."""
    checkpoint_id: builtins.str
    """ID of the checkpoint, for which to return state variables."""
    @property
    def variable_names(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """Names of variables to return."""

    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        notebook_id: builtins.str = ...,
        variable_names: collections.abc.Iterable[builtins.str] | None = ...,
        checkpoint_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["checkpoint_id", b"checkpoint_id", "notebook_id", b"notebook_id", "project_id", b"project_id", "variable_names", b"variable_names"]) -> None: ...

global___GetStateVariablesRequest = GetStateVariablesRequest

@typing.final
class GetStateVariablesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    VARIABLES_FIELD_NUMBER: builtins.int
    @property
    def variables(self) -> google.protobuf.struct_pb2.Struct:
        """Values of the specified variables."""

    def __init__(
        self,
        *,
        variables: google.protobuf.struct_pb2.Struct | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["variables", b"variables"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["variables", b"variables"]) -> None: ...

global___GetStateVariablesResponse = GetStateVariablesResponse

@typing.final
class SetProjectAccessBindingsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project which access bindings are set."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___SetProjectAccessBindingsMetadata = SetProjectAccessBindingsMetadata

@typing.final
class UpdateProjectAccessBindingsMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project which access bindings are updated."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___UpdateProjectAccessBindingsMetadata = UpdateProjectAccessBindingsMetadata

@typing.final
class AddResourceToProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    resource_type: yandex.cloud.datasphere.v2.resource_types_pb2.ResourceType.ValueType
    resource_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        resource_type: yandex.cloud.datasphere.v2.resource_types_pb2.ResourceType.ValueType = ...,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id", "resource_id", b"resource_id", "resource_type", b"resource_type"]) -> None: ...

global___AddResourceToProjectRequest = AddResourceToProjectRequest

@typing.final
class RemoveResourceFromProjectRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    RESOURCE_TYPE_FIELD_NUMBER: builtins.int
    RESOURCE_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    resource_type: yandex.cloud.datasphere.v2.resource_types_pb2.ResourceType.ValueType
    resource_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        resource_type: yandex.cloud.datasphere.v2.resource_types_pb2.ResourceType.ValueType = ...,
        resource_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id", "resource_id", b"resource_id", "resource_type", b"resource_type"]) -> None: ...

global___RemoveResourceFromProjectRequest = RemoveResourceFromProjectRequest

@typing.final
class GetProjectRestrictionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___GetProjectRestrictionsRequest = GetProjectRestrictionsRequest

@typing.final
class SetProjectRestrictionsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    RESTRICTIONS_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project."""
    @property
    def restrictions(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.restrictions_pb2.Restriction]:
        """List of restrictions to set."""

    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        restrictions: collections.abc.Iterable[yandex.cloud.datasphere.v2.restrictions_pb2.Restriction] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id", "restrictions", b"restrictions"]) -> None: ...

global___SetProjectRestrictionsRequest = SetProjectRestrictionsRequest
