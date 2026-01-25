#Дано целое число N (>0). С помощью операций деления нацело и взятия остатка от деления определить, имеются ли в записи числа N нечетные цифры. Если имеются, то вывести TRUE, если нет — вывести FALSE.

print("\nЗадание 2: Проверка нечетных цифр")
try:
    N = int(input("Введите число N (N > 0): "))
    
    if N <= 0:
        print("Ошибка: N должно быть больше 0")
    else:
        has_odd = False
        temp = N
        
        while temp > 0:
            digit = temp % 10  
            if digit % 2 == 1: 
                has_odd = True
                break
            temp = temp // 10  
        
        print(has_odd)  
        
except ValueError:
    print("Ошибка ввода!")
