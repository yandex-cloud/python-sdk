"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""

import abc
import collections.abc
import grpc
import grpc.aio
import typing
import yandex.cloud.operation.operation_pb2
import yandex.cloud.video.v1.video_pb2
import yandex.cloud.video.v1.video_service_pb2

_T = typing.TypeVar("_T")

class _MaybeAsyncIterator(collections.abc.AsyncIterator[_T], collections.abc.Iterator[_T], metaclass=abc.ABCMeta): ...

class _ServicerContext(grpc.ServicerContext, grpc.aio.ServicerContext):  # type: ignore[misc, type-arg]
    ...

class VideoServiceStub:
    """Video management service.
    Provides methods for creating, retrieving, updating, and deleting videos,
    as well as managing video-related operations such as transcoding, publishing,
    and generating playback URLs.
    """

    def __init__(self, channel: typing.Union[grpc.Channel, grpc.aio.Channel]) -> None: ...
    Get: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.GetVideoRequest,
        yandex.cloud.video.v1.video_pb2.Video,
    ]
    """Retrieves detailed information about a specific video by its ID.
    Returns all video metadata, status, and related information.
    """

    List: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.ListVideoRequest,
        yandex.cloud.video.v1.video_service_pb2.ListVideoResponse,
    ]
    """Lists all videos in a specific channel with pagination support.
    Results can be filtered and sorted using the provided parameters.
    """

    BatchGet: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.BatchGetVideosRequest,
        yandex.cloud.video.v1.video_service_pb2.BatchGetVideosResponse,
    ]
    """Retrieves multiple videos by their IDs in a specific channel in a single request.
    This is more efficient than making multiple Get requests when retrieving several videos.
    """

    Create: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.CreateVideoRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new video in the specified channel.
    The video can be created from different sources: TUS upload, direct link, or S3 storage.
    """

    Update: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.UpdateVideoRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates an existing video's metadata and settings.
    Only fields specified in the field_mask will be updated.
    """

    Transcode: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.TranscodeVideoRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Initiates or updates video transcoding with specified parameters.
    Can be used to start transcoding for videos with auto_transcode=DISABLE,
    or to re-process a completed video with new transcoding settings.
    Supports additional features like subtitle processing, translation, and summarization.
    """

    Delete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.DeleteVideoRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes a specific video by its ID."""

    BatchDelete: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.BatchDeleteVideosRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes multiple videos in a specific channel in a single request.
    This is more efficient than making multiple Delete requests when removing several videos.
    """

    PerformAction: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.PerformVideoActionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Performs a specific action on a video, such as publishing or unpublishing."""

    GetPlayerURL: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.GetVideoPlayerURLRequest,
        yandex.cloud.video.v1.video_service_pb2.GetVideoPlayerURLResponse,
    ]
    """Generates a standard player URL for watching the video.
    The URL respects the video's access rights and can include custom player parameters.
    For videos with signed URL access, an expiration duration can be specified.
    """

    BatchGetPlayerURLs: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.BatchGetVideoPlayerURLsRequest,
        yandex.cloud.video.v1.video_service_pb2.BatchGetVideoPlayerURLsResponse,
    ]
    """Generates multiple player URLs for a list of videos in a specific channel in a single request.
    This is more efficient than making multiple GetPlayerURL requests when retrieving several URLs.
    """

    GetManifests: grpc.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.GetVideoManifestsRequest,
        yandex.cloud.video.v1.video_service_pb2.GetVideoManifestsResponse,
    ]
    """Retrieves the manifest URLs for a specific video.
    Manifests are used by video players to access the video content with adaptive bitrate streaming.
    Supports different manifest types (HLS, DASH) and configuration parameters.
    """

