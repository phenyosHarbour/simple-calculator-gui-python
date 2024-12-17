from src.constants import CONSTANTS, SCIENTIFIC_FUNCTIONS, factorial


def evaluate_expression(expression):
    try:
        expression = str(expression)  # Ensure expression is a string

        # Replace constants
        for const, value in CONSTANTS.items():
            expression = expression.replace(const, str(value))

        # Replace scientific functions
        for func in SCIENTIFIC_FUNCTIONS:
            expression = expression.replace(
                func, f"SCIENTIFIC_FUNCTIONS['{func}']"
            )

        # Handle factorial
        if "!" in expression:
            parts = expression.split("!")
            return factorial(int(parts[0]))

        # Evaluate the final expression
        result = eval(expression)
        return round(result, 10)
    except Exception:
        return "Error"


# Ensure a newline at the end of the file
