from adafruit_macropad import MacroPad

from magic_macro.utils.context import context
from magic_macro.utils.macro_loader import load_macros_from_folder
from magic_macro.macro_board_handler.macro_board import MacroBoard
from magic_macro.display_handler.display_handler import DisplayHandler
from magic_macro.utils.enums import TriggerType, Topics

from magic_macro.action_queue.action_list import ActionList
from magic_macro.action_queue.queue_elem import QueueElem


class MacroBoardHandler:
    def __init__(self, macropad):
        self._macropad: MacroPad = macropad
        self._display_handler = DisplayHandler(macropad)
        self._selected_board = 0
        self._is_selector_view = False

        self._active_acw_action = None
        self._active_cw_action = None

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
        # Check for a short press on the rotary encoder
        if caller_id == 12 and trigger_type is TriggerType.ON_SHORT_PRESS:
            # switch view
            self.__switch_view()

        # Manage the board selector view
        elif self._is_selector_view:
            if caller_id == 13:
                self.__acw_rotation()
            elif caller_id == 14:
                self.__cw_rotation()

        # Manage the board macros
        else:
            selected_board = self._macro_boards[self._selected_board]

            elems_to_queue: list[list[QueueElem]] = []
            action_methods = []

            # Actions of the rotary encoder rotation
            #  - append their methods to the action_method
            if caller_id == 13:
                pass
            elif caller_id == 14:
                pass

            # Every other button
            else:
                # get the action buttons from the selected combination of button - trigger_type
                buttons_to_queue = selected_board.get_actions(caller_id, trigger_type)

                # For each action button append their methods to the action_methods list
                for button in buttons_to_queue:
                    action_methods.append(button.method)

            # For all the requested methods to exec
            for method in action_methods:
                try:
                    action_list = method()
                    assert isinstance(action_list, ActionList)
                    atomic_list: list[QueueElem] = action_list.get_atomic_list(caller_id, timestamp)
                    elems_to_queue.append(atomic_list)
                except Exception as e:
                    print("unable to run the action: button {} - trigger type {}".format(caller_id, trigger_type))

            # TODO: Apply some restrictions on the elems to queue
            #  - cannot override the rotary from a rotary action

            for atomic_list in elems_to_queue:
                context.emit(Topics.ADD_TO_QUEUE, atomic_list)

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
