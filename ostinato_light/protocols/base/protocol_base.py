from abc import ABCMeta, abstractmethod


class ProtocolBase():
    __metaclass__ = ABCMeta

    VALUE_TRANSFORM_CLASS = 'value_transform_class'
    VALUE_TRANSFORM_METHOD = 'value_transform_method'
    ENUM_TYPES = 'enum_types'
    FIELD = 'field'

    def __init__(self, **protocol_parameters):
        self.__protocol_parameters = protocol_parameters

    def is_nested_field(self):
        return False

    @abstractmethod
    def _protocol_type_number(self):
        pass

    @abstractmethod
    def _protocol_type(self):
        pass

    @abstractmethod
    def _protocol_class(self):
        pass

    @abstractmethod
    def _protocol_fields_map(self):
        pass

    def build(self, field):
        is_nested_field = self.is_nested_field()
        if not is_nested_field:
            protocol_type = self._protocol_type()
            protocol_fields = field.Extensions[protocol_type]
            field.protocol_id.id = self._protocol_type_number()
        self.__protocol_related_fields_setup()
        for protocol_field, raw_value in self.__protocol_parameters.items():
            protocol_field_map_dict = self._protocol_fields_map()
            assert protocol_field in protocol_field_map_dict.keys(), 'Protocol %s field "%s" is not exist' % (self.__class__.__name__, protocol_field)
            sub_field_name = protocol_field_map_dict[protocol_field][self.__class__.FIELD]
            if not is_nested_field:
                assert hasattr(protocol_fields, sub_field_name), 'Protocol %s map to field "%s" is not exist' % (self.__class__.__name__, sub_field_name)

            if self.__class__.VALUE_TRANSFORM_CLASS in protocol_field_map_dict[protocol_field].keys():
                value_transform_class = protocol_field_map_dict[protocol_field][self.__class__.VALUE_TRANSFORM_CLASS]
                sub_field = getattr(protocol_fields, sub_field_name)
                if hasattr(sub_field, 'add'):
                    assert isinstance(raw_value, list),  'Protocol %s field "%s" \'s value must be a LIST' % (self.__class__.__name__, protocol_field)
                    for protocol_builder in raw_value:
                        assert isinstance(protocol_builder, value_transform_class),  'Protocol %s field "%s" \'s class must be %s' % (self.__class__.__name__, protocol_field, value_transform_class.__name__)
                        nested_field = sub_field.add()
                        protocol_builder.build(nested_field)
                else:
                    assert isinstance(raw_value, value_transform_class),  'Protocol %s field "%s" \'s class must be %s' % (self.__class__.__name__, protocol_field, value_transform_class.__name__)
                    protocol_builder = raw_value
                    protocol_builder.build(sub_field)
                protocol_value = None
            elif self.__class__.VALUE_TRANSFORM_METHOD in protocol_field_map_dict[protocol_field].keys():
                protocol_value = protocol_field_map_dict[protocol_field][self.__class__.VALUE_TRANSFORM_METHOD](raw_value)
            elif self.__class__.ENUM_TYPES in protocol_field_map_dict[protocol_field].keys():
                enum_types = protocol_field_map_dict[protocol_field][self.__class__.ENUM_TYPES]
                assert raw_value in enum_types, 'Protocol %s field "%s" enum field "%s" is not exist' % (self.__class__.__name__, protocol_field, raw_value)
                if isinstance(raw_value, basestring):
                    protocol_value = getattr(self._protocol_class(), raw_value)
                else:
                    protocol_value = raw_value
            else:
                protocol_value = raw_value

            if protocol_value:
                if is_nested_field:
                    setattr(field, sub_field_name, protocol_value)
                else:
                    setattr(protocol_fields, sub_field_name, protocol_value)

    def field_map(self, field_map_to, *value_process):
        field_map_dict = {self.__class__.FIELD: field_map_to}
        if len(value_process) > 0:
            if len(value_process) == 1 and hasattr(value_process[0], 'build'):
                # print(value_process[0])
                field_map_dict[self.__class__.VALUE_TRANSFORM_CLASS] = value_process[0]
            elif len(value_process) == 1 and hasattr(value_process[0], '__call__'):
                field_map_dict[self.__class__.VALUE_TRANSFORM_METHOD] = value_process[0]
            else:
                field_map_dict[self.__class__.ENUM_TYPES] = value_process
        return field_map_dict

    def _protocol_fields_with_related_fields(self):
        related_field = {}
        return related_field

    def __protocol_related_fields_setup(self):
        protocol_fields_with_related_fields_dict = self._protocol_fields_with_related_fields()
        for field, related_fields_dict in protocol_fields_with_related_fields_dict.items():
            if field in self.__protocol_parameters.keys():
                for related_field, value in related_fields_dict.items():
                    self.__protocol_parameters[related_field] = value