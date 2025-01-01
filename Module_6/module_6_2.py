class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'white', 'black', 'gold']

    def __init__(self, owner, model, color, engine_power):
        self.owner = owner
        self.__model = model
        self.__engine_power = engine_power
        self.__color = color

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model() + '\n'
              + self.get_horsepower() + '\n'
              + self.get_color() + '\n'
              + f'Владелец: {self.owner}' + '\n')

    def set_color(self, new_color):
        self.__color = new_color if str.lower(new_color) in self.__COLOR_VARIANTS \
            else print(f'Нельзя сменить цвет на {new_color}' + '\n')


class Sedan(Vehicle):
    __PASSANGERS_LIMIT = 5


vehicle_1 = Sedan('Kate', 'Opel Astra', 'red', 350)

vehicle_1.print_info()

vehicle_1.set_color('Orange')
vehicle_1.set_color('WHITE')
vehicle_1.owner = 'Nadya'

vehicle_1.print_info()
