# 3 задача:
# ✔️ Создайте функцию генератор чисел Фибоначчи (см. Википедию).
# f(n-1)+f(n-2)
# 0 1 1 2 3 5 8 13


def f_gen(n: int):
    a, b = 0, 1
    for _ in range(n + 1):
        yield a  # список из 'a'
        a, b = b, a + b


print(list(f_gen(10)))
