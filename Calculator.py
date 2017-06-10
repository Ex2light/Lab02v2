from abc import ABCMeta, abstractmethod
from scipy.misc import derivative as deriv
from Validator import NumberValidator as valid


class DivException(Exception):
    pass


class AbstractCalculator:
    __metaclass__ = ABCMeta


    def Add(firstInput, secondInput):
        pass

    def Subtract(firstInput, secondInput):
        pass

    def Divide(firstInput, secondInput):
        pass

    def Multiply(firstInput, secondInput):
        pass

    def Derivative(function, x0, dx, n):
        pass


class Calculator:
    def __init__(self):
        pass

    def Add(self, firstInput, secondInput):

        firstNumber = valid(firstInput)
        secondNumber = valid(secondInput)

        if (firstNumber.validateIfNumber() and secondNumber.validateIfNumber()):
            return firstInput + secondInput

    def Subtract(self, firstInput, secondInput):

        firstNumber = valid(firstInput)
        secondNumber = valid(secondInput)

        if (firstNumber.validateIfNumber() and secondNumber.validateIfNumber()):
            return firstInput - secondInput

    def Multiply(self, firstInput, secondInput):

        firstNumber = valid(firstInput)
        secondNumber = valid(secondInput)

        if (firstNumber.validateIfNumber() and secondNumber.validateIfNumber()):
            return firstInput * secondInput

    def Divide(self, firstInput, secondInput):

        firstNumber = valid(firstInput)
        secondNumber = valid(secondInput)

        if (firstNumber.validateIfNumber() and secondNumber.validateIfNumber() and secondNumber.validateIfNotZero()):
            return firstInput / secondInput

    def Derivative(self, function, x0, dx, n):
        return deriv(function, x0, 1.0, n)