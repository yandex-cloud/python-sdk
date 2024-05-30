#!/usr/bin/env python3
import argparse
import json
import logging
import os
import uuid

import yandexcloud
from yandexcloud.operations import OperationError

USER_AGENT = "ycloud-python-sdk:dataproc.example.using_wrapper"


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_cmd()
    if arguments.token:
        sdk = yandexcloud.SDK(token=arguments.token, user_agent=USER_AGENT)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = yandexcloud.SDK(service_account_key=json.load(infile), user_agent=USER_AGENT)
    fill_missing_arguments(sdk, arguments)

    dataproc = sdk.wrappers.Dataproc(
        default_folder_id=arguments.folder_id,
        default_public_ssh_key=arguments.ssh_public_key,
    )
    bucket_for_logs_output = arguments.s3_bucket
    services = (
        "HDFS",
        "YARN",
        "MAPREDUCE",
        "HIVE",
        "SPARK",
    )
    init_actions = None
    if arguments.init_action_url:
        init_actions = [
            sdk.wrappers.InitializationAction(
                uri=arguments.init_action_url,
                args=["arg1", "arg2", "arg3"],
                timeout=60,
            )
        ]
    try:
        dataproc.create_cluster(
            cluster_name=arguments.cluster_name,
            cluster_description=arguments.cluster_desc,
            masternode_resource_preset="s2.micro",
            datanode_count=2,
            datanode_resource_preset="s2.micro",
            subnet_id=arguments.subnet_id,
            service_account_id=arguments.service_account_id,
            zone=arguments.zone,
            services=services,
            log_group_id=arguments.log_group_id,
            initialization_actions=init_actions,
        )

        dataproc.update_cluster_description("New cluster description")

        dataproc.create_subcluster(
            subcluster_type="compute",
            name="compute",
            hosts_count=1,
            resource_preset="s2.micro",
            max_hosts_count=2,
            cpu_utilization_target=66,
            preemptible=True,
        )

        dataproc.create_mapreduce_job(
            main_class="org.apache.hadoop.streaming.HadoopStreaming",
            file_uris=[
                "s3a://data-proc-public/jobs/sources/mapreduce-001/mapper.py",
                "s3a://data-proc-public/jobs/sources/mapreduce-001/reducer.py",
            ],
            args=[
                "-mapper",
                "mapper.py",
                "-reducer",
                "reducer.py",
                "-numReduceTasks",
                "1",
                "-input",
                "s3a://data-proc-public/jobs/sources/data/cities500.txt.bz2",
                "-output",
                "s3a://{bucket}/dataproc/job/results/{uuid}".format(bucket=bucket_for_logs_output, uuid=uuid.uuid4()),
            ],
            properties={
                "yarn.app.mapreduce.am.resource.mb": "2048",
                "yarn.app.mapreduce.am.command-opts": "-Xmx2048m",
                "mapreduce.job.maps": "6",
            },
        )

        dataproc.create_hive_job(
            query_file_uri="s3a://data-proc-public/jobs/sources/hive-001/main.sql",
            script_variables={
                "CITIES_URI": "s3a://data-proc-public/jobs/sources/hive-001/cities/",
                "COUNTRY_CODE": "RU",
            },
        )

        dataproc.create_spark_job(
            name="Spark job: Find total urban population in distribution by country",
            main_jar_file_uri="s3a://data-proc-public/jobs/sources/java/dataproc-examples-1.0.jar",
            main_class="ru.yandex.cloud.dataproc.examples.PopulationSparkJob",
            file_uris=[
                "s3a://data-proc-public/jobs/sources/data/config.json",
            ],
            archive_uris=[
                "s3a://data-proc-public/jobs/sources/data/country-codes.csv.zip",
            ],
            jar_file_uris=[
                "s3a://data-proc-public/jobs/sources/java/icu4j-61.1.jar",
                "s3a://data-proc-public/jobs/sources/java/commons-lang-2.6.jar",
                "s3a://data-proc-public/jobs/sources/java/opencsv-4.1.jar",
                "s3a://data-proc-public/jobs/sources/java/json-20190722.jar",
            ],
            args=[
                "s3a://data-proc-public/jobs/sources/data/cities500.txt.bz2",
                "s3a://{bucket}/dataproc/job/results/${{JOB_ID}}".format(bucket=bucket_for_logs_output),
            ],
            properties={
                "spark.submit.deployMode": "cluster",
            },
            packages=["org.slf4j:slf4j-simple:1.7.30"],
            repositories=["https://repo1.maven.org/maven2"],
            exclude_packages=["com.amazonaws:amazon-kinesis-client"],
        )

        dataproc.create_pyspark_job(
            main_python_file_uri="s3a://data-proc-public/jobs/sources/pyspark-001/main.py",
            python_file_uris=[
                "s3a://data-proc-public/jobs/sources/pyspark-001/geonames.py",
            ],
            file_uris=[
                "s3a://data-proc-public/jobs/sources/data/config.json",
            ],
            archive_uris=[
                "s3a://data-proc-public/jobs/sources/data/country-codes.csv.zip",
            ],
            args=[
                "s3a://data-proc-public/jobs/sources/data/cities500.txt.bz2",
                "s3a://{bucket}/jobs/results/${{JOB_ID}}".format(bucket=bucket_for_logs_output),
            ],
            jar_file_uris=[
                "s3a://data-proc-public/jobs/sources/java/dataproc-examples-1.0.jar",
                "s3a://data-proc-public/jobs/sources/java/icu4j-61.1.jar",
                "s3a://data-proc-public/jobs/sources/java/commons-lang-2.6.jar",
            ],
            properties={
                "spark.submit.deployMode": "cluster",
            },
            packages=["org.slf4j:slf4j-simple:1.7.30"],
            repositories=["https://repo1.maven.org/maven2"],
            exclude_packages=["com.amazonaws:amazon-kinesis-client"],
        )

    except OperationError:
        logging.exception("Operation error:")

    finally:
        if dataproc.cluster_id is not None:
            dataproc.delete_cluster()


