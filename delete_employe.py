import json
import logic

path_to_db = 'db.json'

def delete_employe():
    name = input('Введите имя или фамилию сотрудника, которого надо удалить:  ')

    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
        # if name not in data:
        #         print('Такого контакта нет')
    with open(path_to_db, 'w', encoding='UTF-8') as file:
        json.dump(data, file, indent=4)
    print('\nДанные о сотруднике успешно удалены!\n')
    logic.user_choice()