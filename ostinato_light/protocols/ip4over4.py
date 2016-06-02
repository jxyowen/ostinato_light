__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.ip4over4_pb2 import Ip4over4, ip4over4

from base.protocol_base import ProtocolBase


class IP4OVER4(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kIp4over4FieldNumber

    def _protocol_type(self):
        return ip4over4

    def _protocol_class(self):
        return Ip4over4

    def _protocol_fields_map(self):

        fields_map = dict(
                         )

        return fields_map
