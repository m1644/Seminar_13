import json


''' Задание №4
Вспоминаем задачу из семинара 8 про сериализацию данных, где в бесконечном цикле запрашивали имя, 
личный идентификатор и уровень доступа (от 1 до 7) сохраняя информацию в JSON файл.
Напишите класс пользователя, который хранит эти данные в свойствах экземпляра.
Отдельно напишите функцию, которая считывает информацию из JSON файла и формирует множество пользователей.
'''

class User:
    def __init__(self, identifier, name, access_level):
        self.identifier = identifier
        self.name = name
        self.access_level = access_level

def read_users_from_file(users_file):
    try:
        with open(users_file, 'r', encoding='utf-8') as file:
            users_data = json.load(file)
            users_list = []

            for identifier, user_data in users_data.items():
                name = user_data['name']
                access_level = user_data['access_level']
                user = User(identifier, name, access_level)
                users_list.append(user)

            return users_list
    except FileNotFoundError:
        return []

def add_user(users_file):
    users = read_users_from_file(users_file)

    while True:
        name = input('Введите имя пользователя (или "exit" для завершения): ')
        if name.lower() == 'exit':
            break

        identifier = input('Введите личный идентификатор пользователя: ')
        access_level = int(input('Введите уровень доступа (от 1 до 7): '))

        if access_level not in range(1, 8):
            print('Некорректный уровень доступа. Попробуйте снова.')
            continue

        if any(user.identifier == identifier for user in users):
            print('Идентификатор уже занят. Попробуйте снова.')
            continue

        users.append(User(identifier, name, access_level))

        with open(users_file, 'w', encoding='utf-8') as file:
            json.dump({user.identifier: {'name': user.name, 'access_level': user.access_level} for user in users}, file, indent=4, ensure_ascii=False)

    print('Данные сохранены в файле "users.json".')
    print('Список пользователей:')
    for user in users:
        print(f'Идентификатор: {user.identifier}, Имя: {user.name}, Уровень доступа: {user.access_level}')

users_file = 'Seminar/users.json'
add_user(users_file)
read_users_from_file(users_file)
