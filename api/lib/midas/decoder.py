import struct


class BinaryDecoder:
    def __init__(self):
        pass

    def decode_tagtype(self, s):
        return struct.unpack('>H', s)

    def decode_header_section_length(self, s):
        return struct.unpack('>L', s)

    def decode_object_length(self, s):
        return struct.unpack('>H', s)

    def decode_string(self, length, s):
        return struct.unpack('>%is' % length, s)

    def decode_int(self, s):
        return struct.unpack('>l', s)

    def decode_byte(self, s):
        return struct.unpack('>B', s)
