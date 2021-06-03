grade=[]
gpa_s=[]
gpa_d=[]

class grades:
    def __init__(self,id_std,id_course,grade,gpa=0):
        self.id_std = id_std
        self.id_course = id_course
        self.grade=grade
        self.gpa=gpa
    def get_id_std(self):
        return self.id_std
    def get_id_course(self):
        return self.id_course
    def get_grade(self):
        return self.grade
    def get_Gpa(self):
        return self.Gpa
    def set_Gpa(self,Gpa):
        self.Gpa=Gpa