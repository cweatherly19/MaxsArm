#to access files needed to run the code
import curses
import setup
import RoboPiLib as RPL
#so define motor ports
motor1 = 0
motor2 = 1
#to define the 'screen' in front of functions
screen = curses.initscr()
#to tell the user valid inputs
screen.addstr('Hit q to quit. Use the W, A, S, and D to test if code works. Detected key:')
#to read key inputs
position = 0
key = ''
#to end loop if 'q' is hit
while key != ord('q'):
    #so the key can be read
    key = screen.getch()
    screen.clear()
    screen.addstr('Hit q to quit. Use the W, A, S, and D to test if code works. Detected key: ')
    #to define what keys preform commands
    if key == ord('w'):
        screen.addstr('w key')
        RPL.servoWrite(motor1, 1000)
    if key == ord('a'):
        screen.addstr('a key')
        RPL.servoWrite(motor2, 3000)
    if key == ord('s'):
        screen.addstr('s key')
        position = position + 50
        RPL.servoWrite(motor1, position)
    if key == ord('d'):
        screen.addstr('d key')
        position = position - 50
        RPL.servoWrite(motor2, position)
#to reformat the terminal/end the curses program
curses.endwin()
