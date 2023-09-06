import os
import datetime
from functools import wraps


def logger(old_function):
    @wraps(old_function)
    def new_function(*args, **kwargs):
        start_time = datetime.datetime.now()
        print(f'Начало функции {old_function.__name__} в {start_time}')
        with open('main.log', 'a', encoding='utf-8') as f:
            end_time = datetime.datetime.now()
            work_function_time = end_time - start_time
            log_file = (f'Начало функции {old_function.__name__} в {start_time} \n'
                        f'Аргументы используемые функцией {args} и {kwargs}\n'
                        f'Возвращен результат {old_function(*args, **kwargs)} за {work_function_time}\n'
                        f'\n')
            result = f.writelines(log_file)
        return old_function(*args, **kwargs)

    return new_function



def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists('main.log'), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open('main.log') as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()