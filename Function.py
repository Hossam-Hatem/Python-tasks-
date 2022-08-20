'''
def mysum(x,y):
    print (x+y)
    return(x+y)
x=int(input("Enter the first number = "))
y=int(input("Enter the second number = "))
mysum(x,y)


def mysum2(x=0,y=0):
    r=x+y
    return r
x=int(input("1"))
y=int(input("2"))
print(mysum2(x,y))
print(x,y)
'''

#!Simple calculator

""" def cal(x,y,o):
    if o=='+':
        print (x+y)
        return x+y
    elif o=='-':
        print (x-y)
        return x-y
    elif o=='x' or o=='*' or o=='X':
        print (x*y)
        return x*y
    elif o=='/':
        print (x/y)
        return x/y  
    elif o=='//':
        print (x//y)
        return x//y
    elif o=='%':
        print (x%y)
        return x%y
    elif o=='**' or o=='^':
        print (x**y)
        return x**y   
x=int(input("Enter the first number = "))
y=int(input("Enter the second number = "))
o=input("Choose the operation (+ | - | x | / | // | % | ^):")
cal(x,y,o)  """

"""
 #!anonymous function
mysum =lambda x,y:print(x+y)
mysum(5,4) """

x=1
print(x)
def do():
    global x
    x=0
    print(x)
do()
print(x)
