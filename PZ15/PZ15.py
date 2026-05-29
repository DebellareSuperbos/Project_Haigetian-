import sqlite3

conn = sqlite3.connect('rental.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS Клиент (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    fio TEXT, code TEXT, term INTEGER, cost REAL)''')

c.execute("DELETE FROM Клиент")
clients = [("Иванов Иван", "A101", 30, 45000), ("Петрова Мария", "B202", 15, 22500),
           ("Сидоров Алексей", "C303", 60, 90000), ("Кузнецова Анна", "A102", 45, 67500),
           ("Смирнов Дмитрий", "B203", 20, 30000), ("Васильева Елена", "C304", 90, 135000),
           ("Попов Андрей", "A103", 10, 15000), ("Соколова Татьяна", "B204", 25, 37500),
           ("Михайлов Сергей", "C305", 50, 75000), ("Фёдорова Ольга", "A104", 40, 60000)]
for f, cod, t, co in clients:
    c.execute("INSERT INTO Клиент (fio,code,term,cost) VALUES (?,?,?,?)", (f, cod, t, co))
conn.commit()

while True:
    print("\n1-Все 2-Поиск по ФИО 3-Поиск по коду 4-Поиск по сроку(>) 5-Удалить по ID")
    print("6-Удалить по ФИО 7-Удалить по сроку(<) 8-Изменить ФИО 9-Изменить срок 0-Выход")
    x = input("Выбор: ")

    if x == "1":
        for row in c.execute("SELECT * FROM Клиент"):
            print(f"{row[0]} {row[1]} {row[2]} {row[3]}дн {row[4]}р")

    elif x == "2":
        n = input("ФИО: ")
        for r in c.execute("SELECT * FROM Клиент WHERE fio=?", (n,)):
            print(r)

    elif x == "3":
        cod = input("Код: ")
        for r in c.execute("SELECT * FROM Клиент WHERE code=?", (cod,)):
            print(r)

    elif x == "4":
        d = int(input("Больше дней: "))
        for r in c.execute("SELECT * FROM Клиент WHERE term>?", (d,)):
            print(r)

    elif x == "5":
        i = int(input("ID: "))
        c.execute("DELETE FROM Клиент WHERE id=?", (i,))
        conn.commit()
        print("Удалено")

    elif x == "6":
        n = input("ФИО: ")
        c.execute("DELETE FROM Клиент WHERE fio=?", (n,))
        conn.commit()
        print("Удалено")

    elif x == "7":
        d = int(input("Меньше дней: "))
        c.execute("DELETE FROM Клиент WHERE term<?", (d,))
        conn.commit()
        print("Удалено")

    elif x == "8":
        i = int(input("ID: "))
        n = input("Новое ФИО: ")
        c.execute("UPDATE Клиент SET fio=? WHERE id=?", (n, i))
        conn.commit()
        print("Изменено")

    elif x == "9":
        i = int(input("ID: "))
        t = int(input("Новый срок: "))
        c.execute("UPDATE Клиент SET term=? WHERE id=?", (t, i))
        conn.commit()
        print("Изменено")

    elif x == "0":
        break

conn.close()
