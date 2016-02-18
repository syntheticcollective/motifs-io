A_FLAT = 0x0
A = 0x1
A_SHARP = 0x2
B_FLAT = 0x3
B = 0x4
C = 0x5
C_SHARP = 0x6
D_FLAT = 0x7
D = 0x8
D_SHARP = 0x9
E_FLAT = 0x10
E = 0x11
F = 0x12
F_SHARP = 0x13
G_FLAT = 0x14
G = 0x15
G_SHARP = 0x16


TRANSLATION_TABLE = {
    "Ab": A_FLAT,
    "A": A,
    "A#": A_SHARP,
    "Bb": B_FLAT,
    "B": B,
    "C": C,
    "C#": C_SHARP,
    "Db": D_FLAT,
    "D": D,
    "D#": D_SHARP,
    "Eb": E_FLAT,
    "E": E,
    "F": F,
    "F#": F_SHARP,
    "Gb": G_FLAT,
    "G": G,
    "G#": G_SHARP
}


def key_to_byte(key):
    return TRANSLATION_TABLE[key]
