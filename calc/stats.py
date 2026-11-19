"""calc.stats — показатели числовой последовательности.

Каждый показатель оформлен отдельной функцией: она получает список чисел
и возвращает значение. Показатель, которого не существует, обозначается
значением None — это не ошибка.
"""

import math

# Предельное количество чисел в последовательности
MAX_COUNT = 20
# Предельное по модулю значение числа последовательности
MAX_ABS = 10000


def validate_values(values):

    if not values:
        raise ValueError("последовательность пуста")
    if len(values) > MAX_COUNT:
        raise ValueError("количество чисел вне диапазона")
    for value in values:
        if not math.isfinite(value):
            raise ValueError("значение не является конечным")
        if abs(value) > MAX_ABS:
            raise ValueError("значение вне допустимого диапазона")


def total(values):
    result = 0.0
    for value in values:
        result += value
    return result


def mean(values):
    return total(values) / len(values)


def sum_of_squares(values):
    result = 0.0
    for value in values:
        result += value ** 2
    return result


def root_mean_square(values):
    return math.sqrt(sum_of_squares(values) / len(values))


def sum_of_squared_deviations(values):
    average = mean(values)
    result = 0.0
    for value in values:
        result += (value - average) ** 2
    return result


def variance(values):
    return sum_of_squared_deviations(values) / len(values)


def standard_deviation(values):
    return math.sqrt(variance(values))


def sample_standard_deviation(values):
    if len(values) < 2:
        return None
    return math.sqrt(sum_of_squared_deviations(values) / (len(values) - 1))


def minimum(values):
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def count_positive(values):
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result


def count_negative(values):
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result


def product(values):
    result = 1.0
    for value in values:
        result *= value
    return result


def max_by_modulus(values):

    result = values[0]
    for value in values:
        if abs(value) > abs(result):
            result = value
    return result


def min_by_modulus(values):

    result = values[0]
    for value in values:
        if abs(value) < abs(result):
            result = value
    return result


def total_of_negatives(values):
    result = 0.0
    for value in values:
        if value < 0:
            result += value
    return result


def are_integers(values):

    for value in values:
        if not value.is_integer():
            return False
    return True


def count_even_positive(values):

    if not are_integers(values):
        return None
    result = 0
    for value in values:
        if value > 0 and int(value) % 2 == 0:
            result += 1
    return result


def total_divisible_by_three(values):

    if not are_integers(values):
        return None
    result = 0.0
    for value in values:
        if int(value) % 3 == 0:
            result += value
    return result


# Таблица показателей: подпись, функция, формат вывода.
# Добавление показателя — это новая функция и одна строка таблицы;
# порядок строк задаёт порядок вывода.
REPORT = [
    ("Количество", len, "d"),
    ("Сумма", total, ".3f"),
    ("Ср. арифм.", mean, ".3f"),
    ("Сумма кв.", sum_of_squares, ".3f"),
    ("Ср. кв.", root_mean_square, ".3f"),
    ("Дисперсия", variance, ".3f"),
    ("СКО", standard_deviation, ".3f"),
    ("Станд. откл.", sample_standard_deviation, ".3f"),
    ("Наименьшее", minimum, ".3f"),
    ("Наибольшее", maximum, ".3f"),
    ("Положительных", count_positive, "d"),
    ("Отрицательных", count_negative, "d"),
    # Показатели дополнительных заданий
    ("Произведение", product, ".3f"),
    ("Наиб. по модулю", max_by_modulus, ".3f"),
    ("Наим. по модулю", min_by_modulus, ".3f"),
    ("Сумма отриц.", total_of_negatives, ".3f"),
    ("Чётных полож.", count_even_positive, "d"),
    ("Сумма кратных 3", total_divisible_by_three, ".3f"),
]
