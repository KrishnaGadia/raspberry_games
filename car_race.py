from sense_hat import SenseHat
from time import sleep
from random import randint

sense= SenseHat()

score = 0

speed = 0.20

car = [1,7,2,7,3,7,2,6]
pos = 0

oppo = [1, 2, 3]
opos = randint(0,1)

sense.set_rotation(270)

def draw_car(p):
    if(p==0):
        sense.set_pixel(car[0],car[1],0,127,255)
        sense.set_pixel(car[2],car[3],0,127,255)
        sense.set_pixel(car[4],car[5],0,127,255)
        sense.set_pixel(car[6],car[7],0,255,255)
    else:
        sense.set_pixel(car[0] + 3,car[1],0,127,255)
        sense.set_pixel(car[2] + 3,car[3],0,127,255)
        sense.set_pixel(car[4] + 3,car[5],0,127,255)
        sense.set_pixel(car[6] + 3,car[7],0,255,255)

def draw_opponent(row):
    global opos
    if(opos==0):
        if row <= 7 :
            sense.set_pixel(oppo[0],row,255,127,0)
            sense.set_pixel(oppo[2],row,255,127,0)
        if row >=1 and row<=8:
            sense.set_pixel(oppo[1],row-1,255,127,0)
        
    else:
        
        if row <= 7 :
            sense.set_pixel(oppo[0] + 3,row,255,127,0)
            sense.set_pixel(oppo[2] + 3,row,255,127,0)
        if row >=1 and row<=8:
            sense.set_pixel(oppo[1] + 3,row-1,255,127,0)

def draw_border():
    color = (150,255,100)
    for i in range(8):
        sense.set_pixel(0,i,color)
        sense.set_pixel(7,i,color)
        
def move_left():
    global pos
    pos = 1
def move_right():
    global pos
    pos = 0

sense.stick.direction_up = move_left
sense.stick.direction_down = move_right



r = 0
car_distance = randint(9,15)
while True:
    sense.clear()
    draw_border()
    draw_car(pos);
    draw_opponent(r);
    r +=1

    if (r==8 or r==9) and opos == pos:
        sleep(0.5)
        sense.show_message("Score "+str(score))

        score = 0
        speed = 0.20
        pos = 0
        opos = randint(0,1)
        
        car_distance = randint(9,15)
        r = 0

    if(r == car_distance):
        r = 0
        
        car_distance = randint(9,13)
        opos = randint(0,1)
        score +=1
        if speed > 0.05:
            speed = speed * 0.9
    sleep(speed)
