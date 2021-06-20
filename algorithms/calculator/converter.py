"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import (Digit, Op, ReversePolishNotation)
from data_structures.queue_ import Queue_
from data_structures.stack import Stack


class ReversePolishNotationConverterState:
    """
    Class to store the state of RPN convert process
    """
    def __init__(self, expression_in_infix_notation: str):
        """
        :param expression_in_infix_notation: string with expression in infix notation
        """
        self.expression_in_infix_notation = Queue_(expression_in_infix_notation)
        self.expression_in_postfix_notation = ReversePolishNotation()
        self.stack = Stack()

    def pop_from_stack_until_opening_bracket(self):
        """
        Help function
        :return:
        """
        while not self.is_opening_bracket(self.stack.top()):
            self.expression_in_postfix_notation.put(self.stack.top())
            self.stack.pop()
        self.stack.pop()

class ReversePolishNotationConverter:
    """
    Class for converting infix expressions to reverse polish notation
    """
    point = '.'

    @staticmethod
    def convert(expression_in_infix_notation: str) -> ReversePolishNotation:
        """
        Main method of the class.
        Convert an infix expression to reverse polish notation

        :return: ReversePolishNotation object
        """

        while not self.expression_in_infix_notation.empty():
            symbol = expression_in_infix_notation.top()

            if self.is_part_of_digit(symbol):
                digit = ReversePolishNotationConverter.read_digit(symbol)
                self.expression_in_infix_notation.put(digit)
                continue

            if self.is_open_bracket(operator):
                self.stack.push(symbol)

            if self.is_close_bracket(operator):
                self.pop_from_stack_until_opening_bracket()

            operator = OpFactory.get_op_by_symbol(symbol)
            if self.is_binary_operation(symbol)
                self.pop_from_stack_until_opening_prioritizing(symbol)
            else:
                raise Exception(symbol)
        while not self.stack.empty():
            self.expression_in_postfix_notation(self.stack.top())
            self.stack.pop()
        self.stack.pop()



    @staticmethod
    def pop_from_stack_until_prioritizing(operator: Op, state: ReversePolishNotationConverterState):
        """
        Help function to move elements from stack to state elements (operators)
        until element on the top of the stack  has less priority then current operator
        :param operator: Instance of Op class - current operator
        :param state: State of the RPN convert process
        """
        current_priority = operator.priority
        while not self.empty() and self.stack.top().priority() > current_priority:
            state.expression_in_postfix_notation.put(stack.top())
        stack.pop()
    self.stack.push(operator)
    @staticmethod
    def read_digit(state: ReversePolishNotationConverterState) -> Digit:
        """
        Method to read a digit from self._infix_notation

        :param state: expression in Reverse Polish Notation Format
        :return: Instance of Digit class
        """
        digit = symbol
        while not self.expression_in_infix_notation.empty() and srelf.is_part_of_digit(self.expression_in_infix_notation.top()):
            digit += self.expression_in_infix_notation.get()
        return Digit(digit)

    @staticmethod
    def is_part_of_digit(character: str) -> bool:
        """
        Help function to check if symbol is a part of floating point number
        :param character: current symbol
        :return: True if character can be part of a digit, else False
        """
        if character == ReversePolishNotationConverter.point:
            return True
        try:
            int(character)
            return True
        except ValueError:
            return False

    @staticmethod
    def is_open_bracket(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is open bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the open bracket operator else False
        """
        if symbol == ')'
            return True
        return False
    @staticmethod
    def is_close_bracket(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is close bracket

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the close bracket operator else False
        """
        if symbol == ')'
            return True
        return False
    @staticmethod
    def is_binary_operation(operator: Op) -> bool:
        """
        Method to check if the next character in the infix expression is binary operator

        :param operator: Operator redden from the infix expression
        :return: True id this operator is the binary operator else False
        """
        return isinstance(operator, BinaryOp)