# Task: Напишите программу, чтобы найти значение указанного выражения.


def subtask_a():
    # Task: 101 + 0) / 3
    # 101 + 0) / 3 не является валидным выражением, его вычисление невозможно
    pass


def subtask_b():
    # Task: 3.0e-6 * 10000000.1
    res = 3.0 * 10 ** -6 * 10000000.1
    print(f'b) 3.0e-6 * 10000000.1 = {res}')


def subtask_c():
    # Task: true && true
    res = True and True
    print(f'c) true && true = {res}')


def subtask_d():
    # Task: false && true
    res = False and True
    print(f'd) false && true = {res}')


def subtask_e():
    # Task: (false && false) || (true && true)
    res = False and False or True and True
    print(f'e) (false && false) || (true && true) = {res}')


def subtask_f():
    # Task: (false || false) && (true && true)
    res = (False or False) and True and True
    print(f'f) (false || false) && (true && true) = {res}')


def main():
    print('Task 1')
    subtask_b()
    subtask_c()
    subtask_d()
    subtask_e()
    subtask_f()


if __name__ == '__main__':
    main()
