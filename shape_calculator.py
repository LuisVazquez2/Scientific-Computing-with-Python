class Rectangle:
    # constructor
    def __init__(self, width, height):
        self.width = width
        self.height = height
    # special methods

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    # methods of class

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        else:
            x = "*" * self.width + "\n"
            return x*self.height

    def get_amount_inside(self, shape):
        if isinstance(shape, Square):
            return self.get_area() // shape.get_area()
        elif isinstance(shape, Rectangle):
            return self.get_area() // shape.get_area()
        else:
            return "Error: Shape is not a rectangle or square."


class Square(Rectangle):
    def __init__(self, size):
        self.width = size
        self.height = size

    def __str__(self):
        return f"Square(side={self.width})"

    def set_side(self, size):
        self.width = size
        self.height = size


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
