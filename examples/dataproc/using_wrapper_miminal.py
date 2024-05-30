#!/usr/bin/env python3
import argparse
import json
import logging
import os

import yandexcloud
from yandexcloud.operations import OperationError

USER_AGENT = "ycloud-python-sdk:dataproc.example.using_wrapper_minimal"


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
    services = ("YARN", "SPARK")
    try:
        dataproc.create_cluster(
            masternode_resource_preset="s2.micro",
            subnet_id=arguments.subnet_id,
            s3_bucket=arguments.s3_bucket,
            service_account_id=arguments.service_account_id,
            zone=arguments.zone,
            services=services,
            # Compute subcluster parameters
            computenode_count=1,
            computenode_resource_preset="s2.micro",
            computenode_preemptible=True,
        )

        dataproc.create_spark_job(
            name="Spark job: Estimate Pi number",
            main_jar_file_uri="file:///usr/lib/spark/examples/jars/spark-examples.jar",
            main_class="org.apache.spark.examples.SparkPi",
            args=["1000"],
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
    parser.add_argument(
        "--ssh-public-key", default="ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAII7JOBFU5LGCd/ET220neX7MiWIXHnZI9ZfFjjgnPMmh"
    )
    parser.add_argument("--service-account-id", default="")
    parser.add_argument("--s3-bucket", required=True)
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
