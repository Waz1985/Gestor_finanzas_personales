from datetime import datetime

class Category:
    def __init__(self, name):
        self.name = name

        if not isinstance(name, str):
            raise TypeError("The category name must be a String")
        
        clear_name = name.strip()

        if not clear_name:
            raise ValueError("The category name can't be empty")
    
        self.name = clear_name

class Movement:
    def __init__(self, date, title, amount, category, type):
        self.date = date
        self.title = title.strip()
        self.category = category.strip()
        self.type = str(type).upper()
        
        if self.type not in ("INCOME", "EXPENSE"):
            raise ValueError("Type must be INCOME or EXPENSE")

        try:
            self.amount = float(amount)
        except (TypeError, ValueError):
            raise TypeError("Amount must be a number")
        
        if self.amount <= 0:
            raise ValueError("Amount must be greater than 0")
    
        if not isinstance(date, str):
            raise TypeError("Date must be a String")

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Date must be in format: YYY-MM-DD")
        
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Title can't be empty")
        
        
        if not isinstance(category, str) or not category.strip():
            raise ValueError("Category can't be empty")
        
        


