class Student:
    def __init__(self,id,name,dob):
        self.id = id
        self.sname = name
        self.dob = dob
        self.course_n = 0
        self.course_l = []
        self.grade =[]


    def add_course(self,course):
        self.course_n += 1
        self.course_l.append(course.cname)
    def print_course(self):
        return print(self.course_l)
    #def add_grade(self,course,val):
    #    self.grade[0][0] = course.id
    #    self.grade[0][1] = course.cname
    #    self.grade[0][2] += 1
    #    self.grade[0][3] = val
    #def print_grade(self):
    #    return self.grade

class Course:
    def __init__(self,id,name):
        self.id = id
        self.cname = name
        self.student_n = 0
        self.student_l = []

    def add_student(self,student):
        self.student_n += 1
        self.student_l.append(student.sname)

    def print_student(self):
        return print(self.student_l)

def main():
    stud1 = Student('BI9-034', 'LeDuyAnh', '16/11/2000')
    stud2 = Student('123-546', 'abcdef', '11/22/3333')
    stud3 = Student('678-987', 'ghijkl', '44/55/6666')

    cour1 = Course('PY', 'Python')
    cour2 = Course('OOP', 'Object Oriented programming')


    stud1.add_course(cour1)
    stud1.add_course(cour2)

    stud1.print_course()

    cour1.add_student(stud1)
    cour1.add_student(stud2)

    cour1.print_student()

    cour2.add_student(stud1)
    cour2.add_student(stud3)

    cour2.print_student()

    
    

main()