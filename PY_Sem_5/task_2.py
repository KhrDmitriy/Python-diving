2 задача:
# ✔️ Напишите однострочный генератор словаря, который принимает
# на вход три списка одинаковой длины: имена str, ставка int,
# премия str с указанием процентов вида «10.25%». В результате
# получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


def bonus_dict_gen(names: list[str], salary: list[int], bonus: list[str]):
    new_dict = {name: (salary * float(bonus[:-1]) / 100) for name, salary, bonus in zip(names, salaries, bonuses)}
    return new_dict


names = ['Ivan', 'Petr', 'Nikolay']
salaries = [100000, 90000, 110000]
bonuses = ['10.25%', '12.5%', '20%']
print(bonus_dict_gen(names, salaries, bonuses))
