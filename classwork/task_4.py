from random import randint
# a = list(randint(0,20)for i in range(int (input("длинна 1 списка"))))
# b = list(randint(0,20)for i in range(int (input("длинна 2 списка"))))
# print(a)
# print(b)


def namber_list(x):
    list_1 = []
    for _ in range (x):
        list_1.append(int(input("Введите число")))
    return list_1


def diff_list (a,b):
    c = list()
    for i in a:
        if i not in b:
            c.append(i)
    return c

            
a = int(input("Введите количество чисел в списке1"))
b = int(input("Введите количество чисел в списке2"))
lst_1 = (namber_list(a))
lst_2 = (namber_list(b))
lst_3 = (diff_list(lst_1,lst_2))
print(lst_1,lst_2,lst_3)

 

def lst_diff2(list_1: list, list_2: list):
     return [i for i in list_1 if i not in list_2]


