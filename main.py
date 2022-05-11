import curses
from curses.textpad import Textbox
from encodings import utf_8
import time
import sys

def check_login(stdscr, password):
    with open("resource.txt", "r") as f:
        for line in f.readlines():
            attr = line.split("/")
            pass1 = attr[1]
            if password == pass1:
                return stdscr.addstr("Login success")
                login_page()
    
def login_page():
    pass

def print_slow(str):  #Humanized writing, action film vibe
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.008)

def main(stdscr):
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    stdscr.erase()
    row_id = 0
    menu(stdscr, row_id)
    h, w = stdscr.getmaxyx()
    key = stdscr.getkey()
    stdscr.refresh()
    stdscr.addstr(7,2,f"Key{key}")
    stdscr.refresh()
    

    while True:
        if key == "1":
            #row_id -= 1
            stdscr.clear()
            key2 = stdscr.getch()
            with open("resource.txt", "r", encoding="utf8") as r:
                for line in r.readlines():
                    attr = line.split("/")
                    user = attr[0]
                    password = attr[1]

                    stdscr.addstr(20,((w-w)+1), f"user:{user}")
                    stdscr.addstr(21,((w-w)+1), f"pass:{password}")

                    stdscr.refresh()
            stdscr.addstr(0,1,"Login, type pass below")
            win = curses.newwin(2,15,3,3)
            box = Textbox(win)
            stdscr.refresh()
            box.edit()
            stdscr.getch()
            txt = box.gather().strip().replace("\n", "")
            if key2 == curses.KEY_ENTER:
                check_login(txt)

            
           
        if key == "2":
                stdscr.clear()

                #row_id -= 1

                stdscr.addstr(0,1,"Create account by making pass below.")
                stdscr.refresh()
                
                win = curses.newwin(2,15,3,3)
                box = Textbox(win)             
                box.edit()
                txt2 = box.gather()
                txt2 = txt2.replace("\n", "")
                if len(txt) < 0 :
                    stdscr.addstr(5,5, "saving")
                    stdscr.refresh()
                    txt = box.gather()
                    txt = txt.replace("\n", "")
                    with open("resource.txt", "w", encoding="utf8") as f:
                        for line in txt:
                            f.write(line, "\n")
                    stdscr.addstr(5,1,"Saved")
                    stdscr.refresh()


        elif key == "q":
            return False        

            

            
        
        stdscr.refresh()


myMenu = ["1 - Login", "2 - Create Account", "q - Exit"]
myTitle = "Welcome to suedibank"


myList = ["1"]





def menu(stdscr, row_id):
    stdscr.clear()
    
    h, w = stdscr.getmaxyx()
    max_y, max_x = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    header = stdscr.subwin(1, (max_x//2)-(len(myTitle)//2))
   # header = stdscr.subwin(1, xstring)

    header.attron(curses.color_pair(3))
    header.addstr(myTitle)
    header.refresh()
    
    


    stdscr.refresh()
    for count, row in enumerate(myMenu):
        
        x = w//2 - len(row)//2
        y = h//2 - len(myMenu)//2 + count
        if count == row_id:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x, row, curses.A_STANDOUT)
            stdscr.attroff(curses.color_pair(1))
        elif count != row_id:
            stdscr.addstr(y,x,row)



        

    stdscr.refresh()
        




curses.wrapper(main)




