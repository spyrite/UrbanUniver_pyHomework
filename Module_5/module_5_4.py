class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, кол-во этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        if isinstance(value, int):
            self.__add__(value)
        return self

    def __iadd__(self, value):
        if isinstance(value, int):
            self.__add__(value)
        return self

    def __del__(self):
        print(f'{self.name} снесён, но он остаётся в истории')

    def rename(self, new_name):
        print(f'"{self.name}" был переименован в "{new_name}"')
        self.name = new_name

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует')
        else:
            for n_floor in range(1, new_floor+1):
                print(n_floor)

h1 = House('ЖК Кристалл', 20)
print(House.houses_history)
h2 = House('Коттедж в Усть-Заостровке', 2)
print(House.houses_history)
h3 = House( 'ЖК Матрёшки', 15)
print(House.houses_history)

# __del__
del(h2)
del(h3)

print(House.houses_history)