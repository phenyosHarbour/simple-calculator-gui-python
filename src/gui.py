import tkinter as tk
from tkinter import messagebox
from logic import CalculatorLogic


class CalculatorGUI:
    """
    A class to create and display the calculator GUI.
    """

    def __init__(self):
        self.logic = CalculatorLogic()
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.configure(bg="black")
        self.create_widgets()

    def button_click(self, value: str):
        """
        Handle button clicks and update the display accordingly.
        """
        if value == "=":
            try:
                result = self.logic.evaluate_expression(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        elif value == "C":
            self.entry.delete(0, tk.END)
        elif value == "√":
            try:
                result = self.logic.square_root(float(self.entry.get()))
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except ValueError as e:
                messagebox.showerror("Error", str(e))
        elif value == "⌫":
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, self.logic.backspace(current_text))
        else:
            self.entry.insert(tk.END, value)

    def create_button(self, text, row, col):
        """
        Create a single button widget.
        """
        def on_click():
            self.button_click(text)

        tk.Button(
            self.root, text=text, command=on_click,
            font=("Arial", 18), bg="gray", fg="white",
            bd=0, height=2, width=5
        ).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def create_widgets(self):
        """
        Create all GUI components (buttons, entry field, layout).
        """
        self.entry = tk.Entry(
            self.root, font=("Arial", 24), bg="gray", fg="white",
            bd=0, justify="right"
        )
        self.entry.grid(
            row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew"
        )

        buttons = [
            '7', '8', '9', '/', '4', '5', '6', '*',
            '1', '2', '3', '-', '0', '.', '=', '+',
            'C', '√', '^', '⌫'
        ]

        row, col = 1, 0
        for button in buttons:
            self.create_button(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        for i in range(5):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i % 4, weight=1)

    def run(self):
        """
        Start the main event loop.
        """
        self.root.mainloop()
