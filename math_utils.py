class Calculator:
    def add(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Переменная должна быть числом.")
        return a + b

    def subtract(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Переменная должна быть числом.")
        return a - b

    def multiply(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Переменная должна быть числом.")
        return a * b

    def divide(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Переменная должна быть числом.")
        if b == 0:
            raise ZeroDivisionError("Ошибка! Деление на ноль невозможно.")
        return a / b
