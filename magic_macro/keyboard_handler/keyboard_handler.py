from magic_macro.keyboard_handler.single_key import SingleKey
from adafruit_macropad import MacroPad
from magic_macro.utils.enums import TriggerType
from magic_macro.utils.context import context


class KeyboardHandler:
    _encoder_position: int = None
    _all_keys: list[SingleKey] = None

    def __init__(self):
        # Buttons from 0-11
        # Button 12 is Rotary encoder PRESS
        # Button 13 is Rotary encoder ACW rotation
        # Button 14 is Rotary encoder CW rotation
        for i in range(15):
            self._all_keys.append(SingleKey(i, self.__event_callback))

    @staticmethod
    def __event_callback(caller_id, trigger_type, timestamp):
        context.emit(caller_id, trigger_type, timestamp)

    def update_keyboard(self, timestamp, macropad):
        rotary_btn_pressed, rotary_btn_released, encoder_position, encoder_delta, btn_event = \
            self.__get_button_state(macropad)

        # Updated rotary encoder press
        if rotary_btn_pressed:
            self._all_keys[12].set_status(True, timestamp)
        elif rotary_btn_released:
            self._all_keys[12].set_status(False, timestamp)

        # Read encoder position
        if encoder_delta < 0:
            print("Rotary encoder Anticlockwise")
            self._all_keys[13].fire_button_event(timestamp, TriggerType.ON_SHORT_PRESS)
        elif encoder_delta > 0:
            print("Rotary encoder Clockwise")
            self._all_keys[14].fire_button_event(timestamp, TriggerType.ON_SHORT_PRESS)

        # Check for new button presses
        if btn_event:
            key_number = btn_event.key_number
            self._all_keys[key_number].set_status(btn_event.pressed, timestamp)

        # Update all the statuses of all the buttons
        for single_key in self._all_keys:
            single_key.check_status(timestamp)

    def __get_button_state(self, macropad: MacroPad) -> (bool, bool, int, int, object):
        # Read encoder position. If it's changed, switch apps.
        encoder_position = macropad.encoder
        encoder_delta = encoder_position - self._encoder_position

        # Handle encoder button. (These flags are set only once per press and release)
        macropad.encoder_switch_debounced.update()
        rotary_btn_pressed = macropad.encoder_switch_debounced.pressed
        rotary_btn_released = macropad.encoder_switch_debounced.released

        # Update self state
        self._encoder_position = encoder_position

        # Get other button events
        btn_event = macropad.keys.events.get()

        # Return group
        # (rotary_button_pressed, rotary_button_released, encoder_position, position_delta, button_event)
        return rotary_btn_pressed, rotary_btn_released, encoder_position, encoder_delta, btn_event
