#Задача 1
def sum_numbers(*dit):
    sumy = 0
    for i in dit:
        sumy += i
    return sumy
print(sum_numbers(10,20,30,40))

#Задача 2
def print_kwargs(**info):
    for name, data in info.items():
        print(f'{name}: {data}')
print_kwargs(name='Alice', age=25, country='USA')

#Задача 3
def filter_by_length(min_length, *str):
    new_arr = []
    for s in str:
        if len(s) >= min_length:
            new_arr.append(s)
    return new_arr
strings = ["hello", "world", "how", "are", "you"]
print(filter_by_length(4, *strings)) # ['hello', 'world']
print(filter_by_length(3, *strings)) # ['hello', 'world', 'you']

#Задача 4
def calculate_total_price(cost, **discount):
    all_dis = 0
    for i in discount.items():
        all_dis += i[1]
    return cost * (1 - all_dis/100)
print(calculate_total_price(100, student=10, coupon=20)) # 70.0
print(calculate_total_price(200, holiday=25)) # 150.0
print(calculate_total_price(500)) # 500.0

#Задача 5
def custom_print(*args, **kwargs):
    g = 0
    sepy = ' '
    if 'sep' in kwargs:
        sepy = kwargs['sep']
        g += 1
    endy = ''
    if 'end' in kwargs:
        endy = kwargs['end']
        g += 1
    for i in args:
        if(g == len(kwargs)+len(args)-1):
            print(i, end='')
        else:
            print(i, end=sepy)
        g += 1
    for i, j in kwargs.items():
        if i == 'sep' or i == 'end':
            continue
        if(g == len(kwargs)+len(args)-1):
            print(f'{i}={j}', end='')
        else:
            print(f'{i}={j}', end=sepy)
        g += 1
    print(endy)
custom_print(1, 2, 3, a=4, b=5, sep='-', end='!')
# 1-2-3-a=4-b=5!
custom_print('Hello', 'World', sep=' ')
# Hello World
custom_print('apple', 'banana', 'cherry', sep=', ')
# apple, banana, cherry
custom_print(a=1, b=2, end='...')
# a=1 b=2...
    