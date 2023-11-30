from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def add(x, y):
    return x + y


def multiply(x, y):
    return x * y


def subtraction(x, y):
    return x - y


def generate_round():
    first_random_number = randint(1, 20)
    second_random_number = randint(1, 20)
    random_operation = choice('+-*')
    if random_operation == '+':
        correct_answer =\
            str(add(first_random_number, second_random_number))
    elif random_operation == '-':
        correct_answer =\
            str(subtraction(first_random_number, second_random_number))
    elif random_operation == '*':
        correct_answer =\
            str(multiply(first_random_number, second_random_number))
    print(f'Question: {first_random_number} {random_operation} '
          f'{second_random_number}')
    return correct_answer
