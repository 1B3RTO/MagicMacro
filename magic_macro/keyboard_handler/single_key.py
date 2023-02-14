from magic_macro.utils.enums import TriggerType
from magic_macro.config import LONG_DELAY_MS

_MS_TO_NS = 1000000
_LONG_DELAY = LONG_DELAY_MS * _MS_TO_NS
_HALF_DELAY = int(_LONG_DELAY / 2)


class SingleKey:
    _id = None
    _status = None
    _is_long_press = None
    _timestamp = None

    def __init__(self, single_key_id, event_callback):
        self._id = single_key_id
        self._status = False
        self._is_long_press = False
        self._timestamp = 0
        self._event_callback = event_callback

    def fire_button_event(self, timestamp, trigger_type):
        if trigger_type == TriggerType.ON_INITIAL_PRESS:
            self.__on_first_press(timestamp)
        elif trigger_type == TriggerType.ON_SHORT_PRESS:
            self.__on_short_press(timestamp)
        elif trigger_type == TriggerType.ON_LONG_PRESS:
            self.__on_long_press(timestamp)

    def set_status(self, status, timestamp):
        self._status = status
        if status:
            self._is_long_press = False
            self.__on_first_press(timestamp)
        elif timestamp - self._timestamp < _LONG_DELAY and not self._is_long_press:
            self.__on_short_press(timestamp)
        if not status:
            self.__on_release(timestamp)
        self._timestamp = timestamp

    def check_status(self, timestamp):
        delta = timestamp - self._timestamp
        if self._status and delta >= _LONG_DELAY:
            self._is_long_press = True
            self._timestamp = timestamp - _HALF_DELAY
            self.__on_long_press(timestamp)

    def get_status(self):
        return self._status

    def __on_first_press(self, timestamp):
        trigger_type = TriggerType.ON_INITIAL_PRESS
        print(f"First press of {self._id}")
        self._event_callback(self._id, trigger_type, timestamp)

    def __on_short_press(self, timestamp):
        trigger_type = TriggerType.ON_SHORT_PRESS
        print(f"Short press of {self._id}")
        self._event_callback(self._id, trigger_type, timestamp)

    def __on_long_press(self, timestamp):
        trigger_type = TriggerType.ON_LONG_PRESS
        print(f"Long press of {self._id}")
        self._event_callback(self._id, trigger_type, timestamp)

    def __on_release(self, timestamp):
        trigger_type = TriggerType.NO_PRESS
        print(f"Release of {self._id}")
        self._event_callback(self._id, trigger_type, timestamp)
