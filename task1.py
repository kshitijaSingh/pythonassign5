
student_details = {
    "Tina" : 95,
    "Ram": 90,
    "Gemini": 92,
    "Alice": 80,
    "Varun": 85,
    "Riya": 97,
    "Gopal": 75,
    "Domenic": 93
}

name = input("Enter the student's name : ")

if name in student_details:
    marks = student_details[name]
    print(f"{name}'s marks = {marks}")
else:
    print("Student's record not found.")

print("Get all details of students scoring between")
print("1.100 - 90")
print("2.90 - 80")
print("3.80 - 70")
print("4.70 - 60")
choice = int(input("Enter your choice : "))

if choice==1:
    print("Student's scoring between 90 and 100 :")
    for name, marks in student_details.items():
        if  90<=marks<=100:
            print(name)
if choice==2 :
    print("Student's scoring between 80 and 90:")
    for name, marks in student_details.items():
        if 80<=marks<=90:
            print(name)
if choice==3:
    print("Student's scoring between 70 and 80:")
    for name, marks in student_details.items():
        if 70<=marks<=80:
            print(name)
if choice==4:
    print("Student's scoring between 60 and 70:")
    found = False
    for name, marks in student_details.items():
        if 60<=marks<=70:
            print(name)
            found = True
    if not found:
        print("None")