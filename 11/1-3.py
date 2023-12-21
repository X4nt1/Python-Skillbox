#1
class Soldier:
    name = 0
    def __init__(self, name):
        self.name = name
    healthy = 100
    damage = 20
    def atack(self,soldier):
        soldier.healthy -= self.damage
soldier_1 = Soldier('Первый боец')
soldier_2 = Soldier('Второй боец')
while True:
    soldier_1.atack(soldier_2)
    print(f'{soldier_1.name} атаковал у противника осталось {soldier_2.healthy}')
    if (soldier_2.healthy < 1):
        print(f'{soldier_1.name} победил')
        break
    soldier_2.atack(soldier_1)
    print(f'{soldier_2.name} атаковал у противника осталось {soldier_1.healthy}')
    if (soldier_1.healthy < 1):
        print(f'{soldier_2.name} победил')
        break

#2
import copy
def mid_bal(marks):
    return round(sum(marks)/len(marks), 2)

class Student:
    name = ''
    num_group = 0
    marks = []
    def __init__(self,name, num_group, marks):
        self.name = name
        self.num_group = num_group
        self.marks = marks
    def output(self):
        print(f'{self.name} {self.num_group} {self.marks}')
students = []
students.append(Student('Vlad', 205, [5,4,3,5,4]))
students.append(Student('Irina', 207, [4,3,3,5,5]))
students.append(Student('Olga', 201, [3,4,3,3,3]))
students.append(Student('Alex', 251, [2,4,3,3,4]))
students.append(Student('Nikita', 209, [5,4,5,5,5]))
students.append(Student('Sergey', 203, [5,4,5,5,2]))
students.append(Student('Anton', 202, [5,4,3,2,4]))
students.append(Student('Lera', 222, [3,5,3,3,3]))
students.append(Student('Dasha', 212, [5,5,5,5,4]))
students.append(Student('Vika', 211, [3,4,4,4,4]))
students.sort(key=lambda item: mid_bal(item.marks))
for student in students:
    student.output()

#3
class Parent:
    name = 'Default'
    age = None
    children = []
    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children
    def get_info(self):
        print(f'Имя: {self.name} \nВозраст: {self.age} ')
        if len(self.children) > 0:
            print('Список детей:')
            for child in self.children:
                print(child.name)
        else:
            print('Детей нет')
    def calm_down(self,child):
        if child.calm:
            print(f'{child.name} уже спокоен')
        else:
            child.calm = True
            print(f'{child.name} успокоился')
    def eat(self, child):
        if child.hunger:
            child.calm = False
            print(f'{child.name} сыт')
        else:
            print(f'{child.name} уже сыт')
class Child:
    name = 'Default'
    age = None
    calm = True
    hunger = False
    def __init__(self, name, age, calm, hunger):
        self.name = name
        self.age = age
        self.calm = calm
        self.hunger = hunger
child_1 = Child('Bob', 14, True, False)
child_2 = Child('Ann', 16, False, False)
parent = Parent('Vova', 40,[child_1, child_2])
parent.get_info()
parent.calm_down(child_2)
parent.eat(child_1)

