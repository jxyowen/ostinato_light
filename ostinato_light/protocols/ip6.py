__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.ip6_pb2 import Ip6, ip6

from base.protocol_base import ProtocolBase


class IP6(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kIp6FieldNumber

    def _protocol_type(self):
        return ip6

    def _protocol_class(self):
        return Ip6

    def _protocol_fields_map(self):

        fields_map = dict(is_override_version=self.field_map('is_override_version'),
                          is_override_payload_length=self.field_map('is_override_payload_length'),
                          is_override_next_header=self.field_map('is_override_next_header'),
                          version=self.field_map('version'),
                          traffic_class=self.field_map('traffic_class'),
                          flow_label=self.field_map('flow_label'),
                          payload_length=self.field_map('payload_length'),
                          next_header=self.field_map('next_header'),
                          hop_limit=self.field_map('hop_limit'),
                          src_addr_hi=self.field_map('src_addr_hi'),
                          src_addr_lo=self.field_map('src_addr_lo'),
                          src_addr_mode=self.field_map('src_addr_mode'),
                          src_addr_count=self.field_map('src_addr_count'),
                          src_addr_prefix=self.field_map('src_addr_prefix'),
                          dst_addr_hi=self.field_map('dst_addr_hi'),
                          dst_addr_lo=self.field_map('dst_addr_lo'),
                          dst_addr_mode=self.field_map('dst_addr_mode'),
                          dst_addr_count=self.field_map('dst_addr_count'),
                          dst_addr_prefix=self.field_map('dst_addr_prefix'),
                        )

        return fields_map
