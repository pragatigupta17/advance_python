# INSTANCE METHOD
''''class A:
    def new (self):
        print("1st method")    # declaration
    def new1(self):
        self.new()
        print("2nd method")    # calling
obj=A()
obj.new1()      #calling
obj.new()       #calling '''

# CLASS METHOD
 
class book:
    price=150
    def __init__(self, title, author, price):
        self.title=title
        self.author=author
        self.price=price
    @classmethod
    def change_price(cls, price):
        cls.price=price
    def show_details(self):
        print(self.title)
        print(self.author)
        print(book.price)
obj=book("Python", "John", 150)
obj.change_price(200)
obj.show_details()  # calling instance method
# obj.showdetails()

