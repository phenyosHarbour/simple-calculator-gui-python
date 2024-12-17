class Memory:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

    def subtract(self, val):
        self.value -= val

    def clear(self):
        self.value = 0

    def recall(self):
        return self.value
