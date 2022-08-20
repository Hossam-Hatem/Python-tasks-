""" x="Hello, welcome to my world."
print(x[7])
y="HOSSAM"
y.center(20,"@")
print(y.center(20,"@"))
print(y.endswith('.')) """

# txt = "x"

# x = txt.isidentifier()

# print(x)





""" x="Hello, welcome to my world."
#print(x.count("o"))
print(x.split(' '))
y=" ".join(x)
print(y)
print(x.index("my"))  """



""" 
from posixpath import join


l2=[]
x=input("dakspd")
l=x.split(' ')
print(l)
for i in l:
    if i not in l2:
        l2.append(i)
print (l2)
y=" ".join(l2)
print(y) """



""" x=input("dakspd")
m=input("dakspd")
y=x.replace(m," ")
print(y) """


x=input("dakspd")
l=x.split(' ')
l2=[]
for word in l:
    if word not in l2:
        l2.append(word)
    #else:
    #    print("HOSSAM")
l2=' '.join(l2)
print(l2)

