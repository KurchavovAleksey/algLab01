from user_input import user_input
# Task: Напишите программу для умножения двух заданных целых чисел без использования оператора умножения(*).


def main():
    print('Task 6')

    a: int = user_input('Введите целое число a', int)
    b: int = user_input('Введите целое число b', int)

    res = a.__mul__(b)
    print(f'a * b = {res}')


if __name__ == '__main__':
    main()
