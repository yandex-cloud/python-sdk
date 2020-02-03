#!/usr/bin/env python3
import argparse
import json
import logging

from google.protobuf.field_mask_pb2 import FieldMask

from yandex.cloud.mdb.mongodb.v1.database_pb2 import DatabaseSpec
from yandex.cloud.mdb.mongodb.v1.user_pb2 import Permission, UserSpec
import yandex.cloud.mdb.mongodb.v1.cluster_pb2 as cluster_pb
import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2 as cluster_service
import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2_grpc as cluster_service_grpc

import yandexcloud


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_cmd()
    if arguments.token:
        sdk = yandexcloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = yandexcloud.SDK(service_account_key=json.load(infile))

    fill_missing_arguments(sdk, arguments)

    cluster_id = None
    try:
        operation_result = create_cluster(sdk, create_cluster_request(arguments))
        cluster_id = operation_result.response.id
        change_cluster_description(sdk, cluster_id)
        add_cluster_host(sdk, cluster_id, arguments)
    finally:
        if cluster_id is not None:
            delete_cluster(sdk, cluster_id)


def parse_cmd():
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
    parser.add_argument('--zone', default='ru-central1-b', help='Compute Engine zone to deploy to')
    parser.add_argument('--network-id', default='', help='Your Yandex.Cloud network id')
    parser.add_argument('--subnet-id', default='', help='Subnet for the cluster')
    parser.add_argument('--cluster-name', default='mongodb666', help='New cluster name')
    parser.add_argument('--cluster-desc', default='', help='New cluster description')
    parser.add_argument('--db-name', default='db1', help='New database name')
    parser.add_argument('--user-name', default='user1')
    parser.add_argument('--user-password', default='password123')
    return parser.parse_args()


def fill_missing_arguments(sdk, arguments):
    if not arguments.network_id:
        arguments.network_id = sdk.helpers.find_network_id(folder_id=arguments.folder_id)

    if not arguments.subnet_id:
        arguments.subnet_id = sdk.helpers.find_subnet_id(
            folder_id=arguments.folder_id,
            zone_id=arguments.zone,
            network_id=arguments.network_id
        )


def create_cluster(sdk, request):
    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Create(request)
    return sdk.wait_operation_and_get_result(
        operation,
        response_type=cluster_pb.Cluster,
        meta_type=cluster_service.CreateClusterMetadata,
    )


def add_cluster_host(sdk, cluster_id, params):
    logging.info('Adding host to cluster {}'.format(cluster_id))

    host_specs = [cluster_service.HostSpec(zone_id=params.zone, subnet_id=params.subnet_id, assign_public_ip=False)]
    request = cluster_service.AddClusterHostsRequest(cluster_id=cluster_id, host_specs=host_specs)

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).AddHosts(request)
    return sdk.wait_operation_and_get_result(
        operation,
        meta_type=cluster_service.AddClusterHostsMetadata,
    )


def change_cluster_description(sdk, cluster_id):
    logging.info('Updating cluster {}'.format(cluster_id))
    mask = FieldMask(paths=['description'])
    request = cluster_service.UpdateClusterRequest(
        cluster_id=cluster_id,
        update_mask=mask,
        description='New Description'
    )

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Update(request)
    return sdk.wait_operation_and_get_result(
        operation,
        response_type=cluster_pb.Cluster,
        meta_type=cluster_service.UpdateClusterMetadata,
    )


def delete_cluster(sdk, cluster_id):
    logging.info('Deleting cluster {}'.format(cluster_id))
    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Delete(
        cluster_service.DeleteClusterRequest(cluster_id=cluster_id))
    return sdk.wait_operation_and_get_result(
        operation,
        meta_type=cluster_service.DeleteClusterMetadata,
    )

def create_cluster_request(params):
    database_specs = [DatabaseSpec(name=params.db_name)]
    permissions = [Permission(database_name=params.db_name)]
    user_specs = [UserSpec(name=params.user_name, password=params.user_password, permissions=permissions)]

    host_specs = [cluster_service.HostSpec(zone_id=params.zone, subnet_id=params.subnet_id, assign_public_ip=False)]
    res = cluster_pb.Resources(resource_preset_id='s2.micro', disk_size=10 * (1024 ** 3), disk_type_id='network-ssd')

    config_spec = cluster_service.ConfigSpec(
        version='3.6',
        mongodb_spec_3_6=cluster_service.MongodbSpec3_6(mongod=cluster_service.MongodbSpec3_6.Mongod(resources=res)))

    return cluster_service.CreateClusterRequest(
        folder_id=params.folder_id,
        name=params.cluster_name,
        description=params.cluster_desc,
        environment='PRODUCTION',
        config_spec=config_spec,
        database_specs=database_specs,
        user_specs=user_specs,
        host_specs=host_specs,
        network_id=params.network_id
    )


if __name__ == '__main__':
    main()
