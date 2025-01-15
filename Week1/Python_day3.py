#January 13

#task 1
print('Task 1 ')
n = 1
i = 0
while i < 3:
    j = 0
    while j < 3:
        print(n, end=" ")
        n += 1
        j += 1
    print()
    i += 1


#task 2 (a)
print('Task 2(a)')
for i in range(4):      
    for j in range(4):  
        print("*", end="") 
    print() 

#task 2 (b)
print('Task 2(b) ')
for i in range(4):        
    for j in range(i + 1):    
        print("*", end="")   
    print()               

#task 2 (c)
print('Task 2(c)')
for i in range(1, 4 + 1):  
    for j in range(i):    
        print(i, end=" ")  
    print()    

#task 2 (d)
print('Task 2(d)')
for i in range(4):  
    number = 1          
    for j in range(i + 1): 
        print(number, end=" ") 
        number += 2       
    print()     
