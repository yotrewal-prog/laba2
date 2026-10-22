"""mathtool.py — точка входа приложения mathtool.

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
from cli import build_parser


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


def get_coefficients(args):
    """Получает коэффициенты уравнения из параметров или с клавиатуры.

    Возвращает словарь вида {"A": значение, "B": значение, "C": значение}.
    """
    coefficients = {"A": args.a, "B": args.b, "C": args.c}
    if all(value is None for value in coefficients.values()):
        # Ни одного параметра: значения запрашиваются с клавиатуры
        return read_coefficients_from_keyboard()
    if any(value is None for value in coefficients.values()):
        # Задана только часть коэффициентов: это неверный набор данных
        raise ValueError("укажите все три коэффициента либо ни одного")
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
    # 1. Разбор параметров командной строки
    parser = build_parser()
    args = parser.parse_args(sys.argv[1:])

    # Команда не указана — вывод справки
    if args.command is None:
        parser.print_help()
        sys.exit(0)

    if args.command != "solve":
        print_error(f"ОШИБКА: команда \"{args.command}\" ещё не реализована")
        sys.exit(1)

    # 2. Получение исходных данных, проверка данных, вызов расчёта
    try:
        coefficients = get_coefficients(args)
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
