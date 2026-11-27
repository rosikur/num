print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.RGB import RGB
from kmk.extensions.media_keys import MediaKeys


keyboard = KMKKeyboard()

keyboard.extensions.append(MediaKeys())

keyboard.col_pins = (board.GP0,board.GP1,board.GP2,board.GP3)
keyboard.row_pins = (board.GP4,board.GP5,board.GP6,board.GP7,board.GP8,board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

rgb = RGB(pixel_pin=board.GP10, num_pixels=24)
keyboard.extensions.append(rgb)
rgb_order=(1,0,2)
rgb.val_limit = 100
rgb.val_default = 100
rgb.hue_default = 196
rgb.sat_default = 211 

keyboard.keymap = [


    [KC.AUDIO_MUTE,KC.MPRV,KC.MNXT,KC.MPLY],
    [KC.RGB_TOG,KC.KP_SLASH,KC.KP_ASTERISK,KC.KP_MINUS],
    [KC.N7,KC.N8,KC.N9,KC.KP_PLUS],
    [KC.N4,KC.N5,KC.N6,KC.NO],
    [KC.N1,KC.N2,KC.N3,KC.KP_ENTER],
    [KC.N0,KC.NO,KC.DOT,KC.NO]


]

if __name__ == '__main__':
    keyboard.go()