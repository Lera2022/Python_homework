import csv
import pathlib
from pathlib import Path
import sys
import re


def get_create_table_query():
    res_query = 'CREATE TABLE IF NOT EXISTS telephones(' +\
                'rowid INTEGER PRIMARY KEY AUTOINCREMENT, ' +\
                'name TEXT, ' +\
                'tel TEXT);'
    return res_query


def get_add_tel_query() -> str:
    res_query = 'INSERT INTO telephones(name, tel) ' +\
                'VALUES(?, ?);'
    return res_query


def select_tel_query(str_pattern) -> str:

    res_query = 'SELECT name,tel,rowid FROM telephones'

    if str_pattern == '':
        return res_query + ';'
    else:
        return res_query + f' WHERE name LIKE \"%{str_pattern}%\" OR tel LIKE \"%{str_pattern}%\";'


def get_remove_query(data: tuple) -> str:
    res_query = f'DELETE FROM telephones WHERE rowid = {data[2]};'
    return res_query


def importTxt():
    path = Path("phonebook.txt")
    file1 = open(path, "r", encoding='utf-8')
    list = []
    while True:
        line = file1.readline()
        if not line:
            break
        list.append(line)
    print(list)
    file1.close


def importCsv():
    path = Path("phonebook.csv")
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        list = []
        for row in file_reader:
            list.append(row)
        return list


def exportTxt(data):
    MyFile = open('export.txt', 'w', encoding='utf-8')
    for row in data:
        string = str(row)
        MyFile.writelines(f'{string}\n')
    MyFile.close()
    return 'файл txt создан в общей папке'


def exportCsv(data):
    file = 'export.csv'
    with open(file, 'a', encoding='utf-8') as export:
        export.write(str(data))
    return 'файл scv создан в общей папке'


def findInCsv():
    lastname = input('Введите любую информацию о контакте\n').upper()
    path = Path("phonebook.csv")
    with open(path, encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:
            answer = ';'.join(row)
            if not answer.find(lastname):
                return answer


def addToCsv():
    new_contact = '\n'
    surname = input('Введите фамилию: ')
    new_contact = new_contact + surname + ';'
    name = input('Введите имя и отчество: ')
    new_contact = new_contact + name + ';'
    phone = input('Введите телефон: ')
    new_contact = new_contact + phone + ';'
    comment = input('Введите комментарий: ')
    new_contact = new_contact + comment
    path = Path("phonebook.csv")
    with open(path, 'a', encoding='utf-8') as export:
        export.write(str(new_contact))
    return 'новый контакт добавлен в файл phonebook.csv'
