# Email Extractor Automation

## CodeAlpha Python Programming Internship — Task 3

A simple Python automation program that reads a text file, extracts email addresses using Regular Expressions, displays them in the console, and saves the extracted email addresses into a separate text file.

## Features

* Reads text from a `.txt` file
* Automatically finds email addresses
* Uses Regular Expressions
* Displays extracted email addresses
* Saves extracted emails to `emails.txt`
* Runs completely in the console

## Technologies Used

* Python
* `re` module
* File handling
* Regular Expressions
* Lists
* Loops

## How It Works

1. The program reads the `sample.txt` file.
2. A Regular Expression pattern is used to identify email addresses.
3. All matching email addresses are extracted.
4. The extracted emails are displayed in the terminal.
5. The emails are saved to `emails.txt`.

## Sample Input


Hello,

You can contact us at support@example.com.

For internship queries, email internship@codealpha.com.

You can also contact hr@example.org for HR related questions.

Thank you.


## Sample Output

Email Extractor
----------------
Email addresses found:
support@example.com
internship@codealpha.com
hr@example.org

Email addresses saved to emails.txt


## Project Structure

Task3_Email_Extractor/

 1. email_extractor.py
 2. sample.txt
 3. emails.txt
 4. README.md


## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run: python email_extractor.py


## Internship Task

This project is completed as part of the CodeAlpha Python Programming Internship.

**Task:** Task 3 — Automation: Extract Email Addresses from a Text File
