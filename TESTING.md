# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

⚠️ INSTRUCTIONS ⚠️

The [CI Python Linter](https://pep8ci.herokuapp.com) can be used two different ways.

- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).

It's recommended to validate each file using the API URL. This will give you a custom URL which you can use on your testing documentation. It makes it easier to return back to a file for validating it again in the future. Use the steps above to generate your own custom URLs for each Python file.

**IMPORTANT**: `E501 line too long` errors

You must strive to fix all Python lines that are too long (>80 characters). In rare cases where you cannot break the lines [*without breaking the functionality*], adding "`  # noqa`" (*NO Quality Assurance*) to the end of those lines will ignore linting validation. Do not use "`  # noqa`" all over your project just to clear down validation errors! This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes variables can get too long, or excessive `if/else` conditional statements. These are acceptable instances to use the "`  # noqa`" comment.

When trying to fix "line too long" errors, try to avoid using `/` to split lines. A better approach would be to use any type of opening bracket, and hit `<Enter>` just after that. Any opening bracket type will work: `(`, `[`, `{`. By using an opening bracket, Python knows where to appropriately indent the next line of code, without having to *guess* for yourself and attempt to "tab" to the correct indentation level.

⚠️ --- END --- ⚠️

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | [run.py](https://github.com/Gary-Burke/quizmaster/blob/main/run.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/quizmaster/main/run.py) | ![screenshot](documentation/validation/py--run.png) | ⚠️ Notes (if applicable) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Feature | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Category Selection | Feature is expected to allow users to input the corresponding number of the category they would like to play. | Entered a valid selection. | Program moves to next step. | ![screenshot](documentation/defensive/category-valid.png) |
| Data Validation Category| Feature is expected to catch any number below 1. | Entered an invalid selection e.g. 0. | Program catches invalid input and informs user. | ![screenshot](documentation/defensive/category-min-range.png) |
| Data Validation Category| Feature is expected to catch any number above 4. | Entered an invalid selection e.g. 5. | Program catches invalid input and informs user. | ![screenshot](documentation/defensive/category-max-range.png) |
| Data Validation Category| Feature is expected to catch any input that is not an integer. | Entered an invalid selection e.g. string. | Program catches invalid input and informs user. | ![screenshot](documentation/defensive/category-string.png) |
| Data Validation Category| Feature is expected to catch any empty input. | Entered an empty input. | Program catches invalid input and informs user. | ![screenshot](documentation/defensive/category-empty.png) |
| Input Name | Feature is expected to let user add his name. | Entered a valid name e.g. string. | Program moves to next step. | ![screenshot](documentation/defensive/name-valid.png) |
| Data Validation Name | Feature is expected to catch any empty input. | Entered an empty input. | Program catches invalid input and informs user. | ![screenshot](documentation/defensive/name-empty.png) |
| Input Answer | Feature is expected to let user add his answer. | Entered a valid answer e.g. string. | Program moves to next step. | ![screenshot](documentation/defensive/answer-valid.png) |
| Data Validation Answer | Feature is expected to catch any empty input. | Entered an empty input. | Program catches invalid input and informs user. | ![screenshot](documentation/defensive/answer-empty.png) |

> [!NOTE]  
> As a player may use a pseudonym as a name and as answers might consist out of numbers, both of these inputs allow numbers as valid data.

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a player | it would be good to see a clear and concise landing page | so that I know what the game is about. | ![screenshot](documentation/features/01-category.png) |
| As a player | I want to see the rules clearly seperated from the welcome message | and kept short and direct. | ![screenshot](documentation/features/01-category.png) |
| As a player | it would be exciting if I could choose different categories | with which to play the quiz game. | ![screenshot](documentation/features/01-category.png) |
| As a player | it would be good to know how many questions there are in the selected quiz | so as to know the length of the game. | ![screenshot](documentation/features/03-welcome.png) |
| As a player | my input needs to be validated and a clear error message needs to be displayed when my input is invalid |  so as to ensure a proper and smooth gaming experience. | ![screenshot](documentation/defensive/category-string.png) |
| As a player |  I want to get feedback on my answers, whether they are right or wrong | and if wrong, I want to know what the actual correct answer is. | ![screenshot](documentation/features/04-quiz-feedback.png) |
| As a player |  I would like to be able to submit my name in the game | to get a personalized feedback when the game is over. | ![screenshot](documentation/features/06-game-over.png) |
| As a player |  it would be a good experience to see how many answers I got correct | so that I can challenge myself again next time. | ![screenshot](documentation/features/06-game-over.png) |
| As a player |   I would like to be able to answer a question with a number or with text, e.g. "2" or "Two" | this would add to the user experience. | ![screenshot](documentation/features/05-answers.png) |

## Bugs

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Gary-Burke/quizmaster?query=is%3Aissue%20is%3Aclosed%20label%3Abug&label=Fixed%20Bugs&color=green)](https://www.github.com/Gary-Burke/quizmaster/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/Gary-Burke/quizmaster/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/Gary-Burke/quizmaster/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/gh-issues/bug-closed.png)

### Unfixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search/Gary-Burke/quizmaster?query=is%3Aissue%2Bis%3Aopen%2Blabel%3Abug&label=Unfixed%20Bugs&color=red)](https://www.github.com/Gary-Burke/quizmaster/issues?q=is%3Aissue+is%3Aopen+label%3Abug)

Any remaining open issues can be tracked [here](https://www.github.com/Gary-Burke/quizmaster/issues?q=is%3Aissue+is%3Aopen+label%3Abug).

![screenshot](documentation/gh-issues/bug-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| The Python terminal doesn't work well with Safari, and sometimes users cannot type in the application. | n/a |
| If a user types `CTRL`+`C` in the terminal on the live site, they can manually stop the application and receive and error. | ![screenshot](documentation/testing/issues/ctrl-c.png) |

> [!IMPORTANT]  
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

