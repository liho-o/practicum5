"""
Волшебница сказочного королевства практически совсем
не улыбается. За каждый из трёх дней, количество
её подданных, кто видел её улыбку - не велико .
Программа получает количество подданных,
которые видели  улыбку волшебницы за каждый из трех дней.
Определите сколько раз это количество повторялось.
"""

smile_list = []

for _ in range(3):
    count_smile_viewers = int(input('Kоличество подданных\n'))
    smile_list.append(count_smile_viewers)


v1 = smile_list.count(smile_list[0])
v2 = smile_list.count(smile_list[1])
v3 = smile_list.count(smile_list[2])

print(max(v1, v2, v3))
