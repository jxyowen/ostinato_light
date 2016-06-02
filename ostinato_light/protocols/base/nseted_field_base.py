__author__ = 'jxy'

from protocol_base import ProtocolBase


class NestedFieldBase(ProtocolBase):
    def is_nested_field(self):
        return True

    def _protocol_type_number(self):
        pass

    def _protocol_type(self):
        pass

    def _protocol_class(self):
        pass

    def _protocol_fields_map(self):
        pass