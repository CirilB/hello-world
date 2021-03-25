a=int(input("enter side 1:"))
b=int(input("enter side 2:"))
c=int(input("enter side 3:"))
s=(a+b+c)/2
x=s*(s-a)*(s-b)*(s-c)
A=x**0.5
print("Area of triangle is",A)
