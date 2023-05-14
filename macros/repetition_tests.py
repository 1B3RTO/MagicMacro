from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control_code import ConsumerControlCode

action_tone = [
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 100,
            "duration_ms": 500
        }
    },
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 200,
            "duration_ms": 500
        }
    },
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 300,
            "duration_ms": 500
        }
    },
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 200,
            "duration_ms": 500
        }
    },
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
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
            "color": 0xEB144C,
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
            "color": 0xEB144C,
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
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": [{
                        "action_type": AtomicActionType.KEYCODE,
                        "value": Keycode.A
                    }]
                },
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.NO_PRESS,
                    "combination": [{
                        "action_type": AtomicActionType.KEYCODE,
                        "value": -Keycode.A
                    }]
                }
            ],

        },
        {
            "button": 4,
            "label": "TASKS",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.KEYCODE,
                            "value": Keycode.WINDOWS
                        },
                        {
                            "action_type": AtomicActionType.KEYCODE,
                            "value": Keycode.TAB
                        },
                        {
                            "action_type": AtomicActionType.KEYCODE,
                            "value": - Keycode.WINDOWS
                        },
                        {
                            "action_type": AtomicActionType.KEYCODE,
                            "value": - Keycode.TAB
                        }
                    ]
                }
            ],

        },
        {
            "button": 5,
            "label": "VOLS",
            "color": 0xEB144C,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_INITIAL_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.OVERRIDE_ROTARY,
                            "value": {
                                "cw": [
                                    {
                                        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                                        "value": ConsumerControlCode.VOLUME_INCREMENT
                                    },
                                    {
                                        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
                                        "value": {
                                            "tone": 300,
                                            "duration_ms": 50
                                        }
                                    }
                                ],
                                "acw": [
                                    {
                                        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                                        "value": ConsumerControlCode.VOLUME_DECREMENT
                                    },
                                    {
                                        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
                                        "value": {
                                            "tone": 100,
                                            "duration_ms": 50
                                        }
                                    }
                                ]
                            }
                        }
                    ]
                }
            ],
        }
    ]
}
