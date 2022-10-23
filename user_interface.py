import chek
from export_in_file import export_txt


def start():
    greetings = 'Добрый день! Вас приветствует база данных стоматологической клиники "Добрый стоматолог"'

    print(f'{greetings}\n')


def menu():
    what_to_do = 'Выберите соответствующую цифру в меню:'
    new_book = '0. Создать новую книгу или очистить существующую' # изменить
    new_employe = '1. Добавить нового сотрудника'
    change_number = '2. Изменить номер телефона сотрудника'
    change_surname = '3. Изменить фамилию сотрудника'
    delete_employe = '4. Удалить профиль сотрудника'
    view_all_employe = '5. Показать всех сотрудников'
    export_to_file = '6. Экспортировать все записи в файл'
    to_exit = '7. Выход'
    print(f'{what_to_do}\n\n{new_book}\n{new_employe}\n{change_number}\n{change_surname}\n{delete_employe}\n{view_all_employe}\n{export_to_file}\n{to_exit}')
    return chek.digit_check()