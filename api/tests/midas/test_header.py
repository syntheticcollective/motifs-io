import StringIO as sio
from unittest import TestCase

from api.lib.midas.header import MotifHeader, read_header
from api.lib.midas.encoder import BinaryEncoder
from api.lib.midas.decoder import BinaryDecoder
from api.lib.midas.constants.key import A_SHARP
from api.lib.midas.constants.mode import MAJOR


class MidasHeaderTest(TestCase):
    def test_header_with_title_encode_and_decode(self):
        header = MotifHeader(BinaryEncoder(), title='foobar')
        header_buf = sio.StringIO(header.to_bytes())
        test_header = read_header(header_buf, BinaryDecoder())
        self.assertEquals(test_header.title, 'foobar')

    def test_header_with_composer_encode_and_decode(self):
        header = MotifHeader(BinaryEncoder(), composer='foobar')
        header_buf = sio.StringIO(header.to_bytes())
        test_header = read_header(header_buf, BinaryDecoder())
        self.assertEquals(test_header.title, None)
        self.assertEquals(test_header.composer, 'foobar')

    def test_header_with_bpm_encode_and_decode(self):
        header = MotifHeader(BinaryEncoder(), bpm=120)
        header_buf = sio.StringIO(header.to_bytes())
        test_header = read_header(header_buf, BinaryDecoder())
        self.assertEquals(test_header.title, None)
        self.assertEquals(test_header.composer, None)
        self.assertEquals(test_header.bpm, 120)

    def test_header_with_key_encode_and_decode(self):
        header = MotifHeader(BinaryEncoder(), key=A_SHARP)
        header_buf = sio.StringIO(header.to_bytes())
        test_header = read_header(header_buf, BinaryDecoder())
        self.assertEquals(test_header.title, None)
        self.assertEquals(test_header.composer, None)
        self.assertEquals(test_header.bpm, None)
        self.assertEquals(test_header.key, A_SHARP)

    def test_header_with_mode_encode_and_decode(self):
        header = MotifHeader(BinaryEncoder(), mode=MAJOR)
        header_buf = sio.StringIO(header.to_bytes())
        test_header = read_header(header_buf, BinaryDecoder())
        self.assertEquals(test_header.title, None)
        self.assertEquals(test_header.composer, None)
        self.assertEquals(test_header.bpm, None)
        self.assertEquals(test_header.key, None)
        self.assertEquals(test_header.mode, MAJOR)

    def test_header_with_tags_encode_and_decode(self):
        header = MotifHeader(BinaryEncoder(), tags=['foo', 'bar'])
        header_buf = sio.StringIO(header.to_bytes())
        test_header = read_header(header_buf, BinaryDecoder())
        self.assertEquals(test_header.title, None)
        self.assertEquals(test_header.composer, None)
        self.assertEquals(test_header.bpm, None)
        self.assertEquals(test_header.key, None)
        self.assertEquals(test_header.mode, None)
        self.assertEquals(test_header.tags, ['foo', 'bar'])

    def test_header_with_everything_encode_and_decode(self):
        header = MotifHeader(BinaryEncoder(), title='ode to foo', composer='foochovsky', bpm=1000,
                             key=A_SHARP, mode=MAJOR, tags=['foo', 'bar'])
        header_buf = sio.StringIO(header.to_bytes())
        test_header = read_header(header_buf, BinaryDecoder())
        self.assertEquals(test_header.title, 'ode to foo')
        self.assertEquals(test_header.composer, 'foochovsky')
        self.assertEquals(test_header.bpm, 1000)
        self.assertEquals(test_header.key, A_SHARP)
        self.assertEquals(test_header.mode, MAJOR)
        self.assertEquals(test_header.tags, ['foo', 'bar'])

    def test_can_properly_decode_header_as_part_of_a_larger_file(self):
        header = MotifHeader(BinaryEncoder(), title='foobar')
        header_buf = sio.StringIO(header.to_bytes())
        header_buf.seek(0, 2)
        header_buf.write('some nonsense')
        header_buf.seek(0)
        test_header = read_header(header_buf, BinaryDecoder())
        self.assertEquals(test_header.title, 'foobar')
