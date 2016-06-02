__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.vlanstack_pb2 import VlanStack, vlanStack

from base.protocol_base import ProtocolBase


class VLANStack(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kVlanStackFieldNumber

    def _protocol_type(self):
        return vlanStack

    def _protocol_class(self):
        return VlanStack

    def _protocol_fields_map(self):
        fields_map = dict(is_override_tpid=self.field_map('is_override_tpid'),
                          tpid=self.field_map('tpid'),
                          vlan_tag=self.field_map('vlan_tag'),
                          )
        return fields_map

