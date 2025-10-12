# Задача 1
x = int(input())
y = int(input())
if x >= 5 and y < 25:
    print('True')
else:
    print('False')
# Ответ: При x = 10 и y = 13 выведет True


# Задача 2
password = input('Введите свой пароль: ')
check = input('Введите его ещё раз: ')

if password == check:
    print('True')
else:
    print('False')
# Ответ: False


# Задача 3
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

if (x1 <= x2) and (x1 <= x3) and (x1 <= x4):
    print(x1)
if (x2 <= x1) and (x2 <= x3) and (x2 <= x4):
    print(x2)
if (x3 <= x1) and (x3 <= x2) and (x3 <= x4):
    print(x3)
else:
    print(x4)
# Ответ: 5


# Задача 4
x1 = int(input())
x2 = int(input())
x3 = int(input())
x4 = int(input())

if (x1 >= x2) and (x1 >= x3) and (x1 >= x4):
    print(x1)
if (x2 >= x1) and (x2 >= x3) and (x2 >= x4):
    print(x2)
if (x3 >= x1) and (x3 >= x2) and (x3 >= x4):
    print(x3)
else:
    print(x4)
# Ответ: 30


# Задача 5
a = int(input())
b = int(input())
c = int(input())

if a + b > c and a + c > b and b + c > a:
    print('True')
else:
    print('False')
#Ответ: True

# Задача 6
a = int(input())
b = int(input())
c = int(input())

if (a == 0) or (b == 0) or (c == 0):
    print('Вырожденный')
if (a == b == c) and ((a != 0) or (b != 0) or (c != 0)):
    print('Равносторонний')
else:
    print('Разносторонний')
# Ответ: Разносторонний


# Задача 7
a = int(input())
b = int(input())
c = int(input())
d = int(input())

if a < c:
    if b > c:
        print(b - c + 1)
    else:
        print(0)
else:
    if d > a:
        print(d - a + 1)
    else:
        print(0)