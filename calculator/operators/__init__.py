class Add:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b


class Subtract:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def subtraction(self):
        return self.a - self.b


class Multiply:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def multiplication(self):
        return self.a * self.b


class Divide:
    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def division(self):
        if self.b == 0:
            raise ValueError()

        return self.a / self.b


class Factorial:

    def factorial(self, x):
        if x == 0:
            return 1

        return self.factorial(x - 1) * x


class Fibonacci:

    def fibonacci(self, x):
        if x == 1 or x == 0:
            return x
        else:
            return self.fibonacci(x - 1) + self.fibonacci(x - 2)
