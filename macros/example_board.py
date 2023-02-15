from magic_macro.action_queue.action_list import ActionList
from magic_macro.utils.enums import TriggerType, RepetitionType


def nice_meme():
    mega_action = ActionList()
    mega_action.play_tone(262)
    mega_action.wait(2000)
    mega_action.stop_tone()
    return mega_action


def increase_brightness():
    mega_action = ActionList()
    mega_action.increase_display_brightness(0.1)
    return mega_action


def decrease_brightness():
    mega_action = ActionList()
    mega_action.increase_display_brightness(-0.1)
    return mega_action


def decrease_k_brightness():
    mega_action = ActionList()
    mega_action.increase_keyboard_brightness(-0.01)
    return mega_action


def increase_k_brightness():
    mega_action = ActionList()
    mega_action.increase_keyboard_brightness(0.01)
    return mega_action


def rotary_encoder_display_brightness():
    mega_action = ActionList()
    mega_action.override_rotary_encoder(increase_brightness, decrease_brightness)
    return mega_action


def rotary_encoder_keyboard_brightness():
    mega_action = ActionList()
    mega_action.override_rotary_encoder(increase_k_brightness, decrease_k_brightness)
    return mega_action


def do_nothing() -> ActionList:
    mega_action = ActionList()
    return mega_action


board = {
    "title": "Example Board",
    "macros": [
        {
            "button": 0,
            "label": "BTN_0",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],

        },
        {
            "button": 1,
            "label": "BTN_1",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 2,
            "label": "BTN_2",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 3,
            "label": "BTN_3",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 4,
            "label": "BTN_4",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 5,
            "label": "BTN_5",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 6,
            "label": "BTN_6",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 7,
            "label": "BTN_7",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 8,
            "label": "BTN_8",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 9,
            "label": "BTN_9",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 10,
            "label": "BTN_10",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
        {
            "button": 11,
            "label": "BTN_11",
            "color": 0x0f0f0f,
            "actions": [
                {
                    "repetition_type": RepetitionType.ONE_TIME,
                    "trigger_type": TriggerType.ON_SHORT_PRESS,
                    "method": do_nothing
                }
            ],
        },
    ]
}
