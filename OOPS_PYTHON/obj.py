class Student :
    def __init__(obj, name, age, grade):
        obj.name = name
        obj.age = age
        obj.grade = grade
        print (obj.name)
    def add(self,school):
        self.school= school
    def school_detail(self):
        print(self.school)
        print(self.name)
        print(self.age)
        print(self.grade)

obj=Student('Pragati Gupta',24,96)
obj.add('soni priya')
print (obj.name)
obj.city='BHOPAL'
obj.show_details()