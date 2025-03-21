"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.duration_pb2
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import sys
import typing
import yandex.cloud.datasphere.v2.jobs.jobs_pb2

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _StandardStream:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _StandardStreamEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_StandardStream.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    STANDARD_STREAM_UNSPECIFIED: _StandardStream.ValueType  # 0
    OUT: _StandardStream.ValueType  # 1
    """Stdout."""
    ERR: _StandardStream.ValueType  # 2
    """Stderr."""

class StandardStream(_StandardStream, metaclass=_StandardStreamEnumTypeWrapper): ...

STANDARD_STREAM_UNSPECIFIED: StandardStream.ValueType  # 0
OUT: StandardStream.ValueType  # 1
"""Stdout."""
ERR: StandardStream.ValueType  # 2
"""Stderr."""
global___StandardStream = StandardStream

@typing.final
class CreateProjectJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    JOB_PARAMETERS_FIELD_NUMBER: builtins.int
    CONFIG_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    DATA_TTL_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project."""
    config: builtins.str
    """Config of the job."""
    name: builtins.str
    """Name of the job."""
    desc: builtins.str
    """Description of the job."""
    @property
    def job_parameters(self) -> yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobParameters:
        """Parameters of the job."""

    @property
    def data_ttl(self) -> google.protobuf.duration_pb2.Duration:
        """Job data TTL."""

    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        job_parameters: yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobParameters | None = ...,
        config: builtins.str = ...,
        name: builtins.str = ...,
        desc: builtins.str = ...,
        data_ttl: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["data_ttl", b"data_ttl", "job_parameters", b"job_parameters"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["config", b"config", "data_ttl", b"data_ttl", "desc", b"desc", "job_parameters", b"job_parameters", "name", b"name", "project_id", b"project_id"]) -> None: ...

global___CreateProjectJobRequest = CreateProjectJobRequest

@typing.final
class CreateProjectJobMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project."""
    job_id: builtins.str
    """Job ID."""
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id", "project_id", b"project_id"]) -> None: ...

global___CreateProjectJobMetadata = CreateProjectJobMetadata

@typing.final
class CreateProjectJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    UPLOAD_FILES_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    @property
    def upload_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.jobs.jobs_pb2.StorageFile]:
        """Files to upload with their presigned URLs for upload."""

    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        upload_files: collections.abc.Iterable[yandex.cloud.datasphere.v2.jobs.jobs_pb2.StorageFile] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id", "upload_files", b"upload_files"]) -> None: ...

global___CreateProjectJobResponse = CreateProjectJobResponse

@typing.final
class CloneProjectJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SOURCE_JOB_ID_FIELD_NUMBER: builtins.int
    JOB_PARAMETERS_OVERRIDES_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    DESC_FIELD_NUMBER: builtins.int
    DATA_TTL_FIELD_NUMBER: builtins.int
    source_job_id: builtins.str
    """ID of job to be cloned."""
    name: builtins.str
    """New job name."""
    desc: builtins.str
    """New job description"""
    @property
    def job_parameters_overrides(self) -> yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobParameters:
        """Parameters overrides."""

    @property
    def data_ttl(self) -> google.protobuf.duration_pb2.Duration:
        """Data ttl."""

    def __init__(
        self,
        *,
        source_job_id: builtins.str = ...,
        job_parameters_overrides: yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobParameters | None = ...,
        name: builtins.str = ...,
        desc: builtins.str = ...,
        data_ttl: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["data_ttl", b"data_ttl", "job_parameters_overrides", b"job_parameters_overrides"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["data_ttl", b"data_ttl", "desc", b"desc", "job_parameters_overrides", b"job_parameters_overrides", "name", b"name", "source_job_id", b"source_job_id"]) -> None: ...

global___CloneProjectJobRequest = CloneProjectJobRequest

@typing.final
class CloneProjectJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    UPLOAD_FILES_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """Job ID."""
    @property
    def upload_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.jobs.jobs_pb2.StorageFile]:
        """Files with presigned URLs generated by server to upload them to storage. Order is arbitrary.

        Upload files include input files, executable file (python main script or binary executable) and local modules
        in case of python.

        If file was already uploaded, there will be no element for it.
        """

    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        upload_files: collections.abc.Iterable[yandex.cloud.datasphere.v2.jobs.jobs_pb2.StorageFile] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id", "upload_files", b"upload_files"]) -> None: ...

