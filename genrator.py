#genrator---
def even_no(n):
    i=2
    while i<=n:
        yield i
        i=i+2
n=int(input("Enter any number:"))
data = even_no(n)
print(data)
data1=even_no(n)
print(next(data1))
print("hello")
print(next(data1))
print("welcome")
print(next(data1))
print("Hii")
print(next(data1))