#!/usr/bin/env python3
import argparse
import json
import os
import logging
import uuid

from google.protobuf.field_mask_pb2 import FieldMask

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


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_cmd()
    if arguments.token:
        sdk = yandexcloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = yandexcloud.SDK(service_account_key=json.load(infile))

    fill_missing_arguments(sdk, arguments)

    resources = common_pb.Resources(
        resource_preset_id='s2.micro',
        disk_type_id='network-ssd',
    )
    cluster_id = None
    try:
        operation_result = create_cluster(sdk, create_cluster_request(arguments, resources=resources))
        cluster_id = operation_result.response.id
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
    parser.add_argument('--cluster-name', default='cluster1', help='New cluster name')
    parser.add_argument('--cluster-desc', default='', help='New cluster description')
    parser.add_argument(
        '--ssh-public-key',
        default='ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII7JOBFU5LGCd/ET220neX7MiWIXHnZI9ZfFjjgnPMmh'
    )
    parser.add_argument('--service-account-id', default='')
    parser.add_argument('--log-group-id', default=None)
    parser.add_argument('--s3-bucket', required=True)
    return parser.parse_args()


def fill_missing_arguments(sdk, arguments):
    if os.path.exists(os.path.expanduser(arguments.ssh_public_key)):
        with open(arguments.ssh_public_key) as infile:
            arguments.ssh_public_key = infile.read().strip()

    if not arguments.network_id:
        arguments.network_id = sdk.helpers.find_network_id(folder_id=arguments.folder_id)

    if not arguments.subnet_id:
        arguments.subnet_id = sdk.helpers.find_subnet_id(
            folder_id=arguments.folder_id,
            zone_id=arguments.zone,
            network_id=arguments.network_id
        )

    if not arguments.service_account_id:
        arguments.service_account_id = sdk.helpers.find_service_account_id(folder_id=arguments.folder_id)


def create_cluster(sdk, request):
    operation = sdk.client(cluster_service_grpc_pb.ClusterServiceStub).Create(request)
    return sdk.wait_operation_and_get_result(
        operation,
        response_type=cluster_pb.Cluster,
        meta_type=cluster_service_pb.CreateClusterMetadata,
    )


def add_subcluster(sdk, cluster_id, params, resources):
    logging.info('Adding subcluster to cluster {}'.format(cluster_id))
    autoscaling_config = subcluster_pb.AutoscalingConfig(
        max_hosts_count=2,
        preemptible=True,
        cpu_utilization_target=66,
    )
    request = subcluster_service_pb.CreateSubclusterRequest(
        cluster_id=cluster_id,
        name='compute',
        role=subcluster_pb.Role.COMPUTENODE,
        resources=resources,
        subnet_id=params.subnet_id,
        hosts_count=1,
        autoscaling_config=autoscaling_config,
    )
    operation = sdk.client(subcluster_service_grpc_pb.SubclusterServiceStub).Create(request)
    return sdk.wait_operation_and_get_result(
        operation,
        response_type=subcluster_pb.Subcluster,
        meta_type=subcluster_service_pb.CreateSubclusterMetadata,
    )


def change_cluster_description(sdk, cluster_id):
    logging.info('Updating cluster {}'.format(cluster_id))
    mask = FieldMask(paths=['description'])
    request = cluster_service_pb.UpdateClusterRequest(
        cluster_id=cluster_id, update_mask=mask,
        description='New cluster description',
    )

    operation = sdk.client(cluster_service_grpc_pb.ClusterServiceStub).Update(request)
    return sdk.wait_operation_and_get_result(
        operation,
        response_type=cluster_pb.Cluster,
        meta_type=cluster_service_pb.UpdateClusterMetadata,
    )


def delete_cluster(sdk, cluster_id):
    logging.info('Deleting cluster {}'.format(cluster_id))
    operation = sdk.client(cluster_service_grpc_pb.ClusterServiceStub).Delete(
        cluster_service_pb.DeleteClusterRequest(cluster_id=cluster_id))
    return sdk.wait_operation_and_get_result(
        operation,
        meta_type=cluster_service_pb.DeleteClusterMetadata,
    )


def run_hive_job(sdk, cluster_id):
    logging.info('Running Hive job {}'.format(cluster_id))
    operation = sdk.client(job_service_grpc_pb.JobServiceStub).Create(
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
    return sdk.wait_operation_and_get_result(operation, response_type=job_pb.Job, meta_type=job_service_pb.CreateJobMetadata)


def run_mapreduce_job(sdk, cluster_id, bucket):
    logging.info('Running Mapreduce job {}'.format(cluster_id))
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
                    '-output', 's3a://{bucket}/dataproc/job/results/{uuid}'.format(bucket=bucket, uuid=uuid.uuid4())
                ],
                properties={
                    'yarn.app.mapreduce.am.resource.mb': '2048',
                    'yarn.app.mapreduce.am.command-opts': '-Xmx2048m',
                    'mapreduce.job.maps': '6',
                },
            )
        )
    )
    return sdk.wait_operation_and_get_result(operation, response_type=job_pb.Job, meta_type=job_service_pb.CreateJobMetadata)


def run_spark_job(sdk, cluster_id, bucket):
    logging.info('Running Spark job {}'.format(cluster_id))
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
    return sdk.wait_operation_and_get_result(operation, response_type=job_pb.Job, meta_type=job_service_pb.CreateJobMetadata)


def run_pyspark_job(sdk, cluster_id, bucket):
    logging.info('Running Pyspark job {}'.format(cluster_id))
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
    return sdk.wait_operation_and_get_result(operation, response_type=job_pb.Job, meta_type=job_service_pb.CreateJobMetadata)


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
    services = (
        'HDFS',
        'YARN',
        'MAPREDUCE',
        'HIVE',
        'SPARK',
    )

    return cluster_service_pb.CreateClusterRequest(
        folder_id=params.folder_id,
        name=params.cluster_name,
        description=params.cluster_desc,
        config_spec=cluster_service_pb.CreateClusterConfigSpec(
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
                    hosts_count=1,
                ),
            ],
        ),
        zone_id=params.zone,
        service_account_id=params.service_account_id,
        log_group_id=params.log_group_id,
        bucket=params.s3_bucket,
    )


if __name__ == '__main__':
    main()
