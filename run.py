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
            if category < 1 or category > 3:
                raise ValueError
        except ValueError:
            print("Invalid input. Please enter a number between 1-3")
        else:
            match category:
                case 1:
                    return "sport"
                case 2:
                    return "science"
                case 3:
                    return "geography"


def load_game(category):
    """
    Use the selected category from the user to load the correct worksheet.
    The worksheet contains the question and the answer in a list of lists.
    Randomize the order with shuffle method and return the list of lists
    """
    game = SHEET.worksheet(category).get_all_values()
    total = len(game)
    print(f"You have chosen the category: {category.capitalize()}\n"
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
        user_answer = input("Your answer:\n")
        if user_answer.lower() == game[question_counter][1].lower():
            print("That is correct!\n")
            correct_answers += 1
        else:
            print(f"That is incorrect! The correct answer is:\n"
                  f"{game[question_counter][1]}\n"
                  )
        question_counter += 1

    return correct_answers


def game_over(category, result, game):
    """
    Print a game over message to the user which
    includes the category, amount of correct answers and total questions
    """
    print("CONGRATULATIONS!\n"
          f"You have completed the category of {category.capitalize()} and "
          f"managed to get {result}/{len(game)} answers correct."
          )


def main():
    category = choose_category()
    game = load_game(category)
    result = start_game(game)
    game_over(category, result, game)


print("Welcome to QUIZMASTER!\n"
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
      )

main()
