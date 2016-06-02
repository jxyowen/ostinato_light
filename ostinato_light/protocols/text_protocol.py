__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols import textproto_pb2

from base.protocol_base import ProtocolBase
from base.consts import Enum


class TextProtocol(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kTextProtocolFieldNumber

    def _protocol_type(self):
        return textproto_pb2.textProtocol

    def _protocol_class(self):
        return textproto_pb2.TextProtocol

    def _protocol_fields_map(self):
        fields_map = dict(port_num=self.field_map('port_num'),
                          encoding=self.field_map('encoding',
                                                  Enum.TEXT_PROTOCOL_TEXT_ENCODING_UTF8),
                          text=self.field_map('text'),
                          eol=self.field_map('eol',
                                             Enum.TEXT_PROTOCOL_END_OF_LINE_CR,
                                             Enum.TEXT_PROTOCOL_END_OF_LINE_LF,
                                             Enum.TEXT_PROTOCOL_END_OF_LINE_CRLF),
                          )
        return fields_map

