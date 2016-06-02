__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.ip4over6_pb2  import Ip4over6, ip4over6

from base.protocol_base import ProtocolBase


class IP4OVER6(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kIp4over6FieldNumber

    def _protocol_type(self):
        return ip4over6

    def _protocol_class(self):
        return Ip4over6

    def _protocol_fields_map(self):

        fields_map = dict(
                         )

        return fields_map
