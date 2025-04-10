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
import yandex.cloud.spark.v1.job_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Spark cluster."""
    job_id: builtins.str
    """ID of the Spark job to return."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "job_id", b"job_id"]) -> None: ...

global___GetJobRequest = GetJobRequest

@typing.final
class ListJobsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    FILTER_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to list Spark jobs of."""
    page_size: builtins.int
    """The maximum number of results per page that should be returned. If the number of available
    results is larger than `page_size`, the service returns a `next_page_token` that can be used
    to get the next page of results in subsequent ListJobs requests.
    Acceptable values are 0 to 1000, inclusive. Default value: 100.
    """
    page_token: builtins.str
    """Page token. Set `page_token` to the `next_page_token` returned by a previous ListJobs
    request to get the next page of results.
    """
    filter: builtins.str
    """String that describes a display filter."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
        filter: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "filter", b"filter", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListJobsRequest = ListJobsRequest

@typing.final
class ListJobsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    JOBS_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    next_page_token: builtins.str
    """This token allows you to get the next page of results for ListJobs requests,
    if the number of results is larger than `page_size` specified in the request.
    To get the next page, specify the value of `next_page_token` as a value for
    the `page_token` parameter in the next ListClusters request. Subsequent ListClusters
    requests will have their own `next_page_token` to continue paging through the results.
    """
    @property
    def jobs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[yandex.cloud.spark.v1.job_pb2.Job]:
        """Requested list of Spark jobs."""

    def __init__(
        self,
        *,
        jobs: collections.abc.Iterable[yandex.cloud.spark.v1.job_pb2.Job] | None = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["jobs", b"jobs", "next_page_token", b"next_page_token"]) -> None: ...

global___ListJobsResponse = ListJobsResponse

@typing.final
class CreateJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    SPARK_JOB_FIELD_NUMBER: builtins.int
    PYSPARK_JOB_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the cluster to create Spark job in."""
    name: builtins.str
    """Optional. Name of the job."""
    @property
    def spark_job(self) -> yandex.cloud.spark.v1.job_pb2.SparkJob: ...
    @property
    def pyspark_job(self) -> yandex.cloud.spark.v1.job_pb2.PysparkJob: ...
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        name: builtins.str = ...,
        spark_job: yandex.cloud.spark.v1.job_pb2.SparkJob | None = ...,
        pyspark_job: yandex.cloud.spark.v1.job_pb2.PysparkJob | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing.Literal["job_spec", b"job_spec", "pyspark_job", b"pyspark_job", "spark_job", b"spark_job"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "job_spec", b"job_spec", "name", b"name", "pyspark_job", b"pyspark_job", "spark_job", b"spark_job"]) -> None: ...
    def WhichOneof(self, oneof_group: typing.Literal["job_spec", b"job_spec"]) -> typing.Literal["spark_job", "pyspark_job"] | None: ...

global___CreateJobRequest = CreateJobRequest

@typing.final
class CreateJobMetadata(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Spark cluster."""
    job_id: builtins.str
    """ID of the Spark job."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "job_id", b"job_id"]) -> None: ...

global___CreateJobMetadata = CreateJobMetadata

@typing.final
class CancelJobRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Spark cluster."""
    job_id: builtins.str
    """ID of the Spark job to cancel."""
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        job_id: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "job_id", b"job_id"]) -> None: ...

global___CancelJobRequest = CancelJobRequest

@typing.final
class ListJobLogRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CLUSTER_ID_FIELD_NUMBER: builtins.int
    JOB_ID_FIELD_NUMBER: builtins.int
    PAGE_SIZE_FIELD_NUMBER: builtins.int
    PAGE_TOKEN_FIELD_NUMBER: builtins.int
    cluster_id: builtins.str
    """ID of the Spark cluster."""
    job_id: builtins.str
    """ID of the Spark job to return."""
    page_size: builtins.int
    """The maximum length of job output per papge that should be returned.
    If the number of available output is larger tha `page_size`, the service returns
    a `next_page_token` that can be used to get the next page of job output in subsequent ListLog requests.
    Acceptable values are 0 to 1048576. Default value: 1048576.
    """
    page_token: builtins.str
    """Page token. Set `page_token` to the `next_page_token` returned by a previous ListLog
    request to get the next page of results.
    """
    def __init__(
        self,
        *,
        cluster_id: builtins.str = ...,
        job_id: builtins.str = ...,
        page_size: builtins.int = ...,
        page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["cluster_id", b"cluster_id", "job_id", b"job_id", "page_size", b"page_size", "page_token", b"page_token"]) -> None: ...

global___ListJobLogRequest = ListJobLogRequest

@typing.final
class ListJobLogResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENT_FIELD_NUMBER: builtins.int
    NEXT_PAGE_TOKEN_FIELD_NUMBER: builtins.int
    content: builtins.str
    """Requested part of Spark Job log."""
    next_page_token: builtins.str
    """This token allows you to get the next page of results for ListLog requests,
    if the number of results is larger than `page_size` specified in the request.
    To get the next page, specify the value of `next_page_token` as a value for
    the `page_token` parameter in the next ListLog request. Subsequent ListLog
    requests will have their own `next_page_token` to continue paging through the results.
    """
    def __init__(
        self,
        *,
        content: builtins.str = ...,
        next_page_token: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["content", b"content", "next_page_token", b"next_page_token"]) -> None: ...

global___ListJobLogResponse = ListJobLogResponse
