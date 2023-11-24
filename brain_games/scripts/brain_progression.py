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


def brain_progression():
    print('What number is missing in the progression?')
    count_correct_answers = 0
    while count_correct_answers < 3:
        random_start_number = randint(1, 20)
        random_step = randint(1, 10)
        random_sequence = []
        for i in range(10):
            random_sequence.append(random_start_number + random_step * i)
        random_index_of_seq = randint(0, 9)
        correct_answer = str(random_sequence[random_index_of_seq])
        random_sequence[random_index_of_seq] = '..'
        print('Question:', *random_sequence)
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
    brain_progression()


if __name__ == '__main__':
    main()
