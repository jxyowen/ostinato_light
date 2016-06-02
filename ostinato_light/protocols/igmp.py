__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.igmp_pb2 import igmp
from ostinato.protocols.gmp_pb2 import Gmp

from base.protocol_base import ProtocolBase
from base.nseted_field_base import NestedFieldBase
from base.consts import Enum
from base.utils import *


class IGMP(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kIgmpFieldNumber

    def _protocol_type(self):
        return igmp

    def _protocol_class(self):
        return Gmp

    def _protocol_fields_map(self):

        fields_map = dict(type=self.field_map('type'),
                          is_override_rsvd_code=self.field_map('is_override_rsvd_code'),
                          rsvd_code=self.field_map('rsvd_code'),
                          max_response_time=self.field_map('max_response_time'),
                          is_override_checksum=self.field_map('is_override_checksum'),
                          checksum=self.field_map('checksum'),
                          group_address=self.field_map('group_address',
                                                       IGMPIPAddress),
                          group_mode=self.field_map('group_mode',
                                                    Enum.IGMP_GROUP_MODE_FIXED,
                                                    Enum.IGMP_GROUP_MODE_INCREMENT_GROUP,
                                                    Enum.IGMP_GROUP_MODE_DECREMENT_GROUP,
                                                    Enum.IGMP_GROUP_MODE_RANDOM_GROUP),
                          group_count=self.field_map('group_count'),
                          group_prefix=self.field_map('group_prefix'),
                          s_flag=self.field_map('s_flag'),
                          qrv=self.field_map('qrv'),
                          qqi=self.field_map('qqi'),
                          sources=self.field_map('sources',
                                                 IGMPIPAddress),
                          is_override_source_count=self.field_map('is_override_source_count'),
                          source_count=self.field_map('source_count'),
                          group_records=self.field_map('group_records',
                                                       IGMPGroupRecord),
                          is_override_group_record_count=self.field_map('is_override_group_record_count'),
                          group_record_count=self.field_map('group_record_count'),
                         )

        return fields_map


class IGMPIPAddress(NestedFieldBase):

    def _protocol_fields_map(self):

        fields_map = dict(v4=self.field_map('v4',
                                            Utils.ip4StrToInt),
                          v6_hi=self.field_map('v6_hi'),
                          v6_lo=self.field_map('v6_lo')
                          )

        return fields_map


class IGMPGroupRecord(NestedFieldBase):

    def _protocol_fields_map(self):

        fields_map = dict(type=self.field_map('type',
                                              Enum.IGMP_GROUP_RECORD_TYPE_RESERVED,
                                              Enum.IGMP_GROUP_RECORD_TYPE_IS_INCLUDE,
                                              Enum.IGMP_GROUP_RECORD_TYPE_IS_EXCLUDE,
                                              Enum.IGMP_GROUP_RECORD_TYPE_TO_INCLUDE,
                                              Enum.IGMP_GROUP_RECORD_TYPE_TO_EXCLUDE,
                                              Enum.IGMP_GROUP_RECORD_TYPE_ALLOW_NEW,
                                              Enum.IGMP_GROUP_RECORD_TYPE_BLOCK_OLD),
                          sources=self.field_map('sources',
                                                 IGMPIPAddress),
                          is_override_source_count=self.field_map('is_override_source_count'),
                          source_count=self.field_map('source_count'),
                          aux_data=self.field_map('aux_data'),
                          is_override_aux_data_length=self.field_map('is_override_aux_data_length'),
                          aux_data_length=self.field_map('aux_data_length'),
                          group_address=self.field_map('group_address',
                                                       IGMPIPAddress),
                          )

        return fields_map