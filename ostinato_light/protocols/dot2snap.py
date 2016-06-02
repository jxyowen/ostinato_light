__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.dot2snap_pb2 import Dot2Snap, dot2Snap

from base.protocol_base import ProtocolBase


class DOT2SNAP(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kDot2snapFieldNumber

    def _protocol_type(self):
        return dot2Snap

    def _protocol_class(self):
        return Dot2Snap

    def _protocol_fields_map(self):

        fields_map = dict(
                         )

        return fields_map
