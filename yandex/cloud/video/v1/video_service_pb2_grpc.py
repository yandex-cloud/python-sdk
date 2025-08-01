# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

from yandex.cloud.operation import operation_pb2 as yandex_dot_cloud_dot_operation_dot_operation__pb2
from yandex.cloud.video.v1 import video_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_video__pb2
from yandex.cloud.video.v1 import video_service_pb2 as yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2

GRPC_GENERATED_VERSION = '1.70.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in yandex/cloud/video/v1/video_service_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class VideoServiceStub(object):
    """Video management service.
    Provides methods for creating, retrieving, updating, and deleting videos,
    as well as managing video-related operations such as transcoding, publishing,
    and generating playback URLs.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Get = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/Get',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__pb2.Video.FromString,
                _registered_method=True)
        self.List = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/List',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.ListVideoRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.ListVideoResponse.FromString,
                _registered_method=True)
        self.BatchGet = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/BatchGet',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideosRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideosResponse.FromString,
                _registered_method=True)
        self.Create = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/Create',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.CreateVideoRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Update = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/Update',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.UpdateVideoRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Transcode = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/Transcode',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.TranscodeVideoRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.Delete = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/Delete',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.DeleteVideoRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.BatchDelete = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/BatchDelete',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchDeleteVideosRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.PerformAction = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/PerformAction',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.PerformVideoActionRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
                _registered_method=True)
        self.GetPlayerURL = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/GetPlayerURL',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoPlayerURLRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoPlayerURLResponse.FromString,
                _registered_method=True)
        self.BatchGetPlayerURLs = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/BatchGetPlayerURLs',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideoPlayerURLsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideoPlayerURLsResponse.FromString,
                _registered_method=True)
        self.GetManifests = channel.unary_unary(
                '/yandex.cloud.video.v1.VideoService/GetManifests',
                request_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoManifestsRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoManifestsResponse.FromString,
                _registered_method=True)


class VideoServiceServicer(object):
    """Video management service.
    Provides methods for creating, retrieving, updating, and deleting videos,
    as well as managing video-related operations such as transcoding, publishing,
    and generating playback URLs.
    """

    def Get(self, request, context):
        """Retrieves detailed information about a specific video by its ID.
        Returns all video metadata, status, and related information.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def List(self, request, context):
        """Lists all videos in a specific channel with pagination support.
        Results can be filtered and sorted using the provided parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGet(self, request, context):
        """Retrieves multiple videos by their IDs in a specific channel in a single request.
        This is more efficient than making multiple Get requests when retrieving several videos.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Creates a new video in the specified channel.
        The video can be created from different sources: TUS upload, direct link, or S3 storage.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Updates an existing video's metadata and settings.
        Only fields specified in the field_mask will be updated.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Transcode(self, request, context):
        """Initiates or updates video transcoding with specified parameters.
        Can be used to start transcoding for videos with auto_transcode=DISABLE,
        or to re-process a completed video with new transcoding settings.
        Supports additional features like subtitle processing, translation, and summarization.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Deletes a specific video by its ID.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchDelete(self, request, context):
        """Deletes multiple videos in a specific channel in a single request.
        This is more efficient than making multiple Delete requests when removing several videos.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PerformAction(self, request, context):
        """Performs a specific action on a video, such as publishing or unpublishing.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetPlayerURL(self, request, context):
        """Generates a standard player URL for watching the video.
        The URL respects the video's access rights and can include custom player parameters.
        For videos with signed URL access, an expiration duration can be specified.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def BatchGetPlayerURLs(self, request, context):
        """Generates multiple player URLs for a list of videos in a specific channel in a single request.
        This is more efficient than making multiple GetPlayerURL requests when retrieving several URLs.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetManifests(self, request, context):
        """Retrieves the manifest URLs for a specific video.
        Manifests are used by video players to access the video content with adaptive bitrate streaming.
        Supports different manifest types (HLS, DASH) and configuration parameters.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_VideoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Get': grpc.unary_unary_rpc_method_handler(
                    servicer.Get,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__pb2.Video.SerializeToString,
            ),
            'List': grpc.unary_unary_rpc_method_handler(
                    servicer.List,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.ListVideoRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.ListVideoResponse.SerializeToString,
            ),
            'BatchGet': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGet,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideosRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideosResponse.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.CreateVideoRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.UpdateVideoRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Transcode': grpc.unary_unary_rpc_method_handler(
                    servicer.Transcode,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.TranscodeVideoRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.DeleteVideoRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'BatchDelete': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchDelete,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchDeleteVideosRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'PerformAction': grpc.unary_unary_rpc_method_handler(
                    servicer.PerformAction,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.PerformVideoActionRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.SerializeToString,
            ),
            'GetPlayerURL': grpc.unary_unary_rpc_method_handler(
                    servicer.GetPlayerURL,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoPlayerURLRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoPlayerURLResponse.SerializeToString,
            ),
            'BatchGetPlayerURLs': grpc.unary_unary_rpc_method_handler(
                    servicer.BatchGetPlayerURLs,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideoPlayerURLsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideoPlayerURLsResponse.SerializeToString,
            ),
            'GetManifests': grpc.unary_unary_rpc_method_handler(
                    servicer.GetManifests,
                    request_deserializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoManifestsRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoManifestsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.video.v1.VideoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('yandex.cloud.video.v1.VideoService', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class VideoService(object):
    """Video management service.
    Provides methods for creating, retrieving, updating, and deleting videos,
    as well as managing video-related operations such as transcoding, publishing,
    and generating playback URLs.
    """

    @staticmethod
    def Get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/Get',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_video__pb2.Video.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def List(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/List',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.ListVideoRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.ListVideoResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchGet(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/BatchGet',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideosRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideosResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/Create',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.CreateVideoRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/Update',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.UpdateVideoRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Transcode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/Transcode',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.TranscodeVideoRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/Delete',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.DeleteVideoRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchDelete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/BatchDelete',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchDeleteVideosRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def PerformAction(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/PerformAction',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.PerformVideoActionRequest.SerializeToString,
            yandex_dot_cloud_dot_operation_dot_operation__pb2.Operation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetPlayerURL(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/GetPlayerURL',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoPlayerURLRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoPlayerURLResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def BatchGetPlayerURLs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/BatchGetPlayerURLs',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideoPlayerURLsRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.BatchGetVideoPlayerURLsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def GetManifests(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/yandex.cloud.video.v1.VideoService/GetManifests',
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoManifestsRequest.SerializeToString,
            yandex_dot_cloud_dot_video_dot_v1_dot_video__service__pb2.GetVideoManifestsResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
