# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

list = [2, 3, 5, 9, 3]
sum_odd = 0

for i in range(0, len(list)):
    if i % 2 != 0:
        sum_odd += list[i]

print(sum_odd)
