# main.py
from time import sleep
# Variables
x=4.3
y=6.2
z=5.3
Game_Speed = 0 # 1 Means the game speed is x0, There no game speed for now.
Raid_Minutes = x * y * z # In how many raid will be
# Functions
def ChangeGameSpeed(speed):
	if speed > 2:
		print(str("The speed too much!"))
	else:
		print(str("The speed is now: " + str(speed)))
		Game_Speed = speed

def CGSWT(speed): # CGSWT Means "Change game speed without text"
	if speed > 2:
		return "The speed is too much!"
	else:
		return "The speed is now: " + str(speed)
		Game_Speed = speed

