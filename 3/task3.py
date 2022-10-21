# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19


list = [1.1, 1.2, 3.1, 5, 10.01]
min = list[0] - int(list[0])
max = list[0] - int(list[0])

for i in list:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)
print(max-min)

# newlst = []
# for i in range(len(lst)):
#     n = lst[i] % 1
#     if n != 0:
#         newlst.append(n)

# maxb = max(newlst)
# minb = min(newlst)

# print(maxb - minb)