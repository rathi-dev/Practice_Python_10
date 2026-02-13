a= int(input("enter a number:"))
print("fibonacci series:")
num1=0
num2=1
c=0
print(num1)
print(num2)
while c<a:
    b=num1+num2
    print(b,end="")
    num1=num2
    num2=b
    c=c+1
