#Q1
#python function to solve the problem of tower of
#Hanoi with three disks
#Defining a function with use of recursion
def TowerOfHanoi(n , Tower1, Tower3, Tower2):
	if n == 0:
		return 0
	TowerOfHanoi(n-1, Tower1, Tower2, Tower3)
	print("Move disk",n,"from rod",Tower1,"to rod",Tower3)
	TowerOfHanoi(n-1, Tower2, Tower3, Tower1)
n = 3
TowerOfHanoi(n, 'A', 'C', 'B')
print("\n")

#QUESTION 2
#python program to print the Pascal’s triangle for n number of
#rows given by the user using both recursive and iterative procedures

from math import factorial, remainder
from tracemalloc import start
n=int(input('Enter the size of pascals triangle\n'))

print("USING LOOPS")

for i in range(n):
	for j in range(n-i+1):
		print(end=" ") #for spacing

	for j in range(i+1):
		print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")	# nCr = n!/((n-r)!*r!)
	print()	# for new line
print("\n\n")

print("USING RECURSSIONS")

def pascal_triangle(n,originalength=n):
    if n == 0:
        return
    pascal_triangle(n-1,originalength)
    #printing the spaces
    print('  '*(originalength-n), end='')

    #first number is always 1
    start = 1
    for i in range(1, n+1):

        print(start, end ='   ')
        
        #using Binomial Coefficient
        start = start * (n - i) // i
    print()
pascal_triangle(n)
print("\n")


#QUESTION 3


int1=int(input("Enter first number\n"))
int2=int(input("Enter second number\n"))
Quotient = int1 // int2
Remainder = int1 % int2

#part <a>
print("a. Checking if the quotient and remainder is a callable value or not.")
print(callable(Quotient))
print(callable(Remainder))

#part <b>
if (Quotient == 0):
    print("<b> The quotient is zero")
if (Remainder == 0):
    print("<b> The reminder is zero")
if (Quotient != 0 and Remainder != 0):
    print("<b> All the values are non zero")

#part <c>
partClist = [Quotient + 4, Remainder + 4, Remainder + 5, Quotient + 5, Remainder + 5, Quotient + 6, Remainder + 6]

result = []
for i in range(len(partClist)):
    if partClist[i] > 4:
        result.append(partClist[i])
print(f"<c> Filtered out numbers that are greater than 4 are : {result}")

#part <d>
setresult = set(result)
print("<d> Set:",setresult)

#part <e>
immutableSet = frozenset(setresult) #frozen Set is used to make the set immutable
print("<e> Immutable set:",immutableSet)

#part <f>
print("<f> Hash value of the max value from the above set:", hash(max(immutableSet)))
print("\n")


#QUESTION 4

class Student:
    def __init__(self, student,roll_no):
        self.name = student
        self.roll_no = roll_no
    
    def __del__(self):
        print("Object destroyed")

#creating object
student1 = Student("Divik", 21104058)
print("Object created")
#printing the assigned values
print(f"The name of the student it {student1.name} and SID is {student1.roll_no}.")
#deleting object
del student1
print("\n")



#QUESTION 5
#Python program to store details of three employees: name and salary
#using class.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary 
#creating employee records
employee1 = Employee("Mehak", 40000)
employee2 = Employee("Ashok", 50000)
employee3 = Employee("Viren", 60000)

#part <a> updating salary
employee1.salary = 70000
print(f"<a> The updated salary of {employee1.name} is {employee1.salary} ")
#part <b> deleting a record
print("<b>Record of Viren deleted", end='')
del employee3
print("\n")

#QUESTION 6

a=str(input("George's word."))
a=a.lower()
b=str(input("Barbie's word. "))
b=b.lower()
list1=[]
list2=[]
for i in range(len(a)):
    list1.append(a[i:i+1])
for i in range(len(b)):
    list2.append(b[i:i+1])
list1=sorted(list1)
list2=sorted(list2)
if len(a)!=len(b):
    print("Friendship is fake.")
else:
    count=0
    for i in range(len(a)):
        if list1[i]==list2[i]:
            count=count+1
    if count==len(list1):
        print("Friendship is true.")
    else:
        print("Friendship is fake.")
