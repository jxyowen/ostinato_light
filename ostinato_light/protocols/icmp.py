__author__ = 'jxy'

from ostinato.core import ost_pb
from ostinato.protocols.icmp_pb2 import Icmp, icmp

from base.protocol_base import ProtocolBase
from base.consts import Enum


class ICMP(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kIcmpFieldNumber

    def _protocol_type(self):
        return icmp

    def _protocol_class(self):
        return Icmp

    def _protocol_fields_map(self):

        fields_map = dict(icmp_version=self.field_map('icmp_version',
                                                      Enum.ICMP_VERSION_4,
                                                      Enum.ICMP_VERSION_6),
                          is_override_checksum=self.field_map('is_override_checksum'),
                          type=self.field_map('type'),
                          code=self.field_map('code'),
                          checksum=self.field_map('checksum'),
                          identifier=self.field_map('identifier'),
                          sequence=self.field_map('sequence'),
                          )

        return fields_map
