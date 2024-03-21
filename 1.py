"""
Сказочной фее для приготовления зелья требуется знать
сколько дней в году. Напишите программу, которая
позволит ей осуществить планы по заготовке зелья
на весь год.
"""


def year_check(year):
    if year > 2020:
        i = 4

        while year > 2020:
            year -= i
            print(year)
            if year == 2020:
                return 366

        return 365

    elif year < 2020:
        i = -4

        while year < 2020:
            year -= i
            print(year)
            if year == 2020:
                return 366

        return 365
    else:
        return 366


year = int(input('Введите год\n'))

print(year_check(year))
