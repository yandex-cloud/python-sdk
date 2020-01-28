# -*- coding: utf-8 -*-

from yandex.cloud.iam.v1.service_account_service_pb2 import ListServiceAccountsRequest
from yandex.cloud.iam.v1.service_account_service_pb2_grpc import ServiceAccountServiceStub
from yandex.cloud.vpc.v1.network_service_pb2 import ListNetworksRequest
from yandex.cloud.vpc.v1.network_service_pb2_grpc import NetworkServiceStub
from yandex.cloud.vpc.v1.subnet_service_pb2 import ListSubnetsRequest
from yandex.cloud.vpc.v1.subnet_service_pb2_grpc import SubnetServiceStub


class Helpers(object):
    def __init__(self, sdk):
        self.sdk = sdk
        self.client = sdk.client

    def find_service_account_id(self, folder_id):
        """
        Get service account id in case the folder has the only one service account

        :param folder_id: ID of the folder
        :type operation: str
        :return ID of the service account
        :rtype str
        """
        service = self.client(ServiceAccountServiceStub)
        service_accounts = service.List(ListServiceAccountsRequest(folder_id=folder_id)).service_accounts
        if len(service_accounts) == 1:
            return service_accounts[0].id
        if len(service_accounts) == 0:
            raise RuntimeError(
                'There are no service accounts in folder {folder_id}, please create it.'.format(folder_id=folder_id)
            )
        raise RuntimeError(
            'There are more than one service account in folder {folder_id}, please specify it'.format(folder_id=folder_id)
        )

    def find_network_id(self, folder_id):
        """
        Get ID of the first network in folder

        :param folder_id: ID of the folder
        :type operation: str
        :return ID of the network
        :rtype str
        """
        networks = self.client(NetworkServiceStub).List(ListNetworksRequest(folder_id=folder_id)).networks
        networks = [n for n in networks if n.folder_id == folder_id]

        if not networks:
            raise RuntimeError('No networks in folder: {folder_id}'.format(folder_id=folder_id))
        if len(networks) > 1:
            raise RuntimeError(
                'There are more than one network in folder {folder_id}, please specify it'.format(folder_id=folder_id)
            )
        return networks[0].id

    def find_subnet_id(self, folder_id, zone_id, network_id):
        """
        Get ID of the subnetwork of specified network in specified availability zone

        :param folder_id: ID of the folder
        :type operation: str
        :param zone_id: ID of the availability zone
        :type operation: str
        :param network_id: ID of the network
        :type operation: str
        :return ID of the subnetwork
        :rtype str
        """
        subnet_service = self.client(SubnetServiceStub)
        subnets = subnet_service.List(ListSubnetsRequest(
            folder_id=folder_id)).subnets
        applicable = [s for s in subnets if s.zone_id == zone_id and s.network_id == network_id]
        if len(applicable) == 1:
            return applicable[0].id
        if len(applicable) == 0:
            raise RuntimeError('There are no subnets in {zone_id} zone, please create it.'.format(zone_id=zone_id))
        raise RuntimeError(
            'There are more than one subnet in {zone_id} zone, please specify it'.format(zone_id=zone_id)
        )
