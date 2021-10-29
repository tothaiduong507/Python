class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self,length,width):
        super().__init__(length,width)
class Cube(Rectangle):
    def __init__(self,length,width,height):
        super().__init__(length, width)
        self.height=height
    def volumn(self):
        return self.length*self.width*self.height

square = Square(2,3)
cube= Cube(2,3,4)
print(square.area())
print(cube.volumn())