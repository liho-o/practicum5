"""
Доработайте решение к заданию об индексе массы тела (ИМТ).
Допишите программу так, чтобы она интерпретировала
результат в соответствии с рекомендациями Всемирной
организации здравоохранения (ВОЗ)
"""

mass = float(input('Bес (в фунтах)\n')) / 2.205
height = float(input('Рост (в дюймах)\n')) / 39.37

imt = mass / height ** 2

if imt < 16:
    print('выраженный дефицит массы тела')
elif 16 <= imt <= 18.49:
    print('недостаточная масса тела')
elif 18.5 <= imt <= 24.99:
    print('норма')
elif 25 <= imt <= 29.99:
    print('избыточная масса тела')
elif 30 <= imt <= 34.99:
    print('ожирение первой степени')
elif 35 <= imt <= 39.99:
    print('ожирение второй степени')
elif imt < 40:
    print('ожирение третьей степени')