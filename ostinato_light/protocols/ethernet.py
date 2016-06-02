__author__ = 'jxy'

from ostinato.core import ost_pb
from ostinato.protocols.eth2_pb2 import Eth2, eth2

from base.protocol_base import ProtocolBase


class Ethernet(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kEth2FieldNumber

    def _protocol_type(self):
        return eth2

    def _protocol_class(self):
        return Eth2

    def _protocol_fields_map(self):
        fields_map = dict(is_override_type=self.field_map('is_override_type'),
                          type=self.field_map('type'),
                          )
        return fields_map
