import os
from unittest import TestCase

from api.lib.midas.file import MIDIFile
from api.lib.midas.header import MotifHeader
from api.lib.midas.encoder import BinaryEncoder

TEST_MIDI_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'resources', 'Double Basses.mid')


class MidasHeaderTest(TestCase):
    def setUp(self):
        self.fh = open(TEST_MIDI_FILE, 'a+b')
        self.fh.seek(0)
        self.current_contents = self.fh.read()
        self.fh.seek(0)

    def tearDown(self):
        self.fh.truncate(0)
        self.fh.write(self.current_contents)
        self.fh.close()

    def test_midifile_can_write_and_retrieve_a_motif_header(self):
        midi = MIDIFile(self.fh)
        header = MotifHeader(BinaryEncoder(), title='foobar', composer='foobarovsky', bpm=120,
                             mode=0x0, key=0x0, tags=['foo', 'bar'])
        midi.write_motif_header(header)
        test_header = midi.get_motif_header()
        self.assertEquals(header.title, test_header.title)
        self.assertEquals(header.tags, test_header.tags)

    def test_midifile_returns_none_if_no_header(self):
        midi = MIDIFile(self.fh)
        test_header = midi.get_motif_header()
        self.assertEquals(test_header, None)
