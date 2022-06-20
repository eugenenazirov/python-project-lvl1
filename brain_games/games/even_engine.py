from brain_games.game_process import *


def get_question():
    random_number = generate_number()
    return random_number

def get_correct_answer(question_number):
    correct_answer = 'yes' if question_number % 2 == 0 else 'no'
    return correct_answer


def even_game():
    username = welcome_user()
    success = 0
    finish = False
    mistake = False

    while not finish and not mistake:
        question = get_question()
        correct_answer = get_correct_answer(question)

        turn = game_turn(question, correct_answer)
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