import curses
import time



MenyItems = ["Welcome to the bank", "Login", "Create account", "Exit"]
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


myMenu = ["Welcome To The Bank", "Login", "Create Account", "Exit"]


def menu(stdscr, row_id):
    stdscr.clear()
    h, w = stdscr.getmaxyx()
    
    for count, row in enumerate(myMenu):
        x = w//2 - len(row)//2
        y = h//2 - len(myMenu)//2 + count
        if count == row_id:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x, row, curses.A_STANDOUT)
            stdscr.attroff(curses.color_pair(1))
        else:
            stdscr.addstr(y,x,row)



        

    stdscr.refresh()
        


    time.sleep(5)


curses.wrapper(main)




