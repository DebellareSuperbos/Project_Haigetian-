# Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ... •A (числа A перемножаются N раз).
print("Задание 1: Возведение в степень")
try:
    A = float(input("Введите число A: "))
    N = int(input("Введите степень N (N > 0): "))
    
    if N <= 0:
        print("Ошибка: N должно быть больше 0")
    else:
        result = 1
        for i in range(N):
            result = result * A
        print(f"Результат: {result}")
        
except ValueError:
    print("Ошибка ввода!")
