from random import randint

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_round():
    random_number = randint(1, 100)
    correct_answer = 'yes' if is_even(random_number) else 'no'
    print(f'Question: {random_number}')
    return correct_answer
