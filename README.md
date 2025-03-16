# PyQt6 Calculator

## Overview
This is a simple calculator application built using PyQt6. It provides basic arithmetic operations such as addition, subtraction, multiplication, and division. The user interface consists of a display screen and a grid of buttons for number input and operations.

## Features
- Basic arithmetic operations (+, -, *, /)
- Clear and delete functions
- User-friendly GUI
- Styled using the Fusion theme

## Installation
To run this calculator, ensure you have Python installed along with the required dependencies.

### Prerequisites
You need to install `PyQt6` if it is not already installed:

```sh
pip install PyQt6
```

## Running the Application
To launch the calculator, run the following command in your terminal or command prompt:

```sh
python calculator.py
```

## Usage
1. Click the numeric buttons to input numbers.
2. Click the operation buttons (+, -, *, /) to perform calculations.
3. Use the `=` button to get the result.
4. Use the `AC` button to clear all input.
5. Use the `Del` button to remove the last entered character.

## Code Explanation
### `Ui_MainWindow` Class
This class defines the graphical user interface of the calculator using PyQt6 widgets.

#### Methods:
- `setupUi(MainWindow)`: Sets up the main window layout, buttons, and connections.
- `pressed(number)`: Handles button presses and updates the display.
- `equal()`: Evaluates the entered expression and displays the result.
- `all_clear()`: Clears the entire input field.
- `clear()`: Deletes the last character in the input field.

## Sample Input/Output
**Example 1:**
<img width="487" alt="Screenshot 2025-03-16 at 4 52 29 PM" src="https://github.com/user-attachments/assets/dceeab95-4400-423d-91b1-d7d1d96eb6d1" />

_Input:_ `3 + 5 =`

_Output:_ `8`
<img width="487" alt="Screenshot 2025-03-16 at 4 52 44 PM" src="https://github.com/user-attachments/assets/41867b39-ef80-493e-aa0d-aa924e85d4e6" />

**Example 2:**
<img width="486" alt="Screenshot 2025-03-16 at 4 53 19 PM" src="https://github.com/user-attachments/assets/6d2d428d-f1c8-448f-b109-47bacbce601a" />

_Input:_ `10 / 2 =`

_Output:_ `5`
<img width="486" alt="Screenshot 2025-03-16 at 4 53 28 PM" src="https://github.com/user-attachments/assets/19c3447f-9da7-4200-9e9a-3694f22e468c" />

## Warning
This implementation uses Python's `eval()` function to compute expressions, which can be unsafe if user input is not properly sanitized. Consider using a safer evaluation method for production use.

## License
This project is open-source and free to use.

