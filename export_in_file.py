import json
import logic
path_to_db = 'db.json'


def export_txt():
    name = input('Введите имя или фамилию сотрудника, для экспорта в файл:  ')
    with open(path_to_db, 'r', encoding='UTF-8') as file:
        data = json.load(file)
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                with open('Export_emploe.txt', 'a') as export:
                    export.write('\n' + "".join(data[i]['Name']) + ' ' + "".join(
                        data[i]['Surname']) + ' ' + "".join(data[i]['Phone number']) + ' ' + "".join(data[i]['Comment']))

    print('\nДанные успешно экспортированы в файл!\n')
    logic.user_choice()