import math

class Rectangle:
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        return self.l * self.w

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * pow(self.r, 2)

def main():
    circ = Circle(1)
    print(circ.area())

    rect = Rectangle(2, 3)
    print(rect.area())


if __name__ == '__main__':
    main()
