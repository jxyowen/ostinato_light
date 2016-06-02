__author__ = 'jxy'

from ostinato.core import ost_pb
from ostinato.protocols.ip4_pb2 import Ip4, ip4

from base.protocol_base import ProtocolBase
from base.consts import Enum
from base.utils import *


class IP4(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kIp4FieldNumber

    def _protocol_type(self):
        return ip4

    def _protocol_class(self):
        return Ip4

    def _protocol_fields_map(self):
        fields_map = dict(src_ip=self.field_map('src_ip',
                                                Utils.ip4StrToInt),
                          src_ip_mask=self.field_map('src_ip_mask',
                                                     Utils.ip4StrToInt),
                          src_ip_count=self.field_map('src_ip_count'),
                          src_ip_mode=self.field_map('src_ip_mode',
                                                     Enum.IP4_ADDRESS_MODE_FIEXD,
                                                     Enum.IP4_ADDRESS_MODE_INCREMENT,
                                                     Enum.IP4_ADDRESS_MODE_DECREMENT,
                                                     Enum.IP4_ADDRESS_MODE_RANDOM),

                          dst_ip=self.field_map('dst_ip',
                                                Utils.ip4StrToInt),
                          dst_ip_mask=self.field_map('dst_ip_mask',
                                                     Utils.ip4StrToInt),
                          dst_ip_count=self.field_map('dst_ip_count'),
                          dst_ip_mode=self.field_map('dst_ip_mode',
                                                     Enum.IP4_ADDRESS_MODE_FIEXD,
                                                     Enum.IP4_ADDRESS_MODE_INCREMENT,
                                                     Enum.IP4_ADDRESS_MODE_DECREMENT,
                                                     Enum.IP4_ADDRESS_MODE_RANDOM),

                          is_override_ver=self.field_map('is_override_ver'),
                          is_override_hdrlen=self.field_map('is_override_hdrlen'),
                          is_override_totlen=self.field_map('is_override_totlen'),
                          is_override_proto=self.field_map('is_override_proto'),
                          is_override_cksum=self.field_map('is_override_cksum'),
                          ver_hdrlen=self.field_map('ver_hdrlen'),
                          tos=self.field_map('tos'),
                          id=self.field_map('id'),
                          flags=self.field_map('flags'),
                          frag_ofs=self.field_map('frag_ofs'),
                          ttl=self.field_map('ttl'),
                          proto=self.field_map('proto'),
                          totlen=self.field_map('totlen'),
                          cksum=self.field_map('cksum'),
                          )
        return fields_map



