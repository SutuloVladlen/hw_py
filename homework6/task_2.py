"""
Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
"""
from random import randint


def list_of_nambers(a:int):
    list_of_nambers = []
    # list_of_nambers = [randint(-10,20) for i in range(a)]
    for i in range(a):
        list_of_nambers.append(int(input("Введите число последовательности")))
    return list_of_nambers


def determination_of_membership_in_a_list(max:int, min:int, list_namber:list):
    resalt = []
    if max<min:
        max,min=min,max
    for i in range(len(list_namber)):
        if min <= list_namber[i] <= max:
            resalt.append(i)
    return resalt

list_of_namber = list_of_nambers (int(input("Введите количество чисел в списке")))
print(list_of_namber)
min_n,max_n = int(input("Введте диапазон чиссел от")),int(input("до"))
list_resalt = (determination_of_membership_in_a_list(max_n,min_n,list_of_namber))
print(list_resalt)
