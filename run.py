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
