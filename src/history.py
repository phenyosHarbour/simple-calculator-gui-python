class History:
    def __init__(self):
        self.entries = []

    def add_entry(self, expression, result):
        self.entries.append(f"{expression} = {result}")

    def get_history(self):
        return self.entries[-5:]  # Last 5 entries

    def clear_history(self):
        self.entries.clear()
