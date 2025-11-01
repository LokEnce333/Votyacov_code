# Задание 1
def make_dict(arr):
    s = {}
    for i in arr:
        s[i] = i
    return s

print(make_dict([1, 2, 3, 4, 5]))
# Ответ: {1: 1, 2: 2, 3: 3, 4: 4, 5: 5}


# Задание 2
def dict_Of_Pow_2(n):
    s = {}
    for i in range(1, n+1):
        s[i] = i*i
    return s

print(dict_Of_Pow_2(5))
# Ответ: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# Задание 3
s = {'data1': 375, 'data2': 567, 'data3': -37, 'data4': 21}
multiply = 1
for x in s:
    multiply *= s[x]
print(multiply)
# Ответ: -165209625


# Задание 4
def make_dict(arr):
    s = {}
    for i in arr:
        s[i] = 0
    return s

s = input()
sety = make_dict('.,:;!?')
for i in s:
    if i in '.,:;!?':
        sety[i] += 1
sumy = 0
for x in sety:
    sumy += sety[x]
print(sumy)
# Ответ: 12


# Задание 5
def make_dict(arr):
    s = {}
    for i in arr:
        s[i] = 0
    return s

s = input()
dic = make_dict('0123456789')
for i in s:
    if i in '0123456789':
        dic[i] += 1
sumy = 0
g = ''
for x in '0123456789':
    sumy += dic[x]
    if(dic[x] != 0):
        g += x
if(sumy == 0):
    print("NO")
else:
    print(g)
# Ответ: 12456789

