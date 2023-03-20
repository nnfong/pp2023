class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Mark:
    def __init__(self, student, course, value=0):
        self.student = student
        self.course = course
        self.value = value

class Classroom:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []

    def input(self):
        num_students = int(input("Enter number of students: "))
        for i in range(num_students):
            id = input(f"id of student {i+1} is: ")
            name = input(f"Name of student {i+1} is: ")
            dob = input(f"DoB of student {i+1} is: ")
            student = Student(id, name, dob)
            self.students.append(student)

        num_courses = int(input("Enter number of courses: "))
        for i in range(num_courses):
            id = input(f"id of course {i+1} is: ")
            name = input(f"Name of course {i+1} is: ")
            course = Course(id, name)
            self.courses.append(course)

        for student in self.students:
            for course in self.courses:
                mark = Mark(student, course)
                self.marks.append(mark)

        while True:
            test = int(input("Input 1 to continue or Input 0 to quit: "))
            if test == 1:
                student_name = input("Choose a student: ")
                course_name = input("Choose a course: ")
                value = int(input(f"Enter mark of {student_name} in {course_name} is: "))
                for mark in self.marks:
                    if mark.student.name == student_name and mark.course.name == course_name:
                        mark.value = value
                        break
                else:
                    print("Invalid student or course name, try again!")
            elif test == 0:
                break
            else:
                print("Invalid value, try again!")

    def list(self):
        print(f"There are {len(self.courses)} course(s) include:")
        for course in self.courses:
            print(course.name)

        print(f"There are {len(self.students)} student(s) include:")
        for student in self.students:
            print(student.name)

        while True:
            course_name = input("Choose a course: ")
            course_found = False
            for course in self.courses:
                if course.name == course_name:
                    course_found = True
                    break
            if not course_found:
                print("Invalid course name, try again!")
                continue
            for mark in self.marks:
                if mark.course.name == course_name:
                    print(f"Mark of {mark.student.name} in {mark.course.name} is {mark.value}")

if __name__ == '__main__':
    classroom = Classroom()
    classroom.input()
    classroom.list()
