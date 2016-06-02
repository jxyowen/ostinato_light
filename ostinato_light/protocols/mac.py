__author__ = 'jxy'

from ostinato.core import ost_pb
from ostinato.protocols.mac_pb2 import Mac, mac

from base.protocol_base import ProtocolBase
from base.consts import Enum
from base.utils import *


class MAC(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kMacFieldNumber

    def _protocol_type(self):
        return mac

    def _protocol_class(self):
        return Mac

    def _protocol_fields_map(self):

        fields_map = dict(src_mac=self.field_map('src_mac',
                                                 Utils.macStrToInt),
                          src_mac_count=self.field_map('src_mac_count'),
                          src_mac_step=self.field_map('src_mac_step'),
                          src_mac_mode=self.field_map('src_mac_mode',
                                                      Enum.MAC_ADDRESS_MODE_FIEXD,
                                                      Enum.MAC_ADDRESS_MODE_INCREMENT,
                                                      Enum.MAC_ADDRESS_MODE_DECREMENT),

                          dst_mac=self.field_map('dst_mac',
                                                 Utils.macStrToInt),
                          dst_mac_count=self.field_map('dst_mac_count'),
                          dst_mac_step=self.field_map('dst_mac_step'),
                          dst_mac_mode=self.field_map('dst_mac_mode',
                                                      Enum.MAC_ADDRESS_MODE_FIEXD,
                                                      Enum.MAC_ADDRESS_MODE_INCREMENT,
                                                      Enum.MAC_ADDRESS_MODE_DECREMENT),
                          )

        return fields_map


