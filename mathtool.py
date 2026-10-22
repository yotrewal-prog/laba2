"""mathtool.py — точка входа приложения mathtool.

Команды:
    python mathtool.py solve -a 1 -b -3 -c 2      решение уравнения
    python mathtool.py stats --input numbers.txt  показатели последовательности
    python mathtool.py series --func sqplus --eps 0.0001
    python mathtool.py integrate --func ratio --from 0 --to 20 --steps 1000

Ввод-вывод сосредоточен здесь: расчётные модули пакета calc ничего не
печатают и не запрашивают ввод, а возвращают результат значением.
"""

import sys

from calc import equation
from cli import build_parser


def print_error(message):
    """Выводит сообщение об ошибке в стандартный поток ошибок."""
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


def handle_solve(args):
    """Обработчик команды solve.

    Получает коэффициенты, проверяет их, вызывает расчёт и печатает результат.
    Возвращает код завершения: 0 — расчёт выполнен, 1 — ошибка в данных.
    """
    coefficients = get_coefficients(args)
    equation.validate_coefficients(coefficients)
    kind, discriminant, roots = equation.solve(
        coefficients["A"], coefficients["B"], coefficients["C"]
    )
    print_solution(kind, discriminant, roots)
    return 0


# Обработчики команд: добавление новой команды не изменяет остальные
HANDLERS = {
    "solve": handle_solve,
}


def main(argv):
    """Точка входа приложения. Возвращает код завершения."""
    # 1. Разбор параметров командной строки
    parser = build_parser()
    args = parser.parse_args(argv)

    # Команда не указана — вывод справки
    if args.command is None:
        parser.print_help()
        return 0

    handler = HANDLERS.get(args.command)
    if handler is None:
        print_error(f"ОШИБКА: команда \"{args.command}\" ещё не реализована")
        return 1

    # 2. Обработка команды: получение данных, проверка, расчёт, вывод
    try:
        return handler(args)
    except (ValueError, OSError) as error:
        print_error(f"ОШИБКА: {error}")
        return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
