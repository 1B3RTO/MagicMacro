from adafruit_macropad import MacroPad

from magic_macro.action_queue.queue_elem import *
from magic_macro.utils.enums import Topics
from magic_macro.utils.context import context


class MacroExecutor:
    @staticmethod
    def exec(macropad: MacroPad, atomic_action: QueueElem):
        print(f"Running action: {type(atomic_action)}")

        if isinstance(atomic_action, WriteStringAction):
            macropad.keyboard_layout.write(atomic_action.text)

        elif isinstance(atomic_action, WriteKeycode):
            if atomic_action.code >= 0:
                macropad.keyboard.press(atomic_action.code)
            else:
                macropad.keyboard.release(-atomic_action.code)

        elif isinstance(atomic_action, ConsumerControlCode):
            if atomic_action.code > 0:
                macropad.consumer_control.press(atomic_action.code)
            else:
                macropad.consumer_control.release()

        elif isinstance(atomic_action, MouseButton):
            if atomic_action.code >= 0:
                macropad.mouse.press(atomic_action.code)
            else:
                macropad.mouse.release(-atomic_action.code)

        elif isinstance(atomic_action, MouseMovement):
            macropad.mouse.move(atomic_action.x, atomic_action.y, atomic_action.wheel)

        elif isinstance(atomic_action, Tone):
            macropad.stop_tone()
            if atomic_action.tone > 0:
                macropad.start_tone(atomic_action.tone)

        elif isinstance(atomic_action, DisplayBrightnessIncrement):
            new_brightness = atomic_action.brightness + macropad.display.brightness
            macropad.display.brightness = max(min(new_brightness, 1.0), 0.0)

        elif isinstance(atomic_action, DisplayBrightness):
            new_brightness = atomic_action.brightness
            macropad.pixels.brightness = max(min(new_brightness, 1.0), 0.0)

        elif isinstance(atomic_action, KeyboardBrightnessIncrement):
            new_brightness = atomic_action.brightness + macropad.pixels.brightness
            macropad.pixels.brightness = max(min(new_brightness, 1.0), 0.0)

        elif isinstance(atomic_action, KeyboardBrightness):
            new_brightness = atomic_action.brightness
            macropad.pixels.brightness = max(min(new_brightness, 1.0), 0.0)

        elif isinstance(atomic_action, MacroEnd):
            context.emit(Topics.MACRO_END, atomic_action.action_id)

        elif isinstance(atomic_action, OverrideRotaryEncoder):
            context.emit(Topics.OVERRIDE_ROTARY,
                         atomic_action.action_id,
                         atomic_action.acw_method,
                         atomic_action.cw_method)

        elif isinstance(atomic_action, MacroStart):
            context.emit(Topics.MACRO_START, atomic_action.action_id)
