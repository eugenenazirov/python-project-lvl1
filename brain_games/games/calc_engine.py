from brain_games.game_process import *


def calculate(first_number, second_number):
    if first_number > second_number and second_number < 10:
        action = random.choice(['+', '-', '*'])
    elif second_number < 10:
        action = random.choice(['+', '*'])
    else:
        action = '+'

    if action == '+':
        result = first_number + second_number
    elif action == '-':
        result = first_number - second_number
    else:
        result = first_number * second_number
    return (action, result)


def calc_game():
    username = welcome_user()
    success = 0
    finish = False
    mistake = False

    print("What is the result of the expression?")

    while not finish and not mistake:
        first_number = generate_number()
        second_number = generate_number()
        question_tuple = calculate(first_number, second_number)
        question_str = f"{first_number} {question_tuple[0]} {second_number}"
        correct_answer = str(question_tuple[1])

        turn = game_turn(question_str, correct_answer)
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
