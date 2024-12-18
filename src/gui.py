import tkinter as tk
from tkinter import messagebox
from math import pi, e
from src.utils import evaluate_expression
# Assumes utils.py contains the safe evaluation function


class CalculatorApp:
    def __init__(self):
        # Initialize the main window
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.configure(bg="black")
        self.create_widgets()

    def create_widgets(self):
        # Entry widget for input
        self.entry = tk.Entry(
            self.root, font=("Arial", 20), bg="gray", fg="white",
            bd=5, justify="right"
        )
        self.entry.grid(row=0, column=0, columnspan=8, padx=10,
                        pady=10, sticky="nsew")

        # Buttons configuration
        buttons = [
            # Row 1
            ("(", 1, 0), (")", 1, 1), ("C", 1, 2), ("⌫", 1, 3), ("log", 1, 4),
            ("ln", 1, 5), ("√", 1, 6), ("^", 1, 7),
            # Row 2
            ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("/", 2, 3), ("sin", 2, 4),
            ("cos", 2, 5), ("tan", 2, 6), ("π", 2, 7),
            # Row 3
            ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3), ("asin", 3, 4),
            ("acos", 3, 5), ("atan", 3, 6), ("e", 3, 7),
            # Row 4
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3), ("x²", 4, 4),
            ("x³", 4, 5), ("|x|", 4, 6), ("mod", 4, 7),
            # Row 5
            ("0", 5, 0), (".", 5, 1), ("=", 5, 2), ("+", 5, 3), ("sinh", 5, 4),
            ("cosh", 5, 5), ("tanh", 5, 6), ("exp", 5, 7),
        ]

        for (text, row, col) in buttons:
            button = tk.Button(self.root, text=text, font=("Arial", 18),
                               command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

        # Configure grid weights
        for i in range(8):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "C":
            self.entry.delete(0, tk.END)
        elif char == "⌫":
            self.entry.delete(len(self.entry.get())-1, tk.END)
        elif char == "=":
            self.calculate_result()
        elif char == "π":
            self.entry.insert(tk.END, str(pi))  # Insert pi
        elif char == "e":
            self.entry.insert(tk.END, str(e))  # Insert e
        elif char == "√":
            self.entry.insert(tk.END, "sqrt(")  # Square root
        elif char == "x²":
            self.entry.insert(tk.END, "**2")  # Square
        elif char == "x³":
            self.entry.insert(tk.END, "**3")  # Cube
        elif char == "|x|":
            self.entry.insert(tk.END, "abs(")  # Absolute value
        else:
            self.entry.insert(tk.END, char)

    def calculate_result(self):
        try:
            expression = self.entry.get()
            result = evaluate_expression(expression)
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(result))
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
