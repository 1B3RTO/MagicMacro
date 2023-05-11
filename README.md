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

5. Let's define also one action that overrides the rotary encoder:

```python
from magic_macro.utils.enums import TriggerType, RepetitionType, AtomicActionType
from adafruit_hid.consumer_control_code import ConsumerControlCode
from adafruit_hid.keycode import Keycode
from adafruit_hid.mouse import Mouse

combination = [
    {
        # This action overrides the clockwise and anticlockwise behavior of the rotary encoder
        "action_type": AtomicActionType.OVERRIDE_ROTARY,
        "value": {
            # For both `cw` and `acw` it's needed to define only a new combination.
            # N.B: no inception allowed here. You can't define a sub-combination which overrides again the encoder.
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
```

## Tests

Writing tests makes sure that the code is reliable, right? Yep, but there was no time to do so...