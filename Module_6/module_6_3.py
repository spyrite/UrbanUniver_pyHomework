from random import randint

str_numbers = {1: 'one', 2: 'two', 3: 'three', 4: 'four'}


class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self._coords = [0, 0, 0]
        self.speed = speed

    def move(self, dx, dy, dz):
        if self.speed * dz < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._coords = [self.speed * dx, self.speed * dy, self.speed * dz]

    def get_coords(self):
        print(f'X: {self._coords[0]}; Y: {self._coords[1]}; Z: {self._coords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print("Sorry, I'm peaceful :)")
        else:
            print("Be careful, I'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def __init__(self, speed):
        super().__init__(speed)

    def lay_eggs(self):
        n = randint(1, 4)
        print(f'Here {'are' if n > 1 else 'is'} {str_numbers[n]} egg{'s' if n > 1 else ''} for you')


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        self._coords[2] -= int(abs(dz) * self.speed / 2)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, AquaticAnimal, Bird):
    def __init__(self, speed):
        super().__init__(speed)
        self.sound = 'Click-click-click'

    def speak(self):
        print(self.sound)


db = Duckbill(10) #Утконос

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_coords()
db.dive_in(6)
db.get_coords()

db.lay_eggs()
