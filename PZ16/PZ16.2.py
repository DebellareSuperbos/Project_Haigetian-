# Базовый класс "Транспорт"
class Transport:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"{self.brand} {self.model}, {self.year} год")

# Класс "Автомобиль" наследует "Транспорт"
class Car(Transport):
    def __init__(self, brand, model, year, body_type):
        super().__init__(brand, model, year)  # вызываем конструктор родителя
        self.body_type = body_type

    def info(self):
        print(f"Автомобиль: {self.brand} {self.model}, {self.year} г., кузов: {self.body_type}")

# Тестирование
t = Transport("Generic", "Unknown", 2000)
t.info()

c = Car("Toyota", "Camry", 2020, "седан")
c.info()
print(f"Марка: {c.brand}, Модель: {c.model}, Год: {c.year}, Тип кузова: {c.body_type}")
