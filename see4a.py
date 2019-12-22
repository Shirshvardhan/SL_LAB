class Rectangle:
    def __init__(self,a,b):
        self.length = a
        self.breadth = b
    def area(self):
        return(self.length*self.breadth)
x=int(input("ENTER THE LENGTH"))
y=int(input("ENTER THE BREADTH"))
rec = Rectangle(x,y)
print(rec.area())
