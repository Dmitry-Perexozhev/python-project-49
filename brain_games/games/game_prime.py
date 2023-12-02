from random import randint

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number >= 2:
        if number == 2:
            return True
        divider = 2
        while number % divider != 0:
            divider += 1
        return number == divider
    else:
        return False


def generate_round():
    random_number = randint(2, 100)
    correct_answer = 'yes' if is_prime(random_number) else 'no'
    question = f'Question: {random_number}'
    return correct_answer, question
