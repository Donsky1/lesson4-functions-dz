"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""

# year = input('Ввведите год рождения А.С.Пушкина:')
# while year != '1799':
#     print("Не верно")
#     year = input('Ввведите год рождения А.С.Пушкина:')
#
# day = input('Ввведите день рождения Пушкин?')
# while day != '6':
#     print("Не верно")
#     day = input('В какой день июня родился Пушкин?')
# print('Верно')

def check_year(year):
    while year != '1799':
        print("Неверно")
        year = input('Ввведите год рождения А.С.Пушкина: ')

    return True

def check_day(day):
    while day != '6':
        print("Неверно")
        day = input('В какой день июня родился Пушкин? ')

    return True

def check_birthday_pushkin():
    year = input('Ввведите год рождения А.С.Пушкина: ')
    true_year = check_year(year)

    day = input('Ввведите день рождения Пушкина? ')
    true_day = check_day(day)

    if true_year and true_day:
        print('Верно')


check_birthday_pushkin()