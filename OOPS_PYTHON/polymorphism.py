# method overloading :--
'''class A:
    def add (self,x,y):
        return x+y
    def add (self,x,y,z):
        return x+y+z
        a=A()
        a.add(10,20)'''
# it will return error
#==================================================================
class A:
    def add(self,*n):
        sum=0
        for i in n:
            sum=sum+i
        return sum
obj = A()
x=obj.add(10,20)
print(x)  # Output: 30
y=obj.add(10,20,40)
print(y)  # Output: 70
