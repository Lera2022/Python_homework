# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# list = [2, 3, 5, 9, 3]
# sum_odd = 0

# for i in range(0, len(list)):       # range(len(list))  range(1, len(list), 2)
#     if i % 2 != 0:
#         sum_odd += list[i]

# # i = 1
# # while i < len(str):
# #     sum += list[i]
# #     i+=2

# # sum(lst(1::2))

# print(sum_odd)

from random import randint

lst = [randint(-10, 10) for i in range(10)]

lst2 = lst[1::2]

print(lst)
print(lst2)

lst3 = [lst[i] for i in filter(lambda x: x % 2 == 1, range(10))]

print(lst3)

lst4 = [lst[i] for i in range(10) if i % 2 == 1]

print(lst4)