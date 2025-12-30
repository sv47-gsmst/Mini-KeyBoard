import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap

keyboard = KMKKeyboard()

# Enable macros
macros = Macros()
keyboard.modules.append(macros)

# Your exact pin wiring
PINS = [
    board.GP1,  # K1
    board.GP2,  # K2
    board.GP4,  # K3
    board.GP3,  # K4
    board.GP26, # K5
    board.GP27, # K6
    board.GP28, # K7
    board.GP7,  # K8
    board.GP0,  # K9
]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

keyboard.keymap = [
    [
        # K1 → Ctrl + W
        KC.MACRO(Press(KC.LCTRL), Tap(KC.W), Release(KC.LCTRL)),

        # K2 → Alt + Tab
        KC.MACRO(Press(KC.LALT), Tap(KC.TAB), Release(KC.LALT)),

        # K3 → Windows Key
        KC.LGUI,

        # K4 → Previous Track
        KC.MPRV,

        # K5 → Play/Pause
        KC.MPLY,

        # K6 → Next Track
        KC.MNXT,

        # K7 → Airplane Mode
        KC.AIRPLANE,

        # K8 → Volume Down
        KC.VOLD,

        # K9 → Volume Up
        KC.VOLU,
    ]
]

if __name__ == '__main__':
    keyboard.go()