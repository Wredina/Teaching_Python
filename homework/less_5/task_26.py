# Напишите программу, которая на вход принимает
# два числа A и B, и возводит число А в целую степень B с
# помощью рекурсии.
# A = 3
# B = 5 -> 243 (3⁵)
# A = 2
# B = 3 -> 8

from random import randint


def exp(num_A, num_B):
    if num_B == 0 or num_A == 1:
        return 1
    else:
        return num_A * exp(num_A, num_B - 1)


a = 2
b = 0
print(a, b)
print(exp(a, b))
