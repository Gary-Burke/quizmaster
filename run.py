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
    To avoide spelling errors and typos,
    the user just has to type the corresponding category number instead.
    """
    while True:
        try:
            category = int(input("Choose your category: \n"))
            if category < 1 or category > 3:
                raise ValueError(
                    "Your selection is invalid, choose one number between 1-3")
        except ValueError as e:
            print(f"{e}, choose one number between 1-3")
            continue
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
    The worksheet contains the question and the answer in a list of lists
    """
    game = SHEET.worksheet(category).get_all_values()
    total = len(game)
    print(f"You have chosen the category: {category.capitalize()}\n"
          f"We have a total of {total} questions for you. Good luck!\n"
          )
    shuffle(game)


def main():
    category = choose_category()
    load_game(category)


print("Welcome to QUIZMASTER!\n"
      "\n"
      "The rules are simple:\n"
      "1. Press Enter to submit your responses\n"
      "2. Choose a category by typing the corresponding number\n"
      "3. Spelling matters!\n"
      "\n"
      "Categories:\n"
      "1 - Sport\n"
      "2 - Science\n"
      "3 - Geography\n"
      "\n"
      )

main()
