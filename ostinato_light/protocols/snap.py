__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.snap_pb2 import Snap, snap

from base.protocol_base import ProtocolBase


class SNAP(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kSnapFieldNumber

    def _protocol_type(self):
        return snap

    def _protocol_class(self):
        return Snap

    def _protocol_fields_map(self):

        fields_map = dict(is_override_oui=self.field_map('is_override_oui'),
                          is_override_type=self.field_map('is_override_type'),
                          oui=self.field_map('oui'),
                          type=self.field_map('type'),
                          )

        return fields_map
