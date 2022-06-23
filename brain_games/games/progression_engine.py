from brain_games.game_process import *
from random import randint


def get_progression():
    progression_lenght = randint(5, 11)
    progression_num = generate_number()
    progression_step = randint(2, 10)
    progression_list = []

    for i in range(progression_lenght):
        progression_list.append(progression_num)
        progression_num += progression_step
    return progression_list

def hide_number(progression):
    choosen_num_index = randint(1, len(progression))
    choosen_num = progression[choosen_num_index]
    progression[choosen_num_index] = ".."
    return (progression, choosen_num)



def progression_game():
    username = welcome_user()
    success = 0
    finish = False
    mistake = False

    print("What number is missing in the progression?")

    while not finish and not mistake:
        progression = get_progression()
        question_progression, hidden_number = hide_number(progression)
        correct_answer = str(hidden_number)

        turn = game_turn(question_progression, correct_answer)
        if turn:
            success += 1
        else:
            mistake = True

        if success == 3:
            finish = True

    if finish:
        congratulate_user(username)
    if mistake:
        fail_user(username)
