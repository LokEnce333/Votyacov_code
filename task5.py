# Задача 1
n = int(input())
for i in range(n+1):
    if i % 3 == 0 and i % 6:
        print(i, end=' ')
# Ответ: 3 9 15


# Задача 2
n = int(input())
for i in range(10, n+1):
    if i%10 % 2 == 0:
        print(i, end=' ')
# Ответ: 10 12 14 16


# Задача 3
n = int(input())
if n % 2:
    print(sum(list([i for i in range(1, n + 1, 2)])))
else:
    print(n // 2)
# Ответ: 50 2500


# Задача 4
n = int(input())
if n % 3:
    for i in range(1, n + 1):
        print(n**i, end=' ')
else:
    m = int(input())
    print(n // m)
# Ответ: 8 64 512 4096 32768 262144 2097152 16777216 14


# Задача 5
a = int(input())
b = int(input())
n = int(input())

cnt = 0
x = 0
for _ in range(n):
    x = int(input())
    if a**2 + b**2 == x**2 and x > 10 and (x % 3 == 0 or x % 4 == 0):
        cnt += 1
print(cnt)
# Ответ: 1

