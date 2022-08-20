'''
a=0
b=0
print(a)

while a<4 :
    # while b<4:
    #     print(a,b)
    #     b=b+1
    a=1+a
    b=1+b
    
   
        
print("Hossam")


b=0
while b<4:
    print(b)
    b=b+1
    
a=0
b=0
while a<4 :
    a=1+a
    b=0
    while b<4:
        b=b+1
        print(a,b)
    
   
        
print("Hossam")
''' 
'''
#Number and Square
start = int(input("Enter the start = "))
end = int(input("Enter the end = "))

print('Number\tSquare')
print('----------------')
for x in range(start,end+1):
    print(x,'\t',x**2)
'''


""" for i in range(9,1,-1):
    for c in range(i):
        print('*',end='')
    print()
for x in range(1,9):
    for y in range(x):
        print('*' , end='')
    print() """

for i in range(10):
    if i==5:
        continue
    else :
        print("gh",i)
    #print(i)