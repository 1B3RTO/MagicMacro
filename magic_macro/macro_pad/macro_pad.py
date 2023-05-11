from adafruit_macropad import MacroPad
import time

from magic_macro.config import KEYBOARD_LAYOUT, KEYCODE
from magic_macro.keyboard_handler.keyboard_handler import KeyboardHandler
from magic_macro.macro_board_handler.macro_board_handler import MacroBoardHandler
from magic_macro.action_queue.action_queue import ActionQueue


class MagicMacroPad(object):
    _instance = None
    _macropad = None

    _keyboard_handler: KeyboardHandler = None
    _action_queue: ActionQueue = None

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
        self._macro_board_handler = MacroBoardHandler(self._macropad)
        self._action_queue = ActionQueue(self._macropad)

    def __build_macropad(self):
        if KEYBOARD_LAYOUT is None or KEYCODE is None:
            macropad = self._macropad_library()
        else:
            macropad = self._macropad_library(
                layout_class=KEYBOARD_LAYOUT,
                keycode_class=KEYCODE,
            )

        macropad.display.auto_refresh = False
        macropad.pixels.auto_write = True

        self._macropad = macropad

    def main_loop(self):
        while True:
            timestamp = time.monotonic_ns()

            # Keyboard interaction update
            self._keyboard_handler.update_keyboard(timestamp, self._macropad)

            # Action queue update
            self._action_queue.check_queue(timestamp)

            # Update Board Color
            self._macro_board_handler.update_button_colors()
