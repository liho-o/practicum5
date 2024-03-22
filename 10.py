"""
Владелец банковской карты придумывает четырехзначный PIN-код.
Напишите программу, которая проверяет, правильно ли он придуман.
Банк предъявляет следующие требования к PIN-коду:

4 цифры
нет повторяющихся
не от 1900 до 2050
"""

pin = int(input('Введите пин\n'))


def first_check(pin):
    check = list(str(pin))
    if 4 != len(check):
        print('ERROR')
        return False
    else:
        return True

def second_check(pin):
    l = list(str(pin))
    n1, n2, n3, n4 = l.count(l[0]), l.count(l[1]), l.count(l[2]), l.count(l[3])
    if (n1 + n2 + n3 + n4) != 4:
        print('ERROR')
        return False
    else:
        return True


def third_check(pin):
    if (pin >= 1900) and (pin <= 2050):
        print('ERROR')
        return False
    else:
        return True


if __name__ == '__main__':
    if (first_check(pin)) and (second_check(pin)) and (third_check(pin)):
        print('OK')
