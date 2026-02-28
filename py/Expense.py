class Expense:
    def __init__(self, name, category, amount) -> None:
        self.name = name
        self.amount = amount
        self.category = category

    def __str__(self):
        return f"{self.name},{self.amount},{self.category}"