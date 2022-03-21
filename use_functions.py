"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""
from datetime import datetime

total_cash = 0.0
history = {}

def top_up_on_account(total):
    print('Вы только что внесли сумму', total)
    return total

while True:
    print()
    print('1. пополнение счета')
    print('2. покупка')
    print('3. история покупок')
    print('4. запросить баланс')
    print('5. выход')
    print()

    choice = input('Выберите пункт меню: ')
    # пополнение счета
    if choice == '1':
        total_cash += float(input(f'На текущий момент на Вашем счете {total_cash} усл.ед. \nНа какую сумму Вы хотите пополнить счет: '))
        continue
    # покупка
    elif choice == '2':
        price_bag = float(input('Введите сумму покупки: '))
        if price_bag > total_cash:
            print('К сожалению на Вашем счете недостаточно денег: ')
            print('-' * 30)
        else:
            bag = input('Название покупки: ')
            # В историю записывается инф в  виде словаря {время: название покупки и цена}
            history[str(datetime.now().time())] = (bag, price_bag)
            total_cash -= price_bag
    # история покупок
    elif choice == '3':
        if history == {}:
            print('Вы еще не совершали покупок')
        else:
          print()
          print('{} {:>15} {}'.format('Дата покупки', 'Товар', 'Стоимость'))
          for k, v in history.items():
            print(f'{k} {v}')
    # запросить баланс
    elif choice == '4':
        print(f'Баланс: {total_cash}')
    # выход
    elif choice == '5':
        exit()
        # break
    else:
        print('Неверный пункт меню')
