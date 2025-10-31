# Задача 1
n = int(input())
m = int(input())

arr = []
arr.append(n)
arr.append(m)
print(arr, arr[0] + arr[1])
#Ответ: [12, 34] 46


# Задача 2
s = input()
arr = []

for i in s.split():
    arr.append(i)
print(arr[0], arr[-1])
#Ответ: Программирование школы


# Задача 3
s = input()
arr = []

for i in s.split():
    arr.append(i)
    
maxy = -1
word = ''
for i in arr:
    if maxy < len(i):
        maxy = len(i)
        word = i
print(word)
#Ответ: нетипичный


# Задача 4
n = int(input())

arr = []
for i in range(1, n+1):
    if (i % 3 == 0) or (i % 5 == 0):
        arr.append(i)
print(sum(arr))
#Ответ: 234168


# Задача 5
s = input()
s = " " + s + " "

ind1 = 0
ind2 = 0
arr = []
for i in range(1, len(s)):
    if(s[i] == ' '):
        ind2 = i
        arr.append(s[ind1+1 : ind2])
        ind1 = ind2

ca = 0 
do = 0      
for i in arr:
    if(i == 'cat'):
        ca += 1
    else:
        do += 1

if ca > do:
    print('cat')
else:
    print('dog')
#Ответ: cat

