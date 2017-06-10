import unittest
from Calculator import Calculator
from Calculator import DivException
import Validator


class TestCalc(unittest.TestCase):
    # Tests for Add function

    def TestForAddingTwoIntegers(self):
        calculator = Calculator()
        first = 2
        second = 3
        expectation = 5
        self.assertEqual(calculator.Add(first, second), expectation)

    def TestForAddingTwoFloats(self):
        calculator = Calculator()
        first = 2.5
        second = 3.5
        expectation = 6
        self.assertEqual(calculator.Add(first, second), expectation)

    def TestForAddingIntegerAndFloat(self):
        calculator = Calculator()
        first = 2
        second = 3.5
        expectation = 5.5
        self.assertEqual(calculator.Add(first, second), expectation)

    # Tests for Substract function

    def TestForSubstractingTwoIntegers(self):
        calculator = Calculator()
        first = 2
        second = 3
        expectation = -1
        self.assertEqual(calculator.Subtract(first, second), expectation)

    def TestForSubstractingTwoFloats(self):
        calculator = Calculator()
        first = 2.5
        second = 3.5
        expectation = -1
        self.assertAlmostEqual(calculator.Subtract(first, second), expectation)

    def TestForSubstractingIntegerAndFloat(self):
        calculator = Calculator()
        first = 2
        second = 3.5
        expectation = -1
        self.assertAlmostEqual(calculator.Subtract(first, second), expectation)

    # Tests for Divide function

    def TestForDividingTwoIntegers(self):
        calculator = Calculator()
        first = 6
        second = 2
        expectation = 3
        self.assertEqual(calculator.Divide(first, second), expectation)

    def TestForDividingTwoFloats(self):
        calculator = Calculator()
        first = 4.5
        second = 1.5
        expectation = 3
        self.assertAlmostEqual(calculator.Divide(first, second), expectation)

    def TestForDividingIntegerAndFloat(self):
        calculator = Calculator()
        first = 6
        second = 1.5
        expectation = 4
        self.assertAlmostEqual(calculator.Divide(first, second), expectation)

    def TestForDividingByZero(self):
        calculator = Calculator()
        first = 6
        second = 0
        self.assertRaises(DivException, calculator.Divide, first, second)

    def TestForNotANumberInput(self):
        calculator = Calculator()
        number = 5
        string = 'abcdef'
        self.assertRaises(Validator.NaN, calculator.Add, number, string)
        self.assertRaises(Validator.NaN, calculator.Subtract, number, string)
        self.assertRaises(Validator.NaN, calculator.Divide, number, string)
        self.assertRaises(Validator.NaN, calculator.Multiply, number, string)
        self.assertRaises(Validator.NaN, calculator.Add, string, number)
        self.assertRaises(Validator.NaN, calculator.Subtract, string, number)
        self.assertRaises(Validator.NaN, calculator.Divide, string, number)
        self.assertRaises(Validator.NaN, calculator.Multiply, string, number)
        self.assertRaises(Validator.NaN, calculator.Add, string, string)
        self.assertRaises(Validator.NaN, calculator.Subtract, string, string)
        self.assertRaises(Validator.NaN, calculator.Divide, string, string)
        self.assertRaises(Validator.NaN, calculator.Multiply, string, string)

    # Tests for Multiply function

    def TestForMulitplicationOfTwoIntegers(self):
        calculator = Calculator()
        first = 2
        second = 3
        expectation = 6
        self.assertEqual(calculator.Multiply(first, second), expectation)

    def TestForMultiplicationOfTwoFloats(self):
        calculator = Calculator()
        first = 2.5
        second = 3.5
        expectation = 8.75
        self.assertAlmostEqual(calculator.Multiply(first, second), expectation)

    def TestForMultiplicationOfIntegerAndFloat(self):
        calculator = Calculator()
        first = 2
        second = 3.5
        expectation = 7
        self.assertAlmostEqual(calculator.Multiply(first, second), expectation)


if __name__ == '__main__':
    unittest.main()
