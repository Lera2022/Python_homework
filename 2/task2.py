# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# def is_int(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False


# N = input('Введите целое число:')

# while not is_int(N):
#     print('Введённое значение не явлется целым числом')
#     N = input('Введите целое число:')

# N = int(N)
# factorial = 1
# for i in range(1, (N+1)):
#     factorial *= i
#     print(factorial, end=' ')

n = int(input('--> '))
# lst = []
# f = 1
# for i in range(1, n + 1):
#     f *= i
#     lst.append(f)
# print(lst)


# def fact(x):
#     if x == 0 or x == 1:
#         return 1
#     else:
#         return x * fact(x - 1)


# lst = list(map(lambda x: fact(x), range(1, n + 1)))
# print(lst)

def mult(x):
    mul = 1
    for i in x:
        mul *= i
    return mul

lst = list(map(lambda x: mult(list(range(1, x + 1))), range(1, n + 1)))
print(lst)