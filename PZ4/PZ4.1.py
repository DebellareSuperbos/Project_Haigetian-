# Дано вещественное число A и целое число N (>0). Найти A в степени N: AN = AA ... •A (числа A перемножаются N раз).
print("=== Задача 1 ===")
try:
    A = int(input("Введите A: "))
    B = int(input("Введите B (B > A): "))
    
    if A >= B:
        print("Ошибка: A должно быть меньше B")
    else:
        count = 0
        print("Числа от A до B:")
        for num in range(A, B + 1):
            print(num, end=" ")
            count += 1
        print(f"\nКоличество чисел: {count}")
except:
    print("Ошибка ввода!")
