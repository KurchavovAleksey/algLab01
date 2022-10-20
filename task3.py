import random
from numbers import Number

from user_input import user_input


# Task: Напишите программу для поиска k самых больших элементов в заданном массиве.
# Элементы в массиве могут располагаться в любом порядке.


def task3(array_reversed=False):
    the_array: list[Number] = [random.randint(1, 25) for _ in range(0, 10)]
    print(f'Заданный массив: {the_array}')

    k: int = user_input('Введите k (k > 0)', int, constraint=lambda _k: _k > 0)

    the_array.sort(reverse=array_reversed)

    print(f'{k} самых {"маленьких" if array_reversed else "больших"} элементов в массиве: {the_array[-k:][::-1]}')


def main():
    print('Task 3')
    task3()


if __name__ == '__main__':
    main()
