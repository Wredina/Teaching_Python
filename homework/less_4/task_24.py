# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai
# ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки
# 4 -> 1 2 3 4
# 9

from random import randint

size = randint(6, 10)
bushes = [randint(1, 10) for _ in range(size)]
print(bushes)

max_blueberries = bushes[-1] + bushes[-2] + bushes[0]
sum_tree_bushes = max_blueberries

for i in range(size - 1):
    sum_tree_bushes = bushes[i] + bushes[i-1] + bushes[i+1]
    if sum_tree_bushes > max_blueberries:
        max_blueberries = sum_tree_bushes
print(max_blueberries)

# var_n = int(input("Введите число кустов: "))
# list_berry = []
# for i in range(var_n):
#     list_berry.append(randint(5, 20))
# print(list_berry)
# sum_berry = [list_berry[i] + list_berry[i+1] + list_berry[i+2]
#              for i in range(-2, len(list_berry) - 2)]
# print(sum_berry)
# max_berry = max(sum_berry)
# print(f"Наибольшее число:", max_berry)
