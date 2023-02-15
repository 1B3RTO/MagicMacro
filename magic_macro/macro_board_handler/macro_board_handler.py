from adafruit_macropad import MacroPad

from magic_macro.utils.context import context
from magic_macro.utils.macro_loader import load_macros_from_folder
from magic_macro.macro_board_handler.macro_board import MacroBoard
from magic_macro.display_handler.display_handler import DisplayHandler
from magic_macro.utils.enums import TriggerType, Topics


class MacroBoardHandler:
    def __init__(self, macropad):
        self._macropad: MacroPad = macropad
        self._display_handler = DisplayHandler(macropad)
        self._selected_board = 0
        self._is_selector_view = False

        # Load all the macro boards
        self._macro_boards: list[MacroBoard] = load_macros_from_folder()
        self._titles: list[str] = self.__get_board_titles()

        # Listener: Set menu switch on short press of rotary encoder
        context.subscribe_single(Topics.BUTTON_PRESS, self.__on_button_press)

        # Set menu view
        self.__switch_view()

    def __get_board_titles(self) -> list[str]:
        titles = []
        for board in self._macro_boards:
            titles.append(board.title)
        return titles

    def __on_button_press(self, caller_id, trigger_type, timestamp):
        if caller_id == 12 and trigger_type is TriggerType.ON_SHORT_PRESS:
            # switch view
            self.__switch_view()

        elif self._is_selector_view:
            # menu view operations
            if caller_id == 13:
                self.__acw_rotation()
            elif caller_id == 14:
                self.__cw_rotation()

        else:
            # Board view operation
            # TODO: get action to exec from the board and add it to the queue
            pass
        pass

    def __switch_view(self):
        self._is_selector_view = not self._is_selector_view
        if self._is_selector_view:
            # Set selector view
            self._display_handler.menu_selector(self._selected_board, self._titles)
        else:
            # Setup board view
            self._selected_board %= len(self._titles)
            selected_board = self._macro_boards[self._selected_board]
            print(selected_board.get_names())
            self._display_handler.set_inside_macro_view(**selected_board.get_names())

    def __acw_rotation(self):
        # Short press button 13
        self._selected_board -= 1

        # Update selector view
        self._display_handler.menu_selector(self._selected_board, self._titles)

    def __cw_rotation(self):
        # Short press button 14
        self._selected_board += 1

        # Update selector view
        self._display_handler.menu_selector(self._selected_board, self._titles)
