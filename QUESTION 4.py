#QUESTION 4
Subjects = []
for i in range(5):
    print("Enter Marks for", i + 1,"th subject: ", end="")
    x = int(input())
    Subjects.append(x)
Subjects.sort()  
print("Sorted Order Of Marks for the Subjects are : ", Subjects)
