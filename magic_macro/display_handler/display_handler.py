from displayio import Group
from adafruit_macropad import MacroPad

import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from magic_macro.config import DEFAULT_DISPLAY_WIDTH, DEFAULT_DISPLAY_HEIGHT, CENTRAL_ANCHOR_POINT


class DisplayHandler:
    def __init__(self, macropad: MacroPad):
        self._macropad: MacroPad = macropad
        self._inside_macro_group: Group = Group()
        self._macro_selector_group: Group = Group()
        self.__initialize_groups()

    def __initialize_groups(self):
        # Initiate _inside_macro_group
        for key_index in range(12):
            x = key_index % 3
            y = key_index // 3
            self._inside_macro_group.append(label.Label(terminalio.FONT, text='EMPTY', color=0xFFFFFF,
                                                        anchored_position=((DEFAULT_DISPLAY_WIDTH - 1) * x / 2,
                                                                           DEFAULT_DISPLAY_HEIGHT - 1 -
                                                                           (3 - y) * 12),
                                                        anchor_point=(x / 2, 1.0)))
        self._inside_macro_group.append(Rect(0, 0, DEFAULT_DISPLAY_WIDTH, 12, fill=0xFFFFFF))
        self._inside_macro_group.append(label.Label(terminalio.FONT, text='TITLE', color=0x000000,
                                                    anchored_position=(DEFAULT_DISPLAY_WIDTH // 2, 0),
                                                    anchor_point=(0.5, 0.0)))

        # Initiate macro_selector_group
        self._macro_selector_group.append(Rect(0, 0, DEFAULT_DISPLAY_WIDTH, 16, outline=0xffffff, stroke=1))
        for line in range(4):
            self._macro_selector_group.append(
                label.Label(
                    terminalio.FONT,
                    text=f"Line {line}",
                    color=0xFFFFFF,
                    anchored_position=(DEFAULT_DISPLAY_WIDTH // 2, 16 * line),
                    anchor_point=CENTRAL_ANCHOR_POINT,
                )
            )

    def menu_selector(self, encoder_position: int, menu_list: list, highlight: bool = False):
        """
        Setup and return a group for the specific menu_list
        :param encoder_position: the int position of the rotary encoder
        :param menu_list: list with all the str names of all the boards available
        :param highlight: whether to add or not an arrow beside the board name
        :return: the configured Group object
        """
        norm_encoder = encoder_position % len(menu_list)
        selected_cell = norm_encoder % 4
        starting_index = int(norm_encoder / 4) * 4

        for i in range(4):
            self._macro_selector_group[i + 1].text = ""

        for i, elem in enumerate(menu_list[starting_index: starting_index + 4]):
            self._macro_selector_group[i + 1].text = elem

        if highlight and len(menu_list) > 0:
            self._macro_selector_group[selected_cell+1].text = f"> {self._macro_selector_group[selected_cell+1].text} <"

        self._macro_selector_group[0] = Rect(0, selected_cell * 16, DEFAULT_DISPLAY_WIDTH, 16, outline=0xffffff,
                                             stroke=1)

        self.update_view(self._macropad, self._macro_selector_group)

    def set_inside_macro_view(self, title: str, labels: list[str]):
        """
        Setup and return a group for the specific macro board
        :param title: The name of the board
        :param labels: an array of 12 str names
        :return: the configured Group object
        """
        assert len(labels) == 12

        self._inside_macro_group[13].text = title

        for i, text in enumerate(labels):
            self._inside_macro_group[i].text = text

        self.update_view(self._macropad, self._inside_macro_group)

    def select_line(self, line_index: int) -> displayio.Group:
        """
        Update the selected line of the menu selector
        :param line_index: int of the selected line
        :return: the configured Group object
        """
        self._macro_selector_group[0] = Rect(0, line_index * 16, DEFAULT_DISPLAY_WIDTH, 16, outline=0xffffff, stroke=1)
        return self._macro_selector_group

    def update_macro_selector_line(self, line_index, anchored_position, anchor_point):
        # Debug method
        self._macro_selector_group[line_index + 1] = label.Label(
            terminalio.FONT,
            text=f"Line {line_index}",
            color=0xFFFFFF,
            anchored_position=anchored_position,
            anchor_point=anchor_point,
        )

        return self._macro_selector_group

    @staticmethod
    def update_view(macropad: MacroPad, groups: Group):
        macropad.display.show(groups)
        macropad.display.refresh()
