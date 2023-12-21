#1
from typing import Callable
import functools


def check_permission(precision: str) -> Callable:
    """Декоратор для проверки прав пользователя.
    Возвращает ошибку или право доступа к функции"""
    def check_permission_1(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapped_2(*args, **kwargs):
            try:
                if precision in user_permissions:
                    func(*args, **kwargs)
                else:
                    raise PermissionError
            except PermissionError:
                print(f'PermissionError: у пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapped_2
    return check_permission_1


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
#2
from typing import Callable
import functools
app = dict()


def callback(precision: str) -> Callable:
    def callback_1(func: Callable) -> Callable:
        app[precision] = func

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            func_call = func(*args, **kwargs)
            return func_call
        return wrapped
    return callback_1


@callback(precision='//')
def example() -> str:
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')

#3
from typing import Callable
import time
from datetime import datetime


def timer(cls, func: Callable, date_format: str) -> Callable:
    def wrapped(*args, **kwargs):
        format = date_format
        for sym in format:
            if sym.isalpha():
                format = format.replace(sym, '%' + sym)

        print(f"Запускается '{cls.__name__}.{func.__name__}'. Дата и время запуска: {datetime.now().strftime(format)}")
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Завершение '{cls.__name__}.{func.__name__}', время работы = {round(end - start, 3)} сек.")
        return result

    return wrapped


def log_methods(format_date: str) -> Callable:
    def wrapper(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decor_method = timer(cls, cur_method, format_date)
                setattr(cls, i_method_name, decor_method)
        return cls
    return wrapper


@log_methods("b d Y — H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):
    def test_sum_1(self):
        super().test_sum_1()
        print("Наследник test sum 1")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])
        return result


my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()

#4
from typing import Callable
import functools


def decorator_with_args_for_any_decorator(_func: Callable) -> Callable:
    def decorator_maker(*args, **kwargs):
        def wrapper(func: Callable):
            return _func(func, *args, **kwargs)
        return wrapper
    return decorator_maker


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs) -> Callable:
    @functools.wraps(func)
    def wrapper(*_args, **_kwargs):
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        return func(*_args, **_kwargs)
    return wrapper


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


decorated_function("Юзер", 101)


#5
from typing import Callable
import functools


def singleton(cls) -> Callable:
    @functools.wraps(cls)
    def wrapped(*args, **kwargs):
        if not wrapped.instance:
            wrapped.instance = cls(*args, **kwargs)
        return wrapped.instance
    wrapped.instance = None
    return wrapped

@singleton
class Example:
    pass


my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)

#6
import time


class LoggerDecoration:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы: {args}, {kwargs}')
        start_time = time.time()
        res = self.func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f'Результат: {res}')
        print(f'Время выполнения: {execution_time} секунд')
        return res


@LoggerDecoration
def complex_algorithm(arg1, arg2):
    # Здесь выполняется “сложный” алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    # Можете попробовать вынести создание файла из циклов и проверить, сколько времени алгоритм будет работать в этом случае
    return result

# Пример вызова функции с применением декоратора


result = complex_algorithm(10, 50)
