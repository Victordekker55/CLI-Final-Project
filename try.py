import curses
from curses.textpad import Textbox
import time
import sys


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
    row_id = 0
    menu(stdscr, row_id)
    loop = True
    while loop:
        global xstring
        xstring = 0
        xstring += 1
        kboard = stdscr.getch()
        key = stdscr.getkey()
        stdscr.addstr(5,5,f"Key: {key}")
        stdscr.refresh()
        stdscr.getch()
        if key == "1":
            #row_id -= 1
            stdscr.clear()

            stdscr.addstr(0,xstring,"Login, type pass below")
            win = curses.newwin(2,15,3,3)
            box = Textbox(win)
            stdscr.refresh()
            box.edit()
            stdscr.getch()
            txt = box.gather().strip().replace("\n", "")

            if kboard == "KEY_HOME":
                pass
        if key == "2":
            
                #row_id -= 1
                stdscr.clear()

                stdscr.addstr(0,xstring,"Create account by making pass below.")
                win = curses.newwin(2,15,3,3)
                box = Textbox(win)
                stdscr.refresh()
                box.edit()
                txt = box.gather().strip().replace("\n", "")
                stdscr.getch()
                if len(txt) > 0:
                    stdscr.clear()
                    with open("resource.txt", "w", encoding="utf8") as f:
                        for line in txt:
                            f.write(line)
                            stdscr.addstr(5,1,"Saved")
                            stdscr.refresh()


                stdscr.refresh()

            

            
        
        stdscr.refresh()
        time.sleep(2)


myMenu = ["1 - Login", "2 - Create Account", "3 - Exit"]
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
        


    time.sleep(1)


curses.wrapper(main)