def parse_cmd():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)

    auth = parser.add_mutually_exclusive_group(required=True)
    auth.add_argument(
        "--sa-json-path",
        help="Path to the service account key JSON file.\nThis file can be created using YC CLI:\n"
        "yc iam key create --output sa.json --service-account-id <id>",
    )
    auth.add_argument("--token", help="OAuth token")
    parser.add_argument("--folder-id", help="Your Yandex.Cloud folder id", required=True)
    parser.add_argument("--zone", default="ru-central1-b", help="Compute Engine zone to deploy to")
    parser.add_argument("--network-id", default="", help="Your Yandex.Cloud network id")
    parser.add_argument("--subnet-id", default="", help="Subnet for the cluster")
    parser.add_argument("--cluster-name", default="cluster1", help="New cluster name")
    parser.add_argument("--cluster-desc", default="", help="New cluster description")
    parser.add_argument(
        "--ssh-public-key", default="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII7JOBFU5LGCd/ET220neX7MiWIXHnZI9ZfFjjgnPMmh"
    )
    parser.add_argument("--service-account-id", default="")
    parser.add_argument("--log-group-id", default=None)
    parser.add_argument("--s3-bucket", required=True)
    parser.add_argument("--init-action-url", default=None)
    return parser.parse_args()


def fill_missing_arguments(sdk, arguments):
    if os.path.exists(os.path.expanduser(arguments.ssh_public_key)):
        with open(arguments.ssh_public_key) as infile:
            arguments.ssh_public_key = infile.read().strip()

    if not arguments.network_id:
        arguments.network_id = sdk.helpers.find_network_id(folder_id=arguments.folder_id)

    if not arguments.subnet_id:
        arguments.subnet_id = sdk.helpers.find_subnet_id(
            folder_id=arguments.folder_id, zone_id=arguments.zone, network_id=arguments.network_id
        )

    if not arguments.service_account_id:
        arguments.service_account_id = sdk.helpers.find_service_account_id(folder_id=arguments.folder_id)


if __name__ == "__main__":
    main()
