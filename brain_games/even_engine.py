import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    return user_name


def generate_number():
    return random.randint(0, 100)


def is_correct(random_number, user_answer):
    correct_answer = 'yes' if random_number % 2 == 0 else 'no'
    return True if correct_answer == user_answer else False


def game_turn(random_number):
    print(f"Question: {random_number}")

    user_answer = prompt.string(f"Your answer: ")
    opposite_answer = 'no' if user_answer == 'yes' else 'yes'

    if is_correct(random_number, user_answer):
        print("Correct!")
        return True
    else:
        print(f"{user_answer} is wrong answer ;(. Correct answer was {opposite_answer}")
        return False


def congratulate_user(username):
    print(f"Congratulations, {username}!")


def fail_user(username):
    print(f"Let's try again, {username}!")


def run_game():
    username = welcome_user()
    success = 0
    finish = False
    mistake = False

    while not finish and not mistake:
        turn = game_turn(generate_number())

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
