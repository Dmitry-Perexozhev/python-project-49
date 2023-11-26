from random import randint


def game_gcd():
    print('Find the greatest common divisor of given numbers.')
    first_random_number = randint(1, 100)
    second_random_number = randint(1, 100)
    correct_answer = 1
    for i in range(2, min(first_random_number, second_random_number) + 1):
        if first_random_number % i == 0 and second_random_number % i == 0:
            correct_answer = i
    print(f'Question: {first_random_number} {second_random_number}')
    return str(correct_answer)
        