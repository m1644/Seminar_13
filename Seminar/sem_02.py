


''' Задание №2
Создайте функцию аналог get для словаря.
Помимо самого словаря функция принимает ключ и значение по умолчанию.
При обращении к несуществующему ключу функция должна возвращать дефолтное значение.
Реализуйте работу через обработку исключений.
'''

def get_from_dict(dictionary, key, default='Ключ не существует'):
    try:
        return dictionary[key]
    except KeyError:
        return default


my_dict = {'Яблоко': 4, 'Банан': 8, 'Апельсин': 2}

key_to_find = 'Яблоко'
result = get_from_dict(my_dict, key_to_find)
print(f'Значение по ключу: {result}')
print('------------------------')

key_to_find = 'Груша'
result = get_from_dict(my_dict, key_to_find)
print(f'Значение по ключу: {result}')
