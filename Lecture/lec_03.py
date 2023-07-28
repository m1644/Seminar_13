


#### . Ключевое слово raise

'''
def add_key(dct, key, value):
    if key in dct:
        raise KeyError(f'Перезаписывание существующего ключа запрещено. {dct[key] = }')
    dct[key] = value
    return dct

data = {'one': 1, 'two': 2}
print(add_key(data, 'three', 3))
print(add_key(data, 'three', 3))
'''


#### Поднимаем исключения в классах

class User:
    def __init__(self, name, age):
        if 6 < len(name) < 30:
            self.name = name
        else:
            raise ValueError(f'Длина имени должна быть между 6 и 30 символами. {len(name) = }')
        if not isinstance(age, (int, float)):
            raise TypeError(f'Возраст должен быть числом. Используйте int или float. {type(age) = }')
        elif age < 0:
            raise ValueError(f'Возраст должен быть положительным. {age = }')
        else:
            self.age = age

user = User('Яковлев', 12)


#### Задание_2

def func(a, b, c):
    if a < b < c:
        raise ValueError('Не перемешано!')
    elif sum((a, b, c)) == 42:
        raise NameError('Это имя занято!')
    elif max(a, b, c, key=len) < 5:
        raise MemoryError('Слишком глуп!')
    else:
        raise RuntimeError('Что-то не так!!!')

# func(11, 7, 3)  # 1  # TypeError: object of type 'int' has no len()
# func(3, 2, 3)  # 2   # TypeError: object of type 'int' has no len()
# func(73, -40, 9)  # 3  # NameError: Это имя занято!
# func(10, 20, 30)  # 4  # ValueError: Не перемешано!
