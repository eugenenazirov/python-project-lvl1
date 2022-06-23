from brain_games import game_process


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
    username = game_process.welcome_user()
    success = 0
    finish = False
    mistake = False

    print("Find the greatest common divisor of given numbers.")

    while not finish and not mistake:
        first_number = game_process.generate_number()
        second_number = game_process.generate_number()
        question_gcd = f"{first_number}, {second_number}"
        correct_answer = str(find_gcd(first_number, second_number))

        turn = game_process.game_turn(question_gcd, correct_answer)
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
