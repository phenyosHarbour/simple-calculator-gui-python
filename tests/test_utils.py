# test_utils.py
from src.utils import evaluate_expression
import unittest


class TestUtils(unittest.TestCase):
    def test_evaluate_expression(self):
        self.assertEqual(evaluate_expression("2+2"), 4)
        self.assertEqual(evaluate_expression("sqrt(16)"), 4)
        self.assertEqual(evaluate_expression("2**3"), 8)
        self.assertRaises(ValueError, evaluate_expression, "invalid")


if __name__ == "__main__":
    unittest.main()
