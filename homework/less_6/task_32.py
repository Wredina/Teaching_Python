# Определить индексы элементов массива(списка),
# значения которых принадлежат заданному диапазону(т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# Вывод: [1, 9, 13, 14, 19]

from random import randint

size_arr, ran_arr_min, ran_arr_max = randint(9, 15), randint(
    1, 8), randint(8, 16)  # задаём длину массива и диапазон (cgtwb)
# выводим всё, что занесли в переменные
print(size_arr, ran_arr_min, ran_arr_max)

arr = [randint(1, 16) for _ in range(size_arr)]  # создаём массив
print(arr)

indx_list = []
for i in range(size_arr):
    if ran_arr_min - 1 <= arr[i] <= ran_arr_max:
        indx_list.append(i)
print(indx_list)
