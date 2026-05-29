#Вариант 31: Найти все цены в файле price.txt
#Используем регулярные выражения для поиска цен

import re

file = open('price.txt', 'r', encoding='utf-8')
text = file.read()
file.close()

prices = re.findall(r'\d+[.,]?\d*', text)

print("Найденные цены:")
print(prices)
print("Количество:", len(prices))

result = open('result_prices.txt', 'w', encoding='utf-8')
result.write("Найденные цены:\n")
for price in prices:
    result.write(price + "\n")
result.write("Количество: " + str(len(prices)))
result.close()

print("Готово! Результат в файле result_prices.txt")
