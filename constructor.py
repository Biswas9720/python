class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rec=Rectangle(6,6)

print(rec.length)
print(rec.width)

print(rec.area())



