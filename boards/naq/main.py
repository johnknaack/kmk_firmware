print("Starting NAQ")

import board

from kmk.kmk_keyboard import KMKKeyboard
#from kmk.extensions.rgb import RGB
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.scanners import DiodeOrientation
# from kmk.modules.holdtap import HoldTapRepeat
from kmk.keys import make_consumer_key

# TOOD Move to kb.py
keyboard = KMKKeyboard()
keyboard.row_pins = (board.GP5,board.GP6,board.GP7,board.GP8)
keyboard.col_pins = (board.GP29,board.GP28,board.GP27,board.GP26,board.GP15,board.GP14)
keyboard.diode_orientation = DiodeOrientation.COL2ROW
keyboard.debug_enabled = True
keyboard.coord_mapping = [
     0,  1,  2,  3,  4,  5,  29, 28, 27, 26, 25, 24,
     6,  7,  8,  9, 10, 11,  35, 34, 33, 32, 31, 30,
    12, 13, 14, 15, 16, 17,  41, 40, 39, 38, 37, 36,
                21, 22, 23,  47, 46, 45,
]

# TODO Comment one of these on each side
# split_side = SplitSide.LEFT
# split_side = SplitSide.RIGHT
# split = Split(data_pin=board.GP0,split_side=split_side,uart_flip=False,use_pio=False)
#split = Split(split_type=SplitType.BLE, split_side=split_side)

split = Split(
    split_flip=False,  # If both halves are the same, but flipped, set this True
    split_side=SplitSide.LEFT,  # Sets if this is to SplitSide.LEFT or SplitSide.RIGHT, or use EE hands
    split_type=SplitType.UART,  # Defaults to UART
    split_target_left=True,  # Assumes that left will be the one on USB. Set to False if it will be the right
    uart_interval=20,  # Sets the uarts delay. Lower numbers draw more power
    data_pin=board.GP0,  # The primary data pin to talk to the secondary device with
    data_pin2=None,  # Second uart pin to allow 2 way communication
    uart_flip=True,  # Reverses the RX and TX pins if both are provided
    use_pio=True,  # Use RP2040 PIO implementation of UART. Required if you want to use other pins than RX/TX
)
layers = Layers()

keyboard.modules = [layers, split]
# keyboard.extensions = [rgb]
#
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)

RGB_TOG = KC.A #RGB_TOG
RGB_HUI = KC.A #RGB_HUI
RGB_HUD = KC.A #RGB_HUI
RGB_SAI = KC.A #RGB_SAI
RGB_SAD = KC.A #RGB_SAD
RGB_VAI = KC.A #RGB_VAI
RGB_VAD = KC.A #RGB_VAD

MACOS_MC = KC.LCTL(KC.UP) #make_consumer_key(671, ('MACOS_MC',))
MACOS_LP = KC.LCTL(KC.DOWN) #make_consumer_key(672, ('MACOS_MC',))

keyboard.keymap = [
    [  #QWERTY
        KC.ESC,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
        KC.LSFT,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        KC.LCTL,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #LOWER
        KC.TAB,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0, KC.BSPC,\
        KC.LSFT, MACOS_MC, MACOS_LP, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,\
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #RAISE
        KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                         KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,\
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MINS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,  KC.GRV,\
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #ADJUST
        RGB_TOG, RGB_HUI, RGB_SAI, RGB_VAI, XXXXXXX, KC.F1,                         XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        XXXXXXX, RGB_HUD, RGB_SAD, RGB_VAD, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ]
]
if __name__ == '__main__':
    keyboard.go()
