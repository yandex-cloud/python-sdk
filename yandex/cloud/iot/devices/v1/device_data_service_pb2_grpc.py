# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from yandex.cloud.iot.devices.v1 import device_data_service_pb2 as yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__data__service__pb2


class DeviceDataServiceStub(object):
    """A set of methods to work with IoT Core messages on behalf of device
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Publish = channel.unary_unary(
                '/yandex.cloud.iot.devices.v1.DeviceDataService/Publish',
                request_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__data__service__pb2.PublishDeviceDataRequest.SerializeToString,
                response_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__data__service__pb2.PublishDeviceDataResponse.FromString,
                )


class DeviceDataServiceServicer(object):
    """A set of methods to work with IoT Core messages on behalf of device
    """

    def Publish(self, request, context):
        """Publishes message on behalf of specified device
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DeviceDataServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Publish': grpc.unary_unary_rpc_method_handler(
                    servicer.Publish,
                    request_deserializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__data__service__pb2.PublishDeviceDataRequest.FromString,
                    response_serializer=yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__data__service__pb2.PublishDeviceDataResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'yandex.cloud.iot.devices.v1.DeviceDataService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DeviceDataService(object):
    """A set of methods to work with IoT Core messages on behalf of device
    """

    @staticmethod
    def Publish(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/yandex.cloud.iot.devices.v1.DeviceDataService/Publish',
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__data__service__pb2.PublishDeviceDataRequest.SerializeToString,
            yandex_dot_cloud_dot_iot_dot_devices_dot_v1_dot_device__data__service__pb2.PublishDeviceDataResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)