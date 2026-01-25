# Дан список размера N, все элементы которого, кроме последнего, упорядочены по возрастанию. Сделать список упорядоченным, переместив последний элемент на новую позицию.

print("\nЗадание 3")
try:
    N = int(input("Размер списка: "))
    if N <= 2:
        print("Список слишком мал")
    else:
        A = sorted([random.randint(1, 50) for _ in range(N-1)])
        A.append(random.randint(1, 50))
        print("Исходный:", A)
        
        last = A[-1]
        i = N - 2
        while i >= 0 and A[i] > last:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = last
        
        print("Упорядоченный:", A)
        
except ValueError:
    print("Ошибка ввода")
