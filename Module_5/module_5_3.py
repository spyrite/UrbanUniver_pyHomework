class House:
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

    def rename(self, new_name):
        print(f'"{self.name}" был переименован в "{new_name}"')
        self.name = new_name

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for n_floor in range(1, new_floor+1):
                print(n_floor)

h1 = House('ЖК Кристалл', 20)
h2 = House('Коттедж в Усть-Заостровке', 2)

# __str__
print(h1)
print(h2)

# __eq__
print(h1 == h2)

# __add__
h2 = h2 + 18
h2.rename('ЖК в Усть-Заостровке')
print(h2)
print(h1 == h2)

# __iadd__
h1 += 5
print(h1)

# __radd__
h2 = 5 + h2
print(h2)

# __gt__
print(h1 > h2)
# __ge__
print(h1 >= h2)
# __lt__
print(h1 < h2)
# __le__
print(h1 <= h2)
# __ne__
print(h1 != h2)