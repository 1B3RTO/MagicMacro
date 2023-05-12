from adafruit_macropad import MacroPad

from magic_macro.utils.context import context
from magic_macro.utils.macro_loader import load_macros_from_folder
from magic_macro.macro_board_handler.macro_board import MacroBoard
from magic_macro.display_handler.display_handler import DisplayHandler
from magic_macro.utils.enums import TriggerType, Topics, RepetitionType

from magic_macro.action_queue.action_list import ActionList
from magic_macro.action_queue.queue_elem import QueueElem
import time


class MacroBoardHandler:
    def __init__(self, macropad):
        self._macropad: MacroPad = macropad
        self._display_handler = DisplayHandler(macropad)
        self._selected_board = 0
        self._is_selector_view = False

        self._active_acw_action = None
        self._active_cw_action = None
        self._active_rotary_action = None

        self._running_queue = dict()

        self._board_colors = None
        self._last_colors = None

        # Load all the macro boards
        self._macro_boards: list[MacroBoard] = load_macros_from_folder()
        self._titles: list[str] = self.__get_board_titles()

        # Listener: Set menu switch on short press of rotary encoder
        context.subscribe_single(Topics.BUTTON_PRESS, self.__on_button_press)
        context.subscribe_single(Topics.OVERRIDE_ROTARY, self.__on_override_rotary_actions)
        context.subscribe_single(Topics.MACRO_END, self.__on_macro_end)

        # Set menu view
        self.__switch_view()

    def __get_board_titles(self) -> list[str]:
        titles = []
        for board in self._macro_boards:
            titles.append(board.title)
        return titles

    def __on_button_press(self, caller_id, trigger_type, timestamp):
        caller_and_trigger = f"{caller_id}:{trigger_type}"

        # Check for a short press on the rotary encoder
        if caller_id == 12 and trigger_type is TriggerType.ON_SHORT_PRESS:
            # switch view
            for key in self._running_queue.keys():
                self._running_queue.update({key: RepetitionType.ONE_TIME})
            self.__switch_view()

        # Manage the board selector view
        elif self._is_selector_view:
            if caller_id == 13:
                self.__acw_rotation()
            elif caller_id == 14:
                self.__cw_rotation()

        # Manage the board macros
        else:
            # Check for actions to stop repeating
            if trigger_type is TriggerType.NO_PRESS:
                self.__on_button_release(caller_id, timestamp)

            # Check if the macro is already running
            if trigger_type is TriggerType.ON_INITIAL_PRESS:
                for key, item in self._running_queue.items():
                    if int(key.split(":")[0]) == caller_id and item is RepetitionType.UNTIL_NEXT_PRESS:
                        self._running_queue.update({key: RepetitionType.ONE_TIME})
                        return

            if self._running_queue.get(caller_and_trigger) is None:
                self.__run_button(caller_id, trigger_type, timestamp)

    def __run_button(self, caller_id, trigger_type, timestamp):
        caller_and_trigger = f"{caller_id}:{trigger_type}"

        # If the macro is already running
        if caller_and_trigger in self._running_queue:
            return

        selected_board = self._macro_boards[self._selected_board]

        elems_to_queue: list[list[QueueElem]] = []
        combination = None
        repetition_type = None
        is_rotary_action = False

        # Actions of the rotary encoder rotation
        #  - append their methods to the action_method
        if caller_id == 13 and self._active_acw_action is not None:
            combination = self._active_acw_action
            repetition_type = RepetitionType.ONE_TIME
            is_rotary_action = True
        elif caller_id == 14 and self._active_cw_action is not None:
            combination = self._active_cw_action
            repetition_type = RepetitionType.ONE_TIME
            is_rotary_action = True

        # Every other button
        else:
            # get the action buttons from the selected combination of button - trigger_type
            print("caller_id", caller_id, "trigger_type", trigger_type)

            # It returns at most one item in a list
            buttons_to_queue = selected_board.get_actions(caller_id, trigger_type)

            # For each action button append their methods to the combination list
            if len(buttons_to_queue) == 1:
                button = buttons_to_queue[0]

                combination = button.combination
                repetition_type = button.repetition_type

        # There is nothing to exec
        if combination is None:
            return

        try:
            assert isinstance(combination, list)

            method: ActionList = ActionList()
            method.import_actions(combination, is_rotary_action)
            atomic_list: list[QueueElem] = method.get_atomic_list(caller_and_trigger, timestamp)
            elems_to_queue.append(atomic_list)

            # Add to the running queue
            self._running_queue.update({caller_and_trigger: repetition_type})
        except Exception as e:
            print(e)
            print("unable to run the action: {}".format(caller_and_trigger))

        for atomic_list in elems_to_queue:
            context.emit(Topics.ADD_TO_QUEUE, atomic_list)

    def __on_macro_end(self, caller_and_trigger):
        # Remove running
        repetition_type = self._running_queue.pop(caller_and_trigger)

        # Check repetition type
        if repetition_type is not RepetitionType.ONE_TIME:
            timestamp = time.monotonic_ns()
            caller_id, trigger_type = map(int, caller_and_trigger.split(":"))
            self.__run_button(caller_id, trigger_type, timestamp)

    def __on_button_release(self, caller_id, timestamp):
        # Check if the macro was on KEEP_PRESSED:
        #   if it was -> set it to not be rerun on its end
        for caller_and_trigger, repetition_type in self._running_queue.items():
            if caller_and_trigger.startswith(str(caller_id)) and repetition_type is RepetitionType.KEEP_PRESSED:
                self._running_queue.update({caller_and_trigger: RepetitionType.ONE_TIME})
                break

    def __on_override_rotary_actions(self, action_id, acw_method, cw_method):
        caller_id, trigger_type = map(int, action_id.split(":"))

        if caller_id == self._active_rotary_action:
            self._active_acw_action = None
            self._active_cw_action = None
            self._active_rotary_action = None
        else:
            self._active_acw_action = acw_method
            self._active_cw_action = cw_method
            self._active_rotary_action = caller_id

    def update_button_colors(self):
        colors = [0x000000 for i in range(12)]

        if self._board_colors is not None:
            # Apply base color
            for i in range(12):
                colors[i] = self._board_colors[i]

            # Apply selected rotary encoder color
            if self._active_rotary_action is not None:
                colors[self._active_rotary_action] = 0xFFFFFF

            # Apply active action color
            for caller_and_trigger, repetition_type in self._running_queue.items():
                caller_id, _ = map(int, caller_and_trigger.split(":"))
                if caller_id < 12:
                    color = 0x000000

                    if repetition_type is RepetitionType.ONE_TIME:
                        color = 0xFFBA13
                    elif repetition_type is RepetitionType.KEEP_PRESSED:
                        color = 0x13ffba
                    elif repetition_type is RepetitionType.UNTIL_NEXT_PRESS:
                        color = 0xba13ff

                    colors[caller_id] = color

        for i, color in enumerate(colors):
            if self._last_colors is None:
                self._macropad.pixels[i] = color
            elif self._last_colors[i] != color:
                self._macropad.pixels[i] = color

        self._last_colors = colors

    def __switch_view(self):
        self._is_selector_view = not self._is_selector_view
        if self._is_selector_view:
            # Set selector view
            self._display_handler.menu_selector(self._selected_board, self._titles)
            self._board_colors = None
        else:
            # Setup board view
            self._active_acw_action = None
            self._active_cw_action = None
            self._active_rotary_action = None

            self._selected_board %= len(self._titles)
            selected_board = self._macro_boards[self._selected_board]
            print(selected_board.get_names())

            self._display_handler.set_inside_macro_view(**selected_board.get_names())
            self._board_colors = selected_board.get_colors()

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
