# Даны два неупорядоченных набора целых чисел(может быть, с
# повторениями). Выдать без повторенийвсе те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

from random import randint

# user_size_set_1 = int(input("введите размер множества 1 : "))
# user_size_set_2 = int(input("введите размер множества 2 : "))
user_size_set_2 = randint(5, 10)
user_size_set_1 = randint(5, 10)

# пользовательский ввод:
# user_set_1 = set()
# user_set_2 = set()

# for _ in range(user_size_set_1):
#     user_set_1.add(input('введите число в множество 1: '))
# print()
# for _ in range(user_size_set_2):
#     user_set_2.add(input('введите число в множество 2: '))

# print(user_set_1)
# print(user_set_2)

# автоматизация рандомной генерации значений в множестве
user_set_1 = set(randint(1, 10) for num_1 in range(user_size_set_1))
print(*user_set_1)
user_set_2 = set(randint(1, 10) for num_2 in range(user_size_set_2))
print(*user_set_2)

print(*user_set_1.intersection(user_set_2))
