# Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: a**n = a1 + (n-1) * d.
# Каждое число вводится с новой строки.
# Ввод: 7 2 5
# Вывод: 7 9 11 13 15
from random import randint

num_1, step, size_arr = randint(1, 9), randint(2, 5), randint(5, 9)
print(num_1, step, size_arr)

arr = []
for i in range(size_arr):
    arr.append(num_1)
    num_1 += step
print(arr)
