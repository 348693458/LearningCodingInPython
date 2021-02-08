import curses


def window(stdscr):
  (sh, sw) = stdscr.getmaxyx()
  msg = "Welcome to my decoding game! Press ESC to exit. "
  stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
  while True:
    userKey = stdscr.getch()
    stdscr.addstr(" You typed: {0}, Character {1} ".format(userKey, chr(userKey)))
    if userKey == 27:
      break

#collect user information
  stdscr.getch()

# wrap up the window function
curses.wrapper(window)