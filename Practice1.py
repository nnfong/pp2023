students = []   # list of tuples (name, id)
marks = {}      # dict of dicts {id: {subject: mark}}

def add_student():
    name = input("Enter student name: ")
    id = input("Enter student ID: ")
    students.append((name, id))

    marks[id] = {}  # initialize empty dict for student's marks
    num_subjects = int(input("Enter number of subjects: "))
    for i in range(num_subjects):
        subject = input("Enter subject name: ")
        mark = float(input("Enter mark for {}: ".format(subject)))
        marks[id][subject] = mark

def remove_student():
    id = input("Enter student ID: ")
    for i, student in enumerate(students):
        if student[1] == id:
            del students[i]
            del marks[id]
            print("Student removed")
            return
    print("Student not found")

def display_records():
    for name, id in students:
        print(name, "-", id)
        for subject, mark in marks[id].items():
            print(subject, "-", mark)
        print()

while True:
    print("Enter 1 to add a student")
    print("Enter 2 to remove a student")
    print("Enter 3 to display all records")
    print("Enter 4 to exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        add_student()
    elif choice == 2:
        remove_student()
    elif choice == 3:
        display_records()
    elif choice == 4:
        break
    else:
        print("Invalid choice")
