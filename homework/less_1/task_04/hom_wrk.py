# Петя, Катя и Сережа делают из бумаги журавликов. Вместе
# они сделали S журавликов. Сколько журавликов сделал каждый
# ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

burd = int(input("введите общее кол-во журавлей: "))

if burd % 2 != 0:
    print("введено не правильное число")
else:
    burdKate = burd // 3
    resultPS = burdKate // 2
    burdKate += burdKate


print(f"Катя сделала {burdKate} журавлей, Сергей {resultPS} и Петя {resultPS}")
