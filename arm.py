import time
import setup
import RoboPiLib as RPL
#up and down
motor1 = 1
#left and right
motor2 = 0
#tells the commands
print "press w to go down, press s to go up,"
print "a to go left, d to go right,"
print "and any other key to end code."
#allows for inputs
command = raw_input("> ")
#reads the turn in the loop below
def run( turn ):
    return turn
#reads the up and down in the loops
def speed( go ):
    return go
#allows code to break and stop completely
z = 0
#loop to run robot
while z is 0:
    #allows individual loops to break
    v = 1
    #turn right
    while v is 1 and command is "d":
        now = time.time()
        future = 1 + now
        #starts motor running
        while v is 1 and now < future:
            run(RPL.servoWrite(motor2, 800))
            print "insert new input, then wait one second before entering another"
            #breaks loop
            v = 2
    #return to top of loop if "d"
    if command is "d":
        command = raw_input("> ")
        continue
    #turn left
    while v is 1 and command is "a":
        now = time.time()
        future = 1 + now
        #starts motor running
        while v is 1 and now < future:
            run(RPL.servoWrite(motor2, 3000))
            print "insert new input, then wait one second before entering another"
            #breaks loop
            v = 2
    #return to top of loof if "a"
    if command is "a":
        command = raw_input("> ")
        continue
    #go up
    while v is 1 and command is "w":
        #sets amount of time for motor to run
        now = time.time()
        future = 1 + now
        #starts motor running
        while v is 1 and now < future:
            speed(RPL.servoWrite(motor1, 1000))
            #ends motor running
            while v is 1 and time.time() >= future:
                speed(RPL.servoWrite(motor1, 0))
                print "insert new input, then wait one second before entering another"
                #breaks loops
                v = 2
    #return to top of loop if "w"
    if command is "w":
        command = raw_input("> ")
        continue
    #go down
    while v is 1 and command is "s":
        #set emount of time for motor to run
        now = time.time()
        future = 1 + now
        #starts motor running
        while v is 1 and now < future:
            speed(RPL.servoWrite(motor1, 2000))
            #ends motor running
            while v is 1 and time.time() >= future:
                speed(RPL.servoWrite(motor1, 0))
                print "insert new input, then wait one second before entering another"
                v = 2
    #return to top of loop if "s"
    if command is "s":
        command = raw_input("> ")
        continue
    #stops code
    while command is not "a" or "d" or "w" or "s":
        print "program stopping"
        speed(RPL.servoWrite(motor1,0))
        z = 1
        break
