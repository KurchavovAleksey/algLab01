from typing import Optional

from user_input import user_input

# Task: Напишите программу, которая принимает четыре целых числа от пользователя и выводит надпись равно,
# если все четыре равны, и не равно в противном случае.


def main():
    print('Task 2')
    is_numbers_equal = True
    prev_num: Optional[int] = None
    for num in range(1, 5):
        entered_num: int = user_input(f'Введите число {num}', int)

        if not is_numbers_equal:
            continue

        if prev_num is not None:
            if entered_num != prev_num:
                is_numbers_equal = False

        prev_num = entered_num

    print('равно' if is_numbers_equal else 'не равно')


if __name__ == '__main__':
    main()
