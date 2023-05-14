from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode

action_write_string = [
    {
        "action_type": AtomicActionType.WRITE_STRING,
        "value": "text to write"
    },
]

action_write_keycode = [
    {
        "action_type": AtomicActionType.KEYCODE,
        "value": 12
    }
]

action_delay = [
    {
        "action_type": AtomicActionType.DELAY,
        "value": 1000
    }
]

action_consumer_control_code = [
    {
        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
        "value": 3
    }
]

action_mouse_button = [
    {
        "action_type": AtomicActionType.MOUSE_BUTTON,
        "value": 3
    }
]

action_mouse_movement = [
    {
        "action_type": AtomicActionType.MOUSE_MOVEMENT,
        "value": {
            "x": 0,
            "y": 0,
            "wheel": 0
        }
    }
]

action_tone = [
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 100,
            "duration_ms": 1000
        }
    }
]

action_tone1 = [
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 200,
            "duration_ms": 1000
        }
    }
]

action_tone2 = [
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 300,
            "duration_ms": 1000
        }
    }
]

action_override_rotary = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": action_tone,
            "acw": action_tone
        }
    }
]

action_increment_brightness = [
    {
        "action_type": AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS,
        "value": 0.05
    }
]

action_decrement_brightness = [
    {
        "action_type": AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS,
        "value": -0.05
    }
]

action_override_rotary_display = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": action_increment_brightness,
            "acw": action_decrement_brightness
        }
    }
]

action_decrement_keyboard = [
    {
        "action_type": AtomicActionType.INCREMENT_KEYBOARD_BRIGHTNESS,
        "value": -0.05
    }
]

action_increment_keyboard = [
    {
        "action_type": AtomicActionType.INCREMENT_KEYBOARD_BRIGHTNESS,
        "value": 0.05
    }
]

action_override_rotary_keyboard = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": action_increment_keyboard,
            "acw": action_decrement_keyboard
        }
    }
]

action_vol_up = [
    {
        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
        "value": ConsumerControlCode.VOLUME_INCREMENT
    }
]

action_vol_down = [
    {
        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
        "value": ConsumerControlCode.VOLUME_DECREMENT
    }
]

action_override_rotary_volume = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": action_vol_up,
            "acw": action_vol_down
        }
    }
]

action_increment_override_delay = [
    {
        "action_type": AtomicActionType.OVERRIDE_DEFAULT_DELAY,
        "value": 1000
    },
    action_tone[0],
    action_tone[0],
]

action_example = [
    {
        "action_type": AtomicActionType.WRITE_STRING,
        "value": "text to write"
    },
    {
        "action_type": AtomicActionType.KEYCODE,
        "value": 12
    },
    {
        "action_type": AtomicActionType.DELAY,
        "value": 100
    },
    {
        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
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
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 19,
            "duration_ms": 1000
        }
    },
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": action_tone,
            "acw": action_tone
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

do_nothing = []

board = {
    "title": "Example Board v2",
    "macros": [
        {
            "button": 0,
            "label": "Str",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_write_string
                }
            ],

        },
        {
            "button": 1,
            "label": "kc",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_write_keycode
                }
            ],
        },
        {
            "button": 2,
            "label": "del",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_delay
                }
            ],
        },
        {
            "button": 3,
            "label": "ccc",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_consumer_control_code
                }
            ],
        },
        {
            "button": 4,
            "label": "mb",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_mouse_button
                }
            ],
        },
        {
            "button": 5,
            "label": "mm",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_mouse_movement
                }
            ],
        },
        {
            "button": 6,
            "label": "tone",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_tone
                },
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_LONG_PRESS,
                    "combination": action_tone1
                },
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": action_tone2
                }
            ],
        },
        {
            "button": 7,
            "label": "db",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_override_rotary_display
                }
            ],
        },
        {
            "button": 8,
            "label": "kb",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_override_rotary_keyboard
                }
            ],
        },
        {
            "button": 9,
            "label": "od",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_increment_override_delay
                }
            ],
        },
        {
            "button": 10,
            "label": "or",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_override_rotary
                }
            ],
        },
        {
            "button": 11,
            "label": "VOL",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_override_rotary_volume
                }
            ],
        },
    ]
}
