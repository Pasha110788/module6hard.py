class Figure:
    sides_count = 0

    def __init__(self, __color, *__sides):
        self.__sides = list(__sides) if self.__is_valid_sides(__sides) else list(__sides) * self.sides_count
        self.__color = __color
        self.filled = False

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return all(isinstance(i, int) and 0 <= i <= 255 for i in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(i, int) and i > 0 for i in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)
        self.radius = __sides[0] / (2 * 3.14)

    def get_square(self):
        return 3.14 * self.radius ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, *__sides):
        super().__init__(__color, __sides)

    def get_square(self):
        a, b, c = self.__sides
        s = sum(self.__sides) / 2
        return (s * (s - a) * (s - b) * (s - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, sides):
        super().__init__(__color, sides)
        self.sides = sides

    def get_volume(self):
        return self.sides ** 3


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
triangle1 = Triangle((200, 200, 5), 5)
#print(triangle1.get_square())
