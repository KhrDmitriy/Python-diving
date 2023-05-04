# 2. Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление. .


def reverse_dict(** kwargs) -> dict:
    new_dict = {}
    for k, v in kwargs.items():
        new_dict[v] = k
    return new_dict


print(reverse_dict(name='Ivan', lastname='Ivanov'))