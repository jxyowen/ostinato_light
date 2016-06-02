__author__ = 'jxy'

from ostinato.core import ost_pb


class PortList():
    def __init__(self):
        self.__all_ports = ost_pb.PortIdList()

    def add_port(self, port_number):
        self.__current_port = self.__all_ports.port_id.add()
        self.__current_port.id = int(port_number)
        return self

    @property
    def current_port(self):
        assert(self.__current_port)
        return self.__current_port

    @property
    def all_ports(self):
        return self.__all_ports
