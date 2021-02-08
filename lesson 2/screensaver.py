import curses
import random

def window(stdscr):
  #standard screen.add string format 
  #stdscr.addstr(str) or stdscr.addstr(y, x, str)
  (sh, sw) = stdscr.getmaxyx()

  #setup colors
  curses.start_color()
  curses.use_default_colors()

  #initialize color pairs
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, -1)
    #stdscr.addstr(str(i + 1), curses.color_pair(i + 1))
  
  # turn off delay
  stdscr.nodelay(True)
  stdscr.timeout(100)

  while True:
    # get random letter
    letter = random.randint(33, 126)
    # get color
    color = random.randint(1, curses.COLORS + 1)
    # get location
    y = random.randint(0, sh - 1)
    x = random.randint(0, sw - 1)
    stdscr.addstr(y, x, chr(letter), curses.color_pair(color))
  
    if stdscr.getch() == 27:
      break
  
# wrap up the window function
curses.wrapper(window)