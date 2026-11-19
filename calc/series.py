"""calc.series — суммы числовых рядов.

Слагаемое каждого ряда оформлено отдельной функцией: она получает номер
слагаемого и возвращает его значение со знаком. Цикл суммирования один
и общий для всех рядов — формула передаётся ему параметром.
"""

import math

# Наибольшее значение параметра --terms
MAX_TERMS = 10000
# Наибольшее значение параметра --eps: самая грубая допустимая точность
MAX_EPS = 0.0001
# Число повторений цикла суммирования по точности
MAX_ITERATIONS = 100000
# Число знаков после запятой в выводе суммы ряда
DIGITS = math.ceil(-math.log10(MAX_EPS))


def sign(n):

    return -1 if n % 2 == 0 else 1


def term_sqplus(n):
    return sign(n) / (n * n + 1)


def term_third(n):
    return sign(n) / (3 * n)


def term_triplus(n):
    return sign(n) / (3 * n + 1)


def term_halfsq(n):
    return sign(n) / (2 * n * n)


def term_nsqplus(n):
    return sign(n) * n / (n * n + 1)


def term_nnext(n):
    return sign(n) * n / ((n + 1) ** 2)


def term_ncube(n):
    return sign(n) * n / (n ** 3 + n - 1)


# Таблица рядов: имя из командной строки — пара «функция слагаемого, запись формулы».
# Добавление ряда — новая функция и строка таблицы.
FORMULAS = {
    "sqplus": (term_sqplus, "S = 1/(1^2+1) - 1/(2^2+1) + 1/(3^2+1) - ..."),
    "third": (term_third, "S = 1/3 - 1/6 + 1/9 - ..."),
    "triplus": (term_triplus, "S = 1/(3*1+1) - 1/(3*2+1) + 1/(3*3+1) - ..."),
    "halfsq": (term_halfsq, "S = 1/(2*1^2) - 1/(2*2^2) + 1/(2*3^2) - ..."),
    "nsqplus": (term_nsqplus, "S = 1/(1^2+1) - 2/(2^2+1) + 3/(3^2+1) - ..."),
    "nnext": (term_nnext, "S = 1/2^2 - 2/3^2 + 3/4^2 - ..."),
    "ncube": (term_ncube, "S = 1/(1^3+0) - 2/(2^3+1) + 3/(3^3+2) - ..."),
}


def validate_terms(terms):
    if not 1 <= terms <= MAX_TERMS:
        raise ValueError("количество слагаемых вне диапазона")


def validate_eps(eps):
    if not math.isfinite(eps) or not 0 < eps <= MAX_EPS:
        raise ValueError("точность вне диапазона")


def sum_by_terms(term, count):

    result = 0.0
    for n in range(1, count + 1):
        result += term(n)
    return result, count


def sum_by_eps(term, eps):

    result = 0.0
    n = 0
    while True:
        n += 1
        value = term(n)
        result += value
        if abs(value) < eps:
            return result, n
        if n >= MAX_ITERATIONS:
            raise ValueError("точность не достигнута")
