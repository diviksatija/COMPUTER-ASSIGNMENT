#QUESTION 1
#Python program to count the number of occurrences of each word or
#character in the string entered by the user.


input_value=input("Enter text here\n").lower().split()
if len (input_value)==1:
    input_value=input_value[0]
occurences ={}
for i in input_value:
    if i in occurences:
        occurences[i] +=1
    else:
        occurences[i]=1
print("the occurences of : ")
for i in occurences:
    print((i,occurences[i]))


#QUESTION 2
#Python program to print next date of input date

#Defining a function of leap year

def is_leap(year: int):                                                                                
    if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
while True:
    day= int(input("Enter the Day: "))
    month=int(input("Enter the Month: "))
    year=int(input("Enter the year: "))
    if (day < 1) or (day > 31) or (month < 1) or (month > 12) or (year < 1800) or (year > 2025):                  #Condition for given constraints in the question
        print("Data entered is out of range.")
        continue
    if month in (4,6,9,11) and day == 31:                                                                          #Condition for 31 days in a 30 day month
        print("The given month has only 30 days,\nPlease enter a valid date.")
        continue
    elif month == 2 and day >= 29:                                                                                 #Condition for no. of days in February
        if is_leap(year) and day != 29:
            print("The given month has only 29 days,\nPlease enter a valid date.")
            continue
        elif not is_leap(year):
            print("The given month has only 28 days,\nPlease enter a valid date.")
            continue
    break
if month == 2:                                                                                                      #Setting no. of days in the given month
    if is_leap(year):
        max_days = 29
    else:
        max_days = 28
elif month in (4,6,9,11):
    max_days = 30
else:
    max_days = 31
if day == max_days:                                                                                                #Syntax for incrementing the date
    day = 1
    if month == 12:
        month = 1
        year += 1
    else:
        month += 1
else:
    day += 1
#Printing the date.
date=f"{day}/{month}/{year}"
print("The Next Date is : ", date)
print()
print("-"*80)
print()



#QUESTION 3
#Python program to create a list of tuples with the first element as the
#number and Second element as the square of the number.Python program to create a list of tuples with the first element as the
#number and Second element as the square of the number.


lst = []
 
# number of elements as input
n = int(input("Enter number of elements in list : "))
 
# iterating till the range
for i in range(0, n):
    ele = int(input("enter the numbers in list\n"))
 
    lst.append(ele) # adding the element
     
res = [(val, pow(val, 2)) for val in lst]
  
# print the result
print("list-",lst)
print(res)





#QUESTION 4
#program to prompt the user for a grade between 4 and 10

score=int(input("Enter your grade\n"))
if(score<4 or score>10):
    print("error")
else:
    if(score==10):
        print("Your Grade is A+ and Outstanding Performance")
    elif(score==9):
        print("Your Grade is A and Excellent Performance")
    elif(score==8):
        print("Your Grade is B+ and Very Good Performance")
    elif(score==7):
        print("Your Grade is B and Good Performance")
    elif(score==6):
        print("Your Grade is C+ and Average Performance")
    elif(score==5):
        print("Your Grade is C and Below Average Performance")
    elif(score==4):
        print("Your Grade is D and Poor Performance")


#QUESTION 5
#Python program to print the pattern
n = 6

for i in range(n):
   
    for j in range(i):
        print(' ', end='')
  
    for j in range(2*(n-i)-1):
        print(chr(65 + j), end='')
    print()


#Q6
# To  store the Informationrmation of the students
print("Question 6")
Input = "Y"
SID_Information = {}

while Input == "Y":
    Name = input("Enter the Name of the Student:- ")
    SID  = int(input("Enter the SID of the Student:- "))
    SID_Information[SID] = Name

    while True:
        Input = input(
            "Type 'Y' if want enter another Student's Information or Type 'N' if don't want to Enter:- "
        ).upper()

        if Input == "Y" or Input =="N":
            break
        else:
            print("\nEnter The Correct Input")
    
    if Input == "N":
        break
    
#part a.) Print the dictionary
print(SID_Information)
##part c.) sort according to the SIDs
Sorted_SIDs = sorted(SID_Information.keys())
SID_Sort = {}

for sid in Sorted_SIDs:
    SID_Sort[sid] = SID_Information[sid]


#part b. sort according to the names
Sorted_Names = sorted(SID_Information.values())
Name_Sort = {}


def get_key(val, dicti):
    
    for key, value in dicti.items():
        if val == value:
            return key


for s_name in Sorted_Names:
    s_sid = get_key(s_name, SID_Sort)
    Name_Sort[s_sid] = s_name
#Printing the sorted Names
print(Name_Sort)
#Printing the sorted SIDs
print(SID_Sort)

while True:
    SID_Find = int(input("Enter the SID to find the name:- "))

    if SID_Find in SID_Information:
        print(SID_Information[SID_Find])
        break
    else:
        print("\nEnter the SID that is already in the list")

print()
print("-"*80)
print()


#Q7
#Python program to print Fibonacci sequence and average of the
#resultant Fibonacci series.


#Taking input for the terms required.
print("Question 7")
Total_Terms=int(input("Enter the number of fibonacci terms you want:- \n"))
First_Term=0
Next_Term=1
Nth_Term=0
Sum=0


#Using for loop to get the n terms

for i in range(1,Total_Terms+1):

    if(i==1):
        print(0)
    elif (i==2):
        print(1)
        Sum=Sum+1
    else:
        Nth_Term=First_Term+Next_Term
        Sum=Sum+Nth_Term
        print(Nth_Term)
        First_Term=Next_Term
        Next_Term=Nth_Term
print("The Average of the numbers is:-", float(Sum/Total_Terms))

print()
print("-"*80)
print()

#QUESTION 8
#Initializing the Sets


Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}
#a
a=(Set1.union(Set2)-Set1.intersection(Set2))
print(a)

#b
b=(Set1.union(Set2.union(Set3))-(Set1.intersection(Set2))-(Set2.intersection(Set3))-(Set1.intersection(Set3)))
print(b)

#c
c=((Set1.intersection(Set2))|(Set2.intersection(Set3))|(Set1.intersection(Set3)))-(Set1.intersection(Set2.intersection(Set3)))
print(c)

#d
d=set()
for i in range (1,11):
    if i not in Set1:
        d.add(i)
print(d)

e=set()
for i in range (1,11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        e.add(i)
        




