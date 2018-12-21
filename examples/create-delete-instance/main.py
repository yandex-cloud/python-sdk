import argparse
import sys
import time

from yandex.cloud.compute.v1.image_service_pb2 import GetImageLatestByFamilyRequest
from yandex.cloud.compute.v1.image_service_pb2_grpc import ImageServiceStub
from yandex.cloud.compute.v1.instance_pb2 import IPV4, Instance
from yandex.cloud.compute.v1.instance_service_pb2 import CreateInstanceRequest, ResourcesSpec, AttachedDiskSpec, NetworkInterfaceSpec, PrimaryAddressSpec, OneToOneNatSpec, DeleteInstanceRequest, CreateInstanceMetadata
from yandex.cloud.compute.v1.instance_service_pb2_grpc import InstanceServiceStub
from yandex.cloud.vpc.v1.subnet_service_pb2 import ListSubnetsRequest
from yandex.cloud.vpc.v1.subnet_service_pb2_grpc import SubnetServiceStub

import yandexcloud


def wait_for_operation(sdk, op):
    waiter = sdk.waiter(op.id)
    for _ in waiter:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

    print('done')
    return waiter.operation


def get_subnet(sdk, folder_id, zone):
    subnet_service = sdk.client(SubnetServiceStub)
    subnets = subnet_service.List(ListSubnetsRequest(
        folder_id=folder_id)).subnets
    applicable = [s for s in subnets if s.zone_id == zone]
    if len(applicable) == 1:
        return applicable[0].id
    if len(applicable) == 0:
        message = 'There are no subnets in {} zone, please create it.'
        raise RuntimeError(message.format(zone))
    message = 'There are more than one subnet in {} zone, please specify it'
    raise RuntimeError(message.format(zone))


def create_instance(sdk, folder_id,  zone, name, subnet_id):
    image_service = sdk.client(ImageServiceStub)
    source_image = image_service.GetLatestByFamily(
        GetImageLatestByFamilyRequest(
            folder_id='standard-images',
            family='debian-9'))
    subnet_id = subnet_id or get_subnet(sdk, folder_id, zone)
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


def main(token, folder_id, zone, name, subnet_id):
    sdk = yandexcloud.SDK(token=token)
    operation = create_instance(sdk, folder_id, zone, name, subnet_id)
    meta = CreateInstanceMetadata()
    operation.metadata.Unpack(meta)
    print('Creating instance {}'.format(meta.instance_id))
    operation = wait_for_operation(sdk, operation)

    instance = Instance()
    operation.response.Unpack(instance)

    print('Deleting instance {}'.format(instance.id))
    operation = delete_instance(sdk, instance.id)
    wait_for_operation(sdk, operation)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--token', help='OAuth token')
    parser.add_argument('--folder-id', help='Your Yandex.Cloud folder id')
    parser.add_argument(
        '--zone', default='ru-central1-b',
        help='Compute Engine zone to deploy to.')
    parser.add_argument(
        '--name', default='demo-instance', help='New instance name.')
    parser.add_argument(
        '--subnet-id', default='', help='Subnet of the instance')

    args = parser.parse_args()

    main(args.token, args.folder_id, args.zone, args.name, args.subnet_id)
