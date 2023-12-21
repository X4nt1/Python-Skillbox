#1
from typing import Callable
import functools
def how_are_you(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        input('Как дела? ')
        print('А у меня не очень! Ладно, держи свою функцию.')
        func(*args, **kwargs)
    return wrapped_func
@how_are_you
def test() -> None:
    print('<Тут что-то происходит...>')

test()

#2
from typing import Callable, Any
import functools
import time
def moderator(func: Callable ) -> Callable:
    start_time = time.time()
    while time.time() - start_time < 5:
        pass
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs):
        func(*args, **kwargs)
    return  wrapped_func
@moderator
def test() -> None:
    print('<Тут что-то происходит...>')
test()

#3
from typing import Callable, Any
import functools
import datetime
def logging(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        print(f'Функция \n{func.__name__} \nДокументация\n{func.__doc__}\n')
        try:
            func(*args, **kwargs)
        except Exception as exc:
            now = datetime.datetime.now()
            with open('function_errors.log', 'a', encoding='utf-8') as errors:
                    errors.write(f'Функция {func.__name__} \nОшибка {exc} \nВремя и дата ошибки {now}\n\n')
    return wrapped_func
@logging
def output(text: str) -> str:
    """Функция выводит текст"""
    return text
@logging
def div(num_1: int, num_2: int) -> float:
    """Функция делит числа"""
    res = num_1 / num_2
    return res
output('dfsf')
div(1,0)
output('gfjgfh')

#4
from typing import Callable
import functools


def counter(func: Callable) -> Callable:
    @functools.wraps(func)
    def wrapped_func(*args, **kwargs) -> None:
        wrapped_func.count += 1
        print(f'Функция {func.__name__} была вызвана {wrapped_func.count} раз')
        return func(*args, **kwargs)
    wrapped_func.count = 0
    return wrapped_func


@counter
def do_count(num: int) -> int:
    return num


do_count(5)
do_count(5)
do_count(5)

#5
from typing import Callable
import functools


def dec_fib(func: Callable) -> Callable:

    @functools.wraps(func)
    def wrapped_func(n):
        if n in dec_fib.dict_val:
            return dec_fib.dict_val[n]
        res = func(n)
        dec_fib.dict_val[n] = res
        return res
    dec_fib.dict_val = {}
    return wrapped_func


@dec_fib
def fibonacci(n):
    if n in (1, 2):
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(10))
