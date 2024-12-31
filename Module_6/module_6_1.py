class Animal:
    alive = True
    fed = False
    name = None

    def __init__(self, name):
        self.name = name

    def eat(self, food):
        match food.edible:
            case True:
                print(f'{self.name} съел {food.name}')
                self.fed = True
            case False:
                print(f'{self.name} не стал есть {food.name}')
                self.alive = False


class Mammal(Animal):
    pass


class Predator(Animal):
    pass


class Plant:
    edible = False
    name = None

    def __init__(self, name):
        self.name = name


class Flower(Plant):
    pass


class Fruit(Plant):
    edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
