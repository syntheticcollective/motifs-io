MAJOR = 0x0
DORIAN = 0x1
PHRYGIAN = 0x2
LYDIAN = 0x3
MIXOLYDIAN = 0x4
MINOR = 0x5
LOCRIAN = 0x6

TRANSLATION_TABLE = {
    "major": MAJOR,
    "dorian": DORIAN,
    "phrygian": PHRYGIAN,
    "lydian": LYDIAN,
    "mixolydian": MIXOLYDIAN,
    "minor": MINOR,
    "locrian": LOCRIAN
}


def mode_to_byte(mode):
    return TRANSLATION_TABLE[mode]
