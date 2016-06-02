__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.udp_pb2 import Udp, udp

from base.protocol_base import ProtocolBase


class UDP(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kUdpFieldNumber

    def _protocol_type(self):
        return udp

    def _protocol_class(self):
        return Udp

    def _protocol_fields_map(self):
        fields_map = dict(is_override_src_port=self.field_map('is_override_src_port'),
                          is_override_dst_port=self.field_map('is_override_dst_port'),
                          is_override_totlen=self.field_map('is_override_totlen'),
                          is_override_cksum=self.field_map('is_override_cksum'),
                          src_port=self.field_map('src_port'),
                          dst_port=self.field_map('dst_port'),
                          totlen=self.field_map('totlen'),
                          cksum=self.field_map('cksum'),
                          )
        return fields_map

