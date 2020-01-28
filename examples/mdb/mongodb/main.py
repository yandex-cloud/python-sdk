#!/usr/bin/env python3
import argparse
import json
from sys import stdout

from google.protobuf.field_mask_pb2 import FieldMask

from yandex.cloud.mdb.mongodb.v1.database_pb2 import DatabaseSpec
from yandex.cloud.mdb.mongodb.v1.user_pb2 import Permission, UserSpec
import yandex.cloud.mdb.mongodb.v1.cluster_pb2 as cluster_pb
import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2 as cluster_service
import yandex.cloud.mdb.mongodb.v1.cluster_service_pb2_grpc as cluster_service_grpc

import yandexcloud


def main():
    arguments = parse_cmd()
    if arguments.token:
        sdk = yandexcloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = yandexcloud.SDK(service_account_key=json.load(infile))

    fill_missing_flags(sdk, arguments)

    req = create_cluster_request(arguments)
    cluster = None
    try:
        cluster = create_cluster(sdk, req)
        change_cluster_description(sdk, cluster)
        add_cluster_host(sdk, cluster, arguments)
    finally:
        if cluster is not None:
            delete_cluster(sdk, cluster)


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


def fill_missing_flags(sdk, flags):
    if not flags.network_id:
        flags.network_id = sdk.helpers.find_network_id(folder_id=flags.folder_id)

    if not flags.subnet_id:
        flags.subnet_id = sdk.helpers.find_subnet_id(
            folder_id=flags.folder_id,
            zone_id=flags.zone,
            network_id=flags.network_id
        )


def create_cluster(sdk, req):
    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Create(req)

    meta = cluster_service.CreateClusterMetadata()
    operation.metadata.Unpack(meta)

    print("Creating cluster {}".format(meta.cluster_id))
    operation = sdk.wait_for_operation(operation.id, print_to_stream=stdout)

    cluster = cluster_pb.Cluster()
    operation.response.Unpack(cluster)
    return cluster


def add_cluster_host(sdk, cluster, params):
    print("Adding host to cluster {}".format(cluster.id))

    host_specs = [cluster_service.HostSpec(zone_id=params.zone, subnet_id=params.subnet_id, assign_public_ip=False)]
    req = cluster_service.AddClusterHostsRequest(cluster_id=cluster.id, host_specs=host_specs)

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).AddHosts(req)
    sdk.wait_for_operation(operation.id, print_to_stream=stdout)


def change_cluster_description(sdk, cluster):
    print("Updating cluster {}".format(cluster.id))
    mask = FieldMask(paths=["description"])
    update_req = cluster_service.UpdateClusterRequest(cluster_id=cluster.id, update_mask=mask,
                                                      description="New Description!!!")

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Update(update_req)
    sdk.wait_for_operation(operation.id, print_to_stream=stdout)


def delete_cluster(sdk, cluster):
    print("Deleting cluster {}".format(cluster.id))
    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Delete(
        cluster_service.DeleteClusterRequest(cluster_id=cluster.id))
    sdk.wait_for_operation(operation.id, print_to_stream=stdout)


def create_cluster_request(params):
    database_specs = [DatabaseSpec(name=params.db_name)]
    permissions = [Permission(database_name=params.db_name)]
    user_specs = [UserSpec(name=params.user_name, password=params.user_password, permissions=permissions)]

    host_specs = [cluster_service.HostSpec(zone_id=params.zone, subnet_id=params.subnet_id, assign_public_ip=False)]
    res = cluster_pb.Resources(resource_preset_id="s2.micro", disk_size=10 * (1024 ** 3), disk_type_id="network-ssd")

    config_spec = cluster_service.ConfigSpec(
        version="3.6",
        mongodb_spec_3_6=cluster_service.MongodbSpec3_6(mongod=cluster_service.MongodbSpec3_6.Mongod(resources=res)))

    return cluster_service.CreateClusterRequest(
        folder_id=params.folder_id,
        name=params.cluster_name,
        description=params.cluster_desc,
        environment="PRODUCTION",
        config_spec=config_spec,
        database_specs=database_specs,
        user_specs=user_specs,
        host_specs=host_specs,
        network_id=params.network_id
    )


if __name__ == '__main__':
    main()
