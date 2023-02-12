import displayio
import terminalio
from adafruit_display_shapes.rect import Rect
from adafruit_display_text import label
from magic_macro.config import DEFAULT_DISPLAY_WIDTH, DEFAULT_DISPLAY_HEIGHT, CENTRAL_ANCHOR_POINT

_inside_macro_group = displayio.Group()
_macro_selector_group = displayio.Group()

"""
Examples of lists:

test_label = ["Elem0", "Elem1", "Elem2",
              "Elem3", "Elem4", "Elem5",
              "Elem6", "Elem7", "Elem8",
              "Elem9", "Elem10", "Elem11",
              "LETS GOO"
              ]

test_menu = ["Elem0", "Elem1", "Elem2",
             "Elem3", "Elem4", "Elem5",
             "Elem6", "Elem7", "Elem8",
             "Elem9", "Elem10", "Elem11",
             "Elem12", "Elem13", "Elem14"]
"""


def __initialize_groups():
    # Initiate _inside_macro_group
    for key_index in range(12):
        x = key_index % 3
        y = key_index // 3
        _inside_macro_group.append(label.Label(terminalio.FONT, text='EMPTY', color=0xFFFFFF,
                                               anchored_position=((DEFAULT_DISPLAY_WIDTH - 1) * x / 2,
                                                                  DEFAULT_DISPLAY_HEIGHT - 1 -
                                                                  (3 - y) * 12),
                                               anchor_point=(x / 2, 1.0)))
    _inside_macro_group.append(Rect(0, 0, DEFAULT_DISPLAY_WIDTH, 12, fill=0xFFFFFF))
    _inside_macro_group.append(label.Label(terminalio.FONT, text='TITLE', color=0x000000,
                                           anchored_position=(DEFAULT_DISPLAY_WIDTH // 2, -2),
                                           anchor_point=(0.5, 0.0)))

    # Initiate macro_selector_group
    _macro_selector_group.append(Rect(0, 0, DEFAULT_DISPLAY_WIDTH, 16, outline=0xffffff, stroke=1))
    for line in range(4):
        _macro_selector_group.append(
            label.Label(
                terminalio.FONT,
                text=f"Line {line}",
                color=0xFFFFFF,
                anchored_position=(DEFAULT_DISPLAY_WIDTH // 2, 16 * line),
                anchor_point=CENTRAL_ANCHOR_POINT,
            )
        )


def menu_selector(encoder_position: int, menu_list: list) -> displayio.Group:
    """
    Setup and return a group for the specific menu_list
    :param encoder_position: the int position of the rotary encoder
    :param menu_list: list with all the str names of all the boards available
    :return: the configured Group object
    """
    norm_encoder = encoder_position % len(menu_list)
    selected_cell = norm_encoder % 4
    starting_index = int(norm_encoder / 4) * 4

    for i in range(4):
        _macro_selector_group[i + 1].text = ""

    for i, elem in enumerate(menu_list[starting_index: starting_index + 4]):
        _macro_selector_group[i + 1].text = elem

    _macro_selector_group[0] = Rect(0, selected_cell * 16, DEFAULT_DISPLAY_WIDTH, 16, outline=0xffffff, stroke=1)

    return _macro_selector_group


def set_inside_macro_view(macro_labels: list) -> displayio.Group:
    """
    Setup and return a group for the specific macro board
    :param macro_labels: an array of 13 str names
    :return: the configured Group object
    """
    assert len(macro_labels) == 13

    for i, text in enumerate(macro_labels):
        if i == 12:
            _inside_macro_group[13].text = text
        else:
            _inside_macro_group[i].text = text

    return _inside_macro_group


def select_line(line_index: int) -> displayio.Group:
    """
    Update the selected line of the menu selector
    :param line_index: int of the selected line
    :return: the configured Group object
    """
    _macro_selector_group[0] = Rect(0, line_index * 16, DEFAULT_DISPLAY_WIDTH, 16, outline=0xffffff, stroke=1)
    return _macro_selector_group


def update_macro_selector_line(line_index, anchored_position, anchor_point):
    _macro_selector_group[line_index + 1] = label.Label(
        terminalio.FONT,
        text=f"Line {line_index}",
        color=0xFFFFFF,
        anchored_position=anchored_position,
        anchor_point=anchor_point,
    )

    return _macro_selector_group


# TO SET AND UPDATE THE DISPLAY:
# macropad.display.show(inside_macro_group)
# macropad.display.refresh()

__initialize_groups()
