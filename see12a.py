class Student:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.marks = []

    def display(self):
        print("name:",self.name)
        print("age:",self.age)
        print("marks:",self.marks)

    def insert(self):
        print("ENTER NAME:\t")
        name = input()
        self.name = name
        print("ENTER AGE:\t")
        age = int(input())
        self.age = age
        print("ENTER THREE SUBJECT MARKS:\t")
        marks=[]
        for i in range(3):
            marks.append(int(input()))
        self.marks = marks
a = Student()
b = Student()
a.insert()
b.insert()
a.display()
b.display()

