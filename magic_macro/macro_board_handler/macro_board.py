from magic_macro.macro_board_handler.button import Button
from magic_macro.macro_board_handler.button_action import ButtonAction


class MacroBoard:
    def __init__(self, macro_board):
        self.title = macro_board.get("title")
        self._macros: list[dict] = macro_board.get("macros")
        self._buttons = dict()

        for macro in self._macros:
            button = macro.get("button")
            assert 0 <= button <= 11
            self._buttons.update({button: Button(**macro)})

    def get_actions(self, button, trigger_type):
        try:
            btn = self._buttons.get(button)
            actions: list[ButtonAction] = btn.actions.get(trigger_type)

            return actions
        except KeyError:
            return None

    def get_names(self):
        labels = []
        for i in range(12):
            try:
                btn = self._buttons.get(i)
                labels.append(btn.label)
            except KeyError:
                labels.append("-")

        return {"title": self.title, "labels": labels}
