import random
from statistics import fmean

# Task: Напишите программу для поиска чисел, превышающих среднее значение чисел данного массива.


def main():
    print('Task 5')

    the_array = tuple(random.randint(1, 25) for _ in range(0, 10))
    print(f'Заданный массив: {the_array}')

    avg = int(fmean(the_array))
    print(f'Среднее арифметическое для данного массива: {avg}')

    above_average: tuple[int] = tuple(filter(lambda x: x > avg, the_array))

    print(f'Числа > {avg}: {above_average}')


if __name__ == '__main__':
    main()
