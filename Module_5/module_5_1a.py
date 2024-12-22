class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print('Такого этажа не существует')
        else:
            for n_floor in range(1, new_floor+1):
                print(n_floor)

h1 = House('ЖК Кристалл', 20)
h2 = House('Коттедж в Усть-Заостровке', 2)
h1.go_to(7)
h2.go_to(99)