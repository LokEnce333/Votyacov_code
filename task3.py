# Задание 1
x = int(input())

while(x % 2 and x % 10 != 5):
    x = int(input())


# Задание 2
for i in range(10):
    print(i)


# Задание 3
K = int(input())
N = int(input())

sumy = 0
while(K <= N):
    if(K % 2):
        sumy += K
    K += 1
print(sumy)


# Задание 3
N = int(input())

factorial = 1
for i in range(1, N+1):
    factorial *= i
print(factorial)