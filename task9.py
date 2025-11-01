# # Задача 1
# def sum_array(arr):
#     sumy = 0
#     for i in arr:
#         sumy += i
#     return sumy

# print(sum_array([1, 7, 42, 12,10, 1, 4, 0]))
# # Ответ: 77


# # Задача 2
# def is_in_diopazone(begin, end, val):
#     return begin <= val <= end

# print(is_in_diopazone(1, 9, 7))
# # Ответ: True


# # Задача 3
# def is_perfect(n):
#     sumy = 0
#     for i in range(1, n//2+1):
#         if n % i == 0:
#             sumy += i
#     return n == sumy

# print(is_perfect(8128))
# # Ответ: True


# # Задача 4
# def is_pallindrom(n):
#     s = str(n)
#     for i in range(len(s)//2):
#         if(s[i] != s[len(s)-1-i]):
#             return False
#     return True

# print(is_pallindrom(1234567899876554321))
# # Ответ: False


# # Задача 5
# def is_prime(n):
#     if(n == 1): 
#         return False
#     for i in range(1, n//2):
#         if(n % i == 0):
#             return False
#     return True

# print(is_prime(123321))
# # Ответ: False


# Задача 6
def fibonachy(n):
    if(n == 1):
        return 0
    if(n == 2):
        return 1
    return fibonachy(n-1) + fibonachy(n-2)

print(fibonachy(10))
# Ответ:

