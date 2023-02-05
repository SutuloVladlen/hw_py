'''На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы 
все монетки были повернуты вверх одной и той же стороной.
Выведите минимальное количество монет, которые нужно перевернуть.
Пример:
5 -> 1 0 1 1 0
2
'''
from random import randint
quantity_coins = int (input('Введите количество монет'))
coins = list(range(quantity_coins))
haeds = 0
teil = 0
for i in range (quantity_coins):
    haeds_or_teil = randint(0,1)
    coins [i] = haeds_or_teil
    if coins [i] == 1:
        haeds +=1
    else:
        teil += 1
print(coins)
if haeds == teil:
    print(f'Нужно перевернуть {haeds} монет ')
elif haeds > teil:
    print(f'Нужно перевернуть {teil} монет')
else:
    print(f'Нужно перевернуть {haeds} монет')
