from magic_macro.utils.enums import TriggerType, RepetitionType


class Button:
    button: int = None
    label: str = None
    color = None
    actions: dict = None

    def __init__(self, button, label, color, actions):
        self.button = button
        self.label = label
        self.color = color
        self.actions = dict()

        for action in actions:
            trigger_type = action["trigger_type"]
            if self.actions.get(trigger_type) is None:
                self.actions.update({trigger_type: list()})
            self.actions.get(trigger_type).append(ButtonAction(**action))


class ButtonAction:
    repetition_type: RepetitionType = None
    trigger_type: TriggerType = None
    method = None

    def __init__(self, repetition_type, trigger_type, method):
        self.repetition_type = repetition_type
        self.trigger_type = trigger_type
        self.method = method


class MacroBoard:
    def __init__(self, macro_board):
        self._name = macro_board.get("name")
        self._macros: list[dict] = macro_board.get("macros")
        self._buttons = dict()

        for macro in self._macros:
            button = macro.get("button")
            assert 0 <= button <= 11
            self._buttons.update({button: Button(**macro)})
