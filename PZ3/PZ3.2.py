#Даны три числа. Найти сумму двух наибольших из них

try:
    x = int(input("Введите первое число: "))
    y = int(input("Введите второе число: "))
    z = int(input("Введите третье число: "))
    
    min_num = min(x, y, z)
    
    result = x + y + z - min_num
    print(f"Сумма двух наибольших чисел: {result}")
    
except ValueError:
    print("Ошибка! Введите целые числа.")
