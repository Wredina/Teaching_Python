# создание калькулятора

# nums = [int(i) for i in input("введите числа через пробел").split()]
# print(nums)

# nums_2 = list(map(int, input('введите числа через пробел').split()))
# print(nums_2)

# a,b,x = list(map(int, input('введите числа через пробел '). split()))
# print(a,b,x)

# a,*b, x = (12,23,34,45,56,67)
# print(a)
# print(b)
# print(x)

# for a,*b,x in [(1,2,3, 4, 45), (11,22,33), (111,222,333)]:
# print(a,b,x)

from function_operation import *
from conv_calc import kalk


def main():
    my_primer = input('введите выражение: ').split()
    print(my_primer)

    # print(kalk(my_primer[0], my_primer[2], my_primer[1]))
    while "*" in my_primer or '/' in my_primer:
        for i in range(1, len(my_primer), 2):
            if my_primer[i] in ("*", "/"):
                my_primer[i - 1] = kalk(my_primer[i-1],
                                        my_primer.pop(i + 1), my_primer.pop(i))
                break
    while "+" in my_primer or '-' in my_primer:
        for i in range(1, len(my_primer), 2):
            if my_primer[i] in ("-", "+"):
                my_primer[i - 1] = kalk(my_primer[i-1],
                                        my_primer.pop(i + 1), my_primer.pop(i))
                break
    print(my_primer)


if __name__ == "__main__":
    main()