global___CloneProjectJobResponse = CloneProjectJobResponse

@typing.final
class CloneProjectJobMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    job_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id", "project_id", b"project_id"]) -> None: ...

global___CloneProjectJobMetadata = CloneProjectJobMetadata

@typing.final
class ExecuteProjectJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id"]) -> None: ...

global___ExecuteProjectJobRequest = ExecuteProjectJobRequest

@typing.final
class ExecuteProjectJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OUTPUT_FILES_FIELD_NUMBER: builtins.int
    OUTPUT_FILES_ERRORS_FIELD_NUMBER: builtins.int
    OUTPUT_DATASETS_FIELD_NUMBER: builtins.int
    RESULT_FIELD_NUMBER: builtins.int
    @property
    def output_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.jobs.jobs_pb2.StorageFile]:
        """Uploaded output files with URLs."""

    @property
    def output_files_errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.jobs.jobs_pb2.FileUploadError]:
        """Output file errors"""

    @property
    def output_datasets(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.jobs.jobs_pb2.OutputDataset]:
        """Created datasets"""

    @property
    def result(self) -> yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobResult:
        """Result of the job."""

    def __init__(
        self,
        *,
        output_files: collections.abc.Iterable[yandex.cloud.datasphere.v2.jobs.jobs_pb2.StorageFile] | None = ...,
        output_files_errors: collections.abc.Iterable[yandex.cloud.datasphere.v2.jobs.jobs_pb2.FileUploadError] | None = ...,
        output_datasets: collections.abc.Iterable[yandex.cloud.datasphere.v2.jobs.jobs_pb2.OutputDataset] | None = ...,
        result: yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobResult | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["result", b"result"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["output_datasets", b"output_datasets", "output_files", b"output_files", "output_files_errors", b"output_files_errors", "result", b"result"]) -> None: ...

global___ExecuteProjectJobResponse = ExecuteProjectJobResponse

@typing.final
class ExecuteProjectJobMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_FIELD_NUMBER: builtins.int
    PROGRESS_FIELD_NUMBER: builtins.int
    METADATA_FIELD_NUMBER: builtins.int
    @property
    def job(self) -> yandex.cloud.datasphere.v2.jobs.jobs_pb2.Job:
        """Instance of the job."""

    @property
    def progress(self) -> yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobProgress:
        """Job progress info"""

    @property
    def metadata(self) -> yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobMetadata:
        """Job metadata with main job info"""

    def __init__(
        self,
        *,
        job: yandex.cloud.datasphere.v2.jobs.jobs_pb2.Job | None = ...,
        progress: yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobProgress | None = ...,
        metadata: yandex.cloud.datasphere.v2.jobs.jobs_pb2.JobMetadata | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["job", b"job", "metadata", b"metadata", "progress", b"progress"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["job", b"job", "metadata", b"metadata", "progress", b"progress"]) -> None: ...

global___ExecuteProjectJobMetadata = ExecuteProjectJobMetadata

@typing.final
class CancelProjectJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    REASON_FIELD_NUMBER: builtins.int
    GRACEFUL_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    reason: builtins.str
    """Optional cancellation reason."""
    graceful: builtins.bool
    """If the job is launched with graceful shutdown support, the shutdown will be performed gracefully"""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        reason: builtins.str = ...,
        graceful: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["graceful", b"graceful", "job_id", b"job_id", "reason", b"reason"]) -> None: ...

global___CancelProjectJobRequest = CancelProjectJobRequest

@typing.final
class ReadProjectJobStdLogsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    offset: builtins.int
    """Log offset."""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        offset: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id", "offset", b"offset"]) -> None: ...

global___ReadProjectJobStdLogsRequest = ReadProjectJobStdLogsRequest

@typing.final
class ReadProjectJobStdLogsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOGS_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    offset: builtins.int
    """Log offset."""
    @property
    def logs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___StdLog]: ...
    def __init__(
        self,
        *,
        logs: collections.abc.Iterable[global___StdLog] | None = ...,
        offset: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["logs", b"logs", "offset", b"offset"]) -> None: ...

