#!/usr/bin/env python3

import argparse
import logging
import time
from uuid import uuid4

import grpc
import yandexcloud
from yandex.cloud.marketplace.v1.metering.image_product_usage_service_pb2 import WriteImageProductUsageRequest
from yandex.cloud.marketplace.v1.metering.image_product_usage_service_pb2_grpc import ImageProductUsageServiceStub
from yandex.cloud.marketplace.v1.metering.usage_record_pb2 import UsageRecord


def build_product_usage_write_request(product_id, sku_id, quantity, timestamp=None, uuid=None):
    """Builds an image product usage write request."""

    usage_record = UsageRecord()

    # NOTE: Behaves like idempotency key. Should be unique to prevent duplicates.
    usage_record.uuid = str(uuid4()) if uuid is None else str(uuid)
    usage_record.sku_id = sku_id
    usage_record.quantity = int(quantity)

    # NOTE: UTC timezone
    usage_record.timestamp.seconds = int(time.time()) if timestamp is None else int(timestamp)

    request = WriteImageProductUsageRequest()

    request.product_id = product_id
    request.usage_records.extend([usage_record])

    return request


def business_logic(product_id, sku_id):
    """Example of service."""

    if product_id == 'Secure Firewall' and sku_id == 'Ingress network traffic':
        return 1 + 1

    if product_id == 'Secure Firewall' and sku_id == 'Egress network traffic':
        return 1 * 1

    return 0


def main(product_id, sku_id, quantity, timestamp=None, uuid=None):
    # NOTE: IAM token will be taken automatically from metadata agent of VM

    interceptor = yandexcloud.RetryInterceptor(max_retry_count=5, retriable_codes=[grpc.StatusCode.UNAVAILABLE])
    sdk = yandexcloud.SDK(interceptor=interceptor)
    service = sdk.client(ImageProductUsageServiceStub)
    request = build_product_usage_write_request(product_id, sku_id, quantity, timestamp, uuid)

    # Step 0. Ensure consumer has all permissions to use the product (validate_only=True)

    request.validate_only = True
    response = service.Write(request)

    if len(response.accepted) == 0:
        raise ValueError('Unable to provide the service to customer. Reason: %s' % str(response.rejected))

    # Step 1. Provide your service to the customer

    business_logic(product_id, sku_id)

    # Step 2. Write the product usage to Yandex.Cloud API (validate_only=False)

    request.validate_only = False
    response = service.Write(request)

    if len(response.accepted) == 0:
        raise ValueError('Unable to write the product usage. Reason: %s' % str(response.rejected))

    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--product-id', help='Marketplace image product ID', required=True)
    parser.add_argument('--sku-id', help='Marketplace image product SKU', required=True)
    parser.add_argument('--quantity', help='Usage quantity', required=True)
    parser.add_argument('--timestamp', help='Usage time', required=False)
    parser.add_argument('--uuid', help='Usage request unique identifier', required=False)

    args = parser.parse_args()

    print(main(
        args.product_id,
        args.sku_id,
        args.quantity,
        args.timestamp,
        args.uuid,
    ))
