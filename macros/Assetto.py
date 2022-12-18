# MACROPAD Hotkeys: Assetto Corsa Competizone

from adafruit_hid.keycode import Keycode
# from adafruit_hid.consumer_control_code import ConsumerControlCode
# from consumer import Toolbar

app = {
    'name' : 'Assetto Corsa Comp',
    'order': 1,
    'macros' : [
 	# COLOR    LABEL    KEY SEQUENCE
        # 1st row ----------
        (0x003000, 'TC',   [Keycode.CONTROL, Keycode.T]),
        (0x000010, 'BB+',  [Keycode.SHIFT, Keycode.B]),
        (0x101000, 'ABS', [Keycode.SHIFT, Keycode.A]),
        # 2nd row ----------
        (0x442E00, 'ENG', [Keycode.SHIFT, Keycode.E]),
        (0x000010, 'BB-', [Keycode.CONTROL, Keycode.B]),
        (0x400000, 'STRT',[Keycode.S]),
        # 3rd row ----------
        (0x250445, 'RCL',  [Keycode.ALT, Keycode.D]),
        (0x250115, 'HUD',  [Keycode.INSERT]),
        (0x166000, 'OFF', [Keycode.SHIFT, Keycode.I]),
        # 4th row ----------L
        (0x0A3B44, 'FLS', [Keycode.SHIFT, Keycode.L]),
        (0x404040, 'RLT', [Keycode.CONTROL, Keycode.L]),
        (0x101010, 'LGT', [Keycode.L])
    ]
}