from brain_games.game_process import *


def find_gcd(first_number, second_number):
    a = first_number
    b = second_number
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a + b


def gcd_game():
    username = welcome_user()
    success = 0
    finish = False
    mistake = False

    print("Find the greatest common divisor of given numbers.")

    while not finish and not mistake:
        first_number = generate_number()
        second_number = generate_number()
        question_gcd = f"{first_number}, {second_number}"
        correct_answer = str(find_gcd(first_number, second_number))

        turn = game_turn(question_gcd, correct_answer)
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
