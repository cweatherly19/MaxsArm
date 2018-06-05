import curses
import threading
import RoboPiLib as RPL
screen = curses.initscr()
screen.addstr('press a, then s:')
key = ''
keyhold = 0
def working():
    RPL.servoWrite(1, 1000)
while key != ord('q'):
    key = screen.getch()
    screen.clear()
    screen.refresh()
    screen.addstr('press a, then s: ')
    if key == ord('a'):
        key = keyhold
    if key == ord('s'):
        RPL.servoWrite(1, 0)
        key = 0
    if key == keyhold:
        screen.addstr('thinking')
        threading.Timer(2, working).start()
curses.endwin()
