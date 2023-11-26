import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def engine(brain_game):
    count_correct_answers = 0
    while count_correct_answers < 3:
        correct_answer = brain_game()
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            count_correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    if count_correct_answers == 3:
        print(f"Congratulations, {name}!")