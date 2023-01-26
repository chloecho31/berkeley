import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
import time
from curses import wrapper
import random

#intialization: setting size of screen, drawing the border
curses.initscr()
curses.noecho() #turn off echo read keys
curses.curs_set(0)
screen = curses.newwin(30, 50, 5, 5)
dims = screen.getmaxyx()
MAX_Y = dims[0] - 1
MAX_X = dims[1] - 1
screen.keypad(1) #enable keypad mode
screen.border(0)
screen.move(2,2)
screen.nodelay(1)

#game function
def move():
    GAMEOVER = False
    SCORE = 0 #setting intial score
    SNAKE = [[20,15],[20,14],[20,13]] #setting intial size and location of the snake
    HEAD = SNAKE[0]
    TAIL = SNAKE[-1]
    u = TAIL[0]
    v = TAIL[1]
    y = HEAD[0]
    x = HEAD[1]
    direction = 0

#part of the display, show the score of the game
    screen.addstr(0, 2, ' Score : ' + str(SCORE) + ' ') 
    screen.addstr(0, 18, ' SNAKE GAME ')

#generate food at a random position on the screen
    FOOD = [random.randrange(3, 27), random.randrange(3, 47)] 
    a, b = FOOD[0], FOOD[1]
    screen.addch(a, b, ord('@'))

#sets condition of the game proceeding or ending
    while GAMEOVER == False: 
        for item in SNAKE:
            screen.addch(item[0], item[1], ord('X')) #display the characters in each segment of the snake
        screen.refresh()
        key = screen.getch() #converts physical key press into code (utilizes curses library)
        prevKey = key

        if key == curses.KEY_UP and direction != 1: #defining directions and how the code responds to each user input of the up, down, left, or right key
            direction = 3
        elif key == curses.KEY_DOWN and direction != 3:
            direction = 1
        elif key == curses.KEY_LEFT and direction != 0:
            direction = 2
        elif key == curses.KEY_RIGHT and direction != 2:
            direction = 0

#the movement of the snake
        if direction == 3: #up
            y = y-1
            SNAKE.insert(0, [y,x]) 
            last = SNAKE.pop()
            screen.addch(last[0], last[1], ord(' '))
            screen.addch(SNAKE[0][0], SNAKE[0][1], ord('X'))
            screen.refresh()
            curses.doupdate()
        elif direction == 2: #left
            x = x-1
            SNAKE.insert(0, [y,x])
            last = SNAKE.pop()
            screen.addch(last[0], last[1], ord(' '))
            screen.addch(SNAKE[0][0], SNAKE[0][1], ord('X'))
            screen.refresh()
            curses.doupdate()
        elif direction == 1: #down
            y = y+1
            SNAKE.insert(0, [y,x])
            last = SNAKE.pop()
            screen.addch(last[0], last[1], ord(' '))
            screen.addch(SNAKE[0][0], SNAKE[0][1], ord('X'))
            screen.refresh()
            curses.doupdate()
        elif direction == 0: #right
            x = x+1
            SNAKE.insert(0, [y,x])
            last = SNAKE.pop()
            screen.addch(last[0], last[1], ord(' '))
            screen.addch(SNAKE[0][0], SNAKE[0][1], ord('X'))
            screen.refresh()
            curses.doupdate()

#accounts for if an invalid key is pressed
        if direction not in [0, 1, 2, 3,]:
             key = preKey

#when the snake eats the food
        if y == a and x == b:
            SCORE += 1
            screen.addstr(0, 2, ' Score : ' + str(SCORE) + ' ')
            FOOD = [random.randrange(3, 27), random.randrange(3, 47)]
            a, b = FOOD[0], FOOD[1]
            screen.addch(a, b, ord('@'))
            SNAKE.append([u,v])
            screen.addch(u, v, ord('X'))

#when the snake hits the wall, it will reenter from the opposite side
        if y == MAX_Y -1 and direction == 1:
            y = 1
        if y == 1 and direction == 3:
            y = MAX_Y - 1
        if x == MAX_X -1 and direction == 0:
            x = 1
        if x == 1 and direction == 2:
            x = MAX_X -1

#how to end/exit from the game
        if key == 27:
            GAMEOVER = True
            curses.endwin()

#delays the display, slows the speed at which the display updates
        time.sleep(0.2)

#accounts for if the snake has collided into itself
        if SNAKE[0] in SNAKE[1:]:
            GAMEOVER = True
            curses.endwin()

#prints the score at the end of the game
        if GAMEOVER == True:
            print('GAME OVER' + ' YOUR SCORE: ' + str(SCORE))

#initializes the game when the program is run
move()
