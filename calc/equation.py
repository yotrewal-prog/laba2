"""calc.equation — решение уравнения A*x^2 + B*x + C = 0.

Расчётная часть приложения: функции ничего не печатают и не запрашивают
ввод, исходные данные получают параметрами, результат возвращают значением.
"""

import math

MAX_VALUE = 10000


def validate_coefficients(coefficients):

    for name, value in coefficients.items():
        if abs(value) > MAX_VALUE:
            raise ValueError(f"коэффициент {name} вне допустимого диапазона")


def solve(a, b, c):

    if a == 0:
        if b == 0:
            raise ValueError("это не уравнение, неизвестное отсутствует")
        return "линейное", None, [-c / b]

    d = b * b - 4 * a * c
    if d > 0:
        roots = [(-b + math.sqrt(d)) / (2 * a), (-b - math.sqrt(d)) / (2 * a)]
    elif d == 0:
        roots = [-b / (2 * a)]
    else:
        roots = []
    return "квадратное", d, roots
