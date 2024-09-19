# Birthday Email Sender

This project is a Python script that automates the process of sending personalized birthday emails. It reads data from a CSV file containing birthday information and uses a random email template to send birthday wishes to the person whose birthday matches today's date.

## Features

- Automatically reads birthdays from a CSV file.
- Sends customized birthday messages to recipients via email.
- Uses randomly selected letter templates for each email.

## Where to Use

This script can be used in various scenarios where automated birthday emails need to be sent:

- **Personal Use**: Send birthday greetings to family and friends.
- **Corporate Use**: Send birthday messages to employees or customers.
- **Community Groups**: Automate birthday emails for group members in social, non-profit, or interest-based communities.
- **Event Planners**: Use this tool to send personalized birthday reminders or greetings for clients or attendees.

## How it Works

1. The script reads the current date using Python’s `datetime` module.
2. It then reads the list of birthdays from the CSV file (`birthdays.csv`), which contains columns like `name`, `email`, `month`, and `day`.
3. It checks if today's date matches any of the dates in the CSV file.
4. If there's a match, the script:
   - Randomly selects one of the predefined email templates (`letter_1.txt`, `letter_2.txt`, etc.).
   - Replaces the placeholder `[NAME]` in the email template with the recipient’s actual name.
5. The script then connects to Gmail’s SMTP server using `smtplib`, logs in using your email credentials, and sends the email to the recipient.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python
- Required Python libraries:
  - `pandas`
  - `smtplib`
  - `random`
  - `datetime`