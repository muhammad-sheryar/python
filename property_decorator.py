#Python Property Decorator -> Decorator define to use a method as a property (it can be accessed like an attribute)
#                             Benefit:ADD Additional logic when read write and delete attributes
#                             Gives: Getter Setter and Deleter Methods

class Rectangle:
    
    def __init__(self, width, height):
        
        self._width = width
        self._height = height
    
    @property    
    def width(self):
         return f"{self._width:.2f}"
    
    @property    
    def height(self):
         return f"{self._height:.2f}"
     
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
            
        else:
            print("Width Must Be Greater Than Zero.")
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
            
        else:
            print("Height Must Be Greater Than Zero.")
            
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted!")
        
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted!")    
     
rectangle = Rectangle(3,4)

# rectangle.width = 0
# rectangle.height = 10

del rectangle.width
del rectangle.height

# print(rectangle.width)
# print(rectangle.height)

