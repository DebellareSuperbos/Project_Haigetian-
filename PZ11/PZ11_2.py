#Из заданной строки отобразить только символы нижнего регистра.
#Использовать библиотеку string. Строка 'In PyCharm, you can specify third-party standalone
#applications and run them as External Tools'.

import string

s = 'In PyCharm, you can specify third-party standalone applications and run them as External Tools'
low = [c for c in s if c in string.ascii_lowercase]
print(''.join(low))
