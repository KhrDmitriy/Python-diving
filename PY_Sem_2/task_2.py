import fractions
import math

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение дробей. Для проверки своего кода используйте модуль fractions.


num1 = input("Введите  первую дробь: ").split('/')
num2 = input("Введите вторую дробь: ").split('/')
# print(f'num1: {type(num1)}, num2: {type(num2)}')
# print(f'num1: {num1} num2: {num2}')

a1 = int(num1[0])
b1 = int(num1[1])
# print(f'a1: {a1}, b1: {b1}')
# print(f'a1: {type(a1)}, b1: {type(b1)}')

a2 = int(num2[0])
b2 = int(num2[1])
# print(f'a1: {a2}, b1: {b2}')
# print(f'a1: {type(a2)}, b1: {type(b2)}')

# Сумма
if b1 == b2:
    print(f' Сумма: {a1 + a2}/{b1}')
else:
    print(f' Сумма: {a1*b2 + a2*b1}/{b1*b2}')
# Произведение (умножение)
print(f' Произведение: {a1*a2}/{b1*b2}')


# Проверка.
f1 = fractions.Fraction(1, 3)
print(f1)                               # 1/3
f2 = fractions.Fraction(3, 5)
print(f2)                               # 3/5
print(f' Сумма: {f1 + f2})              # 14/15
print(f' Произведение: {f1 * f2})       # 1/5


