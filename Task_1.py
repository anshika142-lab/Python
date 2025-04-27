Students = {"Chandler":85 ,"Bob":92 ,"Charlie": 78,"Diana":90,"Ethan": 88}
student_name=input("Enter the student's name : ")
if student_name in Students:
    print (f"{student_name}'s marks: {Students[student_name]}")
else:
    print("Student not found")