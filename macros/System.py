from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode

action_override_rotary_display = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": [
                {
                    "action_type": AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS,
                    "value": 0.05
                }
            ],
            "acw": [
                {
                    "action_type": AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS,
                    "value": -0.05
                }
            ]
        }
    }
]

action_override_rotary_keyboard = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": [
                {
                    "action_type": AtomicActionType.INCREMENT_KEYBOARD_BRIGHTNESS,
                    "value": 0.05
                }
            ],
            "acw": [
                {
                    "action_type": AtomicActionType.INCREMENT_KEYBOARD_BRIGHTNESS,
                    "value": -0.05
                }
            ]
        }
    }
]

action_override_rotary_volume = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": [
                {
                    "action_type": AtomicActionType.CONSUMER_CONTROL_CODE,
                    "value": ConsumerControlCode.VOLUME_INCREMENT
                }
            ],
            "acw": [
                {
                    "action_type": AtomicActionType.CONSUMER_CONTROL_CODE,
                    "value": ConsumerControlCode.VOLUME_DECREMENT
                }
            ]
        }
    }
]

board = {
    "title": "SYSTEM",
    "macros": [
        {
            "button": 1,
            "label": "DISPLAY",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_override_rotary_display
                }
            ],

        },
        {
            "button": 4,
            "label": "KEYBOARD",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_override_rotary_keyboard
                }
            ],
        },
        {
            "button": 7,
            "label": "VOLUME",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_override_rotary_volume
                }
            ],
        }
    ]
}
