import unittest
from src.logic import evaluate_expression


class TestLogic(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(evaluate_expression("2+2"), 4)
        self.assertEqual(evaluate_expression("10/2"), 5)
        self.assertEqual(evaluate_expression("2^3"), 8)

    def test_scientific_functions(self):
        self.assertAlmostEqual(evaluate_expression("sin(0)"), 0)
        self.assertAlmostEqual(evaluate_expression("log(10)"), 1)


if __name__ == "__main__":
    unittest.main()
# Compare this snippet from src/memory.py:
