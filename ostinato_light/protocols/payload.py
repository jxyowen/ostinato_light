__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols import payload_pb2

from base.protocol_base import ProtocolBase
from base.consts import Enum


class Payload(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kPayloadFieldNumber

    def _protocol_type(self):
        return payload_pb2.payload

    def _protocol_class(self):
        return payload_pb2.Payload

    def _protocol_fields_map(self):

        fields_map = dict(pattern_mode=self.field_map('pattern_mode',
                                                      Enum.PAYLOAD_DATA_PATTERN_MODE_FIXED_WORD,
                                                      Enum.PAYLOAD_DATA_PATTERN_MODE_INCREMENT_BYTE,
                                                      Enum.PAYLOAD_DATA_PATTERN_MODE_DECREMENT_BYTE,
                                                      Enum.PAYLOAD_DATA_PATTERN_MODE_RANDOM),
                          pattern=self.field_map('pattern'),
                          )

        return fields_map
