# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

from random import randint
size = randint(6, 15)
list_1 = [randint(0, 5) for i in range(size)]
print(list_1)
set_1 = set(list_1)
print(set_1)
print(len(set_1))
