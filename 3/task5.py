# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# F−n = (−1)n+1Fn

# k = 8


# def fib(k):
#     fib_nums = []
#     a, b = 1, 1
#     for i in range(k):
#         fib_nums.append(a)
#         a, b = b, a + b
#     a, b = 0, 1
#     for i in range(k+1):
#         fib_nums.insert(0, a)
#         a, b = b, a - b
#     return fib_nums


# fib_nums = fib(k)
# print(fib_nums)

while True:
    try:
        n = int(input('Введите число: '))
    except ValueError:
        print('Не целое число')
        continue
    else:
        print('Целое число')
        break

fibonacci = [0, 1]
nega_fibonacci = [1, 0]

for i in range(2, n + 1):
    fibonacci.append(fibonacci[i -1] + fibonacci[i -2])
    nega_fibonacci.insert(0, nega_fibonacci[i] - nega_fibonacci[0])

if n == 0:
    print([0])
else:
    nega_fibonacci.extend(fibonacci[1:])
    print(nega_fibonacci)