global___ReadProjectJobStdLogsResponse = ReadProjectJobStdLogsResponse

@typing.final
class ReadProjectJobLogsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    offset: builtins.int
    """Log offset."""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        offset: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id", "offset", b"offset"]) -> None: ...

global___ReadProjectJobLogsRequest = ReadProjectJobLogsRequest

@typing.final
class ReadProjectJobLogsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LOGS_FIELD_NUMBER: builtins.int
    OFFSET_FIELD_NUMBER: builtins.int
    offset: builtins.int
    """Log offset."""
    @property
    def logs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___LogMessage]: ...
    def __init__(
        self,
        *,
        logs: collections.abc.Iterable[global___LogMessage] | None = ...,
        offset: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["logs", b"logs", "offset", b"offset"]) -> None: ...

global___ReadProjectJobLogsResponse = ReadProjectJobLogsResponse

@typing.final
class DownloadProjectJobFilesRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    FILES_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    @property
    def files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.jobs.jobs_pb2.File]: ...
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        files: collections.abc.Iterable[yandex.cloud.datasphere.v2.jobs.jobs_pb2.File] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["files", b"files", "job_id", b"job_id"]) -> None: ...

global___DownloadProjectJobFilesRequest = DownloadProjectJobFilesRequest

@typing.final
class DownloadProjectJobFilesResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    DOWNLOAD_FILES_FIELD_NUMBER: builtins.int
    @property
    def download_files(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.jobs.jobs_pb2.StorageFile]: ...
    def __init__(
        self,
        *,
        download_files: collections.abc.Iterable[yandex.cloud.datasphere.v2.jobs.jobs_pb2.StorageFile] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["download_files", b"download_files"]) -> None: ...

global___DownloadProjectJobFilesResponse = DownloadProjectJobFilesResponse

@typing.final
class ListProjectJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    """ID of the project."""
    page_size: builtins.int
    """The maximum number of results per page to return. If the number of available
    results is larger than [page_size],
    the service returns a [ListProjectJobResponse.page_token]
    that can be used to get the next page of results in subsequent list requests.
    """
    page_token: builtins.str
    """Page token. To get the next page of results, set [page_token] to the
    [ListProjectJobResponse.page_token] returned by a previous list request.
    """
    filter: builtins.str
    """restrictions:
      * only `status` field is supported
      * only `IN` operator is supported
    example:
      * only running jobs == "status IN (EXECUTING, UPLOADING_OUTPUT)"
    """
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["filter", b"filter", "page_size", b"page_size", "page_token", b"page_token", "project_id", b"project_id"]) -> None: ...

global___ListProjectJobRequest = ListProjectJobRequest

