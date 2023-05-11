from magic_macro.macro_board_handler.button_action import ButtonAction


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
            if self.actions.get(trigger_type) is not None:
                continue
            self.actions.update({trigger_type: ButtonAction(**action)})