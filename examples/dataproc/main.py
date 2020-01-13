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
import yandex.cloud.dataproc.v1.job_pb2 as job_pb
import yandex.cloud.dataproc.v1.job_service_pb2 as job_service_pb
import yandex.cloud.dataproc.v1.job_service_pb2_grpc as job_service_grpc_pb
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
    arguments = parse_cmd()
    sdk = yandexcloud.SDK(token=arguments.token)

    fill_missing_flags(sdk, arguments)

    resources = common_pb.Resources(
        resource_preset_id='s2.micro',
        disk_size=15 * (1024 ** 3),
        disk_type_id='network-ssd',
    )
    req = create_cluster_request(arguments, resources=resources)
    cluster_id = None
    try:
        cluster = create_cluster(sdk, req)
        cluster_id = cluster.id
        change_cluster_description(sdk, cluster_id)
        add_subcluster(sdk, cluster_id, arguments, resources=resources)

        run_hive_job(sdk, cluster_id=cluster_id)
        run_mapreduce_job(sdk, cluster_id=cluster_id, bucket=arguments.s3_bucket)
        run_spark_job(sdk, cluster_id=cluster_id, bucket=arguments.s3_bucket)
        run_pyspark_job(sdk, cluster_id=cluster_id, bucket=arguments.s3_bucket)
    finally:
        if cluster_id is not None:
            delete_cluster(sdk, cluster_id)


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


def fill_missing_flags(sdk, arguments):
    if os.path.exists(os.path.expanduser(arguments.ssh_public_key)):
        with open(arguments.ssh_public_key) as infile:
            arguments.ssh_public_key = infile.read().strip()

    if not arguments.network_id:
        arguments.network_id = find_network(sdk, arguments.folder_id)

    if not arguments.subnet_id:
        arguments.subnet_id = find_subnet(
            sdk,
            folder_id=arguments.folder_id,
            zone_id=arguments.zone,
            network_id=arguments.network_id
        )

    if not arguments.service_account_id:
        arguments.service_account_id = find_service_account_id(sdk, folder_id=arguments.folder_id)


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
        raise RuntimeError('No networks in folder: {}'.format(folder_id))

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

    print('Creating cluster {}'.format(meta.cluster_id))
    operation = wait_for_operation(sdk, operation)

    cluster = cluster_pb.Cluster()
    operation.response.Unpack(cluster)
    if not cluster:
        raise RuntimeError('Cluster was not created')
    return cluster


def add_subcluster(sdk, cluster_id, params, resources):
    print('Adding subcluster to cluster {}'.format(cluster_id))
    req = subcluster_service_pb.CreateSubclusterRequest(
        cluster_id=cluster_id,
        name='compute',
        role=subcluster_pb.Role.COMPUTENODE,
        resources=resources,
        subnet_id=params.subnet_id,
        hosts_count=1,
    )

    operation = sdk.client(subcluster_service_grpc_pb.SubclusterServiceStub).Create(req)
    operation = wait_for_operation(sdk, operation)

    subcluster = subcluster_pb.Subcluster()
    operation.response.Unpack(subcluster)
    return subcluster


def change_cluster_description(sdk, cluster_id):
    print('Updating cluster {}'.format(cluster_id))
    mask = FieldMask(paths=['description'])
    update_req = cluster_service_pb.UpdateClusterRequest(cluster_id=cluster_id, update_mask=mask,
                                                         description='New cluster description')

    operation = sdk.client(cluster_service_grpc_pb.ClusterServiceStub).Update(update_req)
    wait_for_operation(sdk, operation)


def delete_cluster(sdk, cluster_id):
    print('Deleting cluster {}'.format(cluster_id))
    operation = sdk.client(cluster_service_grpc_pb.ClusterServiceStub).Delete(
        cluster_service_pb.DeleteClusterRequest(cluster_id=cluster_id))
    wait_for_operation(sdk, operation)


def run_hive_job(self, cluster_id):
    print('Running Hive job {}'.format(cluster_id))
    operation = self.client(job_service_grpc_pb.JobServiceStub).Create(
        job_service_pb.CreateJobRequest(
            cluster_id=cluster_id,
            name='Hive job 1',
            hive_job=job_pb.HiveJob(
                query_file_uri='s3a://data-proc-public/jobs/sources/hive-001/main.sql',
                script_variables={
                    'CITIES_URI': 's3a://data-proc-public/jobs/sources/hive-001/cities/',
                    'COUNTRY_CODE': 'RU',
                }
            )
        )
    )
    wait_for_operation(self, operation)
    return operation


