#Создайте класс «Книга», который имеет атрибуты название, автор и количество
#страниц. Добавьте методы для чтения и записи книги.
# Класс "Книга"
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def read(self):
        print(f"Читаем книгу: {self.title}")

    def write(self, new_title, new_author):
        self.title = new_title
        self.author = new_author
        print(f"Книга перезаписана! Теперь это '{self.title}' автора {self.author}")

# Тестирование
b = Book("Война и мир", "Толстой", 1200)
b.read()
b.write("Преступление и наказание", "Достоевский")
print(f"Название: {b.title}, Автор: {b.author}, Страниц: {b.pages}")
