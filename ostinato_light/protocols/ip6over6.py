__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.ip6over6_pb2  import Ip6over6, ip6over6

from base.protocol_base import ProtocolBase


class IP6OVER6(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kIp6over6FieldNumber

    def _protocol_type(self):
        return ip6over6

    def _protocol_class(self):
        return Ip6over6

    def _protocol_fields_map(self):

        fields_map = dict(
                         )

        return fields_map
