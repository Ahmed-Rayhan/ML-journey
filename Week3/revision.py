# Write a program to print 'Twinkle Twinkle Little Star' poem in python
print("Twinkle Twinkle little star")
print("How I wonder what you are")
print("Up above the world so high")
print("Like a diamond in the sky")

# Write a python program to find remainder when a number 'x' taken from user input is divided by another number 'y' which is also taken from user input
x = int(input("Enter x: "))
y = int(input("Enter y: "))
z = x % y
print(z)

# Write a python program to find average of 'n' numbers taken from user input
a = int(input("Enter how many numbers you want to average: "))
total = 0  
for i in range(a):
    total = total + int(input("Enter number: "))
average = total / a
print(average)

# Write a python program to find the square root and squared value of x taken from user input
import math
b = int(input("Enter a number: "))
print("Square root:", math.sqrt(b))
print("Squared value:", b * b)

# Write a program to detect if there are double spaces in a string and replace the double space with a single space
c = input("Enter a string: ")
if "  " in c:
    c = c.replace("  ", " ")
print("Modified string:", c)

# Write a program to store seven fruits in a list entered by the user
p = int(input("How many fruits? "))
fruits = []
for i in range(p):
    fruit = input(f"Enter fruit {i + 1}: ")
    fruits.append(fruit)
print("List of fruits:", fruits)

# Write a program to accept marks of 6 students and display them in a sorted manner and find out their average
marks = []
for i in range(6):
    m = float(input(f"Enter marks {i + 1}: "))
    marks.append(m)
sorted_marks = sorted(marks)
totalMarks = sum(marks)
avg = totalMarks / 6
print("Sorted marks:", sorted_marks)
print("Average marks:", avg)

# Write a python program to count the number of zeros in a list, L=[1,0,0,1,0,0,2,0,3,-5,0,0]
L = [1, 0, 0, 1, 0, 0, 2, 0, 3, -5, 0, 0]
count = 0
for f in L:
    if f == 0:
        count = count + 1
print("Number of 0:", count)

# Write a program to take user input of 8 numbers and count the unique numbers
numbers = []
o = int(input("How many numbers? "))
for i in range(o):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)
unique_numbers = set(numbers)
u_count = len(unique_numbers)
print("List of numbers:", numbers)
print("Unique numbers:", unique_numbers)
print("Number of unique numbers:", u_count)

# Create an empty dictionary, allow 4 friends to enter their favourite programming language as values and keys as their name. and display them. assume the names are unique
languages = {}
for i in range(4):
    name = input(f"Enter name of friend {i + 1}: ")
    l = input(f"Enter {name}'s favorite programming language: ")
    languages[name] = l
for name, l in languages.items():
    print(f"{name}: {l}")
