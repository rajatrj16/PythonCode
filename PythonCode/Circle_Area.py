#Calculate Area of circle
class circle():
    pi = 3.14

    def __init__(self,radious=1):
        self.radious = radious

    def Area(self):
        return self.radious * self.radious * circle.pi

mycircle = circle(2)
print(mycircle.Area())
