import curses
from curses.textpad import Textbox
from encodings import utf_8
import time
import sys
import random


myMenu = ["--> - Login", "--> - Create Account", "q - Exit"]
myTitle = """
Welcome to suedibank 
W for up and S for down
Right arrow twice on selected option to continue
"""

myList = ["1"]


def run_slow1(stdscr):
    x = 0
    the_string = "Login Page - Type in user/pass form, CTRL+G to sumbit"
    for char in the_string:
        x += 1
        curses.delay_output(100)
        stdscr.addstr(0,x, char)
        stdscr.refresh()
    stdscr.getch()

def run_slow2(stdscr):
    x = 0
    the_string = "Create password - Type in user/pass form, CTRL+G to save"
    for char in the_string:
        x += 1
        curses.delay_output(100)
        stdscr.addstr(0,x, char)
        stdscr.refresh()
    stdscr.getch()


def check_login(stdscr, password):
    with open("resource.txt", "r") as f:
        for line in f.readlines():
            attr = line.split("/")
            pass1 = attr[1]
            if password == pass1:
                stdscr.addstr("Login success")
                
                login_page()

def login_page(stdscr, username):
    h,w = stdscr.getmaxyx()
    stdscr.addstr(((h-h)+1),((w-w)+1),f"Nice to have you here {username}")


def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    stdscr.erase()
    row_id = 0
    h, w = stdscr.getmaxyx()
    
    loop = True
    while loop:
        menu(stdscr, row_id)
        c = stdscr.getch
        key = stdscr.getkey()
        stdscr.addstr(7,2,f"Key{key}")
        stdscr.refresh()
        if key == "s":
            row_id += 1
        if key == "w":
            row_id -= 1
        if row_id < 0 or row_id > 3:
            row_id = 0
        if key == "q":
            loop = False
        
        if key == "KEY_RIGHT" and row_id == 0:
            stdscr.clear()
            key2 = stdscr.getch()
            with open("resource.txt", "r", encoding="utf8") as r:
                for line in r.readlines():
                    attr = line.split("/")
                    user_name = attr[0]
                    user_password = attr[1]

                    stdscr.addstr(20,((w-w)+1), f"user:{user_name}")
                    stdscr.addstr(21,((w-w)+1), f"pass:{user_password}")

                    stdscr.refresh()
            run_slow1(stdscr)
            win = curses.newwin(2,15,3,3)
            box = Textbox(win)            
            stdscr.refresh()
            txt = str(box.edit())
            stdscr.addstr(8,8, txt)
            stdscr.refresh()
            with open("resource.txt", "r") as f:
                for line in f.readlines():
                    pos = line.split("/")
                    user_login = pos[0]
                    pass_login = pos[1]
                    if txt == pass_login:
                        stdscr.addstr(9,11,"Login success, redirecting to login page.")
                        login_page(stdscr,user_login)
                    else:
                        stdscr.addstr(9,9,(pass_login))
           
        if key == "KEY_RIGHT" and row_id == 1:
            stdscr.clear()
            key2 = stdscr.getch()
            
            run_slow2(stdscr)
            win = curses.newwin(2,15,3,3)
            box = Textbox(win)            
            stdscr.refresh()
            txt = str(box.edit())
            txt = txt.strip().replace("\n", "")
            stdscr.addstr(10,10, txt)
            stdscr.refresh()
            with open("resource.txt", "w") as l:
                for i in txt:
                    l.write(i)
            stdscr.clear()
                    
def menu(stdscr, row_id):
    
    h, w = stdscr.getmaxyx()
    max_y, max_x = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    header = stdscr.subwin(1, (max_x//2)-(len(myTitle)//4))
   # header = stdscr.subwin(1, xstring)

    header.attron(curses.color_pair(3))
    header.addstr(myTitle)
    header.refresh()
    with open("resource.txt", "r", encoding="utf8") as r:
        for line in r.readlines():
            if len(line) != 0:
                attr = line.split("/")
                user_name = attr[0]
                user_password = attr[1]
                stdscr.addstr(20,((w-w)+1), f"user:{user_name}")
                stdscr.addstr(21,((w-w)+1), f"pass:{user_password}")
                stdscr.refresh()
            else:
                stdscr.addstr(20,((w-w)+1),"No user/pass")

    stdscr.refresh()
    for count, row in enumerate(myMenu):
        
        x = w//2 - len(row)//2
        y = h//2 - len(myMenu) + count
        if count == row_id:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x, row, curses.A_STANDOUT)
            stdscr.attroff(curses.color_pair(1))
        elif count != row_id:
            stdscr.addstr(y,x,row)  

    stdscr.refresh()
        

curses.wrapper(main)




