import tkinter as tk
from src.logic import evaluate_expression
from src.memory import Memory
from src.history import History


class CalculatorApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Scientific Calculator")
        self.root.configure(bg="#333333")
        self.memory = Memory()
        self.history = History()
        self.expression = ""
        self.result_var = tk.StringVar()
        self._create_gui()

    def _create_gui(self):
        display_frame = tk.Frame(self.root, bg="#333333")
        display_frame.grid(row=0, column=0, columnspan=8, sticky="news")
        entry = tk.Entry(
            display_frame,
            textvariable=self.result_var,
            font=("Arial", 24),
            justify="right",
            bg="#111111",
            fg="#FFFFFF",
            bd=10,
            relief=tk.FLAT,
        )
        entry.pack(fill="both", expand=True, padx=10, pady=10)

        buttons = [
            ("(", 1, 0), (")", 1, 1), ("C", 1, 2), ("←", 1, 3), ("π", 1, 4),
            ("e", 1, 5), ("√", 1, 6), ("^", 1, 7), ("7", 2, 0), ("8", 2, 1),
            ("9", 2, 2), ("/", 2, 3), ("sin", 2, 4),
            ("cos", 2, 5), ("tan", 2, 6),
            ("log", 2, 7), ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("*", 3, 3),
            ("asin", 3, 4), ("acos", 3, 5), ("atan", 3, 6), ("ln", 3, 7),
            ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("-", 4, 3), ("x²", 4, 4),
            ("x³", 4, 5), ("!", 4, 6), ("%", 4, 7), ("0", 5, 0), (".", 5, 1),
            ("±", 5, 2), ("+", 5, 3), ("Exp", 5, 4), ("abs", 5, 5),
            ("M+", 5, 6),
            ("MR", 5, 7), ("←", 6, 2), ("↓", 6, 3), ("→", 6, 4), ("=", 6, 7),
        ]

        button_colors = {
            "bg": "#444444",
            "fg": "#FFFFFF",
            "special_bg": "#FF5733",
            "equal_bg": "#3B82F6",
            "arrow_bg": "#7F8C8D",
        }

        for (text, row, col) in buttons:
            bg_color = button_colors["bg"]
            if text in ["C", "←", "M+", "MR"]:
                bg_color = button_colors["special_bg"]
            elif text == "=":
                bg_color = button_colors["equal_bg"]
            elif text in ["←", "→", "↑", "↓"]:
                bg_color = button_colors["arrow_bg"]

            button = tk.Button(
                self.root,
                text=text,
                font=("Arial", 18),
                bg=bg_color,
                fg=button_colors["fg"],
                relief=tk.FLAT,
                command=lambda t=text: self._on_button_click(t),
            )
            button.grid(row=row, column=col, padx=5, pady=5, sticky="news")

        for i in range(8):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)

    def _on_button_click(self, button_text):
        if button_text == "C":
            self.expression = ""
        elif button_text == "←":
            self.expression = self.expression[:-1]
        elif button_text == "=":
            result = evaluate_expression(self.expression)
            self.history.add_entry(self.expression, result)
            self.expression = str(result)
        else:
            self.expression += button_text
        self.result_var.set(self.expression)

    def mainloop(self):
        self.root.mainloop()


# Ensure a newline at the end of the file
# Compare this snippet from src/constants.py:
