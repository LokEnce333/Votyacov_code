# Задача 1
D = ['Женя': 89, 'Вася': 100, 'Марк': 71, 'Мария': 79]
f = list(filter(lambda x: D[x] > 80, D))
print(f)
# Ответ: ошибку, так как синтаксис словаря написан неправильно. При правильном написании выведет: ['Женя', 'Вася']


# Задача 2
print(list(map(lambda x: x**3, list(map(int, input().split())))))
# Ответ: [8, 64, 216, 512, 1000]


# Задача 3
a = list(map(int, input().split()))
b = []
c = list(map(lambda x: b.append(x) if x < 0 else 0, a))
print(b)
# Ответ: [-1, -7, -8, -10]


# Задача 4
from functools import reduce
print(reduce(lambda x, y: x * y, range(1, int(input())+1)))
# Ответ: 40320


# Задача 5
maxy = -1e9
arr = list(map(lambda x: x if ((x**2 % 9 == 0) and x > maxy) else -1, list(map(int, input().split()))))
print(max(arr))
# Ответ: 6

