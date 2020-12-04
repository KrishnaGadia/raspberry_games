from sense_hat import SenseHat
from time import sleep
from random import randint

sense= SenseHat()
sense.set_rotation(270)

selection = 1
begin = False

def display():
    global selection
    if(selection == 1):
        return "[*]car []frog []snake"
    if(selection == 2):
        return "[]car [*]frog []snake"
    if(selection = 3):
        return "[]car []frog [*]snake"

def start():
    global begin
    begin = True
    
def left():
    global selection
    if(selection<3):
        selection+=1
        
def right():
    global selection
    if(selection>1):
        selection-=1

sense.stick.direction_up = left
sense.stick.direction_down = right
sense.stick.middle = start

while not begin:
    sense.show_message(display())
if(selection == 1):
    import car
if(selection == 2):
    import frog 
if(selection = 3):
    import snake
