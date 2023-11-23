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


def brain_calc():
    print('What is the result of the expression?')
    count_correct_answers = 0
    while count_correct_answers < 3:
        first_random_number = randint(1, 20)
        second_random_number = randint(1, 20)
        random_operation = choice('+-*')
        if random_operation == '+':
            correct_answer = str(first_random_number + second_random_number)
        elif random_operation == '-':
            correct_answer = str(first_random_number - second_random_number)
        elif random_operation == '*':
            correct_answer = str(first_random_number * second_random_number)
        print(f'Question: {first_random_number} {random_operation} {second_random_number}')
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
    brain_calc()


if __name__ == '__main__':
    main()
