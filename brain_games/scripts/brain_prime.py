#!/usr/bin/env python3
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


def brain_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count_correct_answers = 0
    while count_correct_answers < 3:
        random_number = randint(3, 100)
        correct_answer = 'yes'
        for i in range(2, random_number):
            if random_number % i == 0:
                correct_answer = 'no'
                break
        print(f'Question: {random_number}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
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
    brain_prime()


if __name__ == '__main__':
    main()
