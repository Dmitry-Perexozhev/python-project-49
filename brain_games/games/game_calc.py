from random import randint, choice


def game_calc():
    print('What is the result of the expression?')
    first_random_number = randint(1, 20)
    second_random_number = randint(1, 20)
    random_operation = choice('+-*')
    if random_operation == '+':
        correct_answer = str(first_random_number + second_random_number)
    elif random_operation == '-':
        correct_answer = str(first_random_number - second_random_number)
    elif random_operation == '*':
        correct_answer = str(first_random_number * second_random_number)
    print(f'Question: {first_random_number} {random_operation} '
          f'{second_random_number}')
    return correct_answer
