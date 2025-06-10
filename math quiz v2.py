import random

def yes_no(question):
    """Checks user response to a question is yes / no (y/n), returns 'yes' or 'no' """

    while True:

        response = input(question).lower()

        # check the user says yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes / no")


def instructions():
    """Prints instructions"""

    print("""
*** Instructions ****

To begin, choose the number of rounds (or press <enter> for infinite mode).

Then you pick any integer to answer the following questions.

    Good luck!🤞🏽
    """)

def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more."

        to_check = input(question)

        try:
            response = int(to_check)

            # checks that the number is more than / equal 13
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

def do_math(a, b, operator):

    if operator == 1:
        ans = a + b
    elif operator == 2:
        ans = a - b
    elif operator == 3:
        ans = a * b
    elif operator == 4:
        ans = a
        a = a * b
    question_string = f"{a} {op_list[operator - 1]} {b} = "

    return question_string, ans


# Main routine:
print("Welcome to the mathematics quiz 😁")

# ask the user if they want instructions (check they say yes / no)
want_instructions = yes_no("Do you want to see the instructions? ")

# Display the instructions if the user wants to see them...
if want_instructions == "yes":
    instructions()

# Initialise game variables
rounds_played = 0
op_list = ["+", "-", "*", "/"]
# initialise list to hold game history
game_history = []

# Ask user for number of rounds / infinite mode
num_rounds = int_check("How many rounds would you like? ")

# Game loop starts here
while rounds_played < num_rounds:

    print(f"\n😃😃😃 Question {rounds_played + 1} of {num_rounds} 😃😃😃 ")

    num_1 = random.randint(1, 50)
    num_2 = random.randint(1, 50)
    op = random.randint(1, 4)

    question, answer = do_math(num_1, num_2, op)

    user_ans = int_check(question)
    if user_ans == answer:
        print(f"Your answer is correct !!😏😏")
        print()
    else:
        print(f"Your answer isn't correct🤣🤣 Try again..")
        print()
    game_history.append(f" {question} = {answer}, Your answer was {user_ans}")
    rounds_played += 1

# ask the user if they want game history (check they say yes / no)
want_history = yes_no("Do you want to see game history? ")
# Display the game history if the user wants to see them...
if want_history == "yes":
    print("Game History")

    for item in game_history:
        print(item)













