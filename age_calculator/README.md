# 🎂 Python Age Calculator

## 📌 Introduction

Python Age Calculator is a simple command-line application that calculates a person's current age based on their date of birth. The project asks the user to enter their birth year, month, and day, then calculates the exact age using Python's built-in `datetime` module.

This project was developed as part of my Python learning journey to practice working with dates, user input, functions, conditional statements, and exception handling.

---

## 🚀 Features

- Calculates age from the user's date of birth.
- Uses Python's built-in `datetime` module.
- Validates invalid calendar dates.
- Prevents future birth dates.
- Handles invalid input using exception handling.
- Beginner-friendly and easy to understand.

---

## 🛠️ Technologies Used

- Python 3
- datetime module

---

## 📖 How It Works

1. The program asks the user to enter their birth year.
2. It asks for the birth month.
3. It asks for the birth day.
4. A date object is created using the entered values.
5. The program compares the birth date with today's date.
6. If the birth date is in the future, an error message is displayed.
7. Otherwise, the program calculates the user's current age and displays it.
8. Invalid dates or non-numeric input are handled gracefully without crashing the program.

---

## 💻 Example Output

```
--- Python Age Calculator ---

Enter birth year: 2005
Enter birth month: 7
Enter birth day: 11

You are exactly 20 years old.
```

### Invalid Input

```
Enter birth year: 2028
Enter birth month: 5
Enter birth day: 10

Error: Birth date cannot be in the future.
```

### Invalid Date

```
Enter birth year: 2004
Enter birth month: 2
Enter birth day: 31

Error: Please enter valid numbers and calendar dates.
```

---

## 📚 Python Concepts Used

- Functions
- User Input
- Integer Type Conversion
- datetime Module
- Date Objects
- Conditional Statements
- Exception Handling
- Comparison Operators

---

## 🎯 Learning Outcome

This project helped me understand how to work with dates in Python and how to build programs that interact with users safely. It also improved my understanding of input validation and error handling using `try` and `except`.

---

## 🔮 Future Improvements

- Display age in years, months, and days.
- Calculate the number of days until the next birthday.
- Support different date formats.
- Build a graphical interface using Tkinter.
- Create a web version using Flask or Django.

---

## 📂 Project Structure

```
age_calculator/
│
├── age_calculator.py
└── README.md
```

---

## 👨‍💻 Author

**Suman M**

This project was created while learning Python programming and is part of my beginner project collection on GitHub. I enjoy building simple projects to strengthen my programming skills and explore new technologies.

If you found this project useful, feel free to fork the repository and give it a ⭐.
