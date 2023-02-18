from magic_macro.utils.context import context
from magic_macro.utils.enums import Topics
from magic_macro.action_queue.queue import Queue
from magic_macro.action_queue.queue_elem import QueueElem


class ActionQueue:
    def __init__(self):
        self._queue = Queue()

        context.subscribe_single(Topics.ADD_TO_QUEUE, self.__on_add_to_queue)
        pass

    def __on_add_to_queue(self, atomic_list: list[QueueElem]):
        self._queue.add_list(atomic_list)
        pass

    def check_queue(self):
        pass

    pass
