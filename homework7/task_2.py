"""
Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве 
аргумента функцию, вычисляющую элемент по номеру строки и столбца.
Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у 
операции умножения.

Пример:

Ввод:
print_operation_table(lambda x, y: x * y)


Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""


def print_operation_table(operration, colomns:int , rows:int):
    table = [[operration(i,j) for i in range(1,colomns+1)] for j in range(1,rows+1)]
    # for i in range(1,colomns+1):
    #     table_str = []
    #     for j in range (1,rows+1):
    #         table_str.append()
    #     table.append(table_str)
    for x in table:
        print("".join (f'{n:3}' for n in x))


print_operation_table(lambda x,y: x*y , 1,8)























# def operation_table( rows:int ,columns:int):
#     table=[]
#     for i in range(1,rows+1):
#         table1=[]
#         for j in range(1,columns+1):
#             table1.append((lambda x,y: x*y) (i,j))
#         table.append(table1)
#     return table
# for i in operation_table(6,6):
#     print("".join(f'{n:3}'for n in i))




# def print_operation_table(operation, rows=6, columns=6):
#     table = []
#     for i in range(1, rows + 1):
#         table1 = []
#         for j in range(1, columns + 1):
#             table1.append(operation(i, j))
#         table.append(table1)
#     for i in table:
#         print("".join(f'{n:12}'for n in i))

# print(print_operation_table(lambda x, y: x**y))