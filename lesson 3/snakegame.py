import curses
from curses import textpad
import random

def board(stdscr):

  #turn of the cursor 
  curses.curs_set(0)
  stdscr.nodelay(1)
  stdscr.timeout(500)

  sh, sw = stdscr.getmaxyx()

  welcome_msg = "Welcome to Snake Game!"
  stdscr.addstr(1, sw // 2 - len(welcome_msg) // 2, welcome_msg)
  
  #define the rectangle box
  box = [
    [3, 3],
    [sh - 3, sw - 3]
  ]

  #draw the border
  textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

  #define the body
  snake = [
    #head
    [sh // 2, sw // 2 + 1],
    #body
    [sh // 2, sw // 2],
    #tail
    [sh // 2, sw // 2 - 1]
  ]
  snake_ch = chr(9608)
  for point in snake:
    stdscr.addstr(point[0], point[1], snake_ch)
  
  #define the snake's moving direction
  direction = curses.KEY_RIGHT

  #setup food variable.
  food = [
    random.randint(box[0][0] , box[1][0] - 1),
    random.randint(box[0][1] , box[1][1] - 1)
  ]
  food_ch = "*"
  stdscr.addstr(food[0], food[1], food_ch)

  while True:
    #ESC to exit
    #will give -1 if timeout
    key = stdscr.getch()
    if key == 27:
      break 
    
    #snake moves based on the user's input
    if key == curses.KEY_UP:
      direction = key
    elif key == curses.KEY_DOWN:
      direction = key
    elif key == curses.KEY_LEFT:
      direction = key
    elif key == curses.KEY_RIGHT:
      direction = key
    
    #current head 
    head = snake[0] 
    #snake moves based on the user's input
    if direction == curses.KEY_UP:
      new_head = [head[0] - 1, head[1]]
    elif direction == curses.KEY_DOWN:
      new_head = [head[0] + 1, head[1]]
    elif direction == curses.KEY_LEFT:
      new_head = [head[0], head[1] - 1]
    elif direction == curses.KEY_RIGHT:
      new_head = [head[0], head[1] + 1]
    #paint the new head 
    stdscr.addstr(new_head[0], new_head[1], snake_ch)
    #change the current body
    snake.insert(0, new_head)
    #take away the current tail
    tail = snake[-1]
    stdscr.addstr(tail[0], tail[1], ' ')
    #pop function will pop out and remove the last item of this list 
    snake.pop()

    #if head touches border, game over
    if (snake[0][0] == box[0][0] or
        snake[0][0] == box[1][0] or
        snake[0][0] == box[0][0] or
        snake[0][0] == box[0][0]):
        stdscr.addstr("GAME OVER!")
        stdscr.nodelay(0)
        stdscr.getch()
        break

curses.wrapper(board)