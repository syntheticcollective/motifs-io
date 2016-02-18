from collections import defaultdict
from io import BytesIO
import struct

from encoder import BinaryEncoder


MOTIF_HEADER = 'MTmf'
TITLE = 0x0
COMPOSER = 0x1
BPM = 0x2
KEY = 0x3
MODE = 0x4
TAG = 0x5


TYPE_TO_STRING_TABLE = {
    TITLE: 'title',
    COMPOSER: 'composer',
    BPM: 'bpm',
    KEY: 'key',
    MODE: 'mode',
    TAG: 'tags'
}


TYPE_DECODER_TABLE = {
    TITLE: 'decode_string',
    COMPOSER: 'decode_string',
    BPM: 'decode_int',
    KEY: 'decode_byte',
    MODE: 'decode_byte',
    TAG: 'decode_string'
}


class MotifHeader:
    def __init__(self, encoder, title=None, composer=None, bpm=None, key=None, mode=None, tags=None):
        self.encoder = encoder
        self.buffer = BytesIO()
        self.title = title
        self.composer = composer
        self.bpm = bpm
        self.key = key
        self.mode = mode
        self.tags = tags

    def clear_buffer(self):
        self.buffer = BytesIO()

    def _encode_title(self, title):
        return self.encoder.encode_string(TITLE, title)

    def _encode_composer(self, composer):
        return self.encoder.encode_string(COMPOSER, composer)

    def _encode_bpm(self, bpm):
        return self.encoder.encode_int(BPM, bpm)

    def _encode_key(self, key):
        return self.encoder.encode_byte(KEY, key)

    def _encode_mode(self, mode):
        return self.encoder.encode_byte(MODE, mode)

    def _encode_tags(self, tags):
        buf = []
        for tag in tags:
            buf.append(self.encoder.encode_string(TAG, tag))
        return ''.join(buf)

    def to_bytes(self):
        if self.title is not None:
            self.buffer.write(self._encode_title(self.title))
        if self.composer is not None:
            self.buffer.write(self._encode_composer(self.composer))
        if self.bpm is not None:
            self.buffer.write(self._encode_bpm(self.bpm))
        if self.key is not None:
            self.buffer.write(self._encode_key(self.key))
        if self.mode is not None:
            self.buffer.write(self._encode_mode(self.mode))
        if self.tags is not None:
            self.buffer.write(self._encode_tags(self.tags))
        to_write = self.buffer.getvalue()
        bytes = struct.pack('>4sL%is' % len(to_write), MOTIF_HEADER, len(to_write), to_write)
        self.clear_buffer()
        return bytes


def read_header(header_buffer, decoder):
    current_pos = header_buffer.tell()
    attrs = defaultdict(None)
    attrs[TYPE_TO_STRING_TABLE[TAG]] = []
    header_type = header_buffer.read(4)
    if header_type != MOTIF_HEADER:
        raise ValueError('Header buffer does not begin with the Motif header type')

    (total_length,) = decoder.decode_header_section_length(header_buffer.read(4))

    while (header_buffer.tell() - (current_pos + 8)) < total_length:
        (tagtype,) = decoder.decode_tagtype(header_buffer.read(2))
        (taglength,) = decoder.decode_object_length(header_buffer.read(2))
        decoder_method = TYPE_DECODER_TABLE[tagtype]
        tagstring = TYPE_TO_STRING_TABLE[tagtype]
        if decoder_method == 'decode_string':
            if tagstring == 'tags':
                tag = getattr(decoder, decoder_method)(
                    taglength,
                    header_buffer.read(taglength)
                )
                attrs[tagstring].append(tag[0])
            else:
                attrs[tagstring] = getattr(decoder, decoder_method)(
                    taglength,
                    header_buffer.read(taglength)
                )[0]
        else:
            attrs[tagstring] = getattr(decoder, decoder_method)(
                header_buffer.read(taglength)
            )[0]

    return MotifHeader(BinaryEncoder(), **attrs)
