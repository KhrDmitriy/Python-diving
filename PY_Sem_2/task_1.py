# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.


num = int(input("Введите целое число: "))
print('Функция hex(): ' + hex(num))

data = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

str_represent = ''

DIVIDER = 16

while num > 0:
    i = num % DIVIDER
    str_represent = str(data[i]) + str_represent
    num //= DIVIDER
str_represent = '0x' + str_represent
print('Результат: ' + str_represent)
