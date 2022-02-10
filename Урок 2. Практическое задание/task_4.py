"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. Решение через цикл не принимается.
Нужно обойтисть без создания массива!
"""


def summary(cnt, _sum=0, num=1.0):
    if cnt == 1:
        _sum += num
        return f'сумма - {_sum}'
    else:
        _sum += num
        num = -num / 2
        cnt -= 1
        return summary(cnt, _sum, num)


print(summary(int(input('Введите количество элементов: '))))
