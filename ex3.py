import numpy as np

grade_size = 10
grade_id_pos = 0
grade_name_pos = 1
grade_n_pos = 2

class Student:
    def __init__(self,id,name,dob):
        self.id = id
        self.sname = name
        self.dob = dob
        self.course_n = 0
        self.course_l = []
        self.grade = [[0 for m in range(grade_size)] for n in range(grade_size)]

    def get_id(self):
        return f"{self.id}"

    def add_course(self,course):
        self.grade[self.course_n][grade_id_pos] = course.id
        self.grade[self.course_n][grade_name_pos] = course.cname
        self.grade[self.course_n][grade_n_pos] = 3
        self.course_n += 1
        self.course_l.append(course.cname)

    def print_course(self):
        return print(self.course_l)

    def push_grade(self,course,val):
        i=0    
        while True:
            if self.grade[i][grade_id_pos]==course.id:
                break
            else:
                if i<self.course_n:
                    i+=1
                else:
                    return print("course not found")
        n=self.grade[i][grade_n_pos]    
        self.grade[i][n] = val
        self.grade[i][grade_n_pos] += 1


    def pop_grade(self,course):
        i=0
        while True:
            if self.grade[i][grade_id_pos]==course.id:
                break
            else:
                if i<self.course_n:
                    i+=1
                else:
                    return print("course not found")
        self.grade[i][grade_n_pos] -= 1            

    def print_grade(self):
        for i in range(0,self.course_n):
            print("Course: ",self.grade[i][grade_name_pos],". Grade: ", end = "")
            if (self.grade[i][grade_n_pos]==grade_n_pos+1):
                print("no grade yet")
            else:
                for j in range(grade_n_pos+1,self.grade[i][grade_n_pos]):
                    print(self.grade[i][j], end = "; ")
            print();

    def course_avg(self,course):
        i=0
        sum=0    
        while True:
            if self.grade[i][grade_id_pos]==str(course):
                break
            else:
                if i<self.course_n:
                    i+=1
                else:
                    return print("course not found")
        for j in range(grade_n_pos+1,self.grade[i][grade_n_pos]):
            sum+=self.grade[i][j]
            avg=np.round(float(sum/(int(self.grade[i][grade_n_pos])-grade_n_pos-1)),decimals=1)
        return f"Student:{self.sname}, average {self.grade[i][grade_name_pos]}: "+str(avg)

    def get_gpa(self):
        sum=0
        n=0
        total_sum=0
        for i in range(self.course_n):
            if self.grade[i][grade_n_pos]!=3:
                for j in range(grade_n_pos+1,self.grade[i][grade_n_pos]):
                    sum+=self.grade[i][j]
                    n+=1
            if n!=0:
                print(total_sum)
                total_sum+=float(sum/n)
        gpa=np.round(total_sum/self.course_n,decimals=1)
        
        return f"Student:{self.sname}, GPA: "+str(gpa)


class Course:
    def __init__(self,id,name):
        self.id = id
        self.cname = name
        self.student_n = 0
        self.student_l = []
        self.grade = [[0 for m in range(grade_size)] for n in range(grade_size)]
    
    def __str__(self):
        return f"{self.id}"

    def add_student(self,student):
        self.grade[self.student_n][grade_id_pos] = student.id
        self.grade[self.student_n][grade_name_pos] = student.sname
        self.grade[self.student_n][grade_n_pos] = 3
        self.student_n += 1
        self.student_l.append(student.sname)

    def print_student(self):
        return print(self.student_l)

    def push_grade(self,student,val):
        i=0    
        while True:
            if self.grade[i][grade_id_pos]==student.id:
                break
            else:
                if i<self.student_n:
                    i+=1
                else:
                    return print("student not found")
        n=self.grade[i][grade_n_pos]    
        self.grade[i][n] = val
        self.grade[i][grade_n_pos] += 1


    def pop_grade(self,student):
        i=0
        while True:
            if self.grade[i][grade_id_pos]==student.id:
                break
            else:
                if i<self.student_n:
                    i+=1
                else:
                    return print("student not found")
        self.grade[i][grade_n_pos]-=1            

    def print_grade(self):
        for i in range(0,self.student_n):
            print("student: ",self.grade[i][grade_name_pos],". Grade: ", end = "")
            if (self.grade[i][grade_n_pos]==grade_n_pos+1):
                print("no grade yet")
            else:
                for j in range(grade_n_pos+1,self.grade[i][grade_n_pos]):
                    print(self.grade[i][j], end = "; ")
            print();


            



def main():
    stud1 = Student('BI9-034', 'LeDuyAnh', '16/11/2000')
    stud2 = Student('123-546', 'abcdef', '11/22/3333')
    stud3 = Student('678-987', 'ghijkl', '44/55/6666')

    cour1 = Course('PY', 'Python')
    cour2 = Course('OOP', 'Object Oriented programming')

    stud1.add_course(cour1)
    stud1.add_course(cour2)
    cour1.add_student(stud1)
    cour2.add_student(stud1)
    print("---")
    stud1.push_grade(cour1,4)
    cour1.push_grade(stud1,4)
    stud1.push_grade(cour1,20)
    cour1.push_grade(stud1,20)
    print(stud1.course_avg(cour1))
    print(stud1.get_gpa()) 
    print("---")

    stud1.push_grade(cour2,5)
    cour2.push_grade(stud1,5)
    stud1.push_grade(cour2,8)
    cour2.push_grade(stud1,8)
    print(stud1.course_avg(cour2))
    print(stud1.get_gpa())   

main()