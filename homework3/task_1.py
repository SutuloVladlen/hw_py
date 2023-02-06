"""
Требуется вычислить, сколько раз встречается некоторое число X в массиве 
A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
Пример:
5
1 2 3 4 5
3 -> 1
"""
from random import randint
leng = int (input("Введите длинну списка"))
desird_number =  int (input("Введите число количество которого мы ищем"))
listt = [] #можно создать список заданного размера
caunt = 0
for i in range(leng):
    listt.append(randint(0,10))
print(listt)
for i in listt:
    if i == desird_number:
        caunt += 1
print(f"число {desird_number} всречается {caunt} раз")

count = listt.count(desird_number)
print(f"число {desird_number} всречается {caunt} раз")



