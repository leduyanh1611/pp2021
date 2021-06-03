class Student:
    def __init__ (self,id, name, dob):
        self.id = id
        self.sname = name
        self.dob = dob
        self.course_n = 0 #number of course
        self.course_l = []#list of course
        self.grade =[]    #mark of stud

    def get_id(self):
        return self.id
    def set_id(self,id):
        self.id = id

    def get_name(self):
        return self.name
    def set_name(self,name):
        self.named = name

    def get_dob(self):
        return self.dob
    def set_dob(self,dob):
        self.dob = dob

    def input(self):
        self.name = input("Enter student name: ")
        self.id = input("Enter student ID: ")
        self.dob = input("Enter student dob: ")

    def __str__(self):
        return  "Student name: {self.name}"
                "Student ID: {self.ID}"
                "Student dob: {self.dob}"

    def describe(self):
        print(self.__str__())

class Course:
    def __init__(self, course_n, course_id, course_l)
        self.course_n = course_n
        self.course_id = course_id
        self.course_l = course_l
