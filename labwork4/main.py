import curses
from output import dp
from input import dp
from domain.std import * 
from domain.cousre import * 
from domain.grade import *
 
dhp= curses.initscr() 

def runcode():  
        dhp.addstr("Start Programming")
        Nco=dp.numcourses()
        dhp.refresh()
        for i in range( Nco):
            dhp.addstr(f"course { i+1}\n")
            dp.inputcourses()
            dhp.refresh()
            dhp.clear()
            Num=dp.numstd()
            dhp.refresh()
            for i in range(Num):
                dhp.addstr(f"std {i +1}:\n")
                dp.inputstd()
                dhp.clear()
                dhp.refresh()
                dp.grades() 
                dhp.clear()
                dhp.refresh()   
                break
        dp.gpa()
        dp.liststd()
        dp.listcourses()
        dp.listgrades()
        dp.gpadecending()                                              
             
if __name__ == '__main__':
    runcode()