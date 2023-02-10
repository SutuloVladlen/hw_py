"""
В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты 
высажены только по окружности. Таким образом,
у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное 
число ягод – на i-ом кусте выросло ai ягод.
В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
собирает ягоды с этого куста и с двух соседних с ним.
Напишите программу для нахождения максимального числа ягод, которое может собрать за один 
заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
"""
from random import randint
number_bushes = int(input("Введите количество кустов"))
namber_of_processed_bushes = int(input("Введите количество обрабатываемых кустов за раз"))
number_of_berryes_per_bush_list = list(randint(0,20) for i in range(number_bushes))
print(number_of_berryes_per_bush_list)
sum_berryes = 0
if number_bushes <= namber_of_processed_bushes:
    for i in range(len(number_of_berryes_per_bush_list)):
        sum_berryes += number_of_berryes_per_bush_list[i]
    print(f"Машина обрабатывает все кусты сразу и получает {sum_berryes} ягод")
else:
    startig_bush = -namber_of_processed_bushes +1
    max_berry = int (0)
    for i in range(len(number_of_berryes_per_bush_list)):
        caunt = 0
        sum_berryes = 0 
        number_bush = startig_bush
        while caunt != namber_of_processed_bushes:
            sum_berryes = sum_berryes + number_of_berryes_per_bush_list[number_bush]
            number_bush += 1
            caunt += 1
        if max_berry < sum_berryes:
            max_berry = sum_berryes
        startig_bush += 1
    print("Максимольное число ягод при данной сборке равно", max_berry)


# print(number_bushes)
# max_berry = 0
# if number_bushes[0] + number_bushes[1] + number_bushes[-1] < number_bushes[0] + number_bushes[-2] + number_bushes[-1]:
#     max_berry = number_bushes[0] + number_bushes[-2] + number_bushes[-1]
# else:
#     max_berry = number_bushes[0] + number_bushes[1] + number_bushes[-1]
# print("старт", max_berry)
# for i in range(len(number_bushes)-2) :
#     #print(i)
#     if max_berry < number_bushes[i] + number_bushes[i+1] + number_bushes[i+2]:
#         max_berry = number_bushes[i] + number_bushes[i+1] + number_bushes[i+2]
#         #print("в цикле", max_berry)
# print(f"Максимальное число ягод на 3 кустах равно {max_berry}")