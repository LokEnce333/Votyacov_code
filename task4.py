# Задание 1
n = int(input())
a = [0]
for i in range(n):
    x = int(input())
    a = [i] * x
print(a)
#Ответ: [2, 2, 2]


# Задание 2
n = int(input())
a = []
for i in range(n):
    a = a + [i] * i
print(a)
#Ответ: [1, 2, 2]


# Задание 3
n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
print(sum(a)/len(a))
# Ответ: 4.2


# Задание 4
n = int(input())
m = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
print(a[m])
# Ответ: 32


# Задание 5
n = int(input())
a = [0] * n
for i in range(n):
    a[i] = int(input())
sumy = 0
for i in range(0, n, 2):
    sumy += a[i]
print(sumy)
# Ответ: 6