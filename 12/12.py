#1
class Property:
    def __init__(self, worth):
        self.__worth = worth
    def get_worth(self):
        return self.__worth
    def get_tax(self):
        return self.get_worth()/100
    def __str__(self):
        return f'Налог {self.get_tax()}'
class Apartment(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def get_tax(self):
        return self.get_worth()/1000
class Car(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def get_tax(self):
        return self.get_worth()/200
class CountryHouse(Property):
    def __init__(self, worth):
        super().__init__(worth)
    def get_tax(self):
        return self.get_worth()/500
summ = int(input('Введите количество своих денег: '))
apart = Apartment(int(input('Введите стоимость квартиры ')))
car = Car(int(input('Введите стоимость машины ')))
country_house = CountryHouse(int(input('Введите стоимость дачи ')))
summ -= apart.get_tax() + car.get_tax() + country_house.get_tax()
if summ < 0:
    print(f'Вам не хватает {abs(summ)}')
else:
    print('Вам хватило на все налоги')


#2
import random
class KillError(Exception):
    def __str__(self):
        return 'KillError'
class DrunkError(Exception):
    def __str__(self):
        return 'DrunkError'
class CarCrushError(Exception):
    def __str__(self):
        return 'CarCrushError'
class GluttonyError(Exception):
    def __str__(self):
        return 'GluttonyError'
class DepressionError(Exception):
    def __str__(self):
        return 'DepressionError'
def one_day():
    if random.randrange(1,10) == 1:
        error = random.choice([KillError(), DrunkError(), CarCrushError(), GluttonyError(), DepressionError()])
        raise error
    karma = random.randrange(1,7)
    return karma
with open('karma.log', 'w') as karma_log:
    karma = 0
    while karma < 500:
        try:
            karma += one_day()
        except (KillError, DrunkError, CarCrushError, GluttonyError, DepressionError) as error:
            karma_log.write(f'{error}\n')

#3
class MyDict(dict):
    def get(self, key):
        if key in self:
            return super().get(key)
        return 0
file = MyDict({1 : 'sdf', 2 : "dsda"})
print(file.get(1))
print(file.get(3))
