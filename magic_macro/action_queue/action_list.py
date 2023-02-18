from magic_macro.action_queue.queue_elem import *
from magic_macro.config import DEFAULT_ACTION_DELAY_MS

MS_TO_NS = 1000000


class ActionList:
    _actions: list[QueueElem] = None
    _offset: int = None
    _delay: int = None

    def __init__(self, delay_ms=DEFAULT_ACTION_DELAY_MS):
        self._delay = delay_ms
        self._actions = []
        self._offset = 0

    def __increment_offset(self, delay_ms: int) -> None:
        self._offset += (delay_ms * MS_TO_NS)

    def write_string(self, string: str) -> None:
        action_to_add = WriteStringAction()
        action_to_add.timestamp = self._offset
        action_to_add.text = string

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def keycode_press(self, keycode) -> None:
        action_to_add = WriteKeycode()
        action_to_add.timestamp = self._offset
        action_to_add.code = keycode

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def keycode_release(self, keycode) -> None:
        self.keycode_press(-keycode)

    def keycode_press_and_release(self, keycode) -> None:
        self.keycode_press(keycode)
        self.keycode_release(keycode)

    def wait(self, time_to_wait_ms: int) -> None:
        self.__increment_offset(time_to_wait_ms)

    def consumer_control_code_press(self, consumer_control_code):
        action_to_add = ConsumerControlCode()
        action_to_add.timestamp = self._offset
        action_to_add.code = consumer_control_code

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def consumer_control_code_release(self):
        self.consumer_control_code_press(-1)

    def consumer_control_code_press_and_release(self, consumer_control_code):
        self.consumer_control_code_press(consumer_control_code)
        self.consumer_control_code_release()

    def mouse_button_press(self, button):
        action_to_add = MouseButton()
        action_to_add.timestamp = self._offset
        action_to_add.code = button

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def mouse_button_release(self, button):
        self.mouse_button_press(-button)

    def mouse_button_press_and_release(self, button):
        self.mouse_button_press(button)
        self.mouse_button_release(button)

    def mouse_movement(self, x=0, y=0, wheel=0):
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

    def increase_display_brightness(self, amount):
        action_to_add = DisplayBrightnessIncrement()
        action_to_add.timestamp = self._offset
        action_to_add.brightness = amount

        self._actions.append(action_to_add)
        self.__increment_offset(self._delay)

    def increase_keyboard_brightness(self, amount):
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
