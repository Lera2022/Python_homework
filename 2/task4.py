# 4) Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции вводятся с клавиатуры .

# import random


# def is_int(value):
#     try:
#         int(value)
#         return True
#     except ValueError:
#         return False


# def is_positive(value):
#     value = int(value)
#     if value < 0:
#         return False
#     else:
#         return True


# def is_position(value):
#     value = int(value)
#     if 0 <= value <= (N - 1):
#         return True
#     else:
#         return False


# N = input('Введите натуральное число:')

# while not is_int(N):
#     print('Введённое значение не явлется целым числом')
#     N = input('Введите натуральное число:')

# while not is_positive(N):
#     print('Введённое значение не явлется положительным числом')
#     N = input('Введите натуральное число:')

# N = int(N)

# sum = 0
# list = []
# list = [random.randint(-N, N) for i in range(N)]
# print(list)

# A = input('Введите позицию элемента 1:')

# while not is_int(A):
#     print('Введённое значение не явлется целым числом')
#     A = input('Введите позицию элемента 1:')

# while not is_position(A):
#     print('Введённое значение позиции не существует в данном списке')
#     A = input('Введите позицию элемента 1:')

# B = input('Введите позицию элемента 2:')

# while not is_int(B):
#     print('Введённое значение не явлется целым числом')
#     B = input('Введите позицию элемента 2:')

# while not is_position(B):
#     print('Введённое значение позиции не существует в данном списке')
#     B = input('Введите позицию элемента 2:')

# A = int(A)
# B = int(B)
# prd = list[A] * list[B]
# print('Произведение элементов = ', prd)

from random import randint

n = int(input('--> '))

# index = list(map(int, input('index --> ').split()))
index = [int(i) for i in input().split()]

print(index)

lst = [randint(-n, n) for i in range(n)]
print(lst)

lst2 = [lst[i] for i in list(filter(lambda x: x in index,range(n)))]

print(lst2)