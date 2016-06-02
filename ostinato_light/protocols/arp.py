__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols import arp_pb2

from base.protocol_base import ProtocolBase
from base.consts import Enum
from base.utils import *


class ARP(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kArpFieldNumber

    def _protocol_type(self):
        return arp_pb2.arp

    def _protocol_class(self):
        return arp_pb2.Arp

    def _protocol_fields_map(self):

        fields_map = dict(hw_type=self.field_map('hw_type'),
                          proto_type=self.field_map('proto_type'),
                          hw_addr_len=self.field_map('hw_addr_len'),
                          proto_addr_len=self.field_map('proto_addr_len'),
                          op_code=self.field_map('op_code'),
                          sender_hw_addr=self.field_map('sender_hw_addr',
                                                        Utils.macStrToInt),
                          sender_hw_addr_mode=self.field_map('sender_hw_addr_mode',
                                                             Enum.ARP_HARDWARE_ADDRESS_MODE_FIEXD,
                                                             Enum.ARP_HARDWARE_ADDRESS_MODE_INCREMENT,
                                                             Enum.ARP_HARDWARE_ADDRESS_MODE_DECREMENT),
                          sender_hw_addr_count=self.field_map('sender_hw_addr_count'),
                          sender_proto_addr=self.field_map('sender_proto_addr',
                                                           Utils.ip4StrToInt),
                          sender_proto_addr_mode=self.field_map('sender_proto_addr_mode',
                                                                Enum.ARP_PROTOCOL_ADDRESS_MODE_FIEXD_HOST,
                                                                Enum.ARP_PROTOCOL_ADDRESS_MODE_INCREMENT_HOST,
                                                                Enum.ARP_PROTOCOL_ADDRESS_MODE_DECREMENT_HOST,
                                                                Enum.ARP_PROTOCOL_ADDRESS_MODE_RANDOM_HOST),
                          sender_proto_addr_count=self.field_map('sender_proto_addr_count'),
                          sender_proto_addr_mask=self.field_map('sender_proto_addr_mask'),
                          target_hw_addr=self.field_map('target_hw_addr',
                                                        Utils.macStrToInt),
                          target_hw_addr_mode=self.field_map('target_hw_addr_mode',
                                                             Enum.ARP_HARDWARE_ADDRESS_MODE_FIEXD,
                                                             Enum.ARP_HARDWARE_ADDRESS_MODE_INCREMENT,
                                                             Enum.ARP_HARDWARE_ADDRESS_MODE_DECREMENT),
                          target_hw_addr_count=self.field_map('target_hw_addr_count'),
                          target_proto_addr=self.field_map('target_proto_addr',
                                                           Utils.ip4StrToInt),
                          target_proto_addr_mode=self.field_map('target_proto_addr_mode',
                                                                Enum.ARP_PROTOCOL_ADDRESS_MODE_FIEXD_HOST,
                                                                Enum.ARP_PROTOCOL_ADDRESS_MODE_INCREMENT_HOST,
                                                                Enum.ARP_PROTOCOL_ADDRESS_MODE_DECREMENT_HOST,
                                                                Enum.ARP_PROTOCOL_ADDRESS_MODE_RANDOM_HOST),
                          target_proto_addr_count=self.field_map('target_proto_addr_count'),
                          target_proto_addr_mask=self.field_map('target_proto_addr_mask'),
                          )

        return fields_map

