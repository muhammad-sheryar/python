#Python Super() -> Function Used in a child class to call methods from a parent class (SuperClass)

class Shape:
    
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled
        
        
    def describe(self):
        print(f"It is {self.color} and {'Filled' if self.filled else "Not Filled!"}")
    
class Circle(Shape):
    
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius
        
    def describe(self):
        print(f"It is a Circle with an area of {3.14 * self.radius * self.radius}")
        super().describe()
        

class Square(Shape):
    
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width
        
    def describe(self):
        print(f"It is a Sqaure with an area of {self.radius * self.radius}")
        super().describe()

class Triangle(Shape):
    
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.height = height
        self.width = width

        
    def describe(self):
        print(f"It is a Circle with an area of {(self.width * self.height) / 2}")
        super().describe()
        

square = Square("Red", True, 5)
circle = Circle("Blue", False, 10)
traingle = Triangle("Blue", False, 10, 6)

# print(square.color)
# print(square.filled)
# print(square.width)

# print(circle.color)
# print(circle.filled)
# print(circle.radius)

# print(traingle.color)
# print(traingle.filled)
# print(traingle.width)
# print(traingle.height)

# circle.describe()
# traingle.describe()
 
        