#!/usr/bin/env python3
import argparse
import json
import logging

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
    DeleteInstanceMetadata,
)
from yandex.cloud.compute.v1.instance_service_pb2_grpc import InstanceServiceStub

import yandexcloud


def create_instance(sdk, folder_id, zone, name, subnet_id):
    image_service = sdk.client(ImageServiceStub)
    source_image = image_service.GetLatestByFamily(
        GetImageLatestByFamilyRequest(
            folder_id='standard-images',
            family='debian-9'
        )
    )
    subnet_id = subnet_id or sdk.helpers.get_subnet(folder_id, zone)
    instance_service = sdk.client(InstanceServiceStub)
    operation = instance_service.Create(CreateInstanceRequest(
        folder_id=folder_id,
        name=name,
        resources_spec=ResourcesSpec(
            memory=2 * 2 ** 30,
            cores=1,
            core_fraction=0,
        ),
        zone_id=zone,
        platform_id='standard-v1',
        boot_disk_spec=AttachedDiskSpec(
            auto_delete=True,
            disk_spec=AttachedDiskSpec.DiskSpec(
                type_id='network-hdd',
                size=20 * 2 ** 30,
                image_id=source_image.id,
            )
        ),
        network_interface_specs=[
            NetworkInterfaceSpec(
                subnet_id=subnet_id,
                primary_v4_address_spec=PrimaryAddressSpec(
                    one_to_one_nat_spec=OneToOneNatSpec(
                        ip_version=IPV4,
                    )
                )
            ),
        ],
        metadata={
            'metadata-key': 'metadata-value',
        },
    ))
    logging.info('Creating initiated')
    return operation


def delete_instance(sdk, instance_id):
    instance_service = sdk.client(InstanceServiceStub)
    return instance_service.Delete(
        DeleteInstanceRequest(instance_id=instance_id))


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_args()
    interceptor = yandexcloud.RetryInterceptor(max_retry_count=5, retriable_codes=[grpc.StatusCode.UNAVAILABLE])
    if arguments.token:
        sdk = yandexcloud.SDK(interceptor=interceptor, token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = yandexcloud.SDK(interceptor=interceptor, service_account_key=json.load(infile))

    fill_missing_arguments(sdk, arguments)

    instance_id = None
    try:
        operation = create_instance(sdk, arguments.folder_id, arguments.zone, arguments.name, arguments.subnet_id)
        operation_result = sdk.wait_operation_and_get_result(
            operation,
            response_type=Instance,
            meta_type=CreateInstanceMetadata,
        )

        instance_id = operation_result.response.id

    finally:
        if instance_id:
            logging.info('Deleting instance {}'.format(instance_id))
            operation = delete_instance(sdk, instance_id)
            sdk.wait_operation_and_get_result(
                operation,
                meta_type=DeleteInstanceMetadata,
            )


def fill_missing_arguments(sdk, arguments):
    if not arguments.subnet_id:
        network_id = sdk.helpers.find_network_id(folder_id=arguments.folder_id)
        arguments.subnet_id = sdk.helpers.find_subnet_id(
            folder_id=arguments.folder_id,
            zone_id=arguments.zone,
            network_id=network_id,
        )


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
