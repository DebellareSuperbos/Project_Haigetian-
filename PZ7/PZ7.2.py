#Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими). Найти длину самого короткого слова.

print("\nЗадание 2: Длина самого короткого слова")
try:
    text = input("Введите строку: ")
    
    if text.strip() == "":
        print("Строка пустая")
    else:
        words = text.split()
        shortest = len(words[0])
        
        for word in words:
            if len(word) < shortest:
                shortest = len(word)
        
        print(f"Длина самого короткого слова: {shortest}")
        
except Exception as e:
    print(f"Ошибка: {e}")
