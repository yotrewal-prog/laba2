"""calc.integration — численное интегрирование методом левых прямоугольников.

Каждая подынтегральная функция оформлена отдельной функцией. Вместе с
функцией хранится допустимый для команды промежуток пределов интегрирования:
это ограничение задания, выбранное внутри области определения функции.
"""

import math


MAX_STEPS = 100000
DIGITS = 4


def f_ratio(x):
    """F(x) = x / (x + 1)."""
    return x / (x + 1)


def f_root(x):
    """F(x) = sqrt(x^2 + 1)."""
    return math.sqrt(x * x + 1)


def f_exp(x):
    """F(x) = e^(2x - 1)."""
    return math.exp(2 * x - 1)


def f_logsq(x):
    """F(x) = ln(x^2 + 1)."""
    return math.log(x * x + 1)


def f_invroot(x):
    """F(x) = 1 / sqrt(3x + 2)."""
    return 1 / math.sqrt(3 * x + 2)


def f_logcube(x):
    """F(x) = ln(x^3 - 2)."""
    return math.log(x ** 3 - 2)


# Таблица функций: имя из командной строки — кортеж
# (функция, запись формулы, нижняя граница, верхняя граница, строгость границ).
# Признак строгости True означает открытый промежуток, в который границы
# не входят (сравнение строгое); False — замкнутый промежуток.
FUNCTIONS = {
    "ratio": (f_ratio, "F(x) = x / (x + 1)", 0.0, 20.0, False),
    "root": (f_root, "F(x) = sqrt(x^2 + 1)", -5.0, 5.0, True),
    "exp": (f_exp, "F(x) = e^(2x - 1)", 0.0, 3.0, False),
    "logsq": (f_logsq, "F(x) = ln(x^2 + 1)", 1.0, 6.0, False),
    "invroot": (f_invroot, "F(x) = 1 / sqrt(3x + 2)", 0.0, 10.0, False),
    "logcube": (f_logcube, "F(x) = ln(x^3 - 2)", 3.0, 12.0, False),
}


def validate_limits(start, stop, low, high, strict):

    if not math.isfinite(start) or not math.isfinite(stop):
        raise ValueError("предел не является конечным числом")
    if start >= stop:
        raise ValueError("начальный предел не меньше конечного")
    if strict:
        inside = low < start < high and low < stop < high
    else:
        inside = low <= start <= high and low <= stop <= high
    if not inside:
        raise ValueError("предел вне промежутка")


def validate_steps(steps):
    if not 1 <= steps <= MAX_STEPS:
        raise ValueError("количество шагов вне диапазона")


def left_rectangles(function, start, stop, steps):

    dx = (stop - start) / steps
    result = 0.0
    for i in range(steps):
        # Координата вычисляется на каждом шаге заново: накопление
        # x = x + dx даёт погрешность и лишний шаг цикла
        x = start + i * dx
        result += function(x) * dx
    return result
