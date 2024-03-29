from magic_macro.macro_board_handler.button import Button
from magic_macro.macro_board_handler.button_action import ButtonAction


class MacroBoard:
    def __init__(self, macro_board):
        self.title = macro_board.get("title")
        self._macros: list[dict] = macro_board.get("macros")

        # After the initialization we use only the following object
        self._buttons = dict()

        for macro in self._macros:
            button = macro.get("button")
            assert 0 <= button <= 11
            self._buttons.update({button: Button(**macro)})

    def get_actions(self, button: int, trigger_type: int) -> list[ButtonAction]:
        try:
            btn = self._buttons[button]
            action: ButtonAction = btn.actions[trigger_type]

            print("There is an action for button {} and trigger_type {}".format(button, trigger_type))
            return [action]
        except KeyError:
            print("There are no actions for button {} and trigger_type {}".format(button, trigger_type))
            return []

    def get_names(self):
        labels = []
        for i in range(12):
            try:
                btn = self._buttons.get(i)
                labels.append(btn.label)
            except Exception:
                labels.append("-")

        return {"title": self.title, "labels": labels}

    def get_colors(self):
        colors = []
        for i in range(12):
            try:
                btn = self._buttons.get(i)
                colors.append(btn.color)
            except Exception:
                colors.append(0x000000)

        return colors
