
class Color:
    def apply_color(self):
        pass

class Red(Color):
    def apply_color(self):
        return "Red"

class Blue(Color):
    def apply_color(self):
        return "Blue"

class Shape:
    def __init__(self, color: Color):
        self.color = color

    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, color: Color, radius: float):
        super().__init__(color)
        self.radius = radius

    def draw(self):
        return f"Drawing a {self.color.apply_color()} circle with radius {self.radius}"


class Square(Shape):
    def __init__(self, color: Color, side: float):
        super().__init__(color)
        self.side = side

    def draw(self):
        return f"Drawing a {self.color.apply_color()} square with side {self.side}"


if __name__ == "__main__":
    red_color = Red()
    blue_color = Blue()

    
    red_circle = Circle(red_color, 5)
    blue_square = Square(blue_color, 10)

    
    print(red_circle.draw())
    print(blue_square.draw())
