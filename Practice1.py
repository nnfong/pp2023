classroom = []
course = []
mark = []
a = None

NumberOfStudent = int(input("Enter number of students: "))
for x in range(NumberOfStudent):
    IdStudent = input(f"id of student {x+1} is: ")
    StudentName = input(f"Name of student {x+1} is: ")
    DoB = input(f"DoB of student {x+1} is: ")
    temp1 = {'StudentName': StudentName, 'IdStudent': IdStudent, 'DoB': DoB}
    classroom.append(temp1)

NumberOfCourse = int(input("Enter number of courses: "))
for x in range(NumberOfCourse):
    IdCourse = input(f"id of course {x+1} is: ")
    CourseName = input(f"Name of course {x+1} is: ")
    temp2 = {'CourseName': CourseName, 'IdCourse': IdCourse}
    course.append(temp2)

mark = [[0 for x in range(NumberOfStudent)] for x in range(NumberOfCourse)]

while True:
    test = int(input("Input 1 to continue or Input 0 to quit: "))
    if test == 1:
        TempStudent = input("Choose a student: ")
        TempCourse = input("Choose a course: ")
        count = 0
        check = 0
        for x in range(NumberOfCourse):
            if TempCourse == course[x]['CourseName']:
                count += 1
                a = x
        for x in range(NumberOfStudent):
            if TempStudent == classroom[x]['StudentName']:
                check += 1
                b = x

        if check == 0 or count == 0:
            print("Invalid, try again!")
        else:
            mark[a][b] = int(input(f"Enter mark of {classroom[b]['StudentName']} in {course[a]['CourseName']} is: "))
    elif test == 0:
        break
    else:
        print("Invalid value, try again!")

print(f"There are {NumberOfCourse} course(s) include:\n")
for x in range(NumberOfCourse):
    print(f"{course[x]['CourseName']}\n")

print(f"There are {NumberOfStudent} student(s) include:\n")
for x in range(NumberOfStudent):
    print(f"{classroom[x]['StudentName']}\n")

while True:
    CourseCheck = input("Choose a course: ")
    CheckCourse = 0
    for x in range(NumberOfCourse):
        if CourseCheck == course[x]['CourseName']:
            CheckCourse += 1
            c = x
    if CheckCourse == 0:
        print("Invalid course, try again!")
    else:
        for x in range(NumberOfStudent):
            print(f"Mark of {classroom[x]['StudentName']} in {course[c]['CourseName']} is {mark[c][x]}\n")
