"""
Известны высоты трёх башен волшебного города. Значение этих высот вводятся
в одной строке через пробел. Напишите программу, которая упорядочит эти высоты
от наибольшей к наименьшей. Функцию sorted() и метод sort() не использовать.
"""

n, k, m = input('Введите высоты трёх башен\n').split(' ')
n, k, m = int(n), int(k), int(m)

tower_list = [n, k, m]

first = max(tower_list[0], tower_list[1], tower_list[2])
tower_list.remove(first)

second = max(tower_list[0], tower_list[1])
tower_list.remove(second)

print(first, second, tower_list[0])
