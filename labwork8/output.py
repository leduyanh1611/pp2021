import numpy as np
import curses 
from domain.std import *
from domain.course import *
from domain.grade import *
T_pain=curses.initscr()
curses.start_color()
def show_std():
        T_pain.addstr("std list\n")
        T_pain.refresh()
        for stds in std:
            T_pain.addstr("[ID-std: ] %s   [Name-std: ] %s    [DoB_std: ] %s\n" % (stds.get_id(),stds.get_name(),stds.get_dob()))
            T_pain.refresh()
def show_course():
        T_pain.addstr("course list\n")
        T_pain.refresh()
        for courses in course:
            T_pain.addstr("[ID-courses]: %s    [Name-course]: %s      [cre-course]: %s\n"%(courses.get_id(),courses.get_name(),courses.get_cre_course()))
            T_pain.refresh()
def show_grade():
        T_pain.addstr("grade list\n")
        T_pain.refresh()
        for grades in grade:
            T_pain.addstr("[ID-course]: %s      [ID-std]: %s       [grade]: %s\n"%(grades.get_id_course(),grades.get_id_course(),grades.get_grade()))
            T_pain.refresh()
def gpa_decending():
        arrr=np.array([gpa_s])
        arrr[::-1].sort()
        T_pain.addstr("list: \n"%(arrr))
        T_pain.refresh()