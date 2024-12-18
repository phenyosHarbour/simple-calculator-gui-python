import math


def evaluate_expression(expression):
    try:
        # Define a safe evaluation environment
        allowed_names = {
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
            # Add other math functions/constants as needed
        }

        # Evaluate the expression in the context of allowed names
        result = eval(expression, {"__builtins__": None}, allowed_names)

        # Check if the result is a whole number
        if isinstance(result, float) and result.is_integer():
            return int(result)
        return result
    except Exception as e:
        raise ValueError("Invalid expression") from e
