# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

# nums = 47756688399943
# nums = 1113384455229
nums = 1115566773322
str = str(nums)
my_dictionary = {}

for i in str:
    if i not in my_dictionary:
        my_dictionary[i] = 0
    elif i in my_dictionary:
        my_dictionary[i] += 1

print(my_dictionary)
unique = []


for k, v in my_dictionary.items():
    if v == 0:
        unique.append(int(k))


print(unique)
