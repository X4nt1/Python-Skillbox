#1
class File:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode, encoding='utf-8')
        except IOError as error:
            self.file = open(self.filename, 'w', encoding='utf-8')
        finally:
            return self.file

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        if exc_type is not None:
            print(f'An error occurred: {exc_val}')
        self.file.close()
        return True


with File('text.txt', 'w') as file:
    file.write('dfsf')

#2
import math


class MyMath:
    @classmethod
    def circle_len(cls, radius: float) -> float:
        """Вычисление длины окружности."""
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: float) -> float:
        """Вычисление длины окружности."""
        return math.pi * radius ** 2

    @classmethod
    def cube_volume(cls, side: float) -> float:
        """Вычисление объёма куба."""
        return side ** 3

    @classmethod
    def surface_sphere_sq(cls, radius: float) -> float:
        """Вычисление площади поверхности сферы."""
        return 4 * math.pi * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)

#3
class Date:
    def __init__(self, *args):
        self.day, self.month, self.year = args

    @classmethod
    def from_string(cls, date_str: str):
        if cls.is_date_valid(date_str):
            day, month, year = date_str.split('-')
            return cls(day, month, year)
        else:
            raise ValueError

    @classmethod
    def is_date_valid(cls, date_str: str) -> bool:
        date_list = date_str.split('-')
        return 32 > int(date_list[0]) > 0 < int(date_list[0]) and 0 < int(date_list[1]) < 13

    def __str__(self):
        return f'День: {self.day}\tМесяц: {self.month}\tГод: {self.year}'


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))

#4
class Node:
    def __init__(self, ):
        pass
class LRUCache:
    def __init__(self, count: int):
        pass
    @property
    def cache(self):

        return