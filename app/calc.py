from app import util
import math
class InvalidPermissions(Exception):
    pass


class Calculator:
    def add(self, x, y):
        self.check_types(x, y)
        return x + y

    def subtract(self, x, y):
        self.check_types(x, y)
        return x - y

    def multiply(self, x, y):
        if not util.validate_permissions(f"{x} * {y}", "user1"):
            raise InvalidPermissions('User has no permissions')
        self.check_types(x, y)
        return x * y

    def divide(self, x, y):
        self.check_types(x, y)
        if y == 0:
            raise TypeError("Division by zero is not possible")
        return x / y

    def power(self, x, y):
        self.check_types(x, y)
        return x ** y

    def sqrt(self, x):
        self.check_sqrt(x)
        return math.sqrt(x)

    def log10(self, x):
        self.check_log(x)
        return math.log10(x)

    def check_types(self, x, y):
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("Parameters must be numbers")

    def check_sqrt(self, x):
        if x < 0:
            raise ValueError("Cannot take square root of a negative number")

    def check_log(self, x):
        if x <= 0:
            raise ValueError("Cannot take logarithm of a non-positive number")
