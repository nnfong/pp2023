import math

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
                value = float(input(f"Enter mark of {student_name} in {course_name} is: "))
                value = math.floor(value * 10) / 10.0
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
import numpy as np
from math import floor

class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
        self.marks = []

class Course:
    def __init__(self, id, name, credits):
        self.id = id
        self.name = name
        self.credits = credits

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
            credits = int(input(f"Credits of course {i+1} is: "))
            course = Course(id, name, credits)
            self.courses.append(course)

        for student in self.students:
            for course in self.courses:
                mark = Mark(student, course)
                student.marks.append(mark)
                self.marks.append(mark)

        while True:
            test = int(input("Input 1 to continue or Input 0 to quit: "))
            if test == 1:
                student_name = input("Choose a student: ")
                course_name = input("Choose a course: ")
                value = int(input(f"Enter mark of {student_name} in {course_name} is: "))
                for mark in self.marks:
                    if mark.student.name == student_name and mark.course.name == course_name:
                        mark.value = floor(value)
                        break
                else:
                    print("Invalid student or course name, try again!")
            elif test == 0:
                break
            else:
                print("Invalid value, try again!")

    def calculate_gpa(self, student):
        marks = []
        for mark in self.marks:
            if mark.student == student:
                marks.append(mark)
        if not marks:
            return 0.0
        weighted_sum = 0.0
        credit_sum = 0
        for mark in marks:
            weighted_sum += mark.value * mark.course.credits
            credit_sum += mark.course.credits
        gpa = np.average(weighted_sum/credit_sum, weights=credit_sum)
        return round(gpa, 1)

    def list(self):
        print(f"There are {len(self.courses)} course(s).")
        print(f"There are {len(self.students)} student(s).")
        for student in self.students:
            gpa = self.calculate_gpa(student)
            print(f"Student ID: {student.id}, Name: {student.name}, GPA: {gpa:.1f}")
        print("")

if __name__ == '__main__':
    classroom = Classroom()
    classroom.input()
    classroom.list()
class Student:
    def __init__(self, name):
        self.name = name

class Course:
    def __init__(self, name):
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

    def add_student(self, name):
        student = Student(name)
        self.students.append(student)

    def add_course(self, name):
        course = Course(name)
        self.courses.append(course)

    def add_mark(self, student_name, course_name, value):
        student = next((s for s in self.students if s.name == student_name), None)
        course = next((c for c in self.courses if c.name == course_name), None)
        if student and course:
            mark = Mark(student, course, value)
            self.marks.append(mark)
        else:
            print("Invalid student or course name, try again!")

    def calculate_gpa(self, student_name):
        student = next((s for s in self.students if s.name == student_name), None)
        if not student:
            print("Invalid student name, try again!")
            return
        student_marks = [m for m in self.marks if m.student == student]
        if not student_marks:
            print(f"No marks found for {student_name}")
            return
        total_points = 0
        total_credits = 0
        for mark in student_marks:
            total_points += mark.value * 3
            total_credits += 3
        gpa = total_points / total_credits
        print(f"The GPA for {student_name} is {gpa:.2f}")    
class Classroom:
    def calculate_gpa(self, student_name):
        student_marks = [mark for mark in self.marks if mark.student.name == student_name]
        total_credits = sum([mark.course.credit for mark in student_marks])
        weighted_sum = sum([mark.value * mark.course.credit for mark in student_marks])
        if total_credits == 0:
            return 0
        else:
            return weighted_sum / total_credits
classroom = Classroom()
gpa = classroom.calculate_gpa("ban a")
print(f"GPA for ban a is: {gpa}")