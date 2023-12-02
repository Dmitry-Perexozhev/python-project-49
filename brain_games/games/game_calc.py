from random import randint, choice

DESCRIPTION = 'What is the result of the expression?'


def calculate(x, y, operator):
    func = {'+': x + y, '-': x - y, '*': x * y}
    return func[operator]


def generate_round():
    first_random_number = randint(1, 20)
    second_random_number = randint(1, 20)
    random_operation = choice('+-*')
    correct_answer = str(calculate(first_random_number,
                                   second_random_number, random_operation))
    question = (f'Question: {first_random_number} {random_operation} '
                f'{second_random_number}')
    return correct_answer, question
