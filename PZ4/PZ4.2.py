#Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить, имеются ли в записи числа N нечетные цифры. Если имеются, то вывести TRUE, если нет — вывести FALSE.

print("\n=== Задача 2 ===")
try:
    A = float(input("Введите сторону A: "))
    B = float(input("Введите сторону B: "))
    C = float(input("Введите сторону квадрата C: "))
    
    if A <= 0 or B <= 0 or C <= 0:
        print("Все числа должны быть положительными!")
    else:
        width_count = 0
        temp = 0
        while temp + C <= A:
            width_count += 1
            temp += C
          
        height_count = 0
        temp = 0
        while temp + C <= B:
            height_count += 1
            temp += C
        total = 0
        for i in range(height_count):
            total += width_count
        
        print(f"Поместится квадратов: {total}")
except:
    print("Ошибка ввода!")
