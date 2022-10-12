# 5) Реализуйте алгоритм перемешивания списка.

from random import randint
list = [-1, -4, -7, -7, 8, -8, 4, 6]

for i in range(0, len(list) - 1):
    tmp = list[i]
    r = randint(0, len(list) - 1)
    list[i] = list[r]
    list[r] = tmp

print(list)
