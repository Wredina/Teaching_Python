# Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел. Из
# всех арифметических операций допускаются только + 1 и - 1.
# Также нельзя использовать циклы.
# 2 2
# 4

from random import randint


def num_sum(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    return num_sum(a - 1, b+1)


num_A, num_B = randint(1, 9), randint(1, 9)
print(num_A, num_B)
print(num_sum(num_A, num_B))
