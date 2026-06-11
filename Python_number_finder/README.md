# 🔢 Even and Odd Finder

## 📌 Introduction

Even and Odd Finder is a simple Python project developed to identify whether a number entered by the user is even or odd. This project was created as part of my Python learning journey to practice basic programming concepts and improve problem-solving skills.

The program continuously accepts user input until the user types **"exit"**. It also handles invalid input gracefully using exception handling, making the application more reliable and user-friendly.

---

## 🚀 Features

- Checks whether a number is even or odd.
- Accepts unlimited user inputs.
- Exit option by typing **exit**.
- Handles invalid input without crashing.
- Uses functions for better code organization.
- Uses exception handling (`try` and `except`).
- Beginner-friendly project.

---

## 🛠️ Technologies Used

- Python 3

---

## 📖 How the Program Works

1. The program starts by calling the `num_finder()` function.
2. It asks the user to enter a number.
3. If the user enters **exit**, the program displays a goodbye message and stops.
4. Otherwise, the input is converted into an integer.
5. The modulus (`%`) operator checks whether the number is divisible by 2.
6. If the remainder is 0, the number is even.
7. Otherwise, the number is odd.
8. If the user enters invalid data, an error message is displayed and the program continues running.

---

## 💻 Example

```
Enter number: 20
20 is an Even Number

Enter number: 15
15 is an Odd Number

Enter number: hello
Invalid Input

Enter number: exit
Goodbye
```

---

## 📚 Python Concepts Used

- Functions
- While Loop
- If-Else Statements
- User Input
- Integer Conversion
- Modulus Operator
- Try and Except
- Break Statement

---

## 🎯 Learning Outcome

By building this project, I learned how to:

- Create reusable functions.
- Use loops for continuous execution.
- Take input from users.
- Validate user input.
- Handle exceptions without crashing the program.
- Apply conditional statements to solve real problems.

---

## 🔮 Future Improvements

- Add Positive/Negative Number Checker.
- Count total Even and Odd numbers entered.
- Save results to a text file.
- Build a graphical interface using Tkinter.
- Add support for checking multiple numbers at once.

---

## 📂 Project Structure

```
/Python_number_finder
│
├── num_finder.py
└── README.md
```

---

## 👨‍💻 Author

**Suman M**

This project was created while learning Python programming and is one of my beginner projects uploaded to GitHub. I will continue building more projects to improve my coding skills and explore new technologies.

⭐ If you like this project, feel free to fork it and give it a star!
