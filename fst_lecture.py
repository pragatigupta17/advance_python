#MAP
'''my_list = [10,20,30,40,50]
def dec(x):
    return x - 5
x=map(dec,my_list)
print(list(x))'''

#FILTER
'''my_tuple = (10,20,70,40,89,56,78,)
def grater_60(x):
    if x>60:
        return x
x=(filter(grater_60,my_tuple))
print(list(x))'''

#REDUCE

from functools import reduce
#from functools.reduce
#from operator import add

my_list = [10,20,30,70,40,50,60]
def max_digit(x,y):
     if x>y :
        return x
     else:
        return y    
x=reduce(max_digit,my_list)
print(x)


