from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def find_divisors(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]
    return divisors


def generate_round():
    first_random_number = randint(1, 100)
    second_random_number = randint(1, 100)
    divisors_of_first_random_number = set(find_divisors(first_random_number))
    divisors_of_second_random_number = set(find_divisors(second_random_number))
    correct_answer =\
        max(divisors_of_first_random_number & divisors_of_second_random_number)
    print(f'Question: {first_random_number} {second_random_number}')
    return str(correct_answer)
