import random
class People:
    name = None
    satiety = 50
    house = None
    alive = True
    def __init__(self, name, house):
        self.name = name
        self.house = house
    def eat(self):
        self.satiety += 1
        self.house.food -= 1
        print(f'{self.name} поел. Сытость: {self.satiety}')
    def work(self):
        self.satiety -= 1
        self.house.money += 1
        print(f'{self.name} поработал. Сытость: {self.satiety}')
    def play(self):
        self.satiety -= 1
        print(f'{self.name} поиграл. Сытость: {self.satiety}')
    def go_shop(self):
        self.house.food += 1
        self.house.money -= 1
        print(f'{self.name} сходил в магазин. Сытость: {self.satiety}')
    def live(self):
        num = random.randrange(1,6)
        if self.satiety < 20:
            self.eat()
        elif self.house.food < 10:
            self.go_shop()
        elif self.house.money < 50:
            self.work()
        elif num == 1:
            self.work()
        elif num == 2:
            self.eat()
        else:
            self.play()
        if self.satiety < 0:
            self.alive = False
class House:
    food = 50
    money = 0
