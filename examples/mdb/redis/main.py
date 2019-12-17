#!/usr/bin/env python3
import argparse
import sys
import time

from google.protobuf.field_mask_pb2 import FieldMask

from yandex.cloud.vpc.v1.network_service_pb2 import ListNetworksRequest
from yandex.cloud.vpc.v1.network_service_pb2_grpc import NetworkServiceStub
from yandex.cloud.vpc.v1.subnet_service_pb2 import ListSubnetsRequest
from yandex.cloud.vpc.v1.subnet_service_pb2_grpc import SubnetServiceStub

import yandex.cloud.mdb.redis.v1.cluster_pb2 as cluster_pb
import yandex.cloud.mdb.redis.v1.config.redis5_0_pb2 as redis5_0_pb2
import yandex.cloud.mdb.redis.v1.cluster_service_pb2 as cluster_service
import yandex.cloud.mdb.redis.v1.cluster_service_pb2_grpc as cluster_service_grpc

import yandexcloud


def wait_for_operation(sdk, op):
    waiter = sdk.waiter(op.id)
    for _ in waiter:
        sys.stdout.write('.')
        sys.stdout.flush()
        time.sleep(1)

    print('done')
    return waiter.operation


def main():
    flags = parse_cmd()
    sdk = yandexcloud.SDK(token=flags.token)

    fill_missing_flags(sdk, flags)

    req = create_cluster_request(flags)
    cluster = None
    try:
        cluster = create_cluster(sdk, req)
        change_cluster_description(sdk, cluster)
        add_cluster_host(sdk, cluster, flags)
    finally:
        if cluster is not None:
            delete_cluster(sdk, cluster)


def parse_cmd():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--token', help='OAuth token')
    parser.add_argument('--folder-id', help='Your Yandex.Cloud folder id')
    parser.add_argument('--zone', default='ru-central1-b', help='Compute Engine zone to deploy to')
    parser.add_argument('--network-id', default='', help='Your Yandex.Cloud network id')
    parser.add_argument('--subnet-id', default='', help='Subnet for the cluster')
    parser.add_argument('--cluster-name', default='cluster1', help='New cluster name')
    parser.add_argument('--cluster-desc', default='', help='New cluster description')
    parser.add_argument('--password', default='password123')

    return parser.parse_args()


def fill_missing_flags(sdk, flags):
    if not flags.network_id:
        flags.network_id = find_network(sdk, flags.folder_id)

    if not flags.subnet_id:
        flags.subnet_id = find_subnet(sdk, folder_id=flags.folder_id, zone_id=flags.zone, network_id=flags.network_id)


def find_network(sdk, folder_id):
    networks = sdk.client(NetworkServiceStub).List(ListNetworksRequest(folder_id=folder_id)).networks
    networks = [n for n in networks if n.folder_id == folder_id]

    if not networks:
        raise RuntimeError("no networks in folder: {}".format(folder_id))

    return networks[0].id


def find_subnet(sdk, folder_id, zone_id, network_id):
    subnet_service = sdk.client(SubnetServiceStub)
    subnets = subnet_service.List(ListSubnetsRequest(
        folder_id=folder_id)).subnets
    applicable = [s for s in subnets if s.zone_id == zone_id and s.network_id == network_id]
    if len(applicable) == 1:
        return applicable[0].id
    if len(applicable) == 0:
        message = 'There are no subnets in {} zone, please create it.'
        raise RuntimeError(message.format(zone_id))
    message = 'There are more than one subnet in {} zone, please specify it'
    raise RuntimeError(message.format(zone_id))


def create_cluster(sdk, req):
    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Create(req)

    meta = cluster_service.CreateClusterMetadata()
    operation.metadata.Unpack(meta)

    print("Creating cluster {}".format(meta.cluster_id))
    operation = wait_for_operation(sdk, operation)

    cluster = cluster_pb.Cluster()
    operation.response.Unpack(cluster)
    return cluster


def add_cluster_host(sdk, cluster, params):
    print("Adding host to cluster {}".format(cluster.id))

    host_specs = [cluster_service.HostSpec(zone_id=params.zone, subnet_id=params.subnet_id, assign_public_ip=False)]
    req = cluster_service.AddClusterHostsRequest(cluster_id=cluster.id, host_specs=host_specs)

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).AddHosts(req)
    wait_for_operation(sdk, operation)


def change_cluster_description(sdk, cluster):
    print("Updating cluster {}".format(cluster.id))
    mask = FieldMask(paths=["description"])
    update_req = cluster_service.UpdateClusterRequest(cluster_id=cluster.id, update_mask=mask,
                                                      description="New Description!!!")

    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Update(update_req)
    wait_for_operation(sdk, operation)


def delete_cluster(sdk, cluster):
    print("Deleting cluster {}".format(cluster.id))
    operation = sdk.client(cluster_service_grpc.ClusterServiceStub).Delete(
        cluster_service.DeleteClusterRequest(cluster_id=cluster.id))
    wait_for_operation(sdk, operation)


def create_cluster_request(params):
    host_specs = [cluster_service.HostSpec(zone_id=params.zone, subnet_id=params.subnet_id)]
    res = cluster_pb.Resources(resource_preset_id="b1.small", disk_size=8 * (1024 ** 3))

    config_spec = cluster_service.ConfigSpec(
        version='5.0',
        redis_config_5_0=redis5_0_pb2.RedisConfig5_0(
            maxmemory_policy="MAXMEMORY_POLICY_UNSPECIFIED",
            password=params.password,
        ),
        resources=res,
        access=cluster_pb.Access(data_lens=False),
    )

    return cluster_service.CreateClusterRequest(
        folder_id=params.folder_id,
        name=params.cluster_name,
        description=params.cluster_desc,
        environment="PRODUCTION",
        config_spec=config_spec,
        host_specs=host_specs,
        network_id=params.network_id,
        sharded=False,
    )


if __name__ == '__main__':
    main()
