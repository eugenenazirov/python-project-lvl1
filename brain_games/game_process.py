import random
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    return user_name


def generate_number():
    return random.randint(1, 50)


def is_correct(correct_answer, user_answer):
    return True if correct_answer == user_answer else False


def game_turn(question, correct_answer):
    print(f"Question: {question}")

    user_answer = prompt.string("Your answer: ")

    if is_correct(correct_answer, user_answer):
        print("Correct!")
        return True
    else:
        print(f"\'{user_answer}\' is wrong answer ;(. \
            Correct answer was \'{correct_answer}\'.")
        return False


def congratulate_user(username):
    print(f"Congratulations, {username}!")


def fail_user(username):
    print(f"Let's try again, {username}!")
