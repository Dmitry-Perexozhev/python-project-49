import prompt
from random import randint, choice


def welcome_user():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def greeting():
    print('Welcome to the Brain Games!')


def try_again(name):
    print(f"Let's try again, {name}!")


def congratulations(name):
    print(f"Congratulations, {name}!")


def brain_gcd():
    print('Find the greatest common divisor of given numbers.')
    count_correct_answers = 0
    while count_correct_answers < 3:
        first_random_number = randint(1, 100)
        second_random_number = randint(1, 100)
        correct_answer = 1
        for i in range(2, min(first_random_number, second_random_number)+1):
            if first_random_number % i == 0 and second_random_number % i == 0:
                correct_answer = i
        print(f'Question: {first_random_number} {second_random_number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == str(correct_answer):
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            try_again(name)
            break
    if count_correct_answers == 3:
        congratulations(name)


def main():
    greeting()
    welcome_user()
    brain_gcd()


if __name__ == '__main__':
    main()
