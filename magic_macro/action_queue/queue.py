from magic_macro.action_queue.queue_elem import QueueElem


class Queue:
    _queue: list[QueueElem] = None

    def __init__(self):
        self._queue = list()
        # [{timestamp of execution, what to do}, ...]

    def get_until(self, timestamp: int) -> list:
        if len(self._queue) > 0:
            print(f"Requesting until {timestamp}")

        result = list()

        while True:
            if len(self._queue) == 0:
                break
            elif timestamp < self._queue[0].timestamp:
                break
            else:
                print(f"Found: {self._queue[0].timestamp}")
                # just add the action to exec in the result, not the timestamp
                result.append(self._queue.pop(0))

        if len(self._queue) > 0 or len(result) > 0:
            print(f"Remaining queue len: {len(self._queue)}")
            print(f"Requested queue elems: {len(result)}")

        return result

    def add_list(self, atomic_list: list[QueueElem]) -> None:
        # We assume the atomic_list is already sorted.
        # atomic_list: [{timestamp, action_to_exec}]

        # The queue is empty, just add everything
        if len(self._queue) == 0:
            self._queue.extend(atomic_list)
            return

        # The queue is already populated.
        # Find the right spot in which add each element
        queue_index = 0
        for atomic_action in atomic_list:
            while True:
                if queue_index < 0:
                    # we already reached the end of the queue
                    break
                elif queue_index >= len(self._queue):
                    # we reached the end of the queue
                    queue_index = -1
                    break
                elif atomic_action.timestamp < self._queue[queue_index].timestamp:
                    # we found the right index
                    break
                else:
                    queue_index += 1

            if queue_index < 0:
                # we reached the end of the queue
                self._queue.append(atomic_action)
            else:
                self._queue.insert(queue_index, atomic_action)
                queue_index += 1  # the atomic list is already sorted
