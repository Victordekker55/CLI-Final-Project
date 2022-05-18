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

with open("resource.txt", "r") as file:
    data = file.read()



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
    """_summary_

    Args:
        stdscr (Terminal value): Enables the function to control the cmd prompt screen
        username (str): Takes the username from the login input and welcomes the user that logged in 
    

    Returns:
        It returns the login page
    """
    #Clear the screen and dont show the inputs and enable
    stdscr.clear()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    #Get max height, width of screen
    h,w = stdscr.getmaxyx()
    #Centering calculation
    max_y = h//2
    max_x = w//2
    
    #Calcuting how much should be filled in the footer with white color
    footerfiller = " " * (w-len(footer)-1)
    #Enabling color for the footer
    stdscr.attron(curses.color_pair(1))
    #Rendering footer
    stdscr.addstr((h-1), 0, footer)
    stdscr.addstr((h-1), len(footer), footerfiller)
    #Disabling color
    stdscr.attroff(curses.color_pair(1))
    stdscr.refresh()
    moneycount = 0

    while True:
        #Get inputs from screen
        mainkey = stdscr.getkey()
        
        
        txtadd = "Money added"
        #Make random cordinates
        ran_y = random.randrange(0,h)
        ran_x = random.randrange(0,w)

        with open("resource.txt", "r+") as f:
            for line in f.readlines():
                attr = line.split("/")
                money = attr[2]
                money = int(money)
                moneytxt = f"{money}btc"

                stdscr.addstr(1,1,f"Nice to have you here {username}, you have {moneytxt} in your wallet press + to add btc")
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

            stdscr.addstr(ran_y, ran_x, txtadd)
            

        if mainkey == "q":
            return main(stdscr)

        stdscr.refresh()
def main(stdscr):
    """_summary_

    Args:
        stdscr (Terminal value): Enables the function to control the cmd prompt screen
    """
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
        
        #checking if a key is pressed and row id is on log in 
        if key == ("a" or "d") and row_id == 0:
        

            stdscr.clear()
            txt_list = []
            user_list = []
            with open("resource.txt", "r", encoding="utf8") as r:
                for line in r.readlines():
                    #Getting username and password with line.split
                    attr = line.split("/")
                    user_name = attr[0]
                    user_password = attr[1]
                    #Rendering the user and password for testing purposes, so you know if it works. Can be removed
                    stdscr.addstr(19,((w-w)+1), "Beta version, for test purposes, can be removed")

                    stdscr.addstr(20,((w-w)+1), f"user:{user_name}")
                    stdscr.addstr(21,((w-w)+1), f"pass:{user_password}")

                    stdscr.refresh()
            #Using humanized writing function, takes in a str
            run_slow(stdscr, "Login Page - Type in user/pass form, CTRL+G to sumbit")
            # Creating first a window a certain size, then making it a textbox
            win2 = curses.newwin(2,15,3,3)
            box2 = Textbox(win2)            
            stdscr.refresh()
            #Users can type in the textbox until CTRL+ G is pressed with .edit()
            box2.edit()
            #Takes the content of the textbox
            txt_login = box2.gather()
            #Putting the content into a list
            txt_list.append(txt_login)
            # Using lamba to replace \n in the list with blank space for the login system to work.
            txt_list = list(map(lambda x: x.replace("\n", ""), txt_list))
            
            stdscr.refresh()

            with open("resource.txt", "r") as f:
                #Readlines to read each line
                for line in f.readlines():
                    pos = line.split("/")
                    #Separate user and pass with line.split
                    user_login = pos[0]
                    pass_login = pos[1]
                    #Adding blank to pass because the input from the textbox adds an blank
                    pass_login = pass_login + " "
                #Putting it in a list
                user_list.append(f"{user_login}/{pass_login}")
            # checking if the input list equals to 
            if txt_list == user_list:
                
                stdscr.addstr(10,9,"logging in...")
                time.sleep(1)
                stdscr.refresh()
                login_page(stdscr, user_login)
                
                        
            else:
                stdscr.clear()
                stdscr.addstr(8,9,"Wrong credentials, shutting down")
                stdscr.refresh()
                time.sleep(3)
                loop = False
        if key == ("a" or "d") and row_id == 1: 
            stdscr.clear()
            #Using humanized funcion, takes str            
            run_slow(stdscr, "Create password - Type in user/pass form, CTRL+G to save")
            #Creating a subwindow as above
            win = curses.newwin(2,15,3,3)
            #Creating a textbox in that subwindow as above
            box = Textbox(win)            
            stdscr.refresh()
            box.edit()
            #Getting the content from the textbox
            txt = box.gather()
            #Organizing the content
            txt = txt.strip().replace("\n", "")
            txt = txt + "/0"
            stdscr.addstr(10,10, txt)
            stdscr.refresh()
            #Writing the account into a textfile
            with open("resource.txt", "w", encoding="utf8") as file:
                for i in txt:
                                
                    file.write(i)
                file.write("\n")
                stdscr.addstr(12,12, "Account has been created")
                stdscr.refresh()
                time.sleep(2)
            stdscr.clear()    
        
            
            
def menu(stdscr, row_id):
    """_summary_

    Args:
        stdscr (terminal): stdscr is from the module curses, its used to controll the cmd screen
        row_id (int): row_id takes in a number and starts the menu on that number, it should be 0 so it starts on the first item
    """
    # Get max with height
    h, w = stdscr.getmaxyx()
    #filler for footer
    footerfiller = " " * (w-len(footer)-1)
    #creating header & subtitle
    header = stdscr.subwin(1, (w//2)-(len(myTitle)//2))
    subheader = stdscr.subwin(2, (w//2)-(len(subtitle)//2))
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

    #Show login credentials in main screen, uncomment for testing purposes

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
        #centering calculations
        x = w//2 - len(row)//2
        y = h//2 - len(myMenu) + count
        #Rendering menu 
        if count == row_id:
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y,x, row, curses.A_STANDOUT)
            stdscr.attroff(curses.color_pair(1))
        elif count != row_id:
            stdscr.addstr(y,x,row)  
    # refreshing screen
    stdscr.refresh()
        
if __name__ == "__main__":

    curses.wrapper(main)




