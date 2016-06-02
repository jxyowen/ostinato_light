__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.ip6over4_pb2  import Ip6over4, ip6over4

from base.protocol_base import ProtocolBase


class IP6OVER4(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kIp6over4FieldNumber

    def _protocol_type(self):
        return ip6over4

    def _protocol_class(self):
        return Ip6over4

    def _protocol_fields_map(self):

        fields_map = dict(
                         )

        return fields_map
