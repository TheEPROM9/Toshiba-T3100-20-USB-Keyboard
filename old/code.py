#PiPi-GHERKIN - Raspberry Pi PICO
#Rpi pico keyboard keymap, I used the gherkin keymap as a example :)
#print("Starting")

#run the led
#import board
#import pwmio
#import time
#import supervisor

#led = pwmio.PWMOut(board.GP25, frequency=1, duty_cycle=1024, variable_frequency=True)




#import board
#from kmk.kmk_keyboard import KMKKeyboard
#from kmk.keys import KC
#from kmk.matrix import DiodeOrientation
#from kmk.modules.layers import Layers
#from kmk.keys import KC, make_key
#envkb = KMKKeyboard()

#envkb.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10)
#envkb.row_pins = (board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18)
#envkb.diode_orientation = DiodeOrientation.COLUMNS

#rollover_cols_every_rows = 2
#envkb.diode_orientation = DiodeOrientation.COLUMNS
#envkb.debug_enabled = False

#layers = Layers()
#envkb.modules = [layers]

#nokey = KC.NO
#envkb.keymap = [
#    [
    #Layer 0?
#        KC.DEL, KC.DOT, KC.SCLN, KC.L, KC.LEFT, KC.P, KC.MINUS, KC.N0, KC.F6, KC.F7, KC.F8, KC.M, KC.COMM, KC.K, KC.J, KC.O, KC.I, KC.N9,
#        KC.N8, KC.N1, KC.N2, KC.N3, KC.SPC, KC.N, KC.B, KC.H, KC.U, KC.Y, KC.N7, KC.N6, KC.EQUAL, KC.LCTL, KC.BSPC, KC.C, KC.V, KC.G,
#        KC.F, KC.MO(1), KC.R, KC.N5, KC.N4, KC.R, KC.T, KC.Y, KC.X, KC.Z, KC.D, KC.S, KC.E, KC.W, KC.BSLS, KC.N2, KC.END, KC.PGDN,
#        KC.CAPS, KC.NONUS_BSLASH, KC.LSHIFT, KC.LCTL, KC.A, KC.Q, KC.TAB, KC.N1, KC.ESC, KC.K, KC.L, KC.SCLN, KC.LALT, KC.F10, KC.F8, KC.F6, KC.PGUP, KC.F4,   
#        KC.SCROLLLOCK, KC.F2, KC.Z, KC.X, KC.C, KC.END, KC.F9, KC.F7, KC.F5, KC.PGDN, KC.F3, KC.NUMLOCK,
#    ],
#    [
    #Layer 1
#        KC.TRNS, nokey, KC.F13, KC.F14, KC.F15, KC.F16, nokey, KC.F17, KC.F18, KC.F19, KC.F20, KC.F21, KC.F22, KC.F23, KC.F24, KC.MUTE, KC.VOLD, KC.VOLU,
#        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
#        KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
#        KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, nokey, nokey, nokey,
#        KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, nokey, KC.TRNS, nokey, nokey, KC.TRNS, nokey,
#        KC.TRNS, KC.TRNS, nokey, KC.TRNS, nokey, nokey, KC.TRNS, nokey, nokey, nokey, KC.TRNS, KC.TRNS, nokey, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
#    ],
#]

#def usbfunc():
    
#    if __name__ == '__main__':
#        led.duty_cycle=16384
#        led.frequency=144
#        print("Started")
#        envkb.go()
#        raise Exception('Something has caused an error.')
        
#try:
#    usbfunc()
#except KeyboardInterrupt:
#    led.duty_cycle=0
#    print("Keyboard Interrupt")
#except Exception as e:
#    print(e)
#    led.duty_cycle=0
#    supervisor.reload()


#supervisor.reload()