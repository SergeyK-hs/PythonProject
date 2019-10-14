import  math
class Figure:
    def perimeter(self):
        raise  NotImplementedError


class Circle(Figure):
    def __init__(self,radius):
        self.radius = radius

    def perimeter(self):
        return math.pi*2*self.radius

class Rectangle (Figure):
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def perimeter(self):
        return (self.a + self.b)*2

class Triangle(Rectangle):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = math.sqrt(a**2 + b**2)

    def perimeter(self):
        return self.a + self.b + self.c

class Trapiciya(Figure):
    def __init__(self,a,b,c,d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.d + self.c

class Romb(Figure):
    def __init__(self,a):
        self.a = a

    def perimeter(self):
        return 4*self.a

romb = Romb(4)
cir = Circle(5)
print(cir.perimeter())
