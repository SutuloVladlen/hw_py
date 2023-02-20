"""Дан список чисел. Посчитайте сколько в нем пар
элементов, равных друг другу. Считается, что любые
два элемента, равные друг другу образуют одну пару,
которую необходимо посчитать. Вводится список
чисел. Все числа списка находятся на разных
строках.
Ввод: 
1 2 3 2 3 2
Вывод:
2
"""
# from random import randint
def namber_list(x):
    list_1 = []
    for _ in range(x):
        list_1.append(int(input("Введите число")))
    return list_1

def count_pair(list_1: list):
    sum_count = 0
    for i in set(list_1):
         sum_count += list_1.count(i)//2
    return sum_count
# list_2 = [1, 2, 3, 2, 3, 2]

list_2 = (namber_list(int(input("Введите количество чисел"))))
print(list_2)
print(count_pair(list_2))

# def count_pairs(inp_lst: list):
#     return sum([inp_lst.count(i) // 2 for i in set(inp_lst)])
#     return sum(inp_lst.count(i) // 2 for i in set(inp_lst))





# def number_of_paired_numbers(a):
#     print(a)
#     count = 0
#     for i in range(len(a)):
#         # print(i,len(a))
#         if a[i] in a[i+1:len(a)]:
#             print(a[i],a[i+1:len(a)])
#             count += 1
#     return count
# print(number_of_paired_numbers(list(randint(1,20) for _ in range(int(input("Введите длинну списка"))))))