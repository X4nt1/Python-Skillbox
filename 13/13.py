#1
from collections.abc import Iterable
class SquareNum:
    def __init__(self, num: int) -> None:
        self.__num = num + 1
        self.__count = 0
    def __iter__(self):
        return self
    def __next__(self) -> int:
        self.__count += 1
        if self.__count == self.__num:
            raise StopIteration
        return self.__count ** 2

def get_squares(num: int) -> Iterable[int]:
    for i in range(1,num+1):
        yield i ** 2


squares_1 = SquareNum(10)
for i in squares_1:
    print(i)

for i in get_squares(10):
    print(i)

for i in (i ** 2 for i in range(1,int(input('Введите  N: ')) + 1)):
    print(i)

#2
import os
from collections.abc import Iterable
def gen_files_path(name: str, path = "C:" ) -> Iterable:
    for i in os.walk(os.path.abspath(os.path.join('..', '..', path))):
        if i[0].endswith(name):
            print(f'Найден каталог {name}')
            return
        if len(i[2]) != 0:
            for file in i[2]:
                yield os.path.join(i[0], file)
for i in gen_files_path('task_7', "11th_work"):
    print(i)

#3
import os
from collections.abc import Iterable
def count_line(path: str) -> Iterable:
     for i in os.walk(os.path.abspath(os.path.join('..', '..', path))):
         if i[2]:
             for file in i[2]:
                 if file.endswith('.py'):
                     count = 0
                     with open(os.path.join(i[0], file),'r') as text:
                         for line in text.readlines():
                             if line != "" and not line.startswith('#'):
                                count += 1
                     yield count
for count in count_line('12th_work'):
    print(count)

#4
from collections.abc import Iterable
class Node:
    def __init__(self, data, next=None):
        self.__data = data
        self.__next = next
    def get_next(self):
        return self.__next
    def set_next(self, value):
        self.__next = value
    def get_data(self):
        return self.__data
class LinkedList:
    def __init__(self):
        self.__head = None
        self.__curr_node = None

    def __str__(self) -> str:
        if not self.__head:
            return ""
        lastNode = self.__head
        res = f'{lastNode.get_data()}'
        while lastNode.get_next():
            lastNode = lastNode.get_next()
            res += f' {lastNode.get_data()}'
        return res

    def append(self, data):
        new_node = Node(data)
        if not self.__head:
            self.__head = new_node
            return
        lastNode = self.__head
        while (lastNode.get_next()):
            lastNode = lastNode.get_next()
        lastNode.set_next(new_node)

    def get(self, index: int):
        if not self.__head:
            raise IndexError
        lastNode = self.__head
        count = 0
        while count != index:
            if not lastNode.get_next():
                raise IndexError
            count += 1
            lastNode = lastNode.get_next()
        return lastNode.get_data()

    def remove(self, index: int) -> None:
        if not self.__head:
            raise IndexError
        if index == 0:
            self.__head = self.__head.get_next()
            return
        curr_Node = self.__head
        last_Node = None
        count = 0
        while count != index:
            if not curr_Node.get_next():
                raise IndexError
            count += 1
            last_Node = curr_Node
            curr_Node = last_Node.get_next()
        last_Node.set_next(curr_Node.get_next())


    def __iter__(self) -> Iterable:
        return self
    def __next__(self):
        if not self.__head:
            raise StopIteration
        if not self.__curr_node:
            self.__curr_node = self.__head
            return self.__curr_node.get_data()
        if self.__curr_node.get_next():
            self.__curr_node = self.__curr_node.get_next()
            return self.__curr_node.get_data()
        else:
            raise StopIteration
my_list = LinkedList()
my_list.append(10)
my_list.append(12)
my_list.append(14)
print('Текущий список:', my_list)
print('Получение третьего элемента:', my_list.get(2))
print('Удаление второго элемента.')
my_list.remove(1)
print('Новый список:', my_list)
for i in my_list:
    print(i)

#5
def error_log_generator(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        line = file.readline()
        while line != '':
            if 'ERROR' in line:
                yield line
            line = file.readline()
with open('errors.log', 'a', encoding='utf-8') as errors_file:
    for i in error_log_generator('text.log'):
        errors_file.write(i)

