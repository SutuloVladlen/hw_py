"""
Напишите программу, которая на вход принимает два числа A и B, и 
возводит число А в целую степень B с помощью рекурсии.
Пример:
A = 3; B = 5 -> 243 (3**5)
A = 2; B = 3 -> 8
"""

def exponentiate (a,b, resalt = 1):
    
    if b !=0:
        resalt = resalt * a
        b-=1
        return exponentiate (a, b, resalt)
    else:
        return resalt
print(exponentiate(int (input("Введите число возводимое в степень")),int (input("Введите степень в которую возводим"))))


