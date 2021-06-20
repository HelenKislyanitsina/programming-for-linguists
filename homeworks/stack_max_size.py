"""
Programming for linguists

Implementation of the data structure "Stack"
"""

from typing import Iterable


class Stack:
    """
    Stack Data Structure
    """
    # pylint: disable=missing-module-docstring
    def __init__(self, max_size: int, data: Iterable = None):
        self.max_size = max_size
        self.data = list(data) if data else []

    def push(self, element):
        """
        Add the element ‘element’ at the top of stack
        :param element: element to add to stack
        """
        if len(self.data) < self.max_size:
            self.data.append(element)
        else:
            raise IndexError('Max size of stack has been reached ')

    def pop(self):
        """
        Delete the element on the top of stack
        """
        self.data.pop(-1)

    def top(self):
        """
        Return the element on the top of stack
        :return: the element that is on the top of stack
        """
        return self.data[-1]

    def size(self) -> int:
        """
        Return the number of elements in stack
        :return: Number of elements in stack
        """
        return len(self.data)

    def empty(self) -> bool:
        """
        Return whether stack is empty or not
        :return: True if stack does not contain any elements
                 False if stack contains elements
        """
        return not bool(self.size())
