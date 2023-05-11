from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

action_left_btn = [
    {
        "action_type": AtomicActionType.MOUSE_BUTTON,
        "value": Mouse.LEFT_BUTTON
    }
]

action_right_btn = [
    {
        "action_type": AtomicActionType.MOUSE_BUTTON,
        "value": Mouse.RIGHT_BUTTON
    }
]

action_middle_btn = [
    {
        "action_type": AtomicActionType.MOUSE_BUTTON,
        "value": Mouse.MIDDLE_BUTTON
    }
]

action_wheel_up = [
    {
        "action_type": AtomicActionType.MOUSE_MOVEMENT,
        "value": {
            "x": 0,
            "y": 0,
            "wheel": 1
        }
    }
]

action_wheel_down = [
    {
        "action_type": AtomicActionType.MOUSE_MOVEMENT,
        "value": {
            "x": 0,
            "y": 0,
            "wheel": -1
        }
    }
]

action_override_rotary_wheel = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "acw": action_wheel_up,
            "cw": action_wheel_down
        }
    }
]

board = {
    "title": "MUSIC CONTROLS",
    "macros": [
        {
            "button": 0,
            "label": "BTN_SX",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": action_left_btn
                }
            ],

        },
        {
            "button": 1,
            "label": "WHEEL",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_LONG_PRESS,
                    "combination": action_override_rotary_wheel
                },
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_middle_btn
                }
            ],
        },
        {
            "button": 2,
            "label": "BTN_RX",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_right_btn
                }
            ],
        }
    ]
}