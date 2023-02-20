"""
Хакер Василий получил доступ к классному журналу и
хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая
заменяет оценки Василия, но наоборот: все 
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
"""
from random import randint
def replacement (a):
    class_list = list (randint(1,5)for i in range(a))
    print (class_list)
    for i in range (len(class_list)):
        if class_list[i]==4 or class_list[i]==5:
            print(i)
            class_list[i]=1
    return class_list
print (replacement (int(input('Введите количество оценок в журнале'))))


def replacement1 (a):
    max_mark = max(a)
    min_mark = min(a)
    for i in range(len(a)):
        if a[i]==max_mark:
            a[i]=min_mark
    return a
# a = list(randint(1,5) for _ in range(int(input("введите количество оценок"))))
# print(a)
print(*replacement1(list(randint(1,5) for _ in range(int(input("введите количество оценок"))))))