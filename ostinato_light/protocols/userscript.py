__author__ = 'zc'

from ostinato.core import ost_pb
from ostinato.protocols import userscript_pb2

from base.protocol_base import ProtocolBase


class UserScript(ProtocolBase):

    def _protocol_type_number(self):
        return ost_pb.Protocol.kUserScriptFieldNumber

    def _protocol_type(self):
        return userscript_pb2.userScript

    def _protocol_class(self):
        return userscript_pb2.UserScript

    def _protocol_fields_map(self):
        fields_map = dict(program=self.field_map('program'),
                          )
        return fields_map

