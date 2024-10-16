# Quiz Application

This repo contains a simple Python-based quiz application that presents multiple-choice questions to users, tracks their score, and shows the final results upon completion.

## Project Structure

- **question_model.py**  
  Contains the `Question` class. Each `Question` object has two attributes: 
  - `text`: The quiz question.
  - `answer`: The correct answer to the question.
  
- **data.py**  
  Contains the `question_data`, a list of dictionaries where each dictionary represents a quiz question and its correct answer.

- **quiz_brain.py**  
  Contains the `QuizBrain` class that manages the core functionality of the quiz, including:
  - Storing the list of questions.
  - Presenting the next question.
  - Checking if the user's answer is correct.
  - Keeping track of the score and the question number.

- **ui.py**  
  Implements the user interface (UI) using `tkinter`. It manages the display of questions and interacts with the user for answering, while updating the score in real-time.

## Features

- **Interactive User Interface**: The quiz has a graphical interface built with `tkinter`, making it easy and engaging for users to interact with the questions.
- **Real-time Feedback**: The user is immediately informed whether their answer is correct or incorrect after each question.
- **Score Tracking**: The quiz tracks and displays the user's current score in real-time.
- **Multiple-choice Questions**: The questions are presented in a multiple-choice format, allowing users to select their answers by clicking.
- **Completion Summary**: After the user completes the quiz, a final score summary is displayed.
- **Dynamic Question Loading**: The application pulls questions dynamically from a pre-defined data source.



