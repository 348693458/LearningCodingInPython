import curses

def window(stdscr):
  #standard screen.add string format 
  #stdscr.addstr(str) or stdscr.addstr(y, x, str)
  (sh, sw) = stdscr.getmaxyx()

  #Setup colors
  curses.start_color()
  curses.use_default_colors()

  #Initialize color pairs
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)
    stdscr.addstr(str(i + 1), curses.color_pair(i + 1))
  
  stdscr.getch()
# wrap up the window function
curses.wrapper(window)
