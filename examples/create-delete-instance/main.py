#!/usr/bin/env python3
import argparse
import json
from sys import stdout

import grpc

from yandex.cloud.compute.v1.image_service_pb2 import GetImageLatestByFamilyRequest
from yandex.cloud.compute.v1.image_service_pb2_grpc import ImageServiceStub
from yandex.cloud.compute.v1.instance_pb2 import IPV4, Instance
from yandex.cloud.compute.v1.instance_service_pb2 import (
    CreateInstanceRequest,
    ResourcesSpec,
    AttachedDiskSpec,
    NetworkInterfaceSpec,
    PrimaryAddressSpec,
    OneToOneNatSpec,
    DeleteInstanceRequest,
    CreateInstanceMetadata,
)
from yandex.cloud.compute.v1.instance_service_pb2_grpc import InstanceServiceStub

import yandexcloud


def create_instance(sdk, folder_id,  zone, name, subnet_id):
    image_service = sdk.client(ImageServiceStub)
    source_image = image_service.GetLatestByFamily(
        GetImageLatestByFamilyRequest(
            folder_id='standard-images',
            family='debian-9'))
    subnet_id = subnet_id or sdk.helpers.get_subnet(folder_id, zone)
    instance_service = sdk.client(InstanceServiceStub)
    operation = instance_service.Create(CreateInstanceRequest(
        folder_id=folder_id,
        name=name,
        resources_spec=ResourcesSpec(
            memory=2 * 2**30,
            cores=1,
            core_fraction=0),
        zone_id=zone,
        platform_id='standard-v1',
        boot_disk_spec=AttachedDiskSpec(
            auto_delete=True,
            disk_spec=AttachedDiskSpec.DiskSpec(
                type_id='network-hdd',
                size=20 * 2 ** 30,
                image_id=source_image.id)),
        network_interface_specs=[
            NetworkInterfaceSpec(
                subnet_id=subnet_id,
                primary_v4_address_spec=PrimaryAddressSpec(
                    one_to_one_nat_spec=OneToOneNatSpec(
                        ip_version=IPV4,
                    ))),
        ],
    ))
    print('Creating initiated')
    return operation


def delete_instance(sdk, instance_id):
    instance_service = sdk.client(InstanceServiceStub)
    return instance_service.Delete(
        DeleteInstanceRequest(instance_id=instance_id))


def main():
    arguments = parse_args()
    interceptor = yandexcloud.RetryInterceptor(max_retry_count=5, retriable_codes=[grpc.StatusCode.UNAVAILABLE])
    if arguments.token:
        sdk = yandexcloud.SDK(interceptor=interceptor, token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = yandexcloud.SDK(interceptor=interceptor, service_account_key=json.load(infile))

    subnet_id = arguments.subnet_id
    if not subnet_id:
        network_id = sdk.helpers.find_network_id(folder_id=arguments.folder_id)
        subnet_id = sdk.helpers.find_subnet_id(
            folder_id=arguments.folder_id,
            zone_id=arguments.zone,
            network_id=network_id,
        )
    operation = create_instance(sdk, arguments.folder_id, arguments.zone, arguments.name, subnet_id)
    meta = CreateInstanceMetadata()
    operation.metadata.Unpack(meta)
    print('Creating instance {}'.format(meta.instance_id))
    operation = sdk.wait_for_operation(operation.id, print_to_stream=stdout)

    instance = Instance()
    operation.response.Unpack(instance)

    print('Deleting instance {}'.format(instance.id))
    operation = delete_instance(sdk, instance.id)
    sdk.wait_for_operation(operation.id, print_to_stream=stdout)


def parse_args():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawTextHelpFormatter)

    auth = parser.add_mutually_exclusive_group(required=True)
    auth.add_argument(
        '--sa-json-path',
        help='Path to the service account key JSON file.\nThis file can be created using YC CLI:\n'
        'yc iam key create --output sa.json --service-account-id <id>',
    )
    auth.add_argument('--token', help='OAuth token')
    parser.add_argument('--folder-id', help='Your Yandex.Cloud folder id', required=True)
    parser.add_argument(
        '--zone', default='ru-central1-b',
        help='Compute Engine zone to deploy to.')
    parser.add_argument(
        '--name', default='demo-instance', help='New instance name.')
    parser.add_argument(
        '--subnet-id', help='Subnet of the instance')

    return parser.parse_args()


if __name__ == '__main__':
    main()
