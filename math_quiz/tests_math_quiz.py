import unittest
from math_quiz import GetRandomNumber, GetRandomOperator, GetSolution


class TestMathGame(unittest.TestCase):

    def test_function_A(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = GetRandomNumber(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_function_B(self):
        # Test if operator generated is a valid operator
        operators = ['+','-','*']
        for k in range(1000):
            rand_operator = GetRandomOperator()
            self.assertTrue(rand_operator in operators)

    def test_function_C(self):
        #tests some math problems
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (3,3, '-', '3 - 3', 0),
                (4,6, '*', '4 * 6', 24),
                (3,5, '+', '3 + 5', 8),
                (6,7, '*', '6 * 7', 42)
            ]
            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, result = GetSolution(num1, num2, operator)
                self.assertTrue(problem == expected_problem and result == expected_answer)

if __name__ == "__main__":
    unittest.main()
