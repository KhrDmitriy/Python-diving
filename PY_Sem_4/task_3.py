# 3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


my_sum = 0
counter = 0
flag = True
transactions = []


def start():
    transactions = []
    print('Банкомат. Выберете пункт из меню:')
    while flag:
        enter = int(input('Пополнить: нажмите 1 \n'
                          'Снять: нажмите 2 \n'
                          'Выйти: нажмите 3 \n'
                          'Мой счет: нажмите 4 \n'))
        if enter == 1:
            print('Пополнение счета')
            deposit()
        elif enter == 2:
            print('Снятие со счета')
            withdraw()
        elif enter == 3:
            print('Выход')
            exiting()
        elif enter == 4:
            slip()
            print('Возьмите чек.\n'
                  'Операция завершена.')
            exiting()
        else:
            print('Ошибка. Выберете пункт из меню.')
        print(f'Счетчик операций по карте: {counter}')


def deposit():
    global my_sum
    global counter

    if my_sum >= 5_000_000:
        my_sum -= my_sum * 0.1

    money = int(input('Пополнить на: '))
    if money > 0 and money % 50 == 0:
        transactions.append(money)
        my_sum += money
        counter += 1
        if counter % 3 == 0:
            my_sum += (my_sum * 0.03)
    else:
        print('Ошибка. Сумма пополнения должна быть кратна 50')
        deposit()
    print(f'Пополнение на {money} y.e.\n'
          f'На счете: {my_sum} у.е.')
    print(f'Операции по счету: {transactions}')


def withdraw():
    global my_sum
    global counter

    if my_sum >= 5_000_000:
        my_sum -= my_sum * 0.1

    money = int(input('Снять со счета: '))
    if money % 50 == 0 and (my_sum - money) >= 0:
        transactions.append(-money)
        commission_fee = money * 0.015
        if commission_fee < 30:
            my_sum -= (money + 30)
        elif commission_fee > 600:
            my_sum -= (money + 600)
        else:
            my_sum -= (money + commission_fee)
        counter += 1
        if counter % 3 == 0:
            my_sum += (my_sum * 0.03)
    else:
        if money % 50 != 0:
            print('Ошибка. Сумма снятия должна быть кратна 50')
        elif (my_sum - money) < 0:
            print('Ошибка. Сумма для снятия превышает баланс по карте...')
        else:
            print('Ошибка. Сумма снятия должна быть кратна 50.\n'
                  'Сумма для снятия превышает баланс по карте...')
        withdraw()
    print(f'Вы сняли {money} y.e.\n'
          f'На счете: {my_sum} у.е.')
    print(f'Операции по счету: {transactions}')


def exiting():
    global flag
    flag = False
    print(transactions)


def slip():
    print(f'На вашем счете {my_sum} y.e.')


start()
print()
print(transactions)

