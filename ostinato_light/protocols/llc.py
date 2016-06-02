__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.llc_pb2 import Llc, llc

from base.protocol_base import ProtocolBase


class LLC(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kLlcFieldNumber

    def _protocol_type(self):
        return llc

    def _protocol_class(self):
        return Llc

    def _protocol_fields_map(self):

        fields_map = dict(is_override_dsap=self.field_map('is_override_dsap'),
                          is_override_ssap=self.field_map('is_override_ssap'),
                          is_override_ctl=self.field_map('is_override_ctl'),
                          dsap=self.field_map('dsap'),
                          ssap=self.field_map('ssap'),
                          ctl=self.field_map('ctl'),
                         )

        return fields_map
