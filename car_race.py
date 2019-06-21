from sense_hat import SenseHat
from time import sleep
import copy

sense = SenseHat()
sense.rotation = 270
car_pos_left=True
def matrix_add(base,mask,r,c,x,y):
    print "start " , base
    for j in range(c):
        for i in range(r):
            """print("i ",i,"j ",j, "x ",x,"y ",y)"""
            print("base",x+i+8*(j+y),"mask",i+r*j)
            for d in range(3):
                base[x+i+8*(j+y)][d]+=mask[i+r*j][d]
                base[x+i+8*(j+y)][d]%=256
    print "done " , base

def collision(board):
    for p in board[47:63]:
        if(p[0]==255):
            if(p[1]>0 or p[2]>0):
                return True
    return False

O = (0, 0, 0)
R = (255,0,0)
W = (255, 255, 255)
car_mask=[O,R,O,R,O,R]

display = [[i for i in O] for x in range(64)]
line = [W] * 8
try:
        
    while( True):
        car_x=2 if (car_pos_left) else 5;
        car_pos_left= not car_pos_left;
        for event in sense.stick.get_events():
            print("The joystick was {} {}".format(event.action, event.direction))
            
        matrix_add(display,car_mask,3,2,car_x,6)
        matrix_add(display,line,1,8,1,0)
        sleep(1)
        sense.set_pixels(display)
        display = [[i for i in O] for x in range(64)]
except KeyboardInterrupt:
    sense.clear()
    raise

    
    
    
