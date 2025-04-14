#!/usr/bin/env python3
import argparse
import grpc
import json
import logging
import os

import yandexcloud
from yandexcloud.operations import OperationError


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
    parser.add_argument("--service-account-id", type=str, default="")
    parser.add_argument("--subnet-id", type=str, action="extend", nargs="*", dest="subnet_ids")
    parser.add_argument("--security-group-id", type=str, action="extend", nargs="*", dest="security_group_ids")
    parser.add_argument(
        "--job-name",
        type=str, default="pi number",
    )
    parser.add_argument(
        "--job-script",
        type=str, default="local:///opt/bitnami/spark/examples/src/main/python/pi.py",
    )
    parser.add_argument(
        "--job-arg",
        type=str, action="extend", nargs="*", dest="job_args", default=["1000"],
    )
    return parser.parse_args()


def main():
    logging.basicConfig(level=logging.INFO)
    arguments = parse_cmd()

    if arguments.token:
        sdk = yandexcloud.SDK(token=arguments.token)
    else:
        with open(arguments.sa_json_path) as infile:
            sdk = yandexcloud.SDK(service_account_key=json.load(infile))

    spark_client = sdk.wrappers.Spark()

    cluster_spec = sdk.wrappers.SparkClusterParameters(
        folder_id=arguments.folder_id,
        description="created with python-sdk",
        service_account_id=arguments.service_account_id,
        subnet_ids=arguments.subnet_ids,
        security_group_ids=arguments.security_group_ids,
        driver_pool_resource_preset="c2-m8",
        driver_pool_size=1,
        executor_pool_resource_preset="c4-m16",
        executor_pool_min_size=1,
        executor_pool_max_size=2,
    )

    try:
        spark_client.create_cluster(cluster_spec)

        try:
            job_spec = sdk.wrappers.PysparkJobParameters(
                name=arguments.job_name,
                main_python_file_uri=arguments.job_script,
                args=arguments.job_args,
            )
            job_operation = spark_client.create_pyspark_job(job_spec)
            job_id = job_operation.response.id
            job_info = job_operation.response

        except OperationError as job_error:
            job_id = job_error.operation_result.meta.job_id
            job_info, _ = spark_client.get_job(job_id=job_id)
            raise

        finally:
            job_log = spark_client.get_job_log(job_id=job_id)
            for line in job_log:
                logging.info(line)

            logging.info("Job info: %s", job_info)

    except grpc.RpcError:
        logging.exception("GRPC Error:")
    except OperationError:
        logging.exception("Operation Error:")
    finally:
        if spark_client.cluster_id is not None:
            spark_client.delete_cluster()


if __name__ == "__main__":
    main()
