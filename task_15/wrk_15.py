# Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!

# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

from random import randint

n = int(input("введите число арбузов: "))
minNum = 10
maxNum = 1
for i in range(n):
    watermelon = randint(1, 10)
    print(watermelon)
    if watermelon > maxNum:
        maxNum = watermelon
    if watermelon < minNum:
        minNum = watermelon
print(f"max kg {maxNum}")
print(f"min kg {minNum}")
