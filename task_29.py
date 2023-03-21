"""Ваня и Петя поспорили, кто быстрее решит
следующую задачу: “Задана последовательность
неотрицательных целых чисел. Требуется определить
значение наибольшего элемента
последовательности, которая завершается первым
встретившимся нулем(число 0 не входит в
последовательность)”. Однако 2 друга оказались не
такими смышлеными. Никто из ребят не смог до
конца сделать это задание. Они решили так: у кого
будет меньше ошибок в коде, тот и выиграл спор. За
помощью товарищи обратились к Вам, студентам.
Примечание: Программные коды на следующих
слайдах
Задача – «На вход программе подаются цифры, как только пользователь введёт 0 ввод прекращается. Вывести наибольший элемент получившейся последовательности».
Есть два кода с ошибками, нужно определить  где ошибок меньш
Ваня:
n = int(input())
max_number = 1000
while n != 0:
 n = int(input())
 if max_number > n:
 max_number = n
print(max_number)

Петя
n = int(input())
max_number = -1
while n < 0:
 n = int(input())
 if max_number < n:
 n = max_number
print(n)
"""
# Ваня:
n = int(input())
max_number = 1000  # max_number = n
while n != 0:
    n = int(input())
    if max_number > n:  # max_number < n:
        max_number = n
print(max_number)

# Петя

n = int(input())
max_number = -1
while n < 0:  # n > 0
    n = int(input())  # переместить на 51-ю строчку
    if max_number < n:
        n = max_number  # max_number = n
print(n)  # print(max_number)