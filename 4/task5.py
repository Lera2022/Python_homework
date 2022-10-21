# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x + 33 = 0
# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x + 53 = 0
degrees = ['⁰', '¹', '²', '³', '⁴', '⁵', '⁶', '⁷', '⁸', '⁹']

f = open('5(1).txt', 'r')
str1 = f.readline()
str1 = str1.replace(' ', '')[:-2]
str1 = str1.replace('вЃ№', '^9')
str1 = str1.replace('вЃё', '^8')
str1 = str1.replace('вЃ·', '^7')
str1 = str1.replace('вЃ¶', '^6')
str1 = str1.replace('вЃµ', '^5')
str1 = str1.replace('вЃґ', '^4')
str1 = str1.replace('Ві', '^3')
str1 = str1.replace('ВІ', '^2')
str1 = str1.replace('x-', 'x^1-')
str1 = str1.replace('x+', 'x^1+')
str1 = str1.replace('=', 'x^0')
list1 = str1.replace('-', '+-').split('+')
list1.reverse()

coefficients1 = {}

for i in range(len(list1)):
    for j in range(0, 10):
        if list1[i].find(f'x^{j}') != -1:
            coefficients1[j] = list1[i]
            
for n, v in coefficients1.items():
    coefficients1[n] = v[:-3]
    if v[:-3] == '':
        coefficients1[n] = 1

for n, v in coefficients1.items():
    coefficients1[n] = int(coefficients1[n])

print(coefficients1)

f = open('5(2).txt', 'r')
str2 = f.readline()
str2 = str2.replace(' ', '')[:-1]
str2 = str2.replace('вЃ№', '^9')
str2 = str2.replace('вЃё', '^8')
str2 = str2.replace('вЃ·', '^7')
str2 = str2.replace('вЃ¶', '^6')
str2 = str2.replace('вЃµ', '^5')
str2 = str2.replace('вЃґ', '^4')
str2 = str2.replace('Ві', '^3')
str2 = str2.replace('ВІ', '^2')
str2 = str2.replace('x-', 'x^1-')
str2 = str2.replace('x+', 'x^1+')
str2 = str2.replace('=', 'x^0')
list2 = str2.replace('-', '+-').split('+')
list2.reverse()

coefficients2 = {}

for i in range(len(list2)):
    for j in range(0, 10):
        if list2[i].find(f'x^{j}') != -1:
            coefficients2[j] = list2[i]

for n, v in coefficients2.items():
    coefficients2[n] = v[:-3]
    if v[:-3] == '':
        coefficients1[n] = 1

for n, v in coefficients2.items():
    coefficients2[n] = int(coefficients2[n])

print(coefficients2)

sum_coefficients = coefficients1.copy()
for k, v in coefficients2.items():
    sum_coefficients[k] = sum_coefficients.get(k, 0) + v

print(sum_coefficients)
sum_coefficients = dict(sorted(sum_coefficients.items()))
print(sum_coefficients)
items = list(sum_coefficients.items())
y = {n: v for n, v in reversed(items)}
print(y)
polynomial = ''

for n, v in y.items():
    if v != 0:
        polynomial = polynomial + str(v) + 'x^' + str(n) + '+'

polynomial = polynomial.replace('+-', ' - ')
polynomial = polynomial.replace('+', ' + ')
polynomial = polynomial.replace('x^0', '')
polynomial = polynomial.replace('x^1', 'x')
polynomial = polynomial + '= 0'
polynomial = polynomial.replace('+ =', '=')
polynomial = polynomial.replace('+ =', '=')
polynomial = polynomial.replace('^9', 'вЃ№')
polynomial = polynomial.replace('^8', 'вЃё')
polynomial = polynomial.replace('^7', 'вЃ·')
polynomial = polynomial.replace('^6', 'вЃ¶')
polynomial = polynomial.replace('^5', 'вЃµ')
polynomial = polynomial.replace('^4', 'вЃґ')
polynomial = polynomial.replace('^3', 'Ві')
polynomial = polynomial.replace('^2', 'ВІ')
polynomial = polynomial.replace('- 1x', '- x')
polynomial = polynomial.replace('+ 1x', '+ x')

print(polynomial)

data = open('5(3).txt', 'a')
data.write(polynomial)
data.close()