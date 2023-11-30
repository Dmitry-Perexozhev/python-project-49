import prompt


def engine(brain_game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(brain_game.DESCRIPTION)
    count_correct_answers = 0
    while count_correct_answers < 3:
        correct_answer = brain_game.generate_round()
        user_answer = prompt.string('Your answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            count_correct_answers += 1
            count_correct_answers == 3
        else:
            print(f"'{user_answer}' is wrong answer ;(."
                  f" Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f"Congratulations, {name}!")
