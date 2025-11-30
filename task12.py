# Задача 1
a = [2, 4, 6, 8]
b = [1, 3, 5, 7]
a_itera = iter(a)
b_iterb = iter(b)
next(iter(a_itera))
print(next(iter(a_itera)), next(iter(b_iterb)))
next(iter(b_iterb))
print(next(iter(b_iterb)), next(iter(a_itera)))
# Ответ: 4 1
# 5 6


# Задача 2
string = 'ППШ'
iterator = iter(string)
for x in iterator:
    print(x)
# Ответ: П
# П
# Ш


# # Задача 3
# d = [1: 'bee', 2: 'raccoon', 3: 'snake']
# iterator = iter(d)
# print(d[next(iterator)])
# # Ответ: ошибку синтаксическую, так как словарь не так записывается. При правильной записи вывело бы bee


# Задача 4
a = [int(s) for s in range(1, 20)]
iterator = iter(a)
print(9 in iterator)
print(9 in iterator)
# Ответ: True
# False , так как итератор сначала находит 9, и переключается дальше, где 9 нет, поэтому во втором print выводит False


# Задача 5
a = (i ** 2 for i in range (10) if i % 3 != 0)
print(next(a))
print(next(a))
print(next(a))
# Ответ: 1 4 16


# Задача 6
a = (i**2 for i in range(1, 6))
print(next(a))
next(a)
print(next(a))
next(a)
print(next(a))
# Ответ: 1 9 25


# Задача 7
a = (str(i) + ' ' + j for j in ['Крести', 'Вини', 'Черви', 'Буби'] for i in [6, 7, 8, 9, 10, 'Валет', 'Дама', 'Король', 'Туз'])
for i in range(36):
    print((next(a)))
print('Stop iteration')
# Ответ:

