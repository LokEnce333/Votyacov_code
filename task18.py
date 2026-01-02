#Задача 1
import time
def timer(func):
    def calc_time(*args, **kwargs):
        st = time.time()
        res = func(*args, **kwargs)
        en = time.time()
        print(f'Функция {func.__name__} выполняется {en-st} секунд с результатом {res}')
    return calc_time

@timer
def ultra_calc(x, y):
    k = 0
    for i in range(x):
        for j in range(y):
            k += 1
    return k
@timer
def neultra_calc(x):
    k = 0
    for i in range(x):
        k += 1
    return k

x, y = map(int, input().split())
ultra_calc(x, y)
neultra_calc(x)

#Задача 2
def cache(func):
    d = {}
    def cashing(x):
        if x not in d:
            d[x] = func(x)
        return d[x]
    return cashing

@cache
def fibonachi(x):
    if x <= 1:
        return 1
    return fibonachi(x-1) + fibonachi(x-2)

for i in range(100):
    print(fibonachi(i))
        

#Задача 3
import datetime

def logging(func):
    def past(*args, **kwargs):
        with open('logs.txt', 'a', encoding='utf-8') as f:
            now = datetime.datetime.now()
            f.write(f'[{now}] Функция {func.__name__} с аргументами {*args, *kwargs} с выводом {func(*args, **kwargs)}\n')
    return past

@logging
def test(*args):
    return sum(args)

test(1,2,3,4,5,6,7,8,9,10)

#Задача 4
import time

def retry(attempts, delay=0):
    def decorator(func):
        def tryings(*args, **kwargs):
            att = 0
            while attempts > att:
                res = func(*args, **kwargs)
                if res != None:
                    return res
                att += 1
                time.sleep(delay)
        return tryings
    return decorator

@retry(3, 1)
def f():
    return None
print(f())