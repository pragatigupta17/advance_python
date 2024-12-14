'''x=50
class Student:
    def add1():
        print(x)

    def add():
        x=20
        print(x)
obj=Student
obj.add1()
obj.add()

print(x)'''
x=10
class School:
    global x
    x=10
    def add ():
        print(x)
        z=20
        print(z)
    def add1():
        print(x)
obj=School
obj.add()
obj.add1()
print(x)