__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols import hexdump_pb2

from base.protocol_base import ProtocolBase


class HexDump(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kHexDumpFieldNumber

    def _protocol_type(self):
        return hexdump_pb2.hexDump

    def _protocol_class(self):
        return hexdump_pb2.HexDump

    def _protocol_fields_map(self):

        fields_map = dict(content=self.field_map('content'),
                          pad_until_end=self.field_map('pad_until_end'),
                        )

        return fields_map
