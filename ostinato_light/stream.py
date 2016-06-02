__author__ = 'jxy'
import math
from ostinato.core import ost_pb


class Stream():
    def __init__(self, stream_number, stream_config,
                 stream_average_bps=None, stream_duration_second=1,
                 stream_packet_size_bytes=150,
                 is_stream_packet_size_random_mode=False,
                 stream_packet_size_random_min_bytes=64,
                 stream_packet_size_random_max_bytes=1518,
                 stream_packet_num=1, stream_packets_per_second=1,
                 is_mode_goto_first_stream=False, stream_name=''):
        self.__stream_config = stream_config
        self.__stream_config.stream_id.id = stream_number
        self.__stream_config.core.ordinal = stream_number
        self.__stream_config.core.is_enabled = True

        if stream_average_bps:
            self.__stream_config.control.num_packets = int(math.ceil((stream_average_bps / 8.0) * stream_duration_second / stream_packet_size_bytes))
            self.__stream_config.control.packets_per_sec = int(math.ceil((stream_average_bps / 8.0) / stream_packet_size_bytes))
        else:
            self.__stream_config.control.num_packets = stream_packet_num
            self.__stream_config.control.packets_per_sec = stream_packets_per_second

        if is_mode_goto_first_stream:
            self.control_next_mode_goto_first_stream()
        else:
            self.control_next_mode_goto_next_stream()

        self.__stream_config.core.name = stream_name
        if is_stream_packet_size_random_mode:
            self.__stream_config.core.len_mode = ost_pb.StreamCore.e_fl_random
            self.__stream_config.core.frame_len_min = stream_packet_size_random_min_bytes
            self.__stream_config.core.frame_len_max = stream_packet_size_random_max_bytes
        else:
            self.__stream_config.core.frame_len = stream_packet_size_bytes


    def configure_protocols(self, *protocol_builders):
        for protocol_builder in protocol_builders:
            protocol = self.__stream_config.protocol.add()
            protocol_builder.build(protocol)

    def control_next_mode_goto_next_stream(self):
        self.__stream_config.control.next = ost_pb.StreamControl.e_nw_goto_next

    def control_next_mode_goto_first_stream(self):
        self.__stream_config.control.next = ost_pb.StreamControl.e_nw_goto_id