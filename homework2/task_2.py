'''Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
Помогите Кате отгадать задуманные Петей числа.
Пример:
4 4 -> 2 2
5 6 -> 2 3
'''
sum_of_numbers = int (input('Введите сумму чисел')) 
produkt_of_numbers = int (input('Введите произведение чисел'))
number1 = 1
number2 = sum_of_numbers - 1
while number1 <= number2 or number1 == number2 + 1:
    print(number1 , number2)
    if number1 * number2 == produkt_of_numbers:
        print(f"искомые числа {number2}, {number1} ")
        break
    else:
        
        number1 += 1
        number2 -= 1
        
if number1 * number2 != produkt_of_numbers:
    print('Петя ошибся с числами') 