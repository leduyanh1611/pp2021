import math
import numpy as np
import curses 
from zipfile import ZipFile
import os
from domain.std import *
from domain.course import *
from domain.grade import *
from input import number_course,numberofstd,add_course,add_std_infor,grade_mana,aver_gpa
from output import gpa_decending,show_course,show_std,show_grade
T_pain=curses.initscr()
curses.start_color()
class mains():
    s=int(numberofstd())
    for i in range(0,s):
        add_std_infor()
    show_std()
    c=int(number_course())
    for i in range(0,c):
        add_course()
    show_course()
    grade_mana()
    aver_gpa()
    T_pain.refresh()
    T_pain.clear()
    while True:
        T_pain.addstr("""=====option=====\n""")
        T_pain.addstr("1.view std grade\n")
        T_pain.addstr("2.Comp data:\n")
        T_pain.addstr("3.Decomp data:\n")
        T_pain.addstr("4.null\n")
        T_pain.refresh()
        ol = int(T_pain.getstr().decode())
        if ol == 1:
            T_pain.clear()
            T_pain.addstr("std's grade:\n")
            T_pain.refresh()
            T_pain.clear()
            curses.napms(2000)
            show_grade()
            T_pain.addstr("std's gpa\n")
            T_pain.refresh()
            curses.napms(2000)
            gpa_decending()
        if ol==2:
            listfile=['std.txt','courses.txt','grade.txt']
            with ZipFile('std.dat','w') as zip_fs:
                for filename in listfile:
                    zip_fs.write(filename)
                for filename in listfile:
                    os.remove(filename)    
        if ol==3:
            if os.path.isfile('std.dat'):
                zip_file=ZipFile('std.dat','r')
                zip_file.extractall()
                if os.path.isfile('std.txt'):     
                    s = open('std.txt', 'r').readline()
                if os.path.isfile('courses.txt'):    
                    c = open('courses.txt', 'r').readline()
                if os.path.isfile('grade.txt'):      
                    m = open('grade.txt', 'r').readline()
        elif ol==4:
            T_pain.addstr("end.")
            curses.napms(2000)
            curses.endwin()
            exit()
mains()