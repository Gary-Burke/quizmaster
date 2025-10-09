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

CATEGORIES = {
    1: "sport",
    2: "science",
    3: "geography",
    4: "history",
}


def print_categories():
    """
    Prints the heading 'Categories:' and lists all the items from
    the dictionary CATEGORIES.
    """
    print(" Categories:")
    for num, name in CATEGORIES.items():
        print(f"  {num} - {name.capitalize()}")


def choose_category():
    """
    Ask user to choose a category from a list.
    Data is validated within this function to ensure a valid selection is made.
    To avoid spelling errors and typos,
    the user just has to type the corresponding category number instead.
    """
    while True:
        try:
            choice = int(input("\n Choose your category (number):\n"))
            return CATEGORIES[choice]
        except (ValueError, KeyError):
            print(" Invalid input. Please enter a number between 1-4")


def get_player_name():
    """
    Ask user to supply their name so that it can be
    used in a personalized message when the game is over.
    """
    print("\n First and most important question:")
    player_name = validate_empty_input(" What is your name?\n")
    return player_name


def load_game(player, category, first_round):
    """
    Use the selected category from the user to load the correct worksheet.
    The worksheet contains the question and the answer in a list of lists.
    Randomize the order with shuffle method and return the list of lists.
    Two different messages based on whether it is the first game or a restart.
    """
    game = SHEET.worksheet(category).get_all_values()
    total = len(game)
    if first_round:
        print(f"\n Welcome {player}!\n"
              f" You have chosen the category: {category.capitalize()}\n"
              f" We have a total of {total} questions for you. Good luck!\n"
              )
    else:
        print(f"\n Okay {player}, get ready...\n"
              f" You have chosen the category: {category.capitalize()}\n"
              f" We have a total of {total} questions for you. Good luck!\n"
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
        print(
            f" Question {question_counter + 1}:"
            f" {game[question_counter][0]}"
        )
        user_answer = validate_empty_input(" Your answer:\n")
        correct_answer = game[question_counter][1].strip()
        alt_correct_answer = game[question_counter][2].strip()
        if (
            user_answer.lower() == correct_answer.lower()
            or user_answer.lower() == alt_correct_answer.lower()
        ):
            print(f" {correct_answer} is correct!\n")
            correct_answers += 1
        else:
            print(
                f" {user_answer} is the wrong answer!\n"
                f" The correct answer is: {correct_answer}\n"
            )
        question_counter += 1

    return correct_answers


def game_over(player, category, result, game):
    """
    Print a game over message to the user which
    includes the category, amount of correct answers and total questions
    """
    print(
        f" Well Done {player}!\n"
        f" You have completed the category of {category.capitalize()}.\n"
        f" You managed to get {result}/{len(game)} answers correct.\n"
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
        print(" You can't submit an empty response. Please try again.")


def new_game(player):
    """
    When game is over, this function will prompt
    the user into playing another game.
    """
    while True:
        try:
            answer = validate_empty_input(
                " Would you like to play again? (y/n)\n").lower()
            if answer in ("y", "ye", "yes", "y."):
                print(f"\n A Wise Decision {player}.\n")
                print_categories()
                return True
            elif answer in ("n", "no", "n."):
                print("\033c")
                return False
            else:
                raise ValueError("Type y or n to confirm. Please try again\n")

        except ValueError as e:
            print(e)


def main():
    player = get_player_name()
    restart_game = True
    first_round = True
    while restart_game:
        category = choose_category()
        game = load_game(player, category, first_round)
        result = start_game(game)
        game_over(player, category, result, game)
        restart_game = new_game(player)
        first_round = False


print(
    " Welcome to QUIZMASTER!\n"
    "\n"
    " The rules are simple:\n"
    "  - Press Enter to submit your responses\n"
    "  - Choose a category by typing the corresponding number\n"
    "  - Spelling matters!\n"
)
print_categories()
main()
