"""mathtool.py — решение уравнений вида A*x^2 + B*x + C = 0.

Использование:
    python mathtool.py                          вывод справки
    python mathtool.py --help                   вывод справки
    python mathtool.py solve                    ввод коэффициентов с клавиатуры
    python mathtool.py solve -a 1 -b -3 -c 2     решение с заданными коэффициентами

Расчётная часть вынесена в модуль calc.equation: она ничего не печатает
и возвращает результат значением.
"""

import sys

from calc import equation

HELP_TEXT = (
    "mathtool — решение уравнений вида A*x^2 + B*x + C = 0\n"
    "\n"
    "Использование:\n"
    "    python mathtool.py                          вывод справки\n"
    "    python mathtool.py --help                    вывод справки\n"
    "    python mathtool.py solve                     ввод коэффициентов с клавиатуры\n"
    "    python mathtool.py solve -a 1 -b -3 -c 2      решение с заданными коэффициентами\n"
    "\n"
    "Коэффициенты A, B, C — целые числа, по модулю не превышающие 10000."
)


def print_error(message):
    """Вывод сообщения об ошибке в поток ошибок."""
    print(message, file=sys.stderr)


def read_coefficients_from_keyboard():
    """Запрашивает коэффициенты A, B, C у пользователя с клавиатуры.
    Возвращает словарь вида {"A": значение, "B": значение, "C": значение}."""
    coefficients = {}
    for name in ("A", "B", "C"):
        text = input(f"Введите {name}: ")
        try:
            coefficients[name] = int(text)
        except ValueError:
            raise ValueError("коэффициент не является целым числом") from None
    return coefficients


def parse_arguments(argv):
    """Разбор параметров командной строки.
    Возвращает словарь коэффициентов уравнения."""
    # Параметров нет или запрошена справка
    if len(argv) == 0 or argv[0] == "--help":
        print(HELP_TEXT)
        sys.exit(0)

    # Первая команда должна быть "solve"
    if argv[0] != "solve":
        raise ValueError(f"неизвестная команда \"{argv[0]}\"")

    # Только "solve" — коэффициенты вводятся с клавиатуры
    if len(argv) == 1:
        return read_coefficients_from_keyboard()

    # "solve -a .. -b .. -c .." — коэффициенты заданы параметрами
    if len(argv) == 7:
        if argv[1] != "-a" or argv[3] != "-b" or argv[5] != "-c":
            raise ValueError("неизвестный параметр")
        coefficients = {"A": argv[2], "B": argv[4], "C": argv[6]}
    else:
        # Любой другой набор параметров считается неверным
        raise ValueError("неверный набор параметров")

    for name, text in coefficients.items():
        try:
            coefficients[name] = int(text)
        except ValueError:
            raise ValueError("коэффициент не является целым числом") from None
    return coefficients


def print_solution(kind, discriminant, roots):
    """Выводит вид уравнения, дискриминант и найденные корни."""
    print(f"Уравнение {kind}")
    if discriminant is not None:
        print(f"Дискриминант: {discriminant}")
    if not roots:
        print("Действительных корней нет")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")


def main():
    # 1. Разбор параметров командной строки, получение исходных данных
    # 2. Решение уравнения в модуле calc
    try:
        coefficients = parse_arguments(sys.argv[1:])
        equation.validate_coefficients(coefficients)
        kind, discriminant, roots = equation.solve(
            coefficients["A"], coefficients["B"], coefficients["C"]
        )
    except ValueError as error:
        print_error(f"ОШИБКА: {error}")
        sys.exit(1)

    # 3. Вывод результата
    print_solution(kind, discriminant, roots)

    sys.exit(0)


if __name__ == "__main__":
    main()
