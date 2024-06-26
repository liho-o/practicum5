"""
В королевстве кривых зеркал все наоборот: жабу зовут Абаж,
страной правит король Йагупоп (попугай), живет там и
красавица Анидаг. Однако, такие слова как шалаш,
казак - являются настоящими. То же самое происходит и с числами.
Напишите программу, которая определяет является
ли четырехзначное число "кривым" или "настоящим".
Строки не использовать.
"""


def main_check(num):
    first_n = num // 1000
    second_n = (num // 100) % (first_n * 10)
    third_n = (num - ((first_n * 1000) + (second_n * 100))) // 10
    fourth_n = (num - ((first_n * 1000) + (second_n * 100))) % 10

    if (first_n == fourth_n) and (second_n == third_n):
        print('настоящее')
    else:
        print('кривое')


num_to_check = int(input('Введите число для проверки\n'))

if num_to_check <= 999:
    print('Число не 4-х значное')
elif num_to_check >= 10000:
    print('Число не 4-х значное')
else:
    main_check(num_to_check)
