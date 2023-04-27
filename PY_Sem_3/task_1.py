# Задача №1
# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке
# не должно быть дубликатов.


num = [1, 2, 2, 3, 4, 3, 5, 3, 6]
print(num)

# Вернуть список с дублирующимися элементами
new_num_1 = []
for i in num:
    a = 0
    for j in num:
        if i == j:
            a += 1
    if a > 1:
        new_num_1.append(i)
print(new_num_1)

# Вернуть список без дубликатов
new_num_2 = []
for elem in num:
    if elem not in new_num_2:
        new_num_2.append(elem)
print(new_num_2)

# Вернуть список без повторений (уникальные значения).
new_num_3 = []
for k in num:
    a = 0
    for h in num:
        if k == h:
            a += 1
    if a == 1:
        new_num_3.append(k)
print(new_num_3)




