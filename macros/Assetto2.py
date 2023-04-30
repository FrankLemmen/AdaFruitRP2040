# MACROPAD Hotkeys: Assetto Corsa Competizone
# Definition by: Frank Lemmen

from adafruit_hid.keycode import Keycode

app = {
    'name' : 'Display',
    'order': 2,
    'macros' : [
        # COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x000000, '', [Keycode.KEYPAD_SEVEN]),
        (0x663F00, 'UP', [Keycode.KEYPAD_EIGHT]),
        (0x000000, '      ', [Keycode.KEYPAD_NINE]),
        # 2nd row ----------
        (0x663F00, 'LEFT', [Keycode.KEYPAD_FOUR]),
        (0x360116, 'MFD ', [Keycode.INSERT]),
        (0x663F00, 'RGHT', [Keycode.KEYPAD_SIX]),
        # 3rd row ----------
        (0x000000, ' ', [Keycode.KEYPAD_ONE]),
        (0x663F00, 'DOWN', [Keycode.KEYPAD_TWO]),
        (0x000000, '  ', [Keycode.KEYPAD_THREE]),
        # 4th row ----------
        (0x0A3B66, 'CAM', [Keycode.F1]),
        (0x000000, '', [Keycode.INSERT]),
        (0x404040, 'EXTVIEW', [Keycode.F3])
    ]
}
