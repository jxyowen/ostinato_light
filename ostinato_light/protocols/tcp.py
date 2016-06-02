__author__ = 'jxy'

from ostinato.core import ost_pb
from ostinato.protocols.tcp_pb2 import Tcp, tcp

from base.protocol_base import ProtocolBase


class TCP(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kTcpFieldNumber

    def _protocol_type(self):
        return tcp

    def _protocol_class(self):
        return Tcp

    def _protocol_fields_map(self):
        fields_map = dict(is_override_src_port=self.field_map('is_override_src_port'),
                          is_override_dst_port=self.field_map('is_override_dst_port'),
                          is_override_hdrlen=self.field_map('is_override_hdrlen'),
                          is_override_cksum=self.field_map('is_override_cksum'),
                          src_port=self.field_map('src_port'),
                          dst_port=self.field_map('dst_port'),
                          seq_num=self.field_map('seq_num'),
                          ack_num=self.field_map('ack_num'),
                          hdrlen_rsvd=self.field_map('hdrlen_rsvd'),
                          flags=self.field_map('flags'),
                          window=self.field_map('window'),
                          cksum=self.field_map('cksum'),
                          urg_ptr=self.field_map('urg_ptr'),
                          )
        return fields_map

    def _protocol_fields_with_related_fields(self):
        related_field = dict(src_port=dict(is_override_src_port=True),
                             dst_port=dict(is_override_dst_port=True))
        return related_field

