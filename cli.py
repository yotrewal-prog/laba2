"""cli.py — разбор параметров командной строки.

Разбор выполняется в два этапа: сначала определяется имя команды,
затем разбираются её собственные параметры. Разбор по количеству
параметров не применяется: команд четыре, а количество параметров их
не различает.
"""

import argparse

from calc import integration, series


def build_parser():

    parser = argparse.ArgumentParser(
        prog="mathtool",
        description=(
            "mathtool — расчёты над уравнениями и числовыми последовательностями"
        ),
        allow_abbrev=False,
    )
    subparsers = parser.add_subparsers(dest="command")


    solve_parser = subparsers.add_parser(
        "solve",
        help="решение уравнения A*x^2 + B*x + C = 0",
        description=(
            "Решение уравнения A*x^2 + B*x + C = 0. Коэффициенты задаются "
            "параметрами -a, -b, -c либо, если они не указаны, "
            "запрашиваются с клавиатуры."
        ),
        allow_abbrev=False,
    )
    solve_parser.add_argument(
        "-a", type=int, help="коэффициент A: целое число по модулю не более 10000"
    )
    solve_parser.add_argument(
        "-b", type=int, help="коэффициент B: целое число по модулю не более 10000"
    )
    solve_parser.add_argument(
        "-c", type=int, help="коэффициент C: целое число по модулю не более 10000"
    )

    # Команда stats: числа читаются из файла или со стандартного ввода
    stats_parser = subparsers.add_parser(
        "stats",
        help="показатели числовой последовательности",
        description=(
            "Вычисление показателей числовой последовательности. Числа "
            "читаются из файла --input либо, если он не задан, "
            "со стандартного ввода."
        ),
        allow_abbrev=False,
    )
    stats_parser.add_argument(
        "--input", help="имя файла с числами; без параметра числа читаются со стандартного ввода"
    )

    # Команда series: сумма числового ряда
    series_parser = subparsers.add_parser(
        "series",
        help="сумма числового ряда",
        description=(
            "Вычисление суммы числового ряда. Указывается ровно один из "
            "параметров --terms и --eps: остановка по количеству слагаемых "
            "либо по достигнутой точности."
        ),
        allow_abbrev=False,
    )
    series_parser.add_argument(
        "--func",
        choices=sorted(series.FORMULAS),
        required=True,
        help="имя суммируемого ряда: " + ", ".join(sorted(series.FORMULAS)),
    )
    series_group = series_parser.add_mutually_exclusive_group(required=True)
    series_group.add_argument("--terms", type=int, help="число слагаемых: от 1 до 10000")
    series_group.add_argument("--eps", type=float, help="точность: больше нуля и не грубее 0.0001")

    # Команда integrate: численное интегрирование
    integrate_parser = subparsers.add_parser(
        "integrate",
        help="численное интегрирование",
        description=(
            "Численное интегрирование методом левых прямоугольников. "
            "Оба предела интегрирования должны лежать в промежутке функции."
        ),
        allow_abbrev=False,
    )
    integrate_parser.add_argument(
        "--func",
        choices=sorted(integration.FUNCTIONS),
        required=True,
        help="имя подынтегральной функции: " + ", ".join(sorted(integration.FUNCTIONS)),
    )
    integrate_parser.add_argument(
        "--from", dest="start", type=float, required=True, help="нижний предел интегрирования"
    )
    integrate_parser.add_argument(
        "--to", dest="stop", type=float, required=True, help="верхний предел интегрирования"
    )
    integrate_parser.add_argument(
        "--steps", type=int, required=True, help="число прямоугольников: от 1 до 100000"
    )

    return parser
