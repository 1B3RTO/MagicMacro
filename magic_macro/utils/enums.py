class AtomicActionType:
    WRITE_STRING = 1
    WRITE_KEYCODE = 2
    DELAY = 3
    CONSUMER_CONTROL_CODE = 4
    MOUSE_BUTTON = 5
    MOUSE_MOVEMENT = 6
    TONE = 7
    OVERRIDE_ROTARY = 8
    SET_DISPLAY_BRIGHTNESS = 9
    INCREMENT_DISPLAY_BRIGHTNESS = 10
    KEYBOARD_BRIGHTNESS = 11
    MACRO_END = 12
    MACRO_START = 13
    INCREMENT_KEYBOARD_BRIGHTNESS = 14
    OVERRIDE_DEFAULT_DELAY = 15
    PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE = 16
    PRESS_AND_RELEASE_KEYCODE = 17
    PRESS_AND_RELEASE_MOUSE_BUTTON = 18


class RepetitionType:
    ONE_TIME = 0
    KEEP_PRESSED = 1
    UNTIL_NEXT_PRESS = 2


class TriggerType:
    NO_PRESS = 0
    ON_INITIAL_PRESS = 1
    ON_SHORT_PRESS = 2
    ON_LONG_PRESS = 3


class Topics:
    MACRO_END = 0
    MACRO_START = 1
    OVERRIDE_ROTARY = 2
    BUTTON_PRESS = 3
    ADD_TO_QUEUE = 4
