from magic_macro.action_queue.queue_elem import *
from magic_macro.config import DEFAULT_ACTION_DELAY_MS

from magic_macro.utils.enums import AtomicActionType

MS_TO_NS = 1000000


class ActionList:
    _actions: list[QueueElem] = None
    _offset: int = None
    _delay: int = None
    _parsers: dict = None

    def get_actions(self):
        return self._actions

    def __init__(self, delay_ms=DEFAULT_ACTION_DELAY_MS):
        self._delay = delay_ms
        self._actions = []
        self._offset = 0
        self._is_rotary_action = False

        self._parsers = {
            AtomicActionType.WRITE_STRING: self.write_string,
            AtomicActionType.KEYCODE: self.keycode_press,
            AtomicActionType.DELAY: self.wait,
            AtomicActionType.CONSUMER_CONTROL_CODE: self.consumer_control_code_press,
            AtomicActionType.MOUSE_BUTTON: self.mouse_button_press,
            AtomicActionType.MOUSE_MOVEMENT: self.mouse_movement,
            AtomicActionType.TONE: self.play_tone,
            AtomicActionType.OVERRIDE_ROTARY: self.override_rotary_encoder,
            AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS: self.increase_display_brightness,
            AtomicActionType.INCREMENT_KEYBOARD_BRIGHTNESS: self.increase_keyboard_brightness,
            AtomicActionType.OVERRIDE_DEFAULT_DELAY: self.override_default_delay,
            AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE: self.consumer_control_code_press_and_release,
            AtomicActionType.PRESS_AND_RELEASE_KEYCODE: self.keycode_press_and_release,
            AtomicActionType.PRESS_AND_RELEASE_MOUSE_BUTTON: self.mouse_button_press_and_release,
            AtomicActionType.PLAY_AND_STOP_TONE: self.play_and_stop_tone,
            # AtomicActionType.SET_DISPLAY_BRIGHTNESS: None,
            # AtomicActionType.KEYBOARD_BRIGHTNESS: None,
            # AtomicActionType.MACRO_END: None,
            # AtomicActionType.MACRO_START: None,
        }

    """
    EXAMPLES = [
        {
            "action_type": AtomicActionType.WRITE_STRING,
            "value": "text to write"
        },
        {
            "action_type": AtomicActionType.KEYCODE,
            "value": Keycode.ESCAPE
        },
        {
            "action_type": AtomicActionType.PRESS_AND_RELEASE_KEYCODE,
            "value": Keycode.ESCAPE
        },
        {
            "action_type": AtomicActionType.DELAY,
            "value": 100
        },
        {
            "action_type": AtomicActionType.CONSUMER_CONTROL_CODE,
            "value": ConsumerControlCode.MUTE
        },
        {
            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
            "value": ConsumerControlCode.MUTE
        },
        {
            "action_type": AtomicActionType.MOUSE_BUTTON,
            "value": Mouse.WHEEL
        },
        {
            "action_type": AtomicActionType.PRESS_AND_RELEASE_MOUSE_BUTTON,
            "value": Mouse.WHEEL
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
            "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
            "value": {
                "tone": 200,
                "duration_ms": 1000
            }
        },
        {
            "action_type": AtomicActionType.TONE,
            "value": 100
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
    """

    def import_actions(self, list_of_actions: list, is_rotary_action: bool = False):
        for action in list_of_actions:
            action_type = action.get("action_type")
            value = action.get("value")

            self._parsers[action_type](value)

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

    def mouse_movement(self, dictionary):
        assert isinstance(dictionary, dict)

        x = dictionary['x'] if 'x' in dictionary else 0
        y = dictionary['y'] if 'y' in dictionary else 0
        wheel = dictionary['wheel'] if 'wheel' in dictionary else 0

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

    def play_and_stop_tone(self, dictionary):
        assert isinstance(dictionary, dict)

        tone = dictionary['tone'] if 'tone' in dictionary else 0
        duration_ms = dictionary['duration_ms'] if 'duration_ms' in dictionary else 0

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

    def override_rotary_encoder(self, dictionary):
        if self._is_rotary_action:
            return
        assert isinstance(dictionary, dict)

        action_to_exec_cw = dictionary["cw"] if "cw" in dictionary else list()
        action_to_exec_acw = dictionary["acw"] if "acw" in dictionary else list()

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
