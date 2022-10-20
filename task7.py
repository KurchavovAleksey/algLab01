from random import randint
# Task: Напишите для разбиения заданного массива целых чисел на четное число первым и нечетное число вторым.


def main():
    print('Task 7')
    the_array = tuple(randint(0, 25) for _ in range(10))
    print(f'Заданный массив: {the_array}')

    evens: list[int] = list()
    odds: list[int] = list()

    for num in the_array:
        if num % 2 == 0:
            evens.append(num)

        else:
            odds.append(num)

    print(f'Массив чётных чисел: {evens}')
    print(f'Массив нечётных чисел: {odds}')


if __name__ == '__main__':
    main()
