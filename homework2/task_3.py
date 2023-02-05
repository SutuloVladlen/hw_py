"""
Требуется вывести все целые степени двойки (т.е. числа вида 2**k), не превосходящие числа N.
Пример:
10 -> 1 2 4 8
"""
number = int (input('Введите целое число по отношению к которому будем искать степени двойки'))
degree_of_2 = 0
list_degree_of_2 = []
degree = 0
while degree_of_2 <= number:
    degree_of_2 = 2**degree
    degree += 1
    if degree_of_2 > number:
        break
    list_degree_of_2.append(degree_of_2)
print(*list_degree_of_2) # можно как то сделать принт (f"текст {*list_degree_of_2}") при такой записи не работает код
