import board
import usb_hid
import digitalio
import adafruit_debouncer
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard import Keyboard

# Button mapping
BTN_A = 3
BTN_B = 1
BTN_C = 0
BTN_D = 7
BTN_E = 5
BTN_F = 2
BTN_DOWN = 4
BTN_LEFT = 6
BTN_RIGHT = 8
BTN_UP = 9
BTN_PRESS = 10

button_pins = [
    digitalio.DigitalInOut(board.GP3),
    digitalio.DigitalInOut(board.GP4),
    digitalio.DigitalInOut(board.GP5),
    digitalio.DigitalInOut(board.GP6),
    digitalio.DigitalInOut(board.GP7),
    digitalio.DigitalInOut(board.GP8),
    digitalio.DigitalInOut(board.GP9),
    digitalio.DigitalInOut(board.GP10),
    digitalio.DigitalInOut(board.GP11),
    digitalio.DigitalInOut(board.GP12),
    digitalio.DigitalInOut(board.GP13)
]

buttons = [None] * 11
for i in range(0, 11):
    button_pins[i].direction = digitalio.Direction.INPUT
    button_pins[i].pull = digitalio.Pull.DOWN
    buttons[i] = adafruit_debouncer.Debouncer(button_pins[i])

keyboard = Keyboard(usb_hid.devices)

def get_key(button):
    if button == BTN_A:
        key = Keycode.F12
    elif button == BTN_B:
        key = Keycode.F1
    elif button == BTN_C:
        key = Keycode.ENTER
    elif button == BTN_D:
        key = Keycode.ONE
    elif button == BTN_E:
        key = Keycode.A
    elif button == BTN_F:
        key = Keycode.SPACEBAR
    elif button == BTN_DOWN:
        key = Keycode.DOWN_ARROW
    elif button == BTN_LEFT:
        key = Keycode.LEFT_ARROW
    elif button == BTN_RIGHT:
        key = Keycode.RIGHT_ARROW
    elif button == BTN_UP:
        key = Keycode.UP_ARROW
    elif button == BTN_PRESS:
        key = Keycode.X
    else:
        key = Keycode.ESCAPE
    return key

while True:
    for i in range(0, 11):
        buttons[i].update()
        if buttons[i].rose:
            key = get_key(i)
            keyboard.press(key)
        if buttons[i].fell:
            key = get_key(i)
            keyboard.release(key)