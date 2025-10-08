# Testing

> [!NOTE]  
> Return back to the [README.md](README.md) file.

## Code Validation

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| root | [run.py](https://github.com/Gary-Burke/quizmaster/blob/main/run.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/Gary-Burke/quizmaster/main/run.py) | ![screenshot](documentation/validation/py--run.png) |  |

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
| New Game | Feature is expected to let user choose to play another game. | Entered a valid positive response e.g. "y". | Program starts new game. | ![screenshot](documentation/defensive/new-game-yes.png) |
| New Game | Feature is expected to let user choose to play another game. | Entered a valid negative response e.g. "n". | Program clears terminal and ends itself. | ![screenshot](documentation/defensive/new-game-no.png) |
| Data Validation New Game | Feature is expected to catch any empty input. | Entered an empty input. | Program catches invalid input and informs user. | ![screenshot](documentation/defensive/new-game-empty.png) |

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
| As a player | I want to get feedback on my answers, whether they are right or wrong | and if wrong, I want to know what the actual correct answer is. | ![screenshot](documentation/features/04-quiz-feedback.png) |
| As a player | I would like to be able to submit my name in the game | to get a personalized feedback when the game is over. | ![screenshot](documentation/features/06-game-over.png) |
| As a player | it would be a good experience to see how many answers I got correct | so that I can challenge myself again next time. | ![screenshot](documentation/features/06-game-over.png) |
| As a player | I would like to be able to answer a question with a number or with text, e.g. "2" or "Two" | this would add to the user experience. | ![screenshot](documentation/features/05-answers.png) |
| As a player | I would like to be able to start another round of the quiz at the end of the game | this would add to the user experience and create a natural flow of events. | ![screenshot](documentation/features/07-new-game.png) |

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

