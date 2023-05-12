# MagicMacro

This is an improved version of the [Macropad Hotkeys](https://learn.adafruit.com/macropad-hotkeys/project-code) example
from the Adafruit Learning System Guide. It is deeply inspired by the original version and aims to be helpful.

## Requirements

- The Adafruit Macropad RP2040 with CircuitPython 8.0.5 is required for this project, but it may work with other
  versions as well.

## Differences with the original

While the boards themselves may look similar, there are significant differences in both the board selection phase and
macro management. In this version:

- A menu is available for board selection.
- Every button can trigger one of four different press types:
    1. Initial press: the button is pressed regardless of duration.
    2. Short press: a press shorter than 500ms (configurable).
    3. Long press: a press longer than 500ms (configurable).
    4. Button release: every time the button is released.
- Once a macro board is selected, the behavior of the rotary encoder can be modified, with an action assigned to both
  clockwise and counterclockwise rotations.
- Repeat modes allow for a button to trigger a one-shot action, an action that is kept repeating as long as the button
  is pressed, and an action that is repeated unless the button is pressed again.
- The keyboard and display brightness can be modified.
- Multiple actions can run concurrently (*with the possibility of conflicts between them*).

## Set it up

To use this version, simply copy and paste the `magic_macro` and `macros` folders into the root folder of your Macropad.
Additionally, the `main_code.py` file must be copied into the root folder and renamed to `code.py`, just like in the
original version.

The included macros are only for reference and can be used as a starting point when creating your own customized macros.

## Create your own macros

1. Create a new `.py` file under the macro folder: `macros/incredible_macroboard.py`
2. The macro itself has to be saved inside a variable named: `board`

```python
board = {
    "title": "REALLY NICE.",
    "macros": []
}
```

3. Now let's add a button:

```python
from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode

board = {
    "title": "REALLY NICE.",
    "macros": [
        {
            # The top left button is the number 0, the bottom right one is the number 11.
            # The only button usable are between 0 and 11.
            "button": 1,

            # This is the label that is shown for this button
            "label": "DISPLAY",

            # This is the color in hexadecimal that is used for button
            "color": 0x0099FF,

            # This is an array that can contain at most one action per trigger type
            "actions": [],
        },
    ]
}
```

4. Let's define our first action:

```python
from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

action = {
    # Set the repeat type
    "repetition_type": RepetitionType.ONE_TIME,

    # Set the trigger type
    "trigger_type": TriggerType.ON_SHORT_PRESS,

    # Add an array of atomic actions defined as follows
    "combination": [
        # Every object inside this array is an atomic action
        {
            # This first atomic action presses and releases the shift button
            "action_type": AtomicActionType.PRESS_AND_RELEASE_KEYCODE,
            "value": Keycode.SHIFT
        },
        # The delay between these two actions is set to a default value (10ms)
        # but it can be modified by using a single AtomicActionType.OVERRIDE_DEFAULT_DELAY atomic action
        {
            # This second atomic action presses and releases the mute button
            "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
            "value": ConsumerControlCode.MUTE
        }
    ]
}

# N.B:  Each action requires a specific object.
#  (inside the Examples folder there is an example for each and every single atomic action)
```

5. Put everything together and we are done:

```python
from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode

board = {
    "title": "REALLY NICE.",
    "macros": [
        {
            "button": 1,
            "label": "DISPLAY",
            "color": 0x0099FF,
            "actions": {
                "repetition_type": RepetitionType.ONE_TIME,
                "trigger_type": TriggerType.ON_SHORT_PRESS,
                "combination": [
                    {
                        "action_type": AtomicActionType.PRESS_AND_RELEASE_KEYCODE,
                        "value": Keycode.SHIFT
                    },
                    {
                        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
                        "value": ConsumerControlCode.MUTE
                    }
                ]
            },
        },
    ]
}
```

### Deeper dive into the atomic actions

#### Consumer Control code:

The **ConsumerControlCode**s are `int` values and are used to express the following controls:

```python
BRIGHTNESS_DECREMENT = 112
VOLUME_DECREMENT = 234
MUTE = 226
EJECT = 184
RECORD = 178
SCAN_NEXT_TRACK = 181
FAST_FORWARD = 179
PLAY_PAUSE = 205
STOP = 183
REWIND = 180
VOLUME_INCREMENT = 233
SCAN_PREVIOUS_TRACK = 182
BRIGHTNESS_INCREMENT = 111
```

You can both use them vanilla (through their int value) or you can import the `ConsumerControlCode` Class and then call
the right one:

```python
from adafruit_hid.consumer_control_code import ConsumerControlCode

value = ConsumerControlCode.MUTE
```

To send such a command you can use two approaches: `press and release` or `press`/`release`.

```python
from magic_macro.utils.enums import AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode

# Use the positive value of MUTE to press
press_combination = [
    {
        "action_type": AtomicActionType.CONSUMER_CONTROL_CODE,
        "value": ConsumerControlCode.MUTE
    },
]

# Use the negative value of MUTE to release
release_combination = [
    {
        "action_type": AtomicActionType.CONSUMER_CONTROL_CODE,
        "value": - ConsumerControlCode.MUTE
    },
]

# Change the action type to PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE
press_and_release_combination = [
    {
        "action_type": AtomicActionType.PRESS_AND_RELEASE_CONSUMER_CONTROL_CODE,
        "value": ConsumerControlCode.MUTE
    },
]
```

If you decide to go through the `press`/`release` route **REMEMBER** to always release a pressed button! The reason why
there is no automatic feature to autonomously release a pressed button is because there are some use cases that could be
limited by such a feature.

#### Key Code

The **KeyCode**s are `int` values and are used to express the following controls:

```python
A = 4
...
Z = 29
ONE = 30
TWO = 31
THREE = 32
FOUR = 33
FIVE = 34
SIX = 35
SEVEN = 36
EIGHT = 37
NINE = 38
ZERO = 39
ENTER = 40
ESCAPE = 41
BACKSPACE = 42
TAB = 43
SPACEBAR = 44
MINUS = 45
EQUALS = 46
LEFT_BRACKET = 47
RIGHT_BRACKET = 48
BACKSLASH = 49
POUND = 50
SEMICOLON = 51
QUOTE = 52
GRAVE_ACCENT = 53
COMMA = 54
PERIOD = 55
FORWARD_SLASH = 56
CAPS_LOCK = 57
F1 = 58
...
F12 = 69
PRINT_SCREEN = 70
SCROLL_LOCK = 71
PAUSE = 72
INSERT = 73
HOME = 74
PAGE_UP = 75
DELETE = 76
END = 77
PAGE_DOWN = 78
RIGHT_ARROW = 79
LEFT_ARROW = 80
DOWN_ARROW = 81
UP_ARROW = 82
KEYPAD_NUMLOCK = 83
KEYPAD_FORWARD_SLASH = 84
KEYPAD_ASTERISK = 85
KEYPAD_MINUS = 86
KEYPAD_PLUS = 87
KEYPAD_ENTER = 88
KEYPAD_ONE = 89
KEYPAD_TWO = 90
KEYPAD_THREE = 91
KEYPAD_FOUR = 92
KEYPAD_FIVE = 93
KEYPAD_SIX = 94
KEYPAD_SEVEN = 95
KEYPAD_EIGHT = 96
KEYPAD_NINE = 97
KEYPAD_ZERO = 98
KEYPAD_PERIOD = 99
KEYPAD_BACKSLASH = 100
APPLICATION = 101
POWER = 102
KEYPAD_EQUALS = 103
F13 = 104
...
F24 = 115
LEFT_CONTROL = 224
LEFT_SHIFT = 225
ALT = 226
LEFT_GUI = 227
RIGHT_CONTROL = 228
RIGHT_SHIFT = 229
RIGHT_ALT = 230
RIGHT_GUI = 231
```

As for the Consumer Control Codes you can both `press and release` or `press`/`release`.

You can both use them vanilla (through their int value) or you can import the Keycode Class and then call the right one:

```python
from adafruit_hid.keycode import Keycode

value = Keycode.F4
```

To send a **_press and release_** command just use the action type `AtomicActionType.PRESS_AND_RELEASE_KEYCODE`,
otherwise `AtomicActionType.KEYCODE`. As for the Consumer control codes, REMEMBER TO RELEASE al the pressed
buttons!

#### Mouse Buttons

As for the Keycode and the ConsumerControlCode, the Mouse buttons are `int` values and are used to express the following
controls:

```python
LEFT_BUTTON = 1
RIGHT_BUTTON = 2
MIDDLE_BUTTON = 4
```

As for the ConsumerControlCodes and the Keycode you can both `press and release` or `press`/`release`.

You can both use them vanilla (through their int value) or you can import the Mouse Class and then call the right one:

```python
from adafruit_hid.mouse import Mouse

value = Mouse.LEFT_BUTTON
```

To send a _**press and release**_ command just use the action type `AtomicActionType.PRESS_AND_RELEASE_MOUSE_BUTTON`,
otherwise `AtomicActionType.MOUSE_BUTTON`. As for the Consumer control codes and the Key codes, REMEMBER TO RELEASE al
the pressed buttons!

#### Mouse Movements

To define a combination for the mouse movement there are three attributes to set:

- x
- y
- wheel

The atomic action type is `MOUSE_MOVEMENT` and it is composed as follows:

```python
from magic_macro.utils.enums import AtomicActionType

combination_mouse_movement = [
    {
        "action_type": AtomicActionType.MOUSE_MOVEMENT,
        "value": {
            "x": 0,
            "y": 0,
            "wheel": 0
        }
    }
]
```

#### String writings

A string can be written by using an endless sequence of Key code presses OR through a `WRITE_STRING` atomic action.

```python
from magic_macro.utils.enums import AtomicActionType

combination_write_string = [
    {
        "action_type": AtomicActionType.WRITE_STRING,
        "value": "super nice text to write"
    },
]
```

#### TONE

The Macropad is also capable of emitting sounds. To use them you have two options:

- `PLAY_AND_STOP_TONE`: define a duration in ms and an int tone to play
- `TONE`: Start or Stop playing a sound (positive or negative int tone)

```python
from magic_macro.utils.enums import AtomicActionType

combination_play_and_stop_tone = [
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 300,
            "duration_ms": 1000
        }
    },
]

combination_play_tone = [
    {
        "action_type": AtomicActionType.TONE,
        "value": 300
    },
]

combination_stop_tone = [
    {
        "action_type": AtomicActionType.TONE,
        "value": -300
    },
]
```

#### Increment or Decrement Display/Keyboard brightness

The increment/decrement is expressed as a float value in the range 0.0 - 1.0.

```python
from magic_macro.utils.enums import AtomicActionType

combination_increment_keyboard_brightness = [
    {
        "action_type": AtomicActionType.INCREMENT_KEYBOARD_BRIGHTNESS,
        "value": 0.2
    },
]

combination_decrement_display_brightness = [
    {
        "action_type": AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS,
        "value": - 0.1
    },
]
```

#### Delay

Each sequence of combination introduces between each atomic action a delay which defaults to 10ms. You can both override
this default value (this action is not retroactive, hence it overrides the default delay between all the following
atomic actions in that sequence) or just introduce a one time delay.

```python
from magic_macro.utils.enums import AtomicActionType

combination_override_default_delay = [
    {
        "action_type": AtomicActionType.OVERRIDE_DEFAULT_DELAY,
        "value": 100
    },
]

combination_one_time_delay = [
    {
        "action_type": AtomicActionType.DELAY,
        "value": 1000
    },
]
```

#### Override Rotary Behavior

Once you're inside a macro board, the rotary encoder sits there doing nothing. With this kind of atomic actions you can
define what to do on a clockwise or anticlockwise rotation.

In the following example, every time we rotate clockwise we want to play a sound and send a consumer control code to
increment the volume, in the anticlockwise case we instead want to play a different tone and decrement the volume.

```python
from magic_macro.utils.enums import AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode

combination = [
    {
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            # For both `cw` and `acw` it's needed to define only a new combination.
            # N.B: no inception allowed here. You can't define a sub-combination which overrides again the encoder.
            "cw": [
                {
                    "action_type": AtomicActionType.CONSUMER_CONTROL_CODE,
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
                    "action_type": AtomicActionType.CONSUMER_CONTROL_CODE,
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
```

#### Multiple actions same combination

To use multiple atomic action inside a combination you just need to append all the subsequent atomic actions to the
combination list:

```python
from magic_macro.utils.enums import AtomicActionType

# Play only one tone
combination_one_thing = [
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 300,
            "duration_ms": 1000
        }
    },
]

# Play two tones and increment the display brightness:
combination_more_things = [
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 300,
            "duration_ms": 1000
        }
    },
    {
        "action_type": AtomicActionType.PLAY_AND_STOP_TONE,
        "value": {
            "tone": 400,
            "duration_ms": 1000
        }
    },
    {
        "action_type": AtomicActionType.INCREMENT_DISPLAY_BRIGHTNESS,
        "value": 0.4
    },
]


```

## Tests

Writing tests makes sure that the code is reliable, right? Yep, but there was no time to do so...