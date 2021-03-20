import curses

def clock(stdscr):
    
    curses.curs_set(0)
    #stdscr.nodelay(False)
    #stdscr.timeout(50)

    #write in a file
    file = open("leaderboard", "w")

    file.write("Hello one file! ")
    file.write("Hello file!")
    file.close()

    #read a file
    rf = open("leaderboard", "r")
    content = rf.read()
    stdscr.addstr(0, 0, content)

    userkey = stdscr.getch()

curses.wrapper(clock)
    