from random import randint


def game_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    random_number = randint(3, 100)
    correct_answer = 'yes'
    for i in range(2, random_number):
        if random_number % i == 0:
            correct_answer = 'no'
            break
    print(f'Question: {random_number}')
    return correct_answer
