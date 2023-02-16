'''
Напишите функцию, которая принимает одно число и
проверяет, является ли оно простым
Напоминание: Простое число - это число, которое
имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes 
'''
def simple_number (a):
    for f in range(2,a):
        print(f"{f = }")
        if a%f==0:
            print(f)
            return False
    return True
print(simple_number(int(input("Ввидите число которое будем проверять"))))