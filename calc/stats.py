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
    """Проверяет последовательность на соответствие ограничениям задачи.

    При нарушении ограничения возбуждает исключение ValueError.
    """
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
    """Сумма чисел последовательности."""
    result = 0.0
    for value in values:
        result += value
    return result


def mean(values):
    """Среднее арифметическое: сумма чисел, делённая на их количество."""
    return total(values) / len(values)


def sum_of_squares(values):
    """Сумма квадратов чисел последовательности."""
    result = 0.0
    for value in values:
        result += value ** 2
    return result


def root_mean_square(values):
    """Среднее квадратическое: корень из среднего квадратов самих чисел."""
    return math.sqrt(sum_of_squares(values) / len(values))


def sum_of_squared_deviations(values):
    """Сумма квадратов отклонений чисел от среднего арифметического."""
    average = mean(values)
    result = 0.0
    for value in values:
        result += (value - average) ** 2
    return result


def variance(values):
    """Дисперсия: сумма квадратов отклонений, делённая на количество чисел."""
    return sum_of_squared_deviations(values) / len(values)


def standard_deviation(values):
    """СКО: корень из дисперсии."""
    return math.sqrt(variance(values))


def sample_standard_deviation(values):
    """Стандартное отклонение: корень из суммы квадратов отклонений,
    делённой на количество чисел минус один. При одном числе не существует."""
    if len(values) < 2:
        return None
    return math.sqrt(sum_of_squared_deviations(values) / (len(values) - 1))


def minimum(values):
    """Наименьшее число последовательности."""
    result = values[0]
    for value in values:
        if value < result:
            result = value
    return result


def maximum(values):
    """Наибольшее число последовательности."""
    result = values[0]
    for value in values:
        if value > result:
            result = value
    return result


def count_positive(values):
    """Количество положительных чисел последовательности."""
    result = 0
    for value in values:
        if value > 0:
            result += 1
    return result


def count_negative(values):
    """Количество отрицательных чисел последовательности."""
    result = 0
    for value in values:
        if value < 0:
            result += 1
    return result


def product(values):
    """Произведение всех чисел последовательности."""
    result = 1.0
    for value in values:
        result *= value
    return result


def max_by_modulus(values):
    """Наибольшее по модулю значение.

    Возвращает само число, а не его модуль; при равных модулях
    выбирается первое встретившееся значение.
    """
    result = values[0]
    for value in values:
        if abs(value) > abs(result):
            result = value
    return result


def min_by_modulus(values):
    """Наименьшее по модулю значение.

    Возвращает само число, а не его модуль; при равных модулях
    выбирается первое встретившееся значение.
    """
    result = values[0]
    for value in values:
        if abs(value) < abs(result):
            result = value
    return result


def total_of_negatives(values):
    """Сумма отрицательных чисел последовательности."""
    result = 0.0
    for value in values:
        if value < 0:
            result += value
    return result


def are_integers(values):
    """Проверяет, что все числа последовательности целые.

    Значение 2.0 целым считается: целое ли оно по величине, а не по типу.
    """
    for value in values:
        if not value.is_integer():
            return False
    return True


def count_even_positive(values):
    """Количество чётных положительных чисел.

    На вещественных данных показатель не существует и возвращает None.
    """
    if not are_integers(values):
        return None
    result = 0
    for value in values:
        if value > 0 and int(value) % 2 == 0:
            result += 1
    return result


def total_divisible_by_three(values):
    """Сумма чисел, делящихся на 3.

    На вещественных данных показатель не существует и возвращает None.
    """
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
