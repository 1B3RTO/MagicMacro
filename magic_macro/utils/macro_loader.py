import os

from magic_macro.config import MACRO_FOLDER
from magic_macro.macro_board_handler.macro_board import MacroBoard


def load_macros_from_folder(folder_path=MACRO_FOLDER) -> list[MacroBoard]:
    macro_boards = []
    files = os.listdir(folder_path)
    files.sort()
    for filename in files:
        if filename.endswith('.py') and not filename.startswith('._'):
            try:
                module = __import__(MACRO_FOLDER + '/' + filename[:-3])
                macro_boards.append(MacroBoard(module.board))
            except (SyntaxError, ImportError, AttributeError, KeyError, NameError,
                    IndexError, TypeError) as err:
                print("ERROR in", filename)
                import traceback
                traceback.print_exception(err, err, err.__traceback__)

    return macro_boards
