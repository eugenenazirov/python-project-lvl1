from brain_games.game_process import *


def get_question():
    random_number = generate_number()
    return random_number

def get_correct_answer(question_number):
    if question_number % 2 == 0:
        is_prime = question_number == 2
    else:
        d = 3
        while d * d <= question_number and question_number % d != 0:
            d += 2
        is_prime = d * d > question_number
    correct_answer = 'yes' if is_prime else 'no'
    return correct_answer


def prime_game():
    username = welcome_user()
    success = 0
    finish = False
    mistake = False

    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")

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
