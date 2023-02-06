"""
Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
Пример:
5
1 2 3 4 5
6 -> 5
"""
from random import randint
leng = int (input("Введите длинну списка"))
number1 =  int (input("Введите число которое мы будем искать"))
number2 = number1
listt = []
sett = set()
caunt = 0
for i in range(leng):
    listt.append(randint(0,100))
print(listt)# можно как-то не циклом, а какойто встроенной командой заполнить список рандомными числами
for i in listt:
    sett.add(i)
print(sett)
flag = True
while flag:
    if number1 in sett:
        print(f"Искомое ближайшее число{number1}")
        flag = False
    if number2 in sett:
        print(f"Искомое ближайшее число{number2}")
        flag = False
    number1 += 1
    number2 -= 1