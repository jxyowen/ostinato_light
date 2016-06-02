__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.dot2llc_pb2 import Dot2Llc, dot2Llc

from base.protocol_base import ProtocolBase


class DOT2LLC(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kDot2llcFieldNumber

    def _protocol_type(self):
        return dot2Llc

    def _protocol_class(self):
        return Dot2Llc

    def _protocol_fields_map(self):

        fields_map = dict(
                         )

        return fields_map
