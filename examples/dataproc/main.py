#!/usr/bin/env python3
import argparse
import os
import sys
import time

from google.protobuf.field_mask_pb2 import FieldMask

from yandex.cloud.vpc.v1.network_service_pb2 import ListNetworksRequest
from yandex.cloud.vpc.v1.network_service_pb2_grpc import NetworkServiceStub
from yandex.cloud.vpc.v1.subnet_service_pb2 import ListSubnetsRequest
from yandex.cloud.vpc.v1.subnet_service_pb2_grpc import SubnetServiceStub
from yandex.cloud.iam.v1.service_account_service_pb2 import ListServiceAccountsRequest
from yandex.cloud.iam.v1.service_account_service_pb2_grpc import ServiceAccountServiceStub


import yandex.cloud.dataproc.v1.common_pb2 as common_pb

import yandex.cloud.dataproc.v1.cluster_pb2 as cluster_pb
import yandex.cloud.dataproc.v1.cluster_service_pb2 as cluster_service_pb
import yandex.cloud.dataproc.v1.cluster_service_pb2_grpc as cluster_service_grpc_pb

import yandex.cloud.dataproc.v1.subcluster_pb2 as subcluster_pb
import yandex.cloud.dataproc.v1.subcluster_service_pb2 as subcluster_service_pb
import yandex.cloud.dataproc.v1.subcluster_service_pb2_grpc as subcluster_service_grpc_pb

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

    resources = common_pb.Resources(
        resource_preset_id="s2.small",
        disk_size=15 * (1024 ** 3),
        disk_type_id="network-ssd",
    )
    req = create_cluster_request(flags, resources=resources)
    cluster = None
    try:
        cluster = create_cluster(sdk, req)
        change_cluster_description(sdk, cluster)
        add_subcluster(sdk, cluster, flags, resources=resources)
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
    parser.add_argument(
        '--ssh-public-key',
        default='ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII7JOBFU5LGCd/ET220neX7MiWIXHnZI9ZfFjjgnPMmh'
    )
    parser.add_argument('--service-account-id', default='')
    parser.add_argument('--s3-bucket', default='')

    return parser.parse_args()


def fill_missing_flags(sdk, flags):
    if os.path.exists(flags.ssh_public_key):
        with open(flags.ssh_public_key) as infile:
            flags.ssh_public_key = infile.read().strip()

    if not flags.network_id:
        flags.network_id = find_network(sdk, flags.folder_id)

    if not flags.subnet_id:
        flags.subnet_id = find_subnet(sdk, folder_id=flags.folder_id, zone_id=flags.zone, network_id=flags.network_id)

    if not flags.service_account_id:
        flags.service_account_id = find_service_account_id(sdk, folder_id=flags.folder_id)


def find_service_account_id(sdk, folder_id):
    service = sdk.client(ServiceAccountServiceStub)
    service_accounts = service.List(ListServiceAccountsRequest(folder_id=folder_id)).service_accounts
    if len(service_accounts) == 1:
        return service_accounts[0].id
    if len(service_accounts) == 0:
        message = 'There are no service accounts in folder {}, please create it.'
        raise RuntimeError(message.format(folder_id))
    message = 'There are more than one service account in folder {}, please specify it'
    raise RuntimeError(message.format(folder_id))


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
    operation = sdk.client(cluster_service_grpc_pb.ClusterServiceStub).Create(req)

    meta = cluster_service_pb.CreateClusterMetadata()
    operation.metadata.Unpack(meta)

    print("Creating cluster {}".format(meta.cluster_id))
    operation = wait_for_operation(sdk, operation)

    cluster = cluster_pb.Cluster()
    operation.response.Unpack(cluster)
    if not cluster:
        raise RuntimeError('Cluster was not created')
    return cluster


def add_subcluster(sdk, cluster, params, resources):
    print("Adding subcluster to cluster {}".format(cluster.id))
    req = subcluster_service_pb.CreateSubclusterRequest(
        cluster_id=cluster.id,
        name='compute',
        role=subcluster_pb.Role.COMPUTENODE,
        resources=resources,
        subnet_id=params.subnet_id,
        hosts_count=1,
    )

    operation = sdk.client(subcluster_service_grpc_pb.SubclusterServiceStub).Create(req)
    wait_for_operation(sdk, operation)


def change_cluster_description(sdk, cluster):
    print("Updating cluster {}".format(cluster.id))
    mask = FieldMask(paths=["description"])
    update_req = cluster_service_pb.UpdateClusterRequest(cluster_id=cluster.id, update_mask=mask,
                                                         description="New Description!!!")

    operation = sdk.client(cluster_service_grpc_pb.ClusterServiceStub).Update(update_req)
    wait_for_operation(sdk, operation)


def delete_cluster(sdk, cluster):
    print("Deleting cluster {}".format(cluster.id))
    operation = sdk.client(cluster_service_grpc_pb.ClusterServiceStub).Delete(
        cluster_service_pb.DeleteClusterRequest(cluster_id=cluster.id))
    wait_for_operation(sdk, operation)


def create_cluster_request(params, resources):
    return cluster_service_pb.CreateClusterRequest(
        folder_id=params.folder_id,
        name=params.cluster_name,
        description=params.cluster_desc,
        config_spec=cluster_service_pb.CreateClusterConfigSpec(
            version_id='1.0',
            hadoop=cluster_pb.HadoopConfig(
                services=[
                    cluster_pb.HadoopConfig.Service.HDFS,
                    cluster_pb.HadoopConfig.Service.YARN,
                    cluster_pb.HadoopConfig.Service.MAPREDUCE,
                    cluster_pb.HadoopConfig.Service.HIVE,
                    cluster_pb.HadoopConfig.Service.TEZ,
                    cluster_pb.HadoopConfig.Service.ZOOKEEPER,
                    cluster_pb.HadoopConfig.Service.HBASE,
                    cluster_pb.HadoopConfig.Service.SQOOP,
                    cluster_pb.HadoopConfig.Service.FLUME,
                    cluster_pb.HadoopConfig.Service.SPARK,
                    cluster_pb.HadoopConfig.Service.ZEPPELIN,
                    cluster_pb.HadoopConfig.Service.OOZIE,
                ],
                ssh_public_keys=[params.ssh_public_key],
            ),
            subclusters_spec=[
                cluster_service_pb.CreateSubclusterConfigSpec(
                    name='master',
                    role=subcluster_pb.Role.MASTERNODE,
                    resources=resources,
                    subnet_id=params.subnet_id,
                    hosts_count=1,
                ),
                cluster_service_pb.CreateSubclusterConfigSpec(
                    name='data',
                    role=subcluster_pb.Role.DATANODE,
                    resources=resources,
                    subnet_id=params.subnet_id,
                    hosts_count=1,
                ),
            ],
        ),
        zone_id=params.zone,
        service_account_id=params.service_account_id,
        bucket=params.s3_bucket,
    )


if __name__ == '__main__':
    main()
