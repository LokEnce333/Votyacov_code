#Задача 1
#Ошибочный
def f(a):
    return 18 * a * b
print(f(1))
#Ответ: name ’b’ is not defined
#Правильный
def f(a, b):
    return 18 * a * b
print(f(1, 1))

#Задача 2
#Ошибочный
for i in range(1, 11):
    summa += i
print("The sum is: ", summa)
#Ответ: NameError: name ‘summa‘ is not defined
#Правильный
summa = 0
for i in range(1, 11):
    summa += i
print("The sum is: ", summa)


#Задача 3
#Ошибочный
def is_even(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
is_even('4')
#Ответ: TypeError: not all arguments converted during string formatting
#Правильный
def is_even(n):
    if n % 2 == 0:
        print(n, "is even")
    else:
        print(n, "is odd")
is_even(4)


#Задача 4
#Ошибочный
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n + 1)
#Правильный
def factorial(n):
    if n < 0:
        return None
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
#Ответ:


#Задача 5
#Ошибочный
def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s)-i]:
            return False
    return True
#Правильный
def is_palindrome(s):
    s = s.lower()
    for i in range(len(s)):
        if s[i] != s[len(s)-1-i]:
            return False
    return True
#Ответ:


#Задача 6
#Ошибочный
def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(len(lst)):
            result = result * i
        return result
#Правильный
def multiplylist(lst):
    if len(lst) == 0:
        return None
    else:
        result = 1
        for i in range(len(lst)):
            result = result * lst[i]
        return result
#Ответ:

