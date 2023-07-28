


''' Задача_1
Возьмите 1-3 задачи из тех, что были на прошлых семинарах или в домашних заданиях. 
Напишите к ним классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. 
Например нельзя создавать прямоугольник со сторонами отрицательной длины.
'''

# Задача с прямоугольником

class NegativeSideError(Exception):
    pass

class NotRectangleError(Exception):
    pass


class Rectangle:
    def __init__(self, length, width=None):
        if length < 0 or (width is not None and width < 0):
            raise NegativeSideError("Стороны прямоугольника не могут быть отрицательными")
        self.length = length
        self.width = length if width is None or width == "" else width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        if not isinstance(other, Rectangle):
            raise NotRectangleError("Можно сложить только два прямоугольника")
        new_length = self.length + other.length
        new_width = self.width + other.width
        return Rectangle(new_length, new_width)

    def __sub__(self, other):
        if not isinstance(other, Rectangle):
            raise NotRectangleError("Можно вычесть только другой прямоугольник")
        new_length = self.length - other.length
        new_width = self.width - other.width
        new_length = max(new_length, 0)
        new_width = max(new_width, 0)
        return Rectangle(new_length, new_width)

    def __eq__(self, other):
        if not isinstance(other, Rectangle):
            return False
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Rectangle):
            raise NotRectangleError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() < other.get_area()

    def __le__(self, other):
        if not isinstance(other, Rectangle):
            raise NotRectangleError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() <= other.get_area()

    def __gt__(self, other):
        if not isinstance(other, Rectangle):
            raise NotRectangleError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        if not isinstance(other, Rectangle):
            raise NotRectangleError("Можно сравнивать только с другим прямоугольником")
        return self.get_area() >= other.get_area()


try:
    length_1 = float(input("Введите длину первого прямоугольника: "))  
    width_1 = input("Введите ширину первого прямоугольника (если оставить пустым, будет считаться квадрат): ")
    if width_1:
        width_1 = float(width_1)
    rectangle_instance_1 = Rectangle(length_1, width_1)
except NegativeSideError as e:
    print(e)
    exit()

try:  
    length_2 = float(input("Введите длину второго прямоугольника: "))
    width_2 = input("Введите ширину второго прямоугольника (если оставить пустым, будет считаться квадрат): ")
    if width_2:
        width_2 = float(width_2)
    rectangle_instance_2 = Rectangle(length_2, width_2)
except NegativeSideError as e:
    print(e)
    exit()

try:
    perimeter_1 = rectangle_instance_1.get_perimeter()
    perimeter_2 = rectangle_instance_2.get_perimeter()

    print(f"Периметр первого прямоугольника: {perimeter_1}")
    print(f"Периметр второго прямоугольника: {perimeter_2}")

    sum_rectangle = rectangle_instance_1 + rectangle_instance_2
    sum_perimeter = sum_rectangle.get_perimeter()
    sum_area = sum_rectangle.get_area()
    print(f"Сумма периметров прямоугольников: {sum_perimeter}")
    print(f"Площадь суммы прямоугольников: {sum_area}")

    sub_rectangle = rectangle_instance_1 - rectangle_instance_2
    sub_perimeter = sub_rectangle.get_perimeter()
    sub_area = sub_rectangle.get_area()
    print(f"Разность периметров прямоугольников (не меньше нуля): {sub_perimeter}")
    print(f"Площадь разности прямоугольников (не меньше нуля): {sub_area}")

    if rectangle_instance_1 == rectangle_instance_2:
        print("Прямоугольники равны по площади")
    elif rectangle_instance_1 != rectangle_instance_2:
        print("Прямоугольники не равны по площади")

    if rectangle_instance_1 < rectangle_instance_2:
        print("Первый прямоугольник меньше второго по площади")
    elif rectangle_instance_1 <= rectangle_instance_2:
        print("Первый прямоугольник меньше или равен второму по площади")
    if rectangle_instance_1 > rectangle_instance_2:
        print("Первый прямоугольник больше второго по площади") 
    elif rectangle_instance_1 >= rectangle_instance_2:
        print("Первый прямоугольник больше или равен второму по площади")

except NotRectangleError as e:
    print(e)
    exit()

except NegativeSideError as e:
    print(e) 
    exit()
