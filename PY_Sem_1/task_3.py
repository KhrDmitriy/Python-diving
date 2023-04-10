# 3.  Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать «больше» или «меньше» после каждой попытки.
# Для генерации случайного числа используйте код: from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)


from random import randint
num = randint(0, 1000)
# print(num)
i = 0
if i < 10:
    while i < 10:
        n = int(input("Введите число: "))
        if n == num:
            print("Вы угадали")
            break
        elif n < num:
            print("Загаданное число больше")
        elif n > num:
            print("Загаданное число меньше")
        else:
            print("Попробуйте еще раз")
        i += 1
    else:
        print("Количество попыток превышено, можно плакать")


