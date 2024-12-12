class student:
    "student information"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show_detail(self):
        print(self.name)
        print(self.age)
obj =student("Pragati ",24)
obj. show_detail()
obj1=student("Aditi",24)
obj1. show_detail()