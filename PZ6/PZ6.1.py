#Дан целочисленный список размера N. Увеличить все нечетные числа, содержащиеся в списке, на исходное значение последнего нечетного числа. Если нечетные числа в списке отсутствуют, то оставить список без изменений.
print("Задание 1")
try:
    N = int(input("Размер списка: "))
    if N <= 0:
        print("Ошибка: размер > 0")
    else:
        A = [random.randint(-20, 20) for _ in range(N)]
        print("Исходный:", A)
        
        last_odd = None
        for i in range(len(A)-1, -1, -1):
            if A[i] % 2 != 0:
                last_odd = A[i]
                break
        
        if last_odd:
            for i in range(len(A)):
                if A[i] % 2 != 0:
                    A[i] += last_odd
            print("Результат:", A)
        else:
            print("Нечетных нет")
            
except ValueError:
    print("Ошибка ввода")

