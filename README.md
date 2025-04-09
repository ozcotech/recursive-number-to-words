# Recursive Number to Words Converter

A simple Python program that takes a 4-digit number as input and converts it into its English word form using real recursion.

---

## 🧠 How It Works

- The program asks the user to enter a **numeric 4-digit number**.
- If the input is invalid (not a number or not 4 digits), the program displays an error and gives the user another chance.
- Once a valid number is entered, it is converted into its English words using a **recursive function**.
- After successful conversion, the result is printed and the program ends.

---

## 🚀 Features

- Uses **real recursion** (a function that calls itself) to handle each digit.
- Supports special cases like numbers from **10 to 19** (e.g., `1113 → one thousand one hundred thirteen`).
- Handles input validation using `try-except` for non-numeric inputs.
- Allows **retries only on error** (if the number is valid, the program exits after printing the result).

---

## 📂 File Structure

- `numbers_to_words.py` → Main script

---

## 🧪 Sample Output
```bash
Please enter a 4-digit number: abcd
Invalid input. Please enter a numeric 4-digit number.
```

```bash
Please enter a 4-digit number: 123
Please enter a 4-digit number.
```

```bash
Please enter a 4-digit number: 1985
The written form of the number '1985' is: one thousand nine hundred eighty five
```
---

## 📝 Extension Ideas
	•	Add support for numbers above 9999 (e.g., ten thousand, hundred thousand).
	•	Implement Turkish or multilingual support.
	•	Build a GUI version with Tkinter or Kivy.
	•	Package it as a CLI tool.

---

## 🛠️ How to Run

```bash
python3 numbers_to_words.py
```

📌 You can also check out my [personal portfolio](https://ozco.studio) for more projects and experiments.

