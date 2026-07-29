s={}
m=[]
s["name"]=input("enter name")
s["roll"]=int(input("enter roll no"))
for i in range(5):
    m.append(float(input(f"enter {i+1} subject marks ")))
s["marks of 5 sub"]=m
for key,value in s.items():
    print(f"{key}:{value}")
print("total marks",sum(m))
print("average marks",sum(m)/len(m))
a=sum(m)/len(m)
if a>= 90:
    print("Grade is A")
elif a >= 80:
    print("Grade is B")
elif a >=70:
    print("Grade is C ")
elif a>=50: 
    print("Pass")
else:
    print("Fail")
#for n no.of students
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i+1}")

    name = input("Name: ")
    roll = input("Roll Number: ")

    marks = []
    for j in range(5):
        mark = float(input(f"Enter Subject {j+1} marks: "))
        marks.append(mark)

    total = sum(marks)
    average = total / 5

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    student = {
        "Name": name,
        "Roll": roll,
        "Marks": marks,
        "Total": total,
        "Average": average,
        "Grade": grade
    }

    students.append(student)

print("\n========== STUDENT DETAILS ==========")

for student in students:
    print("\n-------------------------")
    for key, value in student.items():
        print(f"{key}: {value}")