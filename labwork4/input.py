#Input.py
import math
import numpy as np
import curses 
from domain.std import *
from domain.course import *
from domain.grade import *
T_pain=curses.initscr()
curses.start_color()

def numberofstd():
        while True:
            T_pain.addstr("Enter the number of std in  class:")
            T_pain.refresh()
            std_class=int(T_pain.getstr().decode())
            if(std_class<=0):
                curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                T_pain.addstr("Does not exits!!!\n", curses.color_pair(1))
                T_pain.refresh()
                curses.napms(3000)
                T_pain.clear()
                T_pain.refresh()
            else:
                return std_class
#Create func & add-std-info into this func
def add_std_infor():
    T_pain.addstr("Enter the ID:")
    T_pain.refresh()
    id=T_pain.getstr().decode()

    T_pain.addstr("Enter the std name:")
    T_pain.refresh()
    name=T_pain.getstr().decode()

    T_pain.addstr("Enter the dob std:")
    T_pain.refresh()
    dob=T_pain.getstr().decode()

    st_infor=stds(id,name,dob)
    stdID.append(id)
    std.append(st_infor)
    T_pain.refresh()
    T_pain.clear()
    


#Create func to input num of course
def number_course():
    while True:
        T_pain.addstr("====NUMBER course===\n")
        T_pain.refresh()
        T_pain.addstr("Enter the number of course are:")
        T_pain.refresh()
        number_course=int(T_pain.getstr().decode())
        if(number_course<=0):
            curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
            T_pain.addstr("Does not exits!!!\n", curses.color_pair(1))
            T_pain.refresh()
            curses.napms(3000)
            T_pain.clear()
            T_pain.refresh()
            
        else:
            return number_course

#Create func to add course         
def add_course():
    T_pain.addstr("Enter the name course:")
    T_pain.refresh()
    name=T_pain.getstr().decode()
    
    T_pain.addstr("Enter the ID course:")
    T_pain.refresh()
    id=T_pain.getstr().decode()

    T_pain.addstr("Enter the credits are:")
    T_pain.refresh()
    credit_course=T_pain.getstr().decode()

    course_f=courses(name,id,credit_course)
    course.append(course_f)
    credit.append(credit_course)
    courseID.append(id)
    T_pain.refresh()
    T_pain.clear()


#Create grade for stds
def grade_mana(): 
    for i in range(0,len(std)):
        T_pain.clear()
        T_pain.addstr("Enter the ID std:")
        id_std=T_pain.getstr().decode()
        T_pain.refresh()
        if id_std in stdID:
            for j in range(0,len(course)):
                T_pain.addstr("Enter the ID course:")
                id_course= T_pain.getstr().decode()
                T_pain.refresh()
                if id_course in courseID:
                    T_pain.addstr("Enter the grade of std:")
                    grade=math.floor(float(T_pain.getstr().decode()))
                    T_pain.refresh()
                    if (grade<0) or (grade>20):
                        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
                        try:
                            T_pain.addstr("Faild\n",curses.color_pair(1))
                        except curses.error:
                            pass
                        T_pain.refresh()
                        curses.napms(2000)
                        T_pain.clear()
                        T_pain.refresh()
                        T_pain.addstr("Try again\n")
                        grade=math.floor(float(T_pain.getstr().decode()))
                   
                else:
                    exit()
        else:
            exit()                

    infor_grade=grades(id_std,id_course,grade)
    grade.append(infor_grade)
    gpa_d.append(grade)
 

def aver_gpa():
    var=np.array([gpa_d])
    cred=np.array([credit])
    T_pain.addstr("Enter name std that you want to calculate GPA:")
    name =T_pain.getstr().decode()
    if name in std:
        for i in range(len(grade)):
            recallcre=np.sum(cred)
            recallvar=np.sum(np.multiply(var,cred))
            T_pain.refresh()
            Gpa=recallvar/recallcre
            T_pain.refresh()                
    else: 
        return 0

    gpa_s.append(Gpa)
    T_pain.refresh()

    for st_infor in grade:
        T_pain.clear()
        T_pain.refresh()
        T_pain.addstr(" grade_stdid: %s   Gpa:%s \n" %(st_infor.get_id_course(), Gpa))
        T_pain.refresh()

        break