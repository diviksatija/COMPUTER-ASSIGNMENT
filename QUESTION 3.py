#QUESTION 3
Student_Details = []
SID = int(input("Enter SID: "))
Student_Details.append(SID)

Name = str(input("Enter Name: "))
Student_Details.append(Name)

Gender = str(input("Enter Gender from 'F', 'M' or 'U': "))
Student_Details.append(Gender)

Course_Name = str(input("Enter Course Name: "))
Student_Details.append(Course_Name)

CGPA = float(input("Enter CGPA: "))
Student_Details.append(CGPA)

print("Student Details :", Student_Details)
