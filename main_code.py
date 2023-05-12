import time
# import os
# import displayio
# import terminalio
# from adafruit_display_shapes.rect import Rect
# from adafruit_display_text import label
# from adafruit_macropad import MacroPad

# from keyboard_layout_win_it import KeyboardLayout
# from keycode_win_it import Keycode

import time

RUN_TEST = False


def test_run():
    # Do test stuff

    from magic_macro.macro_pad.macro_pad import MagicMacroPad

    a = MagicMacroPad()

    a.main_loop()

    while True:
        time.sleep(1.0)


def main_run():
    # Do production stuff

    from magic_macro.macro_pad.macro_pad import MagicMacroPad

    controller = MagicMacroPad()

    controller.main_loop()


if RUN_TEST:
    test_run()
else:
    main_run()
