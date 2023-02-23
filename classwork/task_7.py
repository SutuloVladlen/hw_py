"""Два различных натуральных числа n и m называются
дружественными, если сумма делителей числа n
(включая 1, но исключая само n) равна числу m и
наоборот. Например, 220 и 284 – дружественные числа.
По данному числу k выведите все пары дружественных
чисел, каждое из которых не превосходит k. Программа
получает на вход одно натуральное число k, не
превосходящее 105
. Программа должна вывести все
пары дружественных чисел, каждое из которых не
превосходит k. Пары необходимо выводить по одной в
строке, разделяя пробелами. Каждая пара должна быть
выведена только один раз (перестановка чисел новую
пару не дает).
Ввод: Вывод:
300 220 284
"""
a = 100000
for i in range(1,a):
    sum1=0
    number2=0
    for j in range(1,i//2+1):
        if i%j==0:
            sum1 +=j
    for x in range (1,sum1//2+1):
        if sum1%x==0:
            number2+=x
            if number2==i:
                    print(i,number2, sum1)


# def sum_divisors(num):
#     summ = 0
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             # print(f'{i = }')
#             summ += i
#     return summ

# # print(sum_divisors(220),sum_divisors(284))

# def friends_num(number):
#     for i in range(1, number):
#         j = sum_divisors(i) 
#         if i < j <= number and i == sum_divisors(j):
#             print(i, j, sum_divisors(i),sum_divisors(j))


# friends_num(int(input('Введите число К: ')))
# number= 10000
# for i in range(1, number):
#     summ=0
#     sum=0
#     for j in range(1, i // 2 + 1):
#         if i % j == 0:
#             summ += j 
            
#             for x in range(1, summ // 2 + 1):
#                 if summ % x == 0:
#                     sum += j 
#                     if i==sum and i<summ:
#                         print(i,summ)