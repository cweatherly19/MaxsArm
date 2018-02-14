import setup
import RoboPiLib as RPL
motor = 1
start = raw_input("press y to go, then n to stop")
while start == "y":
  RPL.servoWrite(motor, 1000)
  if "n":
      RPL.servoWrite(motor, 0)
