# Даны три целых числа. Найти количество положительных чисел в исходном наборе.
a = input("Введите первое число: ")
while True:
    try:
        a = int(a)
        break
    except ValueError:
        print("Неправильно ввели!")
        a = input("Введите первое число: ")

b = input("Введите второе число: ")
while True:
    try:
        b = int(b)
        break
    except ValueError:
        print("Неправильно ввели!")
        b = input("Введите второе число: ")

c = input("Введите третье число: ")
while True:
    try:
        c = int(c)
        break
    except ValueError:
        print("Неправильно ввели!")
        c = input("Введите третье число: ")
k = 0
if a > 0:
    k += 1
if b > 0:
    k += 1
if c > 0:
    k += 1

print('Количество положительных чисел =', k)