def run_mapreduce_job(sdk, cluster_id, bucket):
    print('Running Mapreduce job {}'.format(cluster_id))
    operation = sdk.client(job_service_grpc_pb.JobServiceStub).Create(
        job_service_pb.CreateJobRequest(
            cluster_id=cluster_id,
            name='Mapreduce job 1',
            mapreduce_job=job_pb.MapreduceJob(
                main_class='org.apache.hadoop.streaming.HadoopStreaming',
                file_uris=[
                    's3a://data-proc-public/jobs/sources/mapreduce-001/mapper.py',
                    's3a://data-proc-public/jobs/sources/mapreduce-001/reducer.py'
                ],
                args=[
                    '-mapper', 'mapper.py',
                    '-reducer', 'reducer.py',
                    '-numReduceTasks', '1',
                    '-input', 's3a://data-proc-public/jobs/sources/data/cities500.txt.bz2',
                    '-output', 's3a://{bucket}/dataproc/job/results'.format(bucket=bucket)
                ],
                properties={
                    'yarn.app.mapreduce.am.resource.mb': '2048',
                    'yarn.app.mapreduce.am.command-opts': '-Xmx2048m',
                    'mapreduce.job.maps': '6',
                },
            )
        )
    )
    wait_for_operation(sdk, operation)
    return operation


def run_spark_job(sdk, cluster_id, bucket):
    print('Running Spark job {}'.format(cluster_id))
    operation = sdk.client(job_service_grpc_pb.JobServiceStub).Create(
        job_service_pb.CreateJobRequest(
            cluster_id=cluster_id,
            name='Spark job: Find total urban population in distribution by country',
            spark_job=job_pb.SparkJob(
                main_jar_file_uri='s3a://data-proc-public/jobs/sources/java/dataproc-examples-1.0.jar',
                main_class='ru.yandex.cloud.dataproc.examples.PopulationSparkJob',                
                file_uris=[
                    's3a://data-proc-public/jobs/sources/data/config.json',
                ],
                archive_uris=[
                    's3a://data-proc-public/jobs/sources/data/country-codes.csv.zip',
                ],
                jar_file_uris=[
                    's3a://data-proc-public/jobs/sources/java/icu4j-61.1.jar',
                    's3a://data-proc-public/jobs/sources/java/commons-lang-2.6.jar',
                    's3a://data-proc-public/jobs/sources/java/opencsv-4.1.jar',
                    's3a://data-proc-public/jobs/sources/java/json-20190722.jar'
                ],
                args=[
                    's3a://data-proc-public/jobs/sources/data/cities500.txt.bz2',
                    's3a://{bucket}/dataproc/job/results/${{JOB_ID}}'.format(bucket=bucket),
                ],
                properties={
                    'spark.submit.deployMode': 'cluster',
                },
            )
        )
    )
    wait_for_operation(sdk, operation)
    return operation


def run_pyspark_job(sdk, cluster_id, bucket):
    print('Running Pyspark job {}'.format(cluster_id))
    operation = sdk.client(job_service_grpc_pb.JobServiceStub).Create(
        job_service_pb.CreateJobRequest(
            cluster_id=cluster_id,
            name='Pyspark job',
            pyspark_job=job_pb.PysparkJob(
                main_python_file_uri='s3a://data-proc-public/jobs/sources/pyspark-001/main.py',
                python_file_uris=[
                    's3a://data-proc-public/jobs/sources/pyspark-001/geonames.py',
                ],
                file_uris=[
                    's3a://data-proc-public/jobs/sources/data/config.json',
                ],
                archive_uris=[
                    's3a://data-proc-public/jobs/sources/data/country-codes.csv.zip',
                ],
                args=[
                    's3a://data-proc-public/jobs/sources/data/cities500.txt.bz2',
                    's3a://{bucket}/jobs/results/${{JOB_ID}}'.format(bucket=bucket),
                ],
                jar_file_uris=[
                    's3a://data-proc-public/jobs/sources/java/dataproc-examples-1.0.jar',
                    's3a://data-proc-public/jobs/sources/java/icu4j-61.1.jar',
                    's3a://data-proc-public/jobs/sources/java/commons-lang-2.6.jar',
                ],
                properties={
                    'spark.submit.deployMode': 'cluster',
                },
            )
        )
    )
    wait_for_operation(sdk, operation)
    return operation


def create_cluster_request(params, resources):
    # Available services:
    #  HDFS
    #  YARN (depends on HDFS)
    #  MAPREDUCE
    #  HIVE (depends on HDFS, MAPREDUCE, YARN)
    #  TEZ (depends on HDFS, YARN)
    #  ZOOKEEPER
    #  HBASE (depends on HDFS, YARN, ZOOKEEPER)
    #  SQOOP
    #  FLUME
    #  SPARK (depends on HDFS, YARN)
    #  ZEPPELIN
    #  OOZIE
    services = [
        'HDFS',
        'YARN',
        'MAPREDUCE',
        'HIVE',
        'SPARK',
    ]

    return cluster_service_pb.CreateClusterRequest(
        folder_id=params.folder_id,
        name=params.cluster_name,
        description=params.cluster_desc,
        config_spec=cluster_service_pb.CreateClusterConfigSpec(
            version_id='1.1',
            hadoop=cluster_pb.HadoopConfig(
                services=services,
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
                    hosts_count=2,
                ),
            ],
        ),
        zone_id=params.zone,
        service_account_id=params.service_account_id,
        bucket=params.s3_bucket,
    )


if __name__ == '__main__':
    main()
