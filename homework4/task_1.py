"""
Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
Затем пользователь вводит сами элементы множеств.
"""
from random import randint
n = int(input("Введите количество чисел"))
m = int(input("Введите количество чисел"))
list_n = [randint(0,100) for i in range(n)]
list_m = [randint(0,100) for i in range(m)]
print(list_m,list_n)# можно как-то сделать так чтобы оставить эту запись в одну строчку , 
#но чтоб вывело list_m и list_n с новых строк, а не в одну?
list_n = set(list_n)#как я понял приведение к типу сет автоматически упорядочивает по возрастанию элементы?
list_m = set(list_m)
# print(list_m)
# print(list_n)
set_n_m = list_n.difference(list_m)
print(set_n_m)