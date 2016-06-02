__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.sample_pb2 import Sample, sample

from base.protocol_base import ProtocolBase


class SAMPLE(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kSampleFieldNumber

    def _protocol_type(self):
        return sample

    def _protocol_class(self):
        return Sample

    def _protocol_fields_map(self):

        fields_map = dict(is_override_checksum=self.field_map('is_override_checksum'),
                          ab=self.field_map('ab'),
                          payload_length=self.field_map('payload_length'),
                          checksum=self.field_map('checksum'),
                          x=self.field_map('x'),
                          y=self.field_map('y'),
                          )

        return fields_map
