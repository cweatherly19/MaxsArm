import curses
import setup
import RoboPiLib as RPL

motor1 = 0
motor2 = 1
screen = curses.initscr()
curses.cbreak()
screen.keypad(1)

screen.addstr("Enter q to quit. ")
screen.addstr("Use the W, A, S, and D to move.")
screen.refresh()

#so is can ready what a key is
key = ''
#so if you hit 'q', the loop will end
while key != ord('q'):
    #so the key can be read
    key = screen.getch()
    #so the code can read without hitting return
    screen.refresh()
    #so that you can read the keys and use the functions
    while key == ord('w'):
        RPL.servoWrite(motor1, 1000)
        screen.refresh()
        break
    while key == ord('a'):
        RPL.servoWrite(motor2, 3000)
        screen.refresh()
        break
    while key == ord('s'):
        RPL.servoWrite(motor1, 2000)
        screen.refresh()
        break
    while key == ord('d'):
        RPL.servoWrite(motor2, 800)
        screen.refresh()
        break
    #so the robot will stop
    RPL.servoWrite(motor1, 0)

curses.endwin()
