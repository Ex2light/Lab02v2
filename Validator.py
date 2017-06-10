import abc
import os


class NaN(Exception):
    pass


class Zero(Exception):
    pass


class AbstractValidator(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def validateIfNumber(self, validatedObject):
        pass


class NumberValidator(AbstractValidator):
    def __init__(self, validatedObject):
        self.value = validatedObject

    def validateIfNumber(self):
        if not (isinstance(self.value, int) or isinstance(self.value, float)):
            raise NaN("Input not a number")
        else:
            return 1

    def validateIfNotZero(self):
        if (self.value == 0):
            raise Zero("Input is 0")
        else:
            return 1
