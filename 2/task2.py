# 2) Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

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
factorial = 1
for i in range(1, (N+1)):
    factorial *= i
    print(factorial, end=' ')
