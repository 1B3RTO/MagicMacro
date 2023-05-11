from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.keycode import Keycode

action_tone = [
    {
        "action_type": AtomicActionType.TONE,
        "value": {
            "tone": 100,
            "duration_ms": 500
        }
    },
    {
        "action_type": AtomicActionType.TONE,
        "value": {
            "tone": 200,
            "duration_ms": 500
        }
    },
    {
        "action_type": AtomicActionType.TONE,
        "value": {
            "tone": 300,
            "duration_ms": 500
        }
    },
    {
        "action_type": AtomicActionType.TONE,
        "value": {
            "tone": 200,
            "duration_ms": 500
        }
    },
    {
        "action_type": AtomicActionType.TONE,
        "value": {
            "tone": 100,
            "duration_ms": 500
        }
    },
]

board = {
    "title": "REPETITIONS",
    "macros": [
        {
            "button": 0,
            "label": "TONE_KP",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.KEEP_PRESSED,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": action_tone
                }
            ],

        },
        {
            "button": 2,
            "label": "TONE_UN",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.UNTIL_NEXT_PRESS,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": action_tone
                }
            ],

        },
        {
            "button": 3,
            "label": "A",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": [{
                        "action_type": AtomicActionType.WRITE_KEYCODE,
                        "value": Keycode.A
                    }]
                },
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.NO_PRESS,
                    "combination": [{
                        "action_type": AtomicActionType.WRITE_KEYCODE,
                        "value": -Keycode.A
                    }]
                }
            ],

        },
        {
            "button": 4,
            "label": "TASKS",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.WRITE_KEYCODE,
                            "value": Keycode.WINDOWS
                        },
                        {
                            "action_type": AtomicActionType.WRITE_KEYCODE,
                            "value": Keycode.TAB
                        },
                        {
                            "action_type": AtomicActionType.WRITE_KEYCODE,
                            "value": - Keycode.WINDOWS
                        },
                        {
                            "action_type": AtomicActionType.WRITE_KEYCODE,
                            "value": - Keycode.TAB
                        }
                    ]
                }
            ],

        }
    ]
}
