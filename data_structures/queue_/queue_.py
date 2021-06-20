"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable


# pylint: disable=invalid-name
class Queue_:
    """
    Queue Data Structure
    """

    # pylint: disable=unused-argument,missing-module-docstring
    def __init__(self, max_size:int, data: Iterable = ()):
        self.data = []

    def put(self, element):
        """
        Add the element ‘element’ at the end of queue_
        :param element: element to add to queue_
        """
        self.data.insert(0, element)

    def get(self):
        """
        Remove and return an item from queue_
        """
        return self.data.pop(-1)

    def empty(self) -> bool:
        """
        Return whether queue_ is empty or not
        :return: True if queue_ does not contain any elements.
                 False if the queue_ contains elements
        """
        return not self.data

    # pylint: disable=no-self-use
    def full(self) -> bool:
        """
        Return whether queue_ is full or not
        :return: True if queue_ is full.
                 False if queue_ is not full
        """
        return False

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(self.data)

    def top(self):
        """
        Return the first element in queue_
        :return: Item from queue_
        """
        return self.data[-1]

    # pylint: disable=no-self-use
    def capacity(self) -> int:
        """
        Return the maximal size of queue_
        :return: Maximal size of queue_
        """
        return 0


class PriorityQueue:
    def __init__(self, data, max_size=int, max_priority=int):
        self.data = []
        self.max_priority = max_priority
        for i in range(0, max_priority):
            self.data.append([])

    def put(self, element, priority):
        if priority <= self.max_priority:
            self.data[priority].append(element)

    def get(self):
        new_data = []
        for i in self.data:
            if i:
                new_data.append(i)
        self.data = new_data
        return self.data.pop(0)

if __name__ == "__main__":
    query = PriorityQueue(data=[], max_priority=5)
    query.put('green', 4)
    query.put('blue', 3)
    query.put('black', 0)
    query.put('yellow', 4)
    while query:
        print(query.get())

