#January 12
#task 1
x=input("Enter first number ")
y=input("Enter second number ")
z=input("Enter third number ")

if x>y and x>z:
    print(f"x {x} is the largest")
elif y>x and y>z:
    print(f"b {y} is the largest")
else:
    print(f"z {z} is the largest")

#task 2
a=float(input("Enter first member CGPA "))
b=float(input("Enter second member CGPA "))
c=float(input("Enter third member CGPA "))

if a<b and a<c:
    print(f"Member 1 has the lowest CGPA: {a}")
elif b<a and b<c:
    print(f"Member 2 has the lowest CGPA:  {b}")
else:
    print(f"Member 3 has the lowest CGPA: {c} ")
z=a+b+c
avg=z / 3 
print(f"The average of the three members CGPA is: {avg}")

#task 3
m = 10  #binary: 0000 1010
x=~m    #binary: 1111 0101 = -11
print(f"binary not operation result {x}")
