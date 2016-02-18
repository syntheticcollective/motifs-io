import struct


class BinaryEncoder:
    def __init__(self):
        pass

    def encode_string(self, tagtype, s):
        return struct.pack('>HH%is' % len(s), tagtype, len(s), s)

    def encode_int(self, tagtype, i):
        return struct.pack('>HHl', tagtype, 4, i)

    def encode_byte(self, tagtype, b):
        return struct.pack('>HHB', tagtype, 1, b)
