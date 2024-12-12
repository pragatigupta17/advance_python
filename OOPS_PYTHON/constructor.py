class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age # declaration of instance variable
        print(self.name) #calling
    def add (self,school):
       self.school=school #declartion
    def show_detail(self):
        print(self.name)
        print(self.age) # calling
        print(self.school)
obj=student("Pragati Gupta",24)
obj.add('soni pariya')
obj.show_detail()