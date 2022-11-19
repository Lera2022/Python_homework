from app.view import tk_view
from app.view import c_view
from . import db_sqlite3
from . import db_csv
from app.model import tel
import pathlib
from pathlib import Path
g_mod = None
d_mod = None


path = Path("phonebook.csv")


def init_view():
    global g_mod
    match g_mod:
        case 1: c_view.init()
        case 2: tk_view.init()


def init_db():
    global d_mod
    match d_mod:
        case 1:
            db_sqlite3.init()
        case 2:
            db_csv.init()
#       case 3:
#           db_mysql.init()


def get_data_from_database(str_pattern) -> list:
    global d_mod
    match d_mod:
        case 1:
            return db_sqlite3.get_data(str_pattern)
        case 2:
            return db_csv.get_data(str_pattern)
#        case 3:
#            return db_mysql.get_data(str_pattern)


def load_from_csv(file_name):

    global d_mod

    lst_data = db_csv.get_data_from_file(file_name)
    match d_mod:
        case 1:
            db_sqlite3.push_data(lst_data)
        case 2:
            pass
        case 3:
            pass


def remove_data_from_database(data):
    global d_mod
    match d_mod:
        case 1:
            return db_sqlite3.remove_data(data)
        case 2:
            pass
        case 3:
            pass


def init(g_in, d_in):
    global g_mod
    global d_mod
    g_mod = g_in
    d_mod = d_in
    init_db()
    init_view()


def main_loop():
    global answer
    while True:
        choice = c_view.menu()
        match choice:
            case 1:
                tel.importTxt()
                input('Нажмите Enter, чтобы продолжить')
            case 2:
                c_view.showinfo(tel.importCsv())
                input('Нажмите Enter, чтобы продолжить')
            case 3:
                data = get_data_from_database(str_pattern=' ')
                c_view.showinfo(tel.exportTxt(data))
                input('Нажмите Enter, чтобы продолжить')
            case 4:
                data = get_data_from_database(str_pattern=' ')
                c_view.showinfo(tel.exportCsv(data))
                input('Нажмите Enter, чтобы продолжить')
            case 5:
                data = get_data_from_database(str_pattern='')
                for record in data:
                    c_view.showinfo(f'{record[0]} \t {record[1]}')
                input('Нажмите Enter, чтобы продолжить')
            case 6:
                c_view.showinfo(tel.findInCsv())
                input('Нажмите Enter, чтобы продолжить')
            case 7:
                c_view.showinfo(tel.addToCsv())
                input('Нажмите Enter, чтобы продолжить')
            case 0:
                break
