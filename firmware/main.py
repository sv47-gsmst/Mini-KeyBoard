import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Press, Release, Tap
from kmk.modules.tapdance import TapDance  # <-- already added for K3

keyboard = KMKKeyboard()

# Enable macros
macros = Macros()
keyboard.modules.append(macros)

# Enable tapdance  <-- already present
tapdance = TapDance()
keyboard.modules.append(tapdance)

# Tapdance definition for K3  <-- already present
TD_WIN_LOCK = KC.TD(
    KC.LGUI,  # tap → Windows key
    KC.MACRO(Press(KC.LGUI), Tap(KC.L), Release(KC.LGUI)),  # hold → Win + L
)

# Tapdance definition for K7  <-- NEW
TD_SCREENSHOT = KC.TD(
    KC.MACRO(Tap(KC.PSCR)),  # tap → Full screenshot (PrintScreen)
    KC.MACRO(                 # hold → Win + Shift + S
        Press(KC.LGUI),
        Press(KC.LSHIFT),
        Tap(KC.S),
        Release(KC.LSHIFT),
        Release(KC.LGUI),
    ),
)

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

        # K3 → Tap = Win, Hold = Win+L
        TD_WIN_LOCK,

        # K4 → Previous Track
        KC.MPRV,

        # K5 → Play/Pause
        KC.MPLY,

        # K6 → Next Track
        KC.MNXT,

        # K7 → Tap = Full Screenshot, Hold = Snip Tool  <-- ONLY CHANGE HERE
        TD_SCREENSHOT,

        # K8 → Volume Down
        KC.VOLD,

        # K9 → Volume Up
        KC.VOLU,
    ]
]

if __name__ == '__main__':
    keyboard.go()
