# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров?
# При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.
# Input:
# n = 700
# m = 750
# Output:
# 2

n = int(input("введите сколько киллометров проезжает машина в день: "))
s = int(input("введите сколько киллометров машина должна проехать: "))
day = (s + (n - 1))//n
print(f"{day} - столько дней будет ехать машина")