#Дан список A размера N. Сформировать новый список B того же размера по следующему правилу: элемент BK равен среднему арифметическому элементов списка A с номерами от 1 до K.
print("\nЗадание 2")
try:
    N = int(input("Размер списка: "))
    if N <= 0:
        print("Ошибка: размер > 0")
    else:
        A = [random.randint(1, 10) for _ in range(N)]
        print("Исходный A:", A)
        
        B = []
        for K in range(N):
            total = 0
            for i in range(K+1):
                total += A[i]
            average = total / (K+1)
            B.append(round(average, 2))
        
        print("Список B:", B)
        
except ValueError:
    print("Ошибка ввода")
