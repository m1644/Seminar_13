from base_error import LevelError, AccessError


''' Задание №3
Создайте класс с базовым исключением и дочерние классы исключения:
○ ошибка уровня,
○ ошибка доступа.
'''

def check_access_level(access_level):
    if access_level > 5:
        raise LevelError('Ошибка уровня: Уровень доступа больше 5')
    elif access_level < 1:
        raise LevelError('Ошибка уровня: Уровень доступа меньше 1')
    else:
        print(f'Уровень доступа: {access_level}')

def check_access_error(user_password):
    password = 111
    if user_password != password:
        raise AccessError('Ошибка доступа: доступ запрещен.')


try:
    user_password = int(input('У вас есть доступ? \nВведите пароль: '))
    check_access_error(user_password)
    
    user_number = int(input('Введите уровень доступа (от 1 до 5): '))
    check_access_level(user_number)
except ValueError:
    print('Ошибка: Введите целое число.')
except LevelError as le:
    print(le)
except AccessError as ae:
    print(ae)
