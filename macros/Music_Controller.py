from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode

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

action_fast_forward = [
    {
        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
        "value": ConsumerControlCode.FAST_FORWARD
    }
]

action_rewind = [
    {
        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
        "value": ConsumerControlCode.REWIND
    }
]

action_override_rotary_scroll = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            "cw": action_fast_forward,
            "acw": action_rewind
        }
    }
]

board = {
    "title": "MUSIC CONTROLS",
    "macros": [
        {
            "button": 0,
            "label": "PLAY",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                            "value": ConsumerControlCode.PLAY_PAUSE
                        }
                    ]
                }
            ],

        },
        {
            "button": 1,
            "label": "BACK",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                            "value": ConsumerControlCode.SCAN_PREVIOUS_TRACK
                        }
                    ]
                }
            ],
        },
        {
            "button": 2,
            "label": "NEXT",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                            "value": ConsumerControlCode.SCAN_NEXT_TRACK
                        }
                    ]
                }
            ],
        },
        {
            "button": 3,
            "label": "STOP",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                            "value": ConsumerControlCode.STOP
                        }
                    ]
                }
            ],
        },
        {
            "button": 4,
            "label": "REW",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                            "value": ConsumerControlCode.REWIND
                        }
                    ]
                }
            ],
        },
        {
            "button": 5,
            "label": "FF",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                            "value": ConsumerControlCode.FAST_FORWARD
                        }
                    ]
                }
            ],
        },
        {
            "button": 7,
            "label": "SCROLL",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": action_override_rotary_scroll
                }
            ],
        },
        {
            "button": 9,
            "label": "MUTE",
            "color": 0x0099FF,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "combination": [
                        {
                            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                            "value": ConsumerControlCode.MUTE
                        }
                    ]
                }
            ],
        },
        {
            "button": 11,
            "label": "VOL",
            "color": 0x0099FF,
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
