# x=3
# sum=lambda x:x*x
# print(sum)
# print("hello")
# print(x)
# print(sum(2))
# x = lambda a, b : a * b
# print(x(5, 6))
# x = lambda a, b, c : a + b + c
# print(x(5, 6, 2))
def cub(x):
    return x*x*x
print(cub(2))

li=[2,3,4,5,6,7]
# two function use in map function AS SEPARate def function and lambda function
# lambda function and li is itretor
newl=list(map(lambda x:x*x*x,li))
# cub function defin above 
newl=list(map(cub,li))
# print list by finding eAch item
print("in list find all number  cube  is :",newl)
# second method that define list 
# def myfunc(a, b):
#   return a + b
# x = list(map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple')))
# print(x)
# filter is use for filter any list 
# def evenN(x):
#     return (x % 2) == 0
# newl=list(filter(evenN,li))
# print("only even number in list :",newl)
newl=list(filter(lambda x:x%2 ==0,li))
print("in list only even number is :",newl)
from functools import reduce

suml=reduce(lambda x,y:x+y ,li)
print("in list find all number  sum  is  :",suml)