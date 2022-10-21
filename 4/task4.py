# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени
# Записываем результат в файл.
# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint, random


def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def is_positive(value):
    value = int(value)
    if value < 0:
        return False
    else:
        return True

k = input('Введите натуральное число от 1 до 9:')

while not is_int(k):
    print('Введённое значение не явлется целым числом')
    k = input('Введите натуральное число от 1 до 9:')

while not is_positive(k):
    print('Введённое значение не явлется положительным числом')
    k = input('Введите натуральное число от 1 до 9:')

while (1 > int(k)) or (int(k) > 9):
    print('Введённое значение не явлется натуральным числом от 1 до 9')
    k = input('Введите натуральное число от 1 до 9:')

k = int(k)
coefficients = {}
degrees = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']        # для красивого вывода

for i in range(0, k + 1):
    coefficients['x' + degrees[i]] = randint(-100, 100)

items = list(coefficients.items())
y = {n: v for n, v in reversed(items)}
print(y)

polynomial = ''

for n, v in y.items():
    if v != 0:
        polynomial = polynomial + str(v) + n + '+'

polynomial = polynomial.replace('+-', ' - ')
polynomial = polynomial.replace('+', ' + ')
polynomial = polynomial.replace('x⁰', '')
polynomial = polynomial.replace('x¹', 'x')
polynomial = polynomial + '= 0'
polynomial = polynomial.replace('+ =', '=')


print(polynomial)

# для записи в файл

polynomial = polynomial.replace('+ =', '=')
polynomial = polynomial.replace('⁹', 'вЃ№')
polynomial = polynomial.replace('⁸', 'вЃё')
polynomial = polynomial.replace('⁷', 'вЃ·')
polynomial = polynomial.replace('⁶', 'вЃ¶')
polynomial = polynomial.replace('⁵', 'вЃµ')
polynomial = polynomial.replace('⁴', 'вЃґ')
polynomial = polynomial.replace('³', 'Ві')
polynomial = polynomial.replace('²', 'ВІ')

print(polynomial)

data = open('4.txt', 'a')
data.write(polynomial)
data.close()