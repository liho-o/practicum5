"""
Напишите программу, которая употребляет слово "попугай" в
правильном склонении для заданного числительного.
Введенное число является натуральным числом не превышающим
100. Строки, списки не использовать.
"""

parot_num = int(input("Введите количество попугаев\n"))

last_num = parot_num % 10

match last_num:
    case 1:
        print(f'{parot_num} попугай')
    case 2 | 3 | 4:
        print(f'{parot_num} попугая')
    case 5 | 6 | 7 | 8 | 9 | 10:
        print(f'{parot_num} попугаев')