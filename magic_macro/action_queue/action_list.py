from magic_macro.action_queue.queue_elem import *
from magic_macro.config import DEFAULT_ACTION_DELAY_MS

from magic_macro.utils.enums import AtomicActionType

MS_TO_NS = 1000000


class ActionList:
    _actions: list[QueueElem] = None
    _offset: int = None
    _delay: int = None

    def get_actions(self):
        return self._actions

    def __init__(self, delay_ms=DEFAULT_ACTION_DELAY_MS):
        self._delay = delay_ms
        self._actions = []
        self._offset = 0

    """
    do_nothing = [
        {
            "action_type": AtomicActionType.WRITE_STRING,
            "value": "text to write"
        },
        {
            "action_type": AtomicActionType.WRITE_KEYCODE,
            "value": 12
        },
        {
            "action_type": AtomicActionType.DELAY,
            "value": 100
        },
        {
            "action_type": AtomicActionType.CONSUMER_CONTROL_CODE,
            "value": 3
        },
        {
            "action_type": AtomicActionType.MOUSE_BUTTON,
            "value": 3
        },
        {
            "action_type": AtomicActionType.MOUSE_MOVEMENT,
            "value": {
                "x": 0,
                "y": 0,
                "wheel": 0
            }
        },
        {
            "action_type": AtomicActionType.TONE,
            "value": {
                "tone": 19,
                "duration_ms": 1000
            }
        },
        {
            "action_type": AtomicActionType.OVERRIDE_ROTARY,
            "value": {
                "cw": [{...}],
                "acw": [{...}]
            }
        },
        {
            "action_type": AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS,
            "value": 0.2
        },
        {
            "action_type": AtomicActionType.INCREMENT_KEYBOARD_BRIGHTNESS,
            "value": 0.2
        },
        {
            "action_type": AtomicActionType.OVERRIDE_DEFAULT_DELAY,
            "value": 100
        },
    ]
    
    WRITE_STRING = 1,
    WRITE_KEYCODE = 2,
    DELAY = 3,
    CONSUMER_CONTROL_CODE = 4,
    MOUSE_BUTTON = 5,
    MOUSE_MOVEMENT = 6,
    TONE = 7,
    OVERRIDE_ROTARY = 8,
    INCREMENT_DISPLAY_BRIGHTNESS = 10,
    INCREMENT_KEYBOARD_BRIGHTNESS = 14,
    OVERRIDE_DEFAULT_DELAY = 15
    
    SET_DISPLAY_BRIGHTNESS = 9,
    KEYBOARD_BRIGHTNESS = 11,
    MACRO_START = 13,
    MACRO_END = 12,
    
    """

    def import_actions(self, list_of_actions: list, is_rotary_action: bool = False):
        for action in list_of_actions:
            action_type = action.get("action_type")
            value = action.get("value")

            if action_type == AtomicActionType.WRITE_STRING:
                self.write_string(value)
            elif action_type == AtomicActionType.WRITE_KEYCODE:
                self.keycode_press_and_release(value)
            elif action_type == AtomicActionType.DELAY:
                self.wait(value)
            elif action_type == AtomicActionType.CONSUMER_CONTROL_CODE:
                self.consumer_control_code_press_and_release(value)
            elif action_type == AtomicActionType.MOUSE_BUTTON:
                self.mouse_button_press_and_release(value)
            elif action_type == AtomicActionType.MOUSE_MOVEMENT:
                self.mouse_movement(value.get("x"), value.get("y"), value.get("wheel"))
            elif action_type == AtomicActionType.TONE:
                self.play_and_stop_tone(tone=value.get("tone"), duration_ms=value.get("duration_ms"))
            elif action_type == AtomicActionType.OVERRIDE_ROTARY and not is_rotary_action:
                action_cw = value.get("cw")
                action_acw = value.get("acw")
                self.override_rotary_encoder(action_cw, action_acw)
            elif action_type == AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS:
                self.increase_display_brightness(value)
            elif action_type == AtomicActionType.INCREMENT_KEYBOARD_BRIGHTNESS:
                self.increase_keyboard_brightness(value)
            elif action_type == AtomicActionType.OVERRIDE_DEFAULT_DELAY:
                self.override_default_delay(value)

    def __increment_offset(self, delay_ms: int) -> None:
        self._offset += (delay_ms * MS_TO_NS)

    def override_default_delay(self, delay_ms: int = DEFAULT_ACTION_DELAY_MS):
        assert isinstance(delay_ms, int)
        self._delay = delay_ms

    def write_string(self, string: str) -> None:
        assert isinstance(string, str)

        action_to_add = WriteStringAction()
        action_to_add.timestamp = self._offset
        action_to_add.text = string

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def keycode_press(self, keycode: int) -> None:
        action_to_add = WriteKeycode()
        action_to_add.timestamp = self._offset
        action_to_add.code = keycode

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def keycode_release(self, keycode: int) -> None:
        self.keycode_press(-keycode)

    def keycode_press_and_release(self, keycode: int) -> None:
        assert isinstance(keycode, int)

        self.keycode_press(keycode)
        self.keycode_release(keycode)

    def wait(self, time_to_wait_ms: int) -> None:
        assert isinstance(time_to_wait_ms, int)

        self.__increment_offset(time_to_wait_ms)

    def consumer_control_code_press(self, consumer_control_code: int):
        action_to_add = ConsumerControlCode()
        action_to_add.timestamp = self._offset
        action_to_add.code = consumer_control_code

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def consumer_control_code_release(self):
        self.consumer_control_code_press(-1)

    def consumer_control_code_press_and_release(self, consumer_control_code: int):
        assert isinstance(consumer_control_code, int)

        self.consumer_control_code_press(consumer_control_code)
        self.consumer_control_code_release()

    def mouse_button_press(self, button: int):
        action_to_add = MouseButton()
        action_to_add.timestamp = self._offset
        action_to_add.code = button

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def mouse_button_release(self, button: int):
        self.mouse_button_press(-button)

    def mouse_button_press_and_release(self, button: int):
        assert isinstance(button, int)

        self.mouse_button_press(button)
        self.mouse_button_release(button)

    def mouse_movement(self, x=0, y=0, wheel=0):
        assert isinstance(x, int)
        assert isinstance(y, int)
        assert isinstance(wheel, int)

        action_to_add = MouseMovement()
        action_to_add.timestamp = self._offset
        action_to_add.x = x
        action_to_add.y = y
        action_to_add.wheel = wheel

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def play_tone(self, tone):
        action_to_add = Tone()
        action_to_add.timestamp = self._offset
        action_to_add.tone = tone

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def stop_tone(self):
        self.play_tone(-1)

    def play_and_stop_tone(self, tone, duration_ms):
        assert isinstance(tone, int)
        assert isinstance(duration_ms, int)

        self.play_tone(tone)
        self.wait(duration_ms)
        self.stop_tone()

    def increase_display_brightness(self, amount: float):
        assert isinstance(amount, float)

        action_to_add = DisplayBrightnessIncrement()
        action_to_add.timestamp = self._offset
        action_to_add.brightness = amount

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def increase_keyboard_brightness(self, amount: float):
        assert isinstance(amount, float)

        action_to_add = KeyboardBrightnessIncrement()
        action_to_add.timestamp = self._offset
        action_to_add.brightness = amount

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def override_rotary_encoder(self, action_to_exec_cw, action_to_exec_acw):
        action_to_add = OverrideRotaryEncoder()
        action_to_add.timestamp = self._offset
        action_to_add.cw_method = action_to_exec_cw
        action_to_add.acw_method = action_to_exec_acw

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def get_atomic_list(self, caller_id, timestamp):
        result = []

        end_mark = MacroEnd()
        end_mark.action_id = caller_id
        end_mark.timestamp = self._offset + timestamp

        for elem in self._actions:
            clone = elem.__copy__()
            clone.action_id = caller_id
            clone.timestamp += timestamp
            result.append(clone)

        result += [end_mark]

        return result
