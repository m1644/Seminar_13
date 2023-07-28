


''' Задание №1
Создайте функцию, которая запрашивает числовые данные от пользователя до тех пор, 
пока он не введёт целое или вещественное число.
Обрабатывайте не числовые данные как исключения.
'''

def get_number():
    while True:
        try:
            num = float(input("Введите число: "))
            return num
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз.")

number = get_number()
print(f"Вы ввели число: {number}")