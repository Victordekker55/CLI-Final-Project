import curses
import time


def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.addstr(5,5, "Helloworld")
    stdscr.refresh()
    time.sleep(5)

curses.wrapper(main)


