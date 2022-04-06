import curses
import time

from py import std


def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.addstr(5,5, "Helloworld")
    stdscr.refresh()
    time.sleep(5)


    while True:

        h,w = stdscr.getmaxyx()
        val = stdscr.getch()
        stdscr.clear()

        if val == curses.KEY_UP:
            stdscr.addstr((h//2), (w//2), "Down key ? ")
            

        stdscr.refresh()
curses.wrapper(main)




