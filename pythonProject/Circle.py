class circles:
    def __init__(self,radius,diameter):
        self.radius = radius
        self.diameter = diameter
    def perimeter (self):
        self.diameter*=22/7

circle1 = circles(21,42)
circle1.perimeter()
print(circle1.diameter)
