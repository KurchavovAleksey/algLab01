from typing import Callable, Any


def user_input(prompt: str, target_type: callable, constraint: Callable[[Any], bool] = lambda value: True):
    while True:
        try:
            result = input(f'{prompt}: ')
            result_target_typed = target_type(result)
            if constraint(result_target_typed):
                return result_target_typed

        except EOFError:
            exit(1)

        except ValueError:
            print('Некорректный ввод')
            pass
