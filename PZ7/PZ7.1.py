#Даны строки S и S0. Найти количество вхождений строки S0 в строку S

print("Задача 1")
S = "баобаб баобаб баобаб"
S0 = "бао"

count = 0
i = 0
while i < len(S):
    if S.find(S0, i) == i:
        count += 1
    i += 1

print(f"Строка: {S}")
print(f"Подстрока: {S0}")
print(f"Встречается: {count} раз")

print("\nИли проще:")
count = S.count(S0)
print(f"Встречается: {count} раз")
