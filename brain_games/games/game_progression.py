from random import randint

DESCRIPTION = 'What number is missing in the progression?'


def get_sequence(start, step, number_of_steps):
    sequence = []
    for i in range(number_of_steps):
        sequence.append(start + step * i)
    return sequence


def generate_round():
    random_start_number = randint(1, 20)
    random_step = randint(1, 10)
    number_of_steps = 10
    random_sequence =\
        get_sequence(random_start_number, random_step, number_of_steps)
    random_index_of_seq = randint(0, number_of_steps - 1)
    correct_answer = str(random_sequence[random_index_of_seq])
    random_sequence[random_index_of_seq] = '..'
    print('Question:', *random_sequence)
    return correct_answer
