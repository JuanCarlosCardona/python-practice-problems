from operators import *


def valid_operators(operator):
    switch = {
        '+': True,
        '-': True,
        '*': True,
        'x': True,
        '/': True,
        'add': True,
        'subtract': True,
        'multiply': True,
        'divide': True
    }
    return switch.get(operator, False)


print(valid_operators('add'))


def make_operation(num1, operator, num2):
    switch = {
        '+': Add(num1, num2).addition(),
        '-': Subtract(num1, num2).subtraction(),
        '*': Multiply(num1, num2).multiplication(),
        'x': Multiply(num1, num2).multiplication(),
        '/': Divide(num1, num2).division(),
        'add': Add(num1, num2).addition(),
        'subtract': Subtract(num1, num2).subtraction(),
        'multiply': Multiply(num1, num2).multiplication(),
        'divide': Divide(num1, num2).division()
    }

    return switch.get(operator, ValueError)


def basic_arithmetic():
    try:
        num1 = int(input("Number 1: "))

        operator = input("Operator: ")

        if not valid_operators(operator):
            raise ValueError()

        num2 = int(input("Number 2: "))

        print(f'Result: {make_operation(num1, operator, num2)}')

    except ValueError as ve:
        print(ve)
        print('I know you are not stupid, try to put some valid input!')
        print()


def get_factorial():
    try:
        number = int(input("Number to search: "))

        print(f'Result: {Factorial().factorial(number)}')

    except ValueError as ve:
        print(ve)
        print('I know you are not stupid, try to put some valid input!')
        print()


def get_fibonacci():
    try:
        number = int(input("Number to search: "))

        print(f'Result: {Fibonacci().fibonacci(number)}')

    except ValueError as ve:
        print(ve)
        print('I know you are not stupid, try to put some valid input!')
        print()


while True:
    print('--- Super Calculator ---')
    print('1.- Basic Arithmetic')
    print('2. Factorial of a number')
    print('3. Fibonacci')
    print('4. Exit')
    option = int(input("Select an option: "))

    if option == 1:
        basic_arithmetic()
    elif option == 2:
        get_factorial()
    elif option == 3:
        get_fibonacci()
    elif option == 4:
        break
