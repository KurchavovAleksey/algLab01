from user_input import user_input

# Task: Напишите программу для вычисления индекса массы тела (ИМТ). ИМТ = ВЕС / РОСТ2


def constraint_natural(x):
    return x > 0


def main():
    print('Task 9')

    height: float = user_input('Введите рост (см)', float, constraint=constraint_natural)
    weight: float = user_input('Введите массу (кг)', float, constraint=constraint_natural)

    imt = weight / (height * 2)
    print(f'ИМТ = {imt:.2f}')


if __name__ == '__main__':
    main()
