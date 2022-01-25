#QUESTION 1
input="Python is a case sensitive language" #INPUT STRING

#PART(A)- LENGTH OF STRING
Lenth=len(input)
print(Lenth)

#PART(B)-REVERSING THE STRING
reverseinput=input[::-1]
print(reverseinput)

#PART(C)- STORING "a case sensitive" IN NEW STRING
sliced=input[10:26]
print(sliced)

#PART(D)- REPLACEMENT OF A PHRASE
replacedinput1=input.replace("a case sensitive", "object oriented")
print(replacedinput1)

#PART(E)- FINDING INDEX OF SUBSTRING "a" IN THE INPUT STRING
find=input.find("a")
print(find)

#PART(F)- REMOVING WHITE SPACES FROM THE INPUT STRING
replacedinput2=input.replace(" ","")
print(replacedinput2)

#QUESTION 2

#STORING NAME,SID,DEPARTMENT AND CGPA IN DIFFERENT VARIABLES
Name="Divik Satija"
SID=21104058
Department_Name="ELECTRICAL"
CGPA="9.9"

#PRINTING THE ABOVE DETAILS IN GIVEN FORMAT
print("Hey, %s Here!"%(Name))
print("My SID is %d"%(SID))
print("I am from %s department and my CGPA is %s"%(Department_Name,CGPA))




#QUESTION 3
a=56
b=10


#PART(A)
#56=111000
#10=001010
#a&b=001000
#a&b=8
print(a&b)

#PART(B)
#56=111000
#10=001010
#a|b=111010
#a|b=58
print(a|b)

#PART(C)
#56=111000
#10=001010
#a^b=110010
#a^b=50
print(a^b)

#PART(D)
a1=a<<2
#a1=11100000
#a1=224
b1=b<<2
#b1=101000
#b1=40
print(a1)
print(b1)

#PART(E)
a2=a>>2
#a2=001110
#a2=14
b2=b>>4
#b2=000000
#b2=0
print(a2)
print(b2)




#QUESTION 4

#INPUT THREE NUMBERS BY USER
num1=int(input("Enter the first number\n"))
num2=int(input("Enter the second number\n"))
num3=int(input("Enter the third number\n"))

if(num1>num2 and num1>num3):
   print("The largest number is ",num1)   #FIRST NUMBER IS LARGEST
elif(num2>num1 and num2>num3):
   print("The largest number is ",num2)   #SECOND NUMBER IS LARGEST
else:
   print("The largest number is ",num3)   #THIRD NUMBER IS LARGEST




#QUESTION 5

i=input("ENTER HERE\n") #INPUT FROM USER
b=i.find("name")  #USING FIND FUNCTION TO CHECK STRING "name"

if(b==-1):  #IF "name" NOT PRESENT
  print("NO")
else:       #IF "name" IS PRESENT
  print("YES")





#QUESTION 6
#FINDING IF TRIANGLE IS POSSIBLE OR NOT

#INPUT FROM USER
a=float(input("enter the length of first side\n"))
b=float(input("enter the length of second side\n"))
c=float(input("enter the length of third side\n"))

#CONVERTING FLOAT TO INTEGRAL VALUES
a=int(a)
b=int(b)
c=int(c)

if(a>=b+c or b>=a+c or c>= a+b): #CONDITION: IF SUM OF ANY TWO SIDES IS GREATER THAN THE THIRD SIDE
  print("NO")

else:
  print("YES")


  


















