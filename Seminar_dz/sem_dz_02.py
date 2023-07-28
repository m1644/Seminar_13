


''' Задача_1
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. 
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
'''

# Задача с факториалом

class FactorialInputError(Exception):
    def __init__(self, message):
        super().__init__(message)


class FactorialGenerator:
    def __init__(self, start=1, stop=None, step=1):
        if start < 1 or (stop is not None and stop < start) or step < 1:
            raise FactorialInputError("Неправильные параметры для генерации факториалов")
        self.start = start
        self.stop = stop if stop is not None else start
        self.step = step

    def factorial(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * self.factorial(n - 1)

    def generate_factorials(self):
        current = self.start
        while current <= self.stop:
            yield self.factorial(current)
            current += self.step


def get_input():
    args = input("Введите три параметра через пробел (start stop step): ").split()
    start = int(args[0]) if len(args) >= 1 else 1
    stop = int(args[1]) if len(args) >= 2 else None
    step = int(args[2]) if len(args) >= 3 else 1
    return start, stop, step


if __name__ == "__main__":
    try:
        start, stop, step = get_input()
        generator = FactorialGenerator(start, stop, step)
        for factorial in generator.generate_factorials():
            print(f"Факториал {start} = {factorial}")
            start += step
    except ValueError as ve:
        print(f"Ошибка ввода данных: {ve}")
    except FactorialInputError as ifie:
        print(f"Ошибка в параметрах генерации факториалов: {ifie}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
