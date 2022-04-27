import curses
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
    row_id = 0
    menu(stdscr, row_id)
    loop = True
    while loop:
        kboard = stdscr.getch()
        stdscr.clear()

        if kboard == curses.KEY_DOWN:
            row_id += 1
            stdscr.addstr(0,0,"Downkey")

        stdscr.refresh()
        time.sleep(5)


myMenu = ["Login", "Create Account", "Exit"]
myTitle = "Welcome to suedibank"


myList = ["1"]

def menu(stdscr, row_id):
    stdscr.clear()

    h, w = stdscr.getmaxyx()
    max_y, max_x = stdscr.getmaxyx()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    
    header = stdscr.subwin(1, (max_x//2)-(len(myTitle)//2))

    header.attron(curses.color_pair(1))
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
        


    time.sleep(5)


curses.wrapper(main)




