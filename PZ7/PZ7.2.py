#Дана строка, состоящая из русских слов, разделенных пробелами (одним или несколькими). Найти длину самого короткого слова.

print("\nЗадача 2")
text = "кот собака еж заяц"
words = text.split()

min_len = len(words[0])
for word in words:
    if len(word) < min_len:
        min_len = len(word)

print(f"Строка: '{text}'")
print(f"Длина самого короткого слова: {min_len}")

print("Короткие слова:")
for word in words:
    if len(word) == min_len:
        print(f"  - {word} ({len(word)} букв)")