@typing.final
class ListProjectJobResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOBS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for list requests. If the number of results
    is larger than [ListProjectJobRequest.page_size], use
    the [next_page_token] as the value
    for the [ListProjectJobRequest.page_token] query parameter
    in the next list request. Each subsequent list request will have its own
    [page_token] to continue paging through the results.
    """
    @property
    def jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.datasphere.v2.jobs.jobs_pb2.Job]:
        """Instances of the jobs."""

    def __init__(
        self,
        *,
        jobs: collections.abc.Iterable[yandex.cloud.datasphere.v2.jobs.jobs_pb2.Job] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["jobs", b"jobs", "next_page_token", b"next_page_token"]) -> None: ...

global___ListProjectJobResponse = ListProjectJobResponse

@typing.final
class GetProjectJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id"]) -> None: ...

global___GetProjectJobRequest = GetProjectJobRequest

@typing.final
class DeleteProjectJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id"]) -> None: ...

global___DeleteProjectJobRequest = DeleteProjectJobRequest

@typing.final
class DeleteProjectJobMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id"]) -> None: ...

global___DeleteProjectJobMetadata = DeleteProjectJobMetadata

@typing.final
class DeleteProjectJobDataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id"]) -> None: ...

global___DeleteProjectJobDataRequest = DeleteProjectJobDataRequest

@typing.final
class DeleteProjectJobDataMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    """ID of the job."""
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id"]) -> None: ...

global___DeleteProjectJobDataMetadata = DeleteProjectJobDataMetadata

@typing.final
class DeleteProjectJobDataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteProjectJobDataResponse = DeleteProjectJobDataResponse

@typing.final
class DeleteAllProjectJobDataRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___DeleteAllProjectJobDataRequest = DeleteAllProjectJobDataRequest

@typing.final
class DeleteAllProjectJobDataMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PROJECT_ID_FIELD_NUMBER: builtins.int
    project_id: builtins.str
    def __init__(
        self,
        *,
        project_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["project_id", b"project_id"]) -> None: ...

global___DeleteAllProjectJobDataMetadata = DeleteAllProjectJobDataMetadata

@typing.final
class DeleteAllProjectJobDataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___DeleteAllProjectJobDataResponse = DeleteAllProjectJobDataResponse

@typing.final
class SetProjectJobDataTtlRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOB_ID_FIELD_NUMBER: builtins.int
    TTL_FIELD_NUMBER: builtins.int
    job_id: builtins.str
    @property
    def ttl(self) -> google.protobuf.duration_pb2.Duration: ...
    def __init__(
        self,
        *,
        job_id: builtins.str = ...,
        ttl: google.protobuf.duration_pb2.Duration | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["ttl", b"ttl"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["job_id", b"job_id", "ttl", b"ttl"]) -> None: ...

global___SetProjectJobDataTtlRequest = SetProjectJobDataTtlRequest

@typing.final
class SetProjectJobDataTtlResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___SetProjectJobDataTtlResponse = SetProjectJobDataTtlResponse

@typing.final
class StdLog(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    class _Type:
        ValueType = typing.NewType("ValueType", builtins.int)
        V: typing_extensions.TypeAlias = ValueType

    class _TypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[StdLog._Type.ValueType], builtins.type):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
        TYPE_UNSPECIFIED: StdLog._Type.ValueType  # 0
        OUT: StdLog._Type.ValueType  # 1
        """stdout."""
        ERR: StdLog._Type.ValueType  # 2
        """stderr."""

    class Type(_Type, metaclass=_TypeEnumTypeWrapper): ...
    TYPE_UNSPECIFIED: StdLog.Type.ValueType  # 0
    OUT: StdLog.Type.ValueType  # 1
    """stdout."""
    ERR: StdLog.Type.ValueType  # 2
    """stderr."""

    CONTENT_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    content: builtins.bytes
    """Log contents."""
    type: global___StdLog.Type.ValueType
    """Log type."""
    def __init__(
        self,
        *,
        content: builtins.bytes = ...,
        type: global___StdLog.Type.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["content", b"content", "type", b"type"]) -> None: ...

global___StdLog = StdLog

@typing.final
class LogMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    CREATED_AT_FIELD_NUMBER: builtins.int
    STANDARD_STREAM_FIELD_NUMBER: builtins.int
    FILE_PATH_FIELD_NUMBER: builtins.int
    content: builtins.bytes
    """Log message contents."""
    standard_stream: global___StandardStream.ValueType
    """Program standard streams."""
    file_path: builtins.str
    """System debug log files."""
    @property
    def created_at(self) -> google.protobuf.timestamp_pb2.Timestamp:
        """Log message creation timestamp."""

    def __init__(
        self,
        *,
        content: builtins.bytes = ...,
        created_at: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        standard_stream: global___StandardStream.ValueType = ...,
        file_path: builtins.str = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["created_at", b"created_at", "file_path", b"file_path", "source", b"source", "standard_stream", b"standard_stream"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["content", b"content", "created_at", b"created_at", "file_path", b"file_path", "source", b"source", "standard_stream", b"standard_stream"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["source", b"source"]) -> typing.Literal["standard_stream", "file_path"] | None: ...

global___LogMessage = LogMessage
