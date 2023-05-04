# 1 задача:
# ✔️ Напишите функцию, которая принимает на вход строку —
# абсолютный путь до файла. Функция возвращает кортеж из трёх
# элементов: путь, имя файла, расширение файла.

from pathlib import Path


# 1 вариант
def absolut_path(new_path: str) -> tuple[str, str, str]:
    p = Path(new_path)
    return str(p.parent), p.name, p.suffix


my_path = 'D:\Projects\PythonProjects\GeekBrains\Lecture2\main.py'
print(absolut_path(my_path))


# 2 вариант
def sep_path(new_path: str) -> tuple:
    new_list = new_path.split('\\')
    parent_dir = '\\'.join(new_list[:-1])
    name, ext = new_list[-1].split('.')
    return parent_dir, name, ext


print(sep_path(my_path))
