class QueueElem:
    action_id: int = None
    timestamp: int = None

    def __copy__(self):
        obj = type(self).__new__(self.__class__)
        for key, value in self.__dict__.items():
            setattr(obj, key, value)
        return obj

    def __new__(cls):
        instance = super().__new__(cls)
        return instance


class WriteStringAction(QueueElem):
    text: str = None


class WriteKeycode(QueueElem):
    code: int = None


class ConsumerControlCode(QueueElem):
    code: int = None


class MouseButton(QueueElem):
    code: int = None


class MouseMovement(QueueElem):
    x: int = None
    y: int = None
    wheel: int = None


class Tone(QueueElem):
    tone: int = None


class DisplayBrightness(QueueElem):
    brightness: float = None


class DisplayBrightnessIncrement(DisplayBrightness):
    pass


class KeyboardBrightness(QueueElem):
    brightness: float = None


class KeyboardBrightnessIncrement(KeyboardBrightness):
    pass


class MacroEnd(QueueElem):
    pass


class MacroStart(QueueElem):
    pass


class OverrideRotaryEncoder(QueueElem):
    cw_method = None
    acw_method = None
