import tkinter as tk
from tkinter import messagebox
import math


# Function to evaluate the expression
def evaluate_expression(expression):
    """
    Evaluate a mathematical expression after replacing the caret (^) with
    exponentiation (**).
    Handles invalid input with appropriate error messages.

    Args:
        expression (str): The input mathematical expression.

    Returns:
        float or str: The evaluated result or an error message.
    """
    try:
        # Replace the exponentiation symbol for evaluation
        expression = expression.replace("^", "**")
        result = eval(expression)
        return result
    except Exception:
        messagebox.showerror(
            "Error", "Invalid input. Please check your expression."
        )
        return ""


# Function to handle button clicks
def button_click(value):
    """
    Handle the button click events for the calculator.
    Supports clear, backspace, square root, percentage, and basic arithmetic
    operations.

    Args:
        value (str): The button value clicked.
    """
    if value == "=":
        try:
            result = evaluate_expression(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif value == "C":
        entry.delete(0, tk.END)
    elif value == "√":
        try:
            result = math.sqrt(float(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            messagebox.showerror("Error", "Invalid input for square root.")
            entry.delete(0, tk.END)
    elif value == "%":
        try:
            result = float(entry.get()) / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except ValueError:
            messagebox.showerror("Error", "Invalid input for percentage.")
            entry.delete(0, tk.END)
    elif value == "⌫":
        # Backspace to delete the last character
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])
    else:
        entry.insert(tk.END, value)


# Create the main window
root = tk.Tk()
root.title("Graphical Calculator")
root.configure(bg="black")

# Create an entry widget for the display
entry = tk.Entry(
    root, font=("Arial", 24), bg="gray", fg="white", bd=0, justify="right"
)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

# Define button labels
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+",
    "C", "√", "^", "%", "⌫"
]

# Create buttons and place them in the grid
row, col = 1, 0
for button in buttons:
    def action(x=button):
        button_click(x)

    tk.Button(
        root,
        text=button,
        command=action,
        font=("Arial", 18),
        bg="gray",
        fg="white",
        bd=0,
        height=2,
        width=5,
    ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    col += 1
    if col > 3:
        col = 0
        row += 1

# Configure grid weights
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
    root.grid_columnconfigure(i % 4, weight=1)

# Start the main event loop
root.mainloop()