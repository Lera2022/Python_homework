from app.controller import ctrl


def menu():
    print('\nГлавное меню:\n'
          '\n1. Открыть txt-файл\n'
          '2. Открыть csv-файл\n'
          '3. Сохранить txt-файл\n'
          '4. Сохранить csv-файл\n'
          '5. Показать все контакты из базы данных\n'
          '6. Поиск контакта в csv-файле\n'
          '7. Добавить контакт в csv-файл\n'
          '0. Выход\n')
    return (int(input('->> ')))


def init():
    ctrl.main_loop()


def showinfo(a):
    print(a)
