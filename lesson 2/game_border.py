import curses
from curses import textpad

def window(stdscr):
  (sh, sw) = stdscr.getmaxyx()
  msg = "Welcome to my decoding game! Press ESC to exit. "
  stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)

  #define the rectangle box
  box = [
    [3, 3],
    [sh - 3, sw - 3]
  ]
   #draw the border
  textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])


  while True:
    userKey = stdscr.getch()
    stdscr.addstr(" You typed: {0}, Character {1} ".format(userKey, chr(userKey)))
    if userKey == 27:
      break
  #collect user information
  stdscr.getch()

# wrap up the window function
curses.wrapper(window)