from user_input import user_input

# Task: Напишите, которая считывает число и отображает квадрат, куб и четвертую степень.


def main():
    print('Task 10')

    x: int = user_input('Введите число x для возведения в степень', int)
    print(f'x^2 = {x ** 2}; x^3 = {x ** 3}; x^4 = {x ** 4}')


if __name__ == '__main__':
    main()
