from user_input import user_input

# Task: Напишите программу, чтобы проверить, могут ли три заданные длины сторон (целые числа) образовать треугольник или нет.


def main():
    sides: list[int] = list()
    for side_name in ('a', 'b', 'c'):
        sides.append(user_input(f'Введите сторону {side_name}', int, constraint=lambda x: x >= 0))

    not_exist_flag = True

    if sides[0] + sides[1] > sides[2] and sides[2] + sides[1] > sides[0] and sides[0] + sides[2] > sides[1]:
        not_exist_flag = False

    print(f'Треугольник с такими сторонами {"не существует" if not_exist_flag else "существует"}')


if __name__ == '__main__':
    main()
