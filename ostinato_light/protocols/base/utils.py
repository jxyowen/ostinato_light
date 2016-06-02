__author__ = 'jxy'

import re


class Utils():
    @staticmethod
    def macStrToInt(strMAC):
        return int(re.sub(r'(^0x)?[\s:-]', '', strMAC), 16)

    @staticmethod
    def ip4StrToInt(strIP4):
        return reduce(lambda x, y: (x << 8)+y, map(int, strIP4.split('.')))