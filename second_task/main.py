import re
from typing import Generator, Callable


def generator_numbers(text: str) -> Generator[float, None, None]:
    for match in re.finditer(r'\b\d+(\.\d+)?\b', text):
        yield float(match.group())


def sum_profit(text: str, func: Callable) -> float:
    profit = 0
    iterable = func(text)
    for num in iterable:
        profit+=num

    return profit


def main():
    text = ("Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід,"
            "доповнений додатковими надходженнями 27.45 і 324.00 доларів.")
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == '__main__':
    main()
