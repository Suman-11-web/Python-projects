# 🔐 Python Password Generator

## 📌 Introduction

Python Password Generator is a simple command-line application that creates strong and random passwords using Python. The program allows users to choose the desired password length and generates a secure password containing lowercase letters, uppercase letters, digits, and special symbols.

This project was built as part of my Python learning journey to understand modules, functions, loops, string manipulation, and secure random number generation.

---

## 🚀 Features

- Generate secure random passwords.
- User can choose the password length.
- Includes uppercase letters, lowercase letters, numbers, and symbols.
- Uses Python's `secrets` module for cryptographically secure password generation.
- Warns users when the password length is less than 8 characters.
- Handles invalid user input using exception handling.

---

## 🛠️ Technologies Used

- Python 3
- string module
- secrets module

---

## 📖 How It Works

1. The program starts by asking the user to enter the desired password length.
2. It creates a collection of lowercase letters, uppercase letters, digits, and special characters.
3. If the entered length is less than 8, the program automatically sets the minimum length to 8 for better security.
4. The `secrets.choice()` function randomly selects characters from the combined character set.
5. The generated password is displayed to the user.
6. If the user enters invalid input, an error message is shown instead of crashing the program.

---

## 💻 Example Output

```
Welcome to the Python Password Generator!

Enter the desired password length: 12

Your generated password is:
A@9kL#2mP!7x
```

### Invalid Input

```
Enter the desired password length:
hello

Invalid input! Please enter a valid integer for the password length.
```

---

## 📚 Python Concepts Used

- Functions
- User Input
- String Module
- Secrets Module
- Random Character Selection
- Loops
- Exception Handling
- Conditional Statements

---

## 🎯 Learning Outcome

This project helped me understand how secure passwords are generated using Python. It improved my knowledge of built-in modules, secure random number generation, input validation, and function design.

---

## 🔮 Future Improvements

- Allow users to include or exclude symbols.
- Allow users to include only numbers or letters.
- Copy generated password directly to clipboard.
- Generate multiple passwords at once.
- Build a graphical interface using Tkinter.
- Create a web version using Flask.

---

## 📂 Project Structure

```
password-generator/
│
├── password_generator.py
└── README.md
```

---

## 👨‍💻 Author

**Suman M**

This project is part of my Python learning journey and GitHub portfolio. I enjoy building beginner-friendly Python projects to improve my programming skills and gain practical experience.

I will continue creating more Python projects and exploring new technologies as I progress in software development.

⭐ If you like this project, consider giving it a star and sharing your feedback!
