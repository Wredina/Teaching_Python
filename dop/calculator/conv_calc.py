from function_operation import *


def kalk(a, b, opper):
    if opper == '+':
        result = summa(float(a), float(b))
    elif opper == '-':
        result = minus(float(a), float(b))
    elif opper == '*':
        result = mult(float(a), float(b))
    elif opper == '/':
        result = div(float(a), float(b))
    return result
