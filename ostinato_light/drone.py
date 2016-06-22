__author__ = 'jxy'

import os
import time

# import ostinato modules
from ostinato.core import DroneProxy


class Drone():
    def __init__(self, host_name='127.0.0.1', port_number=7878, tx_port_list=None, rx_port_list=None):
        self.__drone = DroneProxy(host_name, port_number)
        if tx_port_list:
            self.__tx_port_list = tx_port_list.all_ports
        else:
            self.__tx_port_list = None
        if rx_port_list:
            self.__rx_port_list = rx_port_list.all_ports
        else:
            self.__rx_port_list = None

    def connect(self):
        self.__drone.connect()
        self.tx_port_clear_stats()
        self.rx_port_clear_stats()
        return self

    def disconnect(self):
        self.__drone.disconnect()
        return self

    def add_stream_list(self, stream_list):
        self.current_stream_list = stream_list
        self.__drone.addStream(stream_list.all_streams)
        self.__drone.modifyStream(stream_list.all_streams_configurations)
        return self

    def remove_stream_list(self, stream_id):
        self.__drone.deleteStream(stream_id)
        return self

    def remove_current_stream_list(self):
        assert(self.current_stream_list)
        self.__drone.deleteStream(self.current_stream_list.all_streams)
        return self

    def get_port_id_list(self):
        port_id_list = self.__drone.getPortIdList()
        return port_id_list

    def fetch_stream_id_list(self):
        stream_id_list = self.__drone.getStreamIdList(self.__tx_port_list.port_id[0])
        return stream_id_list

    def get_port_config_list(self):
        port_config_list = self.__drone.getPortConfig(self.get_port_id_list())
        return port_config_list

    def start_transmit(self):
        assert(self.__tx_port_list)
        self.tx_port_clear_stats()
        self.__drone.startTransmit(self.__tx_port_list)
        return self

    def wait_for_transmission_complete(self, time_out=None):
        time_start = time.time()
        while True:
            time.sleep(1)
            tx_stats = self.fetch_stats_tx_port()
            print('transmit rate %s bps' % (tx_stats.tx_bps * 8))
            if (not tx_stats.state.is_transmit_on)\
            or (time_out and (time.time() - time_start > time_out)):
                break
            else:
                print('waiting for transmit to finish ,elapsed time %s seconds' % (time.time() - time_start))

        print('transmit total time %s seconds' % (time.time() - time_start))
        return self

    def stop_transmit(self):
        assert(self.__tx_port_list)
        self.__drone.stopTransmit(self.__tx_port_list)
        return self

    def __start_capture(self, port_list):
        assert(port_list)
        self.__drone.startCapture(port_list)

    def __stop_capture(self, port_list):
        assert(port_list)
        self.__drone.stopCapture(port_list)

    def __clear_stats(self, port_list):
        # assert(port)
        if port_list:
            self.__drone.clearStats(port_list)

    def __fetch_stats_port(self, port_list):
        assert(port_list)
        stats = self.__drone.getStats(port_list)
        return stats.port_stats[0]

    def __fetch_capture_buffer(self, port_list, buffer_file_name='capture.pcap'):
        assert(port_list)
        buffer = self.__drone.getCaptureBuffer(port_list.port_id[0])
        self.__drone.saveCaptureBuffer(buffer, buffer_file_name)
        # os.system('tshark -r ' + buffer_file_name)
        # os.remove(buffer_file_name)

    def tx_port_start_capture(self):
        self.__start_capture(self.__tx_port_list)
        return self

    def tx_port_stop_capture(self):
        self.__stop_capture(self.__tx_port_list)
        return self

    def tx_port_clear_stats(self):
        self.__clear_stats(self.__tx_port_list)
        return self

    def rx_port_start_capture(self):
        self.__start_capture(self.__rx_port_list)
        return self

    def rx_port_stop_capture(self):
        self.__stop_capture(self.__rx_port_list)
        return self

    def rx_port_clear_stats(self):
        self.__clear_stats(self.__rx_port_list)
        return self

    def fetch_stats_tx_port(self):
        return self.__fetch_stats_port(self.__tx_port_list)

    def fetch_capture_buffer_tx_port(self):
        self.__fetch_capture_buffer(self.__tx_port_list, buffer_file_name='tx_port_capture.pcap')

    def fetch_stats_rx_port(self):
        return self.__fetch_stats_port(self.__rx_port_list)

    def fetch_capture_buffer_rx_port(self):
        self.__fetch_capture_buffer(self.__rx_port_list, buffer_file_name='rx_port_capture.pcap')
