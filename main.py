print("Starting")

import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

# Definitions for the pins & diode orentation, can't have straght diodes now. ;-)
keyboard.col_pins = [board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18]
keyboard.row_pins = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10]
keyboard.diode_orientation = DiodeOrientation.COL2ROW

#These are the IC codes the keys produced when pressed, map these out to your keyboard or the key function array will be random.
keyboard.coord_mapping = [
    16,0,8,2,10,4,12,5,13,6,14,1,9,78,80,
    17,24,25,32,33,40,41,48,49,56,57,64,72,74,
    18,19,26,27,34,35,42,43,50,51,58,66,67,11,
    21,20,28,29,36,37,44,52,53,60,61,69,75,3,
    22,30,31,39,38,45,46,55,54,62,70,77,65,7,
    15,71,23,47,76,79,63,59,73,68
    ]

# Debug mode, slows the keyboard down but needed to find out the IC codes.
keyboard.debug_enabled = False

# Needed for tyhe layers to work.
keyboard.modules.append(Layers())

# Keyboard keymap, make sure you have defined the coord array first.
keyboard.keymap = [
    [# Layer 0
        KC.ESC, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.NUMLOCK, KC.SCROLLLOCK, KC.PSCREEN, KC.MO(1),
        KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.HOME,
        KC.TAB, KC.Q, KC.W, KC.E, KC.R, KC.T, KC.Y, KC.U, KC.I, KC.O, KC.P, KC.LBRC, KC.RBRC, KC.PGUP,
        KC.LCTL, KC.A, KC.S, KC.D, KC.F, KC.G, KC.H, KC.J, KC.K, KC.L, KC.SCLN, KC.QUOT, KC.ENT, KC.PGDN,
        KC.LSFT, KC.Z, KC.X, KC.C, KC.V, KC.B, KC.N, KC.M, KC.COMM, KC.DOT, KC.SLSH, KC.RSFT, KC.UP, KC.END,
        KC.LALT, KC.CAPS, KC.NONUS_BSLASH, KC.SPC, KC.NUHS, KC.INSERT, KC.DELETE, KC.LEFT, KC.DOWN, KC.RIGHT
    ],
    [# Layer 1
        KC.NO, KC.F11, KC.F12, KC.F13, KC.F14, KC.F15, KC.F16, KC.F17, KC.F18, KC.F19, KC.NO, KC.NO, KC.NO, KC.PAST, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.N7, KC.N8, KC.N9, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.N4, KC.N5, KC.N6, KC.MINUS, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.N1, KC.N2, KC.N3, KC.PLUS, KC.NO, KC.ENT, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.N0, KC.NO, KC.DOT, KC.SLSH, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ]
]

if __name__ == '__main__':
    print("Started")
    keyboard.go()