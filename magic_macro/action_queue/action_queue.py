from magic_macro.utils.context import context
from magic_macro.utils.enums import Topics
from magic_macro.action_queue.queue import Queue
from magic_macro.action_queue.queue_elem import QueueElem


class ActionQueue:
    def __init__(self):
        self._queue = Queue()

        context.subscribe_single(Topics.ADD_TO_QUEUE, self.__on_add_to_queue)

    def __on_add_to_queue(self, atomic_list: list[QueueElem]):
        print("Adding to the queue: {} QueueElems".format(len(atomic_list)))
        self._queue.add_list(atomic_list)

    def check_queue(self, timestamp):
        elems_to_exec = self._queue.get_until(timestamp)
        if len(elems_to_exec) > 0:
            print("Elems to exec", len(elems_to_exec))
        # TODO: exec the queue elements
