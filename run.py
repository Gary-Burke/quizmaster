import gspread
from random import shuffle
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Quizmaster")


def choose_category():
    """
    Ask user to choose a category from a list.
    Data is validated within this function to ensure a valid selection is made.
    To avoid spelling errors and typos,
    the user just has to type the corresponding category number instead.
    """
    while True:
        try:
            category = int(input("Choose your category:\n"))
            if category < 1 or category > 4:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1-4\n")
        else:
            match category:
                case 1:
                    return "sport"
                case 2:
                    return "science"
                case 3:
                    return "geography"
                case 4:
                    return "history"


def get_player_name():
    """
    Ask user to supply their name so that it can be
    used in a personalized message when the game is over.
    """
    print("\nFirst and most important question:")
    player_name = validate_empty_input("What is your name?\n")
    return player_name


def load_game(player, category):
    """
    Use the selected category from the user to load the correct worksheet.
    The worksheet contains the question and the answer in a list of lists.
    Randomize the order with shuffle method and return the list of lists
    """
    game = SHEET.worksheet(category).get_all_values()
    total = len(game)
    print(f"\nWelcome {player}!\n"
          f"You have chosen the category: {category.capitalize()}\n"
          f"We have a total of {total} questions for you. Good luck!\n"
          )
    shuffle(game)
    return game


def start_game(game):
    """
    Loop through the list of lists returned from function load_game.
    Display one question and ask user for an answer.
    Check user answer against stored answer and provide feedback.
    Use lower method to avoid spelling or typo mistakes.
    """
    total_questions = len(game)
    question_counter = 0
    correct_answers = 0

    while question_counter < total_questions:
        print(f"Question {question_counter + 1}:\n{game[question_counter][0]}")
        user_answer = validate_empty_input("Your answer:\n")
        correct_answer = game[question_counter][1].strip()
        alt_correct_answer = game[question_counter][2].strip()
        if (
            user_answer.lower() == correct_answer.lower()
            or user_answer.lower() == alt_correct_answer.lower()
        ):
            print(f"{correct_answer} is correct!\n")
            correct_answers += 1
        else:
            print(
                f"{user_answer} is the wrong answer!\n"
                f"The correct answer is: {correct_answer}\n"
            )
        question_counter += 1

    return correct_answers


def game_over(player, category, result, game):
    """
    Print a game over message to the user which
    includes the category, amount of correct answers and total questions
    """
    print(
        f"Well Done {player}!\n"
        f"You have completed the category of {category.capitalize()}.\n"
        f"You managed to get {result}/{len(game)} answers correct."
    )


# Solution for empty input from user from ChatGPT
def validate_empty_input(prompt):
    """
    Validates user input and ensures they don't submit an empty field
    """
    while True:
        data = input(prompt).strip()
        if data:
            return data
        print("You can't submit an empty response. Please try again.")


def main():
    category = choose_category()
    player = get_player_name()
    game = load_game(player, category)
    result = start_game(game)
    game_over(player, category, result, game)


print(
    "Welcome to QUIZMASTER!\n"
    "\n"
    "The rules are simple:\n"
    " - Press Enter to submit your responses\n"
    " - Choose a category by typing the corresponding number\n"
    " - Spelling matters!\n"
    "\n"
    "Categories:\n"
    " 1 - Sport\n"
    " 2 - Science\n"
    " 3 - Geography\n"
    " 4 - History\n"
)

main()
