import curses
import datetime

def clock(stdscr):
    
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(50)

    start_time = datetime.datetime.now()

    while True:
        userkey = stdscr.getch()

        if userkey in [27, 113]:
            break
        stdscr.addstr(0, 0, str(datetime.datetime.now()))

        stdscr.addstr(3, 0, "Stopwatch: ")
        stdscr.addstr(str((datetime.datetime.now() - start_time).seconds))
        stdscr.addstr(".")
        micros = (datetime.datetime.now () - start_time).microseconds
        stdscr.addstr(str(micros // 100002))
curses.wrapper(clock)
    