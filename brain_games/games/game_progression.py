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
    random_sequence = get_sequence(random_start_number,
                                   random_step, number_of_steps)
    random_sequence_str = list(map(str, random_sequence))
    random_index_of_seq = randint(0, number_of_steps - 1)
    correct_answer = random_sequence_str[random_index_of_seq]
    random_sequence_str[random_index_of_seq] = '..'
    question = 'Question: ' + ' '.join(random_sequence_str)
    return correct_answer, question
