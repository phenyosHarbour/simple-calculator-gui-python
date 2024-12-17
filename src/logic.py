import math


class CalculatorLogic:
    """
    A class to perform core scientific calculator operations.
    """

    @staticmethod
    def evaluate_expression(expression: str) -> float:
        """
        Evaluate a mathematical expression.
        Supports basic operations and exponentiation.
        """
        try:
            expression = expression.replace('^', '**')
            return eval(expression)
        except Exception as e:
            raise ValueError("Invalid mathematical expression.") from e

    @staticmethod
    def square_root(value: float) -> float:
        """
        Calculate the square root of a number.
        """
        if value < 0:
            raise ValueError(
                "Cannot calculate the square root of a negative number."
            )
        return math.sqrt(value)

    @staticmethod
    def backspace(expression: str) -> str:
        """
        Perform backspace operation on the expression.
        """
        return expression[:-1]
# This class contains the core logic for the calculator application.
