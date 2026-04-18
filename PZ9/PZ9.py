#В магазинах имеются следующие товары. Магнит – молоко, соль, сахар. Пятерочка –
#1. в каких магазинах нельзя приобрести сыр.
#2. в каких магазинах можно приобрести одновременно молоко и сахар.
#3. в каких магазинах можно приобрести соль.

magnit = {'молоко', 'соль', 'сахар'}
pyaterochka = {'мясо', 'молоко', 'сыр'}
perekrestok = {'молоко', 'творог', 'сыр', 'сахар'}

print('1. Магазины, в которых нельзя приобрести сыр:')
if 'сыр' not in magnit:
    print('Магнит')
if 'сыр' not in pyaterochka:
    print('Пятерочка')
if 'сыр' not in perekrestok:
    print('Перекресток')
print()

print('2. Магазины, в которых есть молоко и сахар:')
if 'молоко' in magnit and 'сахар' in magnit:
    print('Магнит')
if 'молоко' in pyaterochka and 'сахар' in pyaterochka:
    print('Пятерочка')
if 'молоко' in perekrestok and 'сахар' in perekrestok:
    print('Перекресток')
print()

print('3. Магазины, в которых можно приобрести соль:')
if 'соль' in magnit:
    print('Магнит')
if 'соль' in pyaterochka:
    print('Пятерочка')
if 'соль' in perekrestok:
    print('Перекресток')
