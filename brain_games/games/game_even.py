from random import randint


def game_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    random_number = randint(1, 100)
    correct_answer = ('yes', 'no')[random_number % 2]
    print(f'Question: {random_number}')
    return correct_answer
