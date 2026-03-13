height_dict = {
    "Андрей": 178,
    "Виктор": 150,
    "Максим": 200,
    "Елена": 165,
    "Ольга": 158,
    "Дмитрий": 182
}
print("Словарь роста персон:")
for name, height in height_dict.items():
    print(name + ":", height, "см.")

max_height = max(height_dict.values())
min_height = min(height_dict.values())

print("\nНаибольший рост:", max_height, "см.")
print("Наименьший рост:", min_height, "см.")
