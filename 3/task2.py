# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 4, 5, 6]

# lst2 = list[2:5]    # [4, 5, 6]
# lst2 = list[::3]
# print(lst2)

# lst2 = list(reversed(lst))
# lst3 = []

# for i in range(len(lst)):
#     lst3.append(lst[i] * lst2[i])
# print(lst3[0:len(lst) // 2 + len(lst) % 2])

# if len(lst) % 2 == 0:
#     n = len(lst)//2
# else:
#     n = len(lst)//2 + 1

# a = int(len(list) / 2) - проверила, до какого индекса будет считать
# print(a)

# for i in range(len(lst)//2 + 1):
#     newlst.append(lst[i] * lst[-i-1])

# from math import ceil
# for i in range(ceil(len(lst)/2)):

prd_list = []

for i in range(0, int(len(list) / 2)):
    prd_list.append(list[i] * list[len(list) - 1 - i])

if len(list) % 2 != 0:
    prd_list.append(list[i + 1] ** 2)

print(prd_list)
