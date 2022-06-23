from brain_games import game_process


def get_question():
    random_number = game_process.generate_number()
    return random_number


def get_correct_answer(question_number):
    correct_answer = 'yes' if question_number % 2 == 0 else 'no'
    return correct_answer


def even_game():
    username = game_process.welcome_user()
    success = 0
    finish = False
    mistake = False

    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")

    while not finish and not mistake:
        question = get_question()
        correct_answer = get_correct_answer(question)

        turn = game_process.game_turn(question, correct_answer)
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
