from adafruit_macropad import MacroPad
import time

from magic_macro.config import KEYBOARD_LAYOUT, KEYCODE
from magic_macro.keyboard_handler.keyboard_handler import KeyboardHandler


class MagicMacroPad(object):
    _instance = None
    _macropad = None

    _keyboard_handler: KeyboardHandler = None

    def __new__(cls, *args):
        if cls._instance is None:
            cls._instance = super(MagicMacroPad, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, macropad_library=MacroPad):
        if self._initialized:
            return
        self._macropad_library = macropad_library
        self.__build_macropad()
        self._keyboard_handler = KeyboardHandler()

    def __build_macropad(self):
        if KEYBOARD_LAYOUT is None or KEYCODE is None:
            macropad = self._macropad_library()
        else:
            macropad = self._macropad_library(
                layout_class=KEYBOARD_LAYOUT,
                keycode_class=KEYCODE,
            )

        macropad.display.auto_refresh = False
        macropad.pixels.auto_write = False

        self._macropad = macropad

    def main_loop(self):
        while True:
            timestamp = time.monotonic_ns()

            # Keyboard interaction update
            self._keyboard_handler.update_keyboard(timestamp, self._macropad)

            # Action queue update
            # TODO: Check here the action queue
