from fractions import Fraction
from user_input import user_input
# Task: Напишите програмиу для преобразования температуры из градуса Фаренгейта в градус Цельсия.


def f2c(f: float) -> float:
    return (f - 32.0) * Fraction(5, 9)


def main():
    print('Task 8')

    temp_f: float = user_input('Введите температуру в Фаренгейтах', float)
    temp_c = round(f2c(temp_f), 2)

    print(f'{temp_f} градусов Фаренгейтов = {temp_c} градусов Цельсия')


if __name__ == '__main__':
    main()
