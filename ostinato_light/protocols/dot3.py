__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.dot3_pb2 import Dot3, dot3

from base.protocol_base import ProtocolBase


class DOT3(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kDot3FieldNumber

    def _protocol_type(self):
        return dot3

    def _protocol_class(self):
        return Dot3

    def _protocol_fields_map(self):

        fields_map = dict(is_override_length=self.field_map('is_override_length'),
                          length=self.field_map('length'),
                         )

        return fields_map
