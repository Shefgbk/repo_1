from datetime import datetime
from functools import wraps
from typing import Any

from black.lines import Callable


def log(filename: Any = None) -> Callable:
    '''Функция-декоратор, который будет автоматически регистрировать детали выполнения функций,
    такие как время вызова, имя функции, передаваемые аргументы, результат выполнения и информация об ошибках'''
    def wrapper(func: Callable) -> Callable:
        @wraps(func)
        def inner(*args: Any, **kwargs: Any) -> Any:
            try:
                start_time = datetime.now()
                result = func(*args, **kwargs)
                end_time = datetime.now()
                log_msg = (f'{func.__name__} OK.\n'
                           f'Start time: {start_time.strftime("%H:%M:%S:%MS")}.\n'
                           f'Result: {result}.\n'
                           f'End time: {end_time.strftime("%H:%M:%S:%MS")}.\n')
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_msg)
                else:
                    print(log_msg)
                return result
            except Exception as e:
                end_time = datetime.now()
                log_msg = (f'{func.__name__} ERROR.\n'
                           f'Start time: {start_time.strftime("%H:%M:%S:%MS")}.\n'
                           f'Error: {type(e)}.\n'
                           f'Inputs: {args},{kwargs}.\n'
                           f'End time: {end_time.strftime("%H:%M:%S:%MS")}.\n')
                if filename:
                    with open(filename, 'a') as f:
                        f.write(log_msg)
                else:
                    print(log_msg)
        return inner
    return wrapper
