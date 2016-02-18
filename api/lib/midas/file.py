import struct

from decoder import BinaryDecoder
from header import MOTIF_HEADER, read_header


class MIDIFile:
    def __init__(self, midi_file_handle):
        self.fh = midi_file_handle
        self.fh.seek(0, 2)
        self.filelength = self.fh.tell()
        self.fh.seek(0)

    def close(self):
        self.fh.close()

    def get_motif_header(self):
        self.fh.seek(0)
        while self.fh.tell() < self.filelength:
            header_type = struct.unpack('>4s', self.fh.read(4))[0]
            if header_type == MOTIF_HEADER:
                # we found it, back up 4 bytes and parse the header
                self.fh.seek(-4, 1)
                return read_header(self.fh, BinaryDecoder())
            else:
                # not here, skip this chunk and go to the next
                chunk_length = struct.unpack('>L', self.fh.read(4))[0]
                self.fh.seek(chunk_length, 1)
        self.fh.seek(0)

    def write_motif_header(self, header):
        # we're appending here because midi players whine if the midi header chunk isn't first
        self.fh.seek(0, 2)
        to_write = header.to_bytes()
        self.fh.write(to_write)
        self.filelength = self.fh.tell()
        self.fh.seek(0)
