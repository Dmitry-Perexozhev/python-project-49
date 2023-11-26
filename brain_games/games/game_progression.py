from random import randint


def game_progression():
    print('What number is missing in the progression?')
    random_start_number = randint(1, 20)
    random_step = randint(1, 10)
    random_sequence = []
    for i in range(10):
        random_sequence.append(random_start_number + random_step * i)
    random_index_of_seq = randint(0, 9)
    correct_answer = str(random_sequence[random_index_of_seq])
    random_sequence[random_index_of_seq] = '..'
    print('Question:', *random_sequence)
    return correct_answer
