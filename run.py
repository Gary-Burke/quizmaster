import gspread
from random import shuffle
import re
from google.oauth2.service_account import Credentials
import colorama
from colorama import Fore
colorama.init(autoreset=True)

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("Quizmaster")

# These categories must correspond with the Google Sheets
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
    print(f"{Fore.CYAN} Categories:")
    for num, name in CATEGORIES.items():
        print(f"  {num}: {name.capitalize()}")


def choose_category():
    """
    Ask user to choose a category from a list.
    Data is validated within this function to ensure a valid selection is made.
    To avoid spelling errors and typos,
    the user just has to type the corresponding category number instead.
    """
    while True:
        try:
            choice = int(input(
                f"\n{Fore.CYAN} Choose your category (1-4):{Fore.RESET}\n "
            ))
            return CATEGORIES[choice]
        except (ValueError, KeyError):
            print(
                f"{Fore.RED} Invalid input.{Fore.RESET} "
                "Please enter a number between 1-4"
                )


def get_player_name():
    """
    Ask user to supply their name so that it can be
    used in a personalized message when the game is over.
    """
    print(f"\n{Fore.CYAN} First question:")

    while True:
        player_name = validate_input(
            " What is your username? (max. length 15. "
            "No Special characters)\n "
        )
        if len(player_name) > 15:
            print(
                f"\n{Fore.RED} Invalid Username. {Fore.RESET}"
                "Username must not exceed 15 characters.\n"
                " Please try again.\n"
            )
        else:
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
        print(f"\n{Fore.MAGENTA} Welcome {player}!{Fore.RESET}\n"
              f" You have chosen the category: "
              f"{Fore.MAGENTA}{category.capitalize()}{Fore.RESET}\n"
              f" We have a total of {Fore.MAGENTA}{total} questions "
              f"{Fore.RESET}for you. Good luck!\n"
              )
    else:
        print(f"\n{Fore.MAGENTA} Okay {player}, get ready...{Fore.RESET}\n"
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
            f"{Fore.CYAN} Question {question_counter + 1}:"
            f"{Fore.RESET} {game[question_counter][0]}"
        )
        user_answer = validate_input(" Your answer:\n ")
        correct_answer = game[question_counter][1].strip()
        alt_correct_answer = game[question_counter][2].strip()
        if (
            user_answer.lower() == correct_answer.lower()
            or user_answer.lower() == alt_correct_answer.lower()
        ):
            print(
                f"{Fore.YELLOW} {correct_answer} {Fore.RESET}is the"
                f"{Fore.GREEN} CORRECT {Fore.RESET}answer!\n"
            )
            correct_answers += 1
        else:
            print(
                f"{Fore.YELLOW} {user_answer}{Fore.RESET} is the"
                f"{Fore.RED} WRONG {Fore.RESET}answer!\n"
                f" The correct answer is: {Fore.GREEN}{correct_answer}\n"
            )
        question_counter += 1

    return correct_answers


def game_over(player, category, result, game):
    """
    Print a game over message to the user which
    includes the category, amount of correct answers and total questions
    """
    print(
        f"{Fore.MAGENTA} Well Done {player}!{Fore.RESET}\n"
        f" You have completed the category: {Fore.MAGENTA}"
        f"{category.capitalize()}.{Fore.RESET}\n"
        f" You managed to get {Fore.MAGENTA}{result}/{len(game)}"
        f" {Fore.RESET}answers correct.\n"
    )


def validate_input(prompt):
    """
    Validates user input and ensures they don't submit an empty field.
    Using the re library, we limit the input here to contain only
    letters, numbers, spaces, '_' and '-'
    """
    allowed_char = re.compile(r"^[A-Za-z0-9_ -]+$")
    while True:
        user_input = input(prompt).strip()
        if (allowed_char.fullmatch(user_input)) and (len(user_input) > 0):
            return user_input
        print(
            f"{Fore.RED}\n Invalid Input! {Fore.RESET}Input can't be empty"
            " and may only contain\n"
            " letters, numbers, spaces, '_' and '-'. "
            "Please try again.\n"
        )


def new_game(player):
    """
    When game is over, this function will prompt
    the user into playing another game.
    """
    while True:
        try:
            answer = validate_input(
                f" {Fore.CYAN}Would you like to play again? (y/n)"
                f"\n{Fore.RESET} ").lower()
            if answer in ("y", "ye", "yes", "y."):
                print(f"\n {Fore.MAGENTA}Correct answer {player}!\n")
                print_categories()
                return True
            elif answer in ("n", "no", "n."):
                print("\033c")
                return False
            else:
                raise ValueError(
                    f"\n{Fore.RED} Invalid input! {Fore.RESET}"
                    "Type 'y' or 'n'. Please try again."
                )

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


print("\033c")  # Clear terminal before printing

print(
    f"{Fore.MAGENTA} Welcome to QUIZMASTER!\n"
    f"\n{Fore.RESET}"
    f"{Fore.CYAN} The rules are simple:\n"
    f"{Fore.RESET}  - Press Enter to submit your responses\n"
    "  - Choose a category by typing the corresponding number\n"
    "  - Spelling matters!\n"
)

print_categories()

main()
