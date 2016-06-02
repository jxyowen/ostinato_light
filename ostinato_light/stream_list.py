__author__ = 'jxy'

# import ostinato modules
from ostinato.core import ost_pb
from stream import Stream


class StreamList():
    def __init__(self, tx_port, is_loop_mode=False):
        self.__stream_number = 0
        self.__current_stream = None
        self.__stream_configuration = None
        self.__is_loop_mode = is_loop_mode
        self.__all_streams = ost_pb.StreamIdList()
        self.__all_streams.port_id.id = tx_port.id
        self.__all_streams_configurations = ost_pb.StreamConfigList()
        self.__all_streams_configurations.port_id.id = tx_port.id

    def add_stream(self, stream_packet_size_bytes=150,
                   is_stream_packet_size_random_mode=False,
                   stream_packet_size_random_min_bytes=64,
                   stream_packet_size_random_max_bytes=1518,
                   stream_average_bps=None, stream_duration_second=1,
                   stream_packet_num=1, stream_packets_per_second=1,
                   stream_name=''):
        self.__stream_number += 1
        self.__all_streams.stream_id.add().id = self.__stream_number
        self.__stream_configuration = self.__all_streams_configurations.stream.add()
        if self.__current_stream:
            self.__current_stream.control_next_mode_goto_next_stream()
        self.__current_stream = Stream(stream_number=self.__stream_number, stream_config=self.__stream_configuration,
                                       stream_average_bps=stream_average_bps, stream_duration_second=stream_duration_second,
                                       stream_packet_size_bytes=stream_packet_size_bytes, stream_packet_num=stream_packet_num,
                                       stream_packets_per_second=stream_packets_per_second, is_mode_goto_first_stream=self.__is_loop_mode,
                                       stream_name=stream_name, is_stream_packet_size_random_mode=is_stream_packet_size_random_mode,
                                       stream_packet_size_random_min_bytes=stream_packet_size_random_min_bytes,
                                       stream_packet_size_random_max_bytes=stream_packet_size_random_max_bytes)

        return self

    @property
    def current_stream(self):
        assert(self.__current_stream)
        return self.__current_stream

    @property
    def all_streams(self):
        return self.__all_streams

    @property
    def all_streams_configurations(self):
        return self.__all_streams_configurations

