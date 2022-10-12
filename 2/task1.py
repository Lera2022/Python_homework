# 1) Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

def is_float(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


N = input('Введите вещественное число:')

while not is_float(N):
    print('Введённое значение не является вещественным числом')
    N = input('Введите число:')

sum = 0
for i in N:
    if i != '.' and i != '-':
        sum += int(i)
print(sum)
