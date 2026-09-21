import json
import os


class History:

    def __init__(self, filename="calculation_history.json"):
        self.filename = filename
        self.history = []
        self.load_history()

    def add(self, expression, result):
        calculation = {
            "expression": expression,
            "result": result
        }

        self.history.append(calculation)
        self.save_history()

    def save_history(self):
        with open(self.filename, "w") as file:
            json.dump(self.history, file, indent=4)

    def load_history(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    self.history = json.load(file)
            except (json.JSONDecodeError, OSError):
                self.history = []

    def display_history(self):
        if not self.history:
            print("\nNo calculation history available.")
            return

        print("\n========== CALCULATION HISTORY ==========")

        for index, calculation in enumerate(self.history, start=1):
            print(
                f"{index}. "
                f"{calculation['expression']} = "
                f"{calculation['result']}"
            )

    def clear_history(self):
        self.history = []
        self.save_history()
        print("\nCalculation history cleared successfully.")