class VideoServiceAsyncStub:
    """Video management service.
    Provides methods for creating, retrieving, updating, and deleting videos,
    as well as managing video-related operations such as transcoding, publishing,
    and generating playback URLs.
    """

    Get: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.GetVideoRequest,
        yandex.cloud.video.v1.video_pb2.Video,
    ]
    """Retrieves detailed information about a specific video by its ID.
    Returns all video metadata, status, and related information.
    """

    List: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.ListVideoRequest,
        yandex.cloud.video.v1.video_service_pb2.ListVideoResponse,
    ]
    """Lists all videos in a specific channel with pagination support.
    Results can be filtered and sorted using the provided parameters.
    """

    BatchGet: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.BatchGetVideosRequest,
        yandex.cloud.video.v1.video_service_pb2.BatchGetVideosResponse,
    ]
    """Retrieves multiple videos by their IDs in a specific channel in a single request.
    This is more efficient than making multiple Get requests when retrieving several videos.
    """

    Create: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.CreateVideoRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Creates a new video in the specified channel.
    The video can be created from different sources: TUS upload, direct link, or S3 storage.
    """

    Update: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.UpdateVideoRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Updates an existing video's metadata and settings.
    Only fields specified in the field_mask will be updated.
    """

    Transcode: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.TranscodeVideoRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Initiates or updates video transcoding with specified parameters.
    Can be used to start transcoding for videos with auto_transcode=DISABLE,
    or to re-process a completed video with new transcoding settings.
    Supports additional features like subtitle processing, translation, and summarization.
    """

    Delete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.DeleteVideoRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes a specific video by its ID."""

    BatchDelete: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.BatchDeleteVideosRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Deletes multiple videos in a specific channel in a single request.
    This is more efficient than making multiple Delete requests when removing several videos.
    """

    PerformAction: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.PerformVideoActionRequest,
        yandex.cloud.operation.operation_pb2.Operation,
    ]
    """Performs a specific action on a video, such as publishing or unpublishing."""

    GetPlayerURL: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.GetVideoPlayerURLRequest,
        yandex.cloud.video.v1.video_service_pb2.GetVideoPlayerURLResponse,
    ]
    """Generates a standard player URL for watching the video.
    The URL respects the video's access rights and can include custom player parameters.
    For videos with signed URL access, an expiration duration can be specified.
    """

    BatchGetPlayerURLs: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.BatchGetVideoPlayerURLsRequest,
        yandex.cloud.video.v1.video_service_pb2.BatchGetVideoPlayerURLsResponse,
    ]
    """Generates multiple player URLs for a list of videos in a specific channel in a single request.
    This is more efficient than making multiple GetPlayerURL requests when retrieving several URLs.
    """

    GetManifests: grpc.aio.UnaryUnaryMultiCallable[
        yandex.cloud.video.v1.video_service_pb2.GetVideoManifestsRequest,
        yandex.cloud.video.v1.video_service_pb2.GetVideoManifestsResponse,
    ]
    """Retrieves the manifest URLs for a specific video.
    Manifests are used by video players to access the video content with adaptive bitrate streaming.
    Supports different manifest types (HLS, DASH) and configuration parameters.
    """

class VideoServiceServicer(metaclass=abc.ABCMeta):
    """Video management service.
    Provides methods for creating, retrieving, updating, and deleting videos,
    as well as managing video-related operations such as transcoding, publishing,
    and generating playback URLs.
    """

    @abc.abstractmethod
    def Get(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.GetVideoRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.video_pb2.Video, collections.abc.Awaitable[yandex.cloud.video.v1.video_pb2.Video]]:
        """Retrieves detailed information about a specific video by its ID.
        Returns all video metadata, status, and related information.
        """

    @abc.abstractmethod
    def List(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.ListVideoRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.video_service_pb2.ListVideoResponse, collections.abc.Awaitable[yandex.cloud.video.v1.video_service_pb2.ListVideoResponse]]:
        """Lists all videos in a specific channel with pagination support.
        Results can be filtered and sorted using the provided parameters.
        """

    @abc.abstractmethod
    def BatchGet(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.BatchGetVideosRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.video_service_pb2.BatchGetVideosResponse, collections.abc.Awaitable[yandex.cloud.video.v1.video_service_pb2.BatchGetVideosResponse]]:
        """Retrieves multiple videos by their IDs in a specific channel in a single request.
        This is more efficient than making multiple Get requests when retrieving several videos.
        """

    @abc.abstractmethod
    def Create(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.CreateVideoRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Creates a new video in the specified channel.
        The video can be created from different sources: TUS upload, direct link, or S3 storage.
        """

    @abc.abstractmethod
    def Update(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.UpdateVideoRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Updates an existing video's metadata and settings.
        Only fields specified in the field_mask will be updated.
        """

    @abc.abstractmethod
    def Transcode(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.TranscodeVideoRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Initiates or updates video transcoding with specified parameters.
        Can be used to start transcoding for videos with auto_transcode=DISABLE,
        or to re-process a completed video with new transcoding settings.
        Supports additional features like subtitle processing, translation, and summarization.
        """

    @abc.abstractmethod
    def Delete(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.DeleteVideoRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes a specific video by its ID."""

    @abc.abstractmethod
    def BatchDelete(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.BatchDeleteVideosRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Deletes multiple videos in a specific channel in a single request.
        This is more efficient than making multiple Delete requests when removing several videos.
        """

    @abc.abstractmethod
    def PerformAction(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.PerformVideoActionRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.operation.operation_pb2.Operation, collections.abc.Awaitable[yandex.cloud.operation.operation_pb2.Operation]]:
        """Performs a specific action on a video, such as publishing or unpublishing."""

    @abc.abstractmethod
    def GetPlayerURL(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.GetVideoPlayerURLRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.video_service_pb2.GetVideoPlayerURLResponse, collections.abc.Awaitable[yandex.cloud.video.v1.video_service_pb2.GetVideoPlayerURLResponse]]:
        """Generates a standard player URL for watching the video.
        The URL respects the video's access rights and can include custom player parameters.
        For videos with signed URL access, an expiration duration can be specified.
        """

    @abc.abstractmethod
    def BatchGetPlayerURLs(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.BatchGetVideoPlayerURLsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.video_service_pb2.BatchGetVideoPlayerURLsResponse, collections.abc.Awaitable[yandex.cloud.video.v1.video_service_pb2.BatchGetVideoPlayerURLsResponse]]:
        """Generates multiple player URLs for a list of videos in a specific channel in a single request.
        This is more efficient than making multiple GetPlayerURL requests when retrieving several URLs.
        """

    @abc.abstractmethod
    def GetManifests(
        self,
        request: yandex.cloud.video.v1.video_service_pb2.GetVideoManifestsRequest,
        context: _ServicerContext,
    ) -> typing.Union[yandex.cloud.video.v1.video_service_pb2.GetVideoManifestsResponse, collections.abc.Awaitable[yandex.cloud.video.v1.video_service_pb2.GetVideoManifestsResponse]]:
        """Retrieves the manifest URLs for a specific video.
        Manifests are used by video players to access the video content with adaptive bitrate streaming.
        Supports different manifest types (HLS, DASH) and configuration parameters.
        """

def add_VideoServiceServicer_to_server(servicer: VideoServiceServicer, server: typing.Union[grpc.Server, grpc.aio.Server]) -> None: ...
