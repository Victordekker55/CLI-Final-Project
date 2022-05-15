import curses
from curses.textpad import Textbox
from encodings import utf_8
import time
import random


#Variable str's
myMenu = ["Login", "Create Account", "Exit"]
myTitle = "Welcome to suedibank" 
subtitle = "Beta version"
footer = "Written by Victor Dekker                           Press q to exit                        Press a random key to refresh"
myList = ["1"]



#Cool humanized writing
def run_slow(stdscr, the_string):
    x = 0
    
    for char in the_string:
        x += 1
        curses.delay_output(20)
        stdscr.addstr(0,x, char)
        stdscr.refresh()
    stdscr.getch()


def login_page(stdscr, username):
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    h,w = stdscr.getmaxyx()
    max_y = h//2
    max_x = w//2
    
    
    footerfiller = " " * (w-len(footer)-1)

    stdscr.attron(curses.color_pair(1))
    stdscr.addstr((h-1), 0, footer)
    stdscr.addstr((h-1), len(footer), footerfiller)
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    moneycount = 0

    while True:
        mainkey = stdscr.getkey()
        
        
        moneytxt = "Money added"
        ran_y = random.randrange(0,h)
        ran_x = random.randrange(0,w)

        with open("resource.txt", "r+") as f:
            for line in f.readlines():
                attr = line.split("/")
                money = attr[2]
                

                stdscr.addstr(1,1,f"Nice to have you here {username}, you have {money} btc in your wallet press + to add btc")
                stdscr.addstr(max_y, max_x, f"BTC Wallet:{money}")
                stdscr.refresh()

        if mainkey == "+":
            
            moneycount += 1
            
            with open("resource.txt", "r") as file:
                s_text = f"{money}"
                r_text = f"{moneycount}"
                read = file.read()
                changed = read.replace(s_text, r_text)
                
            with open("resource.txt", "w") as file:
                file.write(changed)

            stdscr.addstr(ran_y, ran_x, moneytxt)
            

        if mainkey == "q":
            return main(stdscr)

        stdscr.refresh()




def main(stdscr):
    #creating diffrent color sets
    curses.curs_set(0)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    stdscr.clear()
    row_id = 0
    h, w = stdscr.getmaxyx()
    loop = True

    while loop:
        #rendering menu
        menu(stdscr, row_id)
        #getting key inputs from the screen
        key = stdscr.getkey()
        #showing user key inputs on screen
        stdscr.addstr(7,2,f"Key{key}")
        stdscr.refresh()
        #checking which key is pressed to navigate in menu
        if key == "s":
            row_id += 1
        if key == "w":
            row_id -= 1
        if row_id < 0 or row_id > 3:
            row_id = 0
        #break the loop by pressing q
        if key =="q":
            loop = False
        
        #checking if 
        if key == ("a" or "d") and row_id == 0:
            stdscr.clear()
            txt_list = []
            user_list = []
            with open("resource.txt", "r", encoding="utf8") as r:
                for line in r.readlines():
                    attr = line.split("/")
                    user_name = attr[0]
                    user_password = attr[1]

                    stdscr.addstr(20,((w-w)+1), f"user:{user_name}")
                    stdscr.addstr(21,((w-w)+1), f"pass:{user_password}")

                    stdscr.refresh()
            run_slow(stdscr, "Login Page - Type in user/pass form, CTRL+G to sumbit")
            win2 = curses.newwin(2,15,3,3)
            box2 = Textbox(win2)            
            stdscr.refresh()
            box2.edit()
            txt_login = box2.gather()
            txt_list.append(txt_login)
            txt_list = list(map(lambda x: x.replace("\n", ""), txt_list))

            stdscr.refresh()
            with open("resource.txt", "r") as f:
                for line in f.readlines():
                    pos = line.split("/")
                    user_login = pos[0]
                    pass_login = pos[1]
                    pass_login = pass_login + " "
                    
                user_list.append(f"{user_login}/{pass_login}")

            if txt_list == user_list:
                
                stdscr.addstr(10,9,"logging in...")
                time.sleep(1)
                stdscr.refresh()
                login_page(stdscr, user_login)
                
                        
            else:
                stdscr.addstr(8,9, f"input:{txt_list}")

                stdscr.addstr(9,9,(f"pass:{user_list}"))
           
        if key == ("a" or "d") and row_id == 1:
            stdscr.clear()
            key2 = stdscr.getch()
            
            run_slow(stdscr, "Create password - Type in user/pass form, CTRL+G to save")
            win = curses.newwin(2,15,3,3)
            box = Textbox(win)            
            stdscr.refresh()
            box.edit()
            txt = box.gather()
            txt = txt.strip().replace("\n", "")
            txt = txt + "/0"
            stdscr.addstr(10,10, txt)
            stdscr.refresh()
            with open("resource.txt", "w", encoding="utf8") as file:
                for i in txt:                    
                    file.write(i)
                file.write("\n")
                stdscr.addstr(12,12, "Account has been created")
                stdscr.refresh()
                time.sleep(2)
            stdscr.clear()    
            
                    
def menu(stdscr, row_id):
    
    h, w = stdscr.getmaxyx()
    max_y, max_x = stdscr.getmaxyx()
    #filler for footer
    footerfiller = " " * (w-len(footer)-1)
    #creating header & subtitle
    header = stdscr.subwin(1, (max_x//2)-(len(myTitle)//2))
    subheader = stdscr.subwin(2, (max_x//2)-(len(subtitle)//2))
    #rendering header
    header.attron(curses.color_pair(3))
    header.addstr(myTitle)
    header.attroff(curses.color_pair(3))
    header.refresh()
    #rendering subtitle
    subheader.attron(curses.color_pair(2))
    subheader.addstr(subtitle)
    subheader.attroff(curses.color_pair(2))
    subheader.refresh()


    #rendering footer
    stdscr.attron(curses.color_pair(1))
    stdscr.addstr((h-1), 0, footer)
    stdscr.addstr((h-1), len(footer), footerfiller)

    stdscr.attroff(curses.color_pair(1))


    # with open("resource.txt", "r", encoding="utf8") as r:
    #     for line in r.readlines():
    #         if len(line) != 0:
    #             attr = line.split("/")
    #             user_name = attr[0]
    #             user_password = attr[1]
    #             stdscr.addstr(20,((w-w)+1), f"user:{user_name}")
    #             stdscr.addstr(21,((w-w)+1), f"pass:{user_password}")
    #             stdscr.refresh()
    #         else:
    #             stdscr.addstr(20,((w-w)+1),"No user/pass")
    
    #creating menu with enumerate so u get 2 values, count is for which count in the list its on and row is the str in the list.
    for count, row in enumerate(myMenu):
        #centering menu
        x = w//2 - len(row)//2
        y = h//2 - len(myMenu) + count
        
        if count == row_id:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x, row, curses.A_STANDOUT)
            stdscr.attroff(curses.color_pair(1))
        elif count != row_id:
            stdscr.addstr(y,x,row)  
    # refreshing screen
    stdscr.refresh()
        

curses.wrapper(main)




