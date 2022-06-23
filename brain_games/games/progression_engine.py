from brain_games import game_process
from random import randint


def get_progression():
    progression_lenght = randint(5, 11)
    progression_num = game_process.generate_number()
    progression_step = randint(2, 10)
    progression_list = []

    for i in range(progression_lenght):
        progression_list.append(progression_num)
        progression_num += progression_step
    return progression_list


def hide_number(progression):
    choosen_num_index = randint(1, len(progression) - 1)
    choosen_num = progression[choosen_num_index]
    progression[choosen_num_index] = ".."
    progression_str = " ".join(map(str, progression))
    return (progression_str, choosen_num)


def progression_game():
    username = game_process.welcome_user()
    success = 0
    finish = False
    mistake = False

    print("What number is missing in the progression?")

    while not finish and not mistake:
        progression = get_progression()
        question_progression, hidden_number = hide_number(progression)
        correct_answer = str(hidden_number)

        turn = game_process.game_turn(question_progression, correct_answer)
        if turn:
            success += 1
        else:
            mistake = True

        if success == 3:
            finish = True

    if finish:
        game_process.congratulate_user(username)
    if mistake:
        game_process.fail_user(username)
