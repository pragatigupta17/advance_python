class father:
    x=10
    y=20
    z=30
    def property_f(self,f_name,f_age):
        self.name=f_name
        self.age=f_age
        print(self.name)
        print(self.age)
        
class mother:
    x=10
    y=20
    i=90
    j=30
    def property_m(self,m_name,m_age):
        self.name1=m_name
        self.age1=m_age
        print(self.name1)
        print(self.age1)
        
class child(mother,father):
   def property(self):
       pass
#print("Son property:",dir(child))
#print("Father's property: ",dir(father))

#print("Mother's property: ",dir(mother))
obj=child()
obj.property_m("MAMTA",45)
obj.property_f("AJAY",49)



