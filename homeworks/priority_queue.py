"""
Programming for linguists

Implementation of the data structure "Queue"
"""

from typing import Iterable
from collections import defaultdict

class PriorityQueue:
    def __init__(self, data, max_size=None):
        self.data = defaultdict(list)
        for el, priority in data:
            self.data[priority].insert(0, element)

    def put(self, element, priority):
        self.data[priority].insert(0, element)

    def get(self):
        return self.data[self.top()[0]].pop(-1)

    def size(self) -> int:
        """
        Return the number of elements in queue_
        :return: Number of elements in queue_
        """
        return len(list(self.data.values()))
    def top(self):
        """
        Return the first element in queue_
        :return: Item from queue_
        """
        for key, value in sorted(self.data.items()):
            if value:
                return key, self.data[key][-1]
    def capacity(self) -> int:
        """
        Return the maximal size of queue_
        :return: Maximal size of queue_
        """
        return 0



