class Water:
    name = 'Вода'
    def __add__(self, other):
        if other.name == 'Воздух':
            return Storm()
        elif other.name == 'Огонь':
            return Steam()
        elif other.name == 'Земля':
            return Dirt()
class Fire:
    name = 'Огонь'
    def __add__(self, other):
        if other.name == 'Воздух':
            return Lightning()
        elif other.name == 'Вода':
            return Steam()
        elif other.name == 'Земля':
            return Lava()
class Air:
    name = 'Воздух'
    def __add__(self, other):
        if other.name == 'Огонь':
            return Lightning()
        elif other.name == 'Вода':
            return Storm()
        elif other.name == 'Земля':
            return Dust()
class Earth:
    name = 'Земля'
    def __add__(self, other):
        if other.name == 'Огонь':
            return Lava()
        elif other.name == 'Вода':
            return Dirt()
        elif other.name == 'Воздух':
            return Dust()
class Lava:
    name = 'Лава'
class Dirt:
    name = 'Грязь'
class Dust:
    name = 'Пыль'
class Storm:
    name = 'Шторм'
class Steam:
    name = 'Пар'
class Lightning:
    name = 'Молния'
