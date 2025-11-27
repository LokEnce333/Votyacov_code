# # Задача 1
# R = [45, 84, 10, 58]
# A = R
# R[0] = 54
# print(A[0] + R[0])
# # Ответ: 108


# # Задача 2
# import copy

# a = list(map(int, input().split()))
# a1 = a[:]
# a2 = copy.copy()
# a2 = copy.copy(a)
# a3 = copy.deepcopy(a)
# a4 = list(a)
# print(sum(a))
# # Ответ: 5 35


# # Задача 3
# AR = [[90, 99, 109, 119]] * 4
# AR[0][0], AR[3][3] = 890, 76
# print(AR[1][0] + AR[2][3])
# # Ответ: 966


# # Задача 4
# import sys
# animals = ["cat", "cat", "dog", "dog", "bird", "capybara", "capybara", "capybara"]
# d = dict()
# for i in animals:
#     if i not in d:
#         d[i] = animals.count(i)
# sumy_ref_animal = 0
# for i in d:
#     sumy_ref_animal += sys.getrefcount(i)
# sumy_ref_dit = 0
# for i in range(1, 4):
#     sumy_ref_dit += sys.getrefcount(i)
# print(sumy_ref_animal, sumy_ref_dit)
# # Ответ: 32 9663676416


# # Задача 5
# cnt_ref, cnt_eq = 0, 0
# backpack = ["capybara", "capyraba", "capyba", "capyba", "capybara", 2999, 2999, "capybara", [7, 7, 7], [7, 7, 7], [7, 7, 7], [7, 7, 7]] + [[8, 8]] * 5
# for i in range(0, len(backpack)):
#     for j in range(i+1, len(backpack)):
#         if(backpack[i] is backpack[j]): cnt_ref += 1
#         if(backpack[i] == backpack[j]): cnt_eq += 1
# print(cnt_ref, cnt_eq)
# # Ответ: 15 21


# Задача 6
import copy

rec_sal = ['lettuce', 'chicken', 'cheese', 'sauce', 'tomatoes', 'croutons']
rec_sal.append(rec_sal)
rec_sal[6].append('slat')
rec_sal[6].append('pepper')
print(rec_sal[4], rec_sal[-1])
# Ответ: tomatoes pepper

