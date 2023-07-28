from user_error import UserNameError, UserAgeError


######## Создание собственных исключений

class User:
    MIN_LEN = 6
    MAX_LEN = 30

    def __init__(self, name, age):
        if self.MIN_LEN < len(name) < self.MAX_LEN:
            self.name = name
        else:
            raise UserNameError(name, self.MIN_LEN, self.MAX_LEN)
        if not isinstance(age, (int, float)) or age < 0:
            raise UserAgeError(age)
        else:
            self.age = age


# user = User('Яков', '-12')  # UserNameError: Имя пользователя Яков содержит 4 символа(ов).
# user = User('Яковлев', '-12')   # UserAgeError: Возраст пользователя должен быть целым int() или вещественным float() больше нуля.
# user = User('Яковлев', -12)  # UserAgeError: Возраст пользователя должен быть целым int() или вещественным float() больше нуля.
user = User('Яковлев', 12)
