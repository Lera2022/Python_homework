# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

lst = [1.1, 1.2, 3.1, 5, 10.01]

newlst = [lst[i] % 1 for i in filter(lambda x: lst[x] % 1 != 0, range(len(lst)))]
maxb = max(newlst)
minb = min(newlst)

print(maxb - minb)