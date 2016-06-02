__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols.fileformat_pb2 import Fileformat, fileformat

from base.protocol_base import ProtocolBase


class FILEFORMAT(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kFileformatFieldNumber

    def _protocol_type(self):
        return fileformat

    def _protocol_class(self):
        return Fileformat

    def _protocol_fields_map(self):

        fields_map = dict(file_type=self.field_map('file_type'),
                          format_version_major=self.field_map('format_version_major'),
                          format_version_minor=self.field_map('format_version_minor'),
                          format_version_revision=self.field_map('format_version_revision'),
                          generator_name=self.field_map('generator_name'),
                          generator_version=self.field_map('generator_version'),
                          generator_revision=self.field_map('generator_revision'),
                         )

        return fields_map
