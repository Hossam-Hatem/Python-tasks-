# Create a Boolean variable named x
x=True

# Create an integer variable named y
y=1

# Create a float variable named z
z=2.5

# Create a string variable names s
s="Hossam"

# Convert the int variable to float
y=float(y)

# Can we convert the str to int ?
#yes

# Create a list of numbers from 1 to 5
l=[1,2,3,4,5]

# Create a tuple from 10 to 15
t=(10,11,12,13,14,15)

# Convert the list to tuple
t2=list(t)

# Create a dict of 3 values
d={'Hossam':1,'Ahmed':2,'Ali':3}

# Can we use semi colon ; with python
#yes

# Python is interpreted or compiled ?
#interpreted

'''
What is the differences between low level & high level
==> Low-level languages are very challenging for humans to learn and understand and are easy for machines to understand
==> High-level languages are easy to learn and understand
'''

# What is the differences between = , ==
'''
= Assign values on the right to the variable on the left
== Checks if two values or two variables are equal
'''

# What do we mean by using !=
#Checks if two values or two variables are not equal

# Create a variable x with value of 10
x=10

# Increase x value by 15 using assignment operators
x+=15

#Divide the x value by 5 using assignment operators
x/=5

# Multiply the x value by 10 using assignment operator
x*=10

# Get module of x on 3 using assignment operators
x%=3

# Using python print the module of 11 to 4
print(11%4)

#● Print the exponent of 2,3
print(2**3)

#● Divide 11 by 3 using python division
print(11/3)

# Can we divide 11 by 3 and get an integer number ?
#yes
print(11//3)

# Check if 10 is bigger than 15 or not
if 10>15:
    print("10 is bigger than 15")
else :
    print("15 is bigger than 10")

# If 10 is not bigger than15 print x is smaller than 15
if 10>15:
    print("10 is bigger than 15")
else :
    print("x is smaller than 15")

# In which cases we will use all
#If we need all the conditions to be true 

# What is the differences between all , and
#all==>When there are more than two conditions, they must be true
#When two conditions exist, they must be true

# What is the differences between any , or
#any==>When there are more than two conditions, at least one must be true
#==>When there are two conditions, at least one of them must be true

# If we need all the conditions to be true we will use ….
#all

'''
What is the differences between if , elif
if ==>   It can be used once in a conditional sentence
elif ==> It can be used more than once in a conditional sentence
'''

# What is the differences between elif else
#elif ==> It can be used once in a conditional sentence
#else ==> It can be used more than once in a conditional sentence

# Can we use more than one elif
#yes

# Can we use more than one else
#no

# write s simple ternary operator
print("The number is even") if (int(input("Enter the number"))%2==0) else print("The number is odd")

# in elif , python will check all the conditions no matter what ?
#no

# in elif we use else for ... ?
#If all conditions are false

'''
if we have this list [2,4,6,8,10] :
    ○ check to see if 4 in this list or not
    ○ check to see if 4 and 6 in this list on not
    ○ check to see if 3 or 6 in this list
    ○ check to see if 2 , 4 and 5 in this list
'''
l2=[2,4,6,8,10]
if 4 in l2:
    print("4 in the list")
if 4 in l2 and 6 in l2:
    print("4 and 6 in the list")
if 3 in l2 or 6 in l2:
    print("3 or 6 in the list")
if all([2, 4, 5]) in l2:
    print("2 , 4 and 5 in the list")

