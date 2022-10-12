# 3) Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# *Пример:*
#     Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
#     Сумма 9.06

def is_int(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


N = input('Введите целое число:')

while not is_int(N):
    print('Введённое значение не явлется целым числом')
    N = input('Введите целое число:')

N = int(N)

sum = 0
MyDictionary = {}
for i in range(1, N + 1):
    MyDictionary[i] = (1 + 1 / i)**i
    sum += MyDictionary[i]
print(MyDictionary)
print(sum)
