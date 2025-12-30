from core.models import Category, Movement


class Manager:
    def __init__(self):
        self.categories = []
        self.movements = []

    def has_categories(self):
        return bool(self.categories)
    
    def add_category(self, category):        
        for existing in self.categories:
            if existing.name.lower() == category.name.lower():
                raise ValueError("Category already exists")        
        self.categories.append(category)

    def add_movement(self, date, title, amount, category, type):
        if not self.categories:
            raise ValueError("No categories available")
        category_exists = False
        for cat in self.categories:
            if cat.name.lower() == category.lower():
                category_exists = True
                break
        
        if not category_exists:
            raise ValueError("Category does not exist")

        movement = Movement(
            date = date,
            title = title,
            amount = amount,
            category = category,
            type = type
        )

        self.movements.append(movement)

    def total_incomes(self):
        return sum(m.amount for m in self.movements if m.type == "INCOME")


    def total_expenses(self):
        return sum(m.amount for m in self.movements if m.type == "EXPENSE")


    def balance(self):
        return self.total_incomes() - self.total_expenses()