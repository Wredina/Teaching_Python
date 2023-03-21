# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально

from random import randint
n = randint(5, 10)
print(n)
k = randint(1, 3)
print(k)
list_1 = [randint(0, 10) for i in range(n)]
print(list_1)
for i in range(k):
    a = list_1.pop()
    list_1.insert(i, a)
print(list_1)
