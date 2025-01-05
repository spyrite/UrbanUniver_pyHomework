import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        if self.__is_valid_sides(sides):
            self.__sides = list(sides)
        else:
            self.__sides = [1 for _ in range(self.sides_count)]
        self.__color = list(color)
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if all([0 <= r <= 255, 0 <= g <= 255, 0 <= b <= 255]):
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, sides):
        if all([True for side in sides if side > 0]) and len(sides) == self.sides_count:
            return True
        return False

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = sides[0] / 2 * math.pi

    def get_square(self):
        return math.pi * self.__radius ** 2

    def __repr__(self):
        return f'Круг радиусом {self.__radius}'


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        p = len(self) / 2
        return math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))

    def __repr__(self):
        return f'Треугольник со сторонами: {self.get_sides()}'


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.set_sides(*[sides[0] for _ in range(self.sides_count)])

    def get_volume(self):
        return super().get_sides()[0] ** 3

    def __repr__(self):
        return f'Куб c ребрами: {self.get_sides()}'


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())

print('\n--- Дополнительные проверки ---\n')

triangle1 = Triangle((20, 30, 40), 45, 6, 7, 8)
print(triangle1)
triangle2 = Triangle((20, 30, 40), 6, 7, 8)
print(triangle2)

# Площадь треугольника
print(triangle2.get_square())

# Площадь круга
print(circle1)
print(circle1.get_square())

# Куб
cube2 = Cube((200, 100, 35), 23, 55, 11)
print(cube2)
print(cube2.get_volume())
