from sense_hat import SenseHat
from time import sleep
from random import randint,sample

sense = SenseHat()

sense.set_rotation(180)

li = list(range(8))
lm1 = sample(li,2)
rm2 = sample(li,3)
lm3 = sample(li,3)
rm4 = sample(li,4)
lm5 = sample(li,5)
rm6 = sample(li,6)

last = []

print(lm1,rm2,lm3,rm4,lm5,rm6)

frog_pos = [0,4]
frog_dir = 0
score = 0

def draw_frog():
   global frog_pos, frog_dir, score
   
   sense.set_pixel(frog_pos[0], frog_pos[1],0,0,0)
   
   if frog_dir == 1 and frog_pos[0]!=7 :
      if(frog_pos[0] != 6 or frog_pos[1] not in last):
         frog_pos[0] += 1
         score+=1
   if frog_dir == 2 and frog_pos[0]!=0 :
      frog_pos[0] -= 1
      score-=1
   if frog_dir == 3 and frog_pos[1]!=7 :
      frog_pos[1] +=1;
   if frog_dir == 4 and frog_pos[1]!=0 :
      frog_pos[1] -=1;
   frog_dir = 0

   sense.set_pixel(frog_pos[0],frog_pos[1],0,125,0)

def move_up(event):
   global frog_dir
   if event.action == 'pressed':
      frog_dir = 1
def move_down(event):
   global frog_dir
   if event.action == 'pressed':
      frog_dir = 2

def move_left(event):
   global frog_dir
   if event.action == 'pressed':
      frog_dir = 3
   
def move_right(event):
   global frog_dir
   if event.action == 'pressed':
      frog_dir = 4

def add_grid(grid, add):
    return [(x+add)%8 for x in grid];

def draw_mover(row, grid,add):
    grid = add_grid(grid,add)
    color = [110,65,30] if (add > 0) else [30,65,110];
    for g in grid:
        sense.set_pixel(row,g,color)
    return grid 

def draw_line(row):
    for i in range(8):
        sense.set_pixel(row,i,200,200,200)

def draw_movers():
   global lm1,rm2,lm3,rm4,lm5,rm6
   lm1 = draw_mover(1,lm1,1)
   rm2 = draw_mover(2,rm2,-1)
   lm3 = draw_mover(3,lm3,1)
   rm4 = draw_mover(4,rm4,-1)
   lm5 = draw_mover(5,lm5,1)
   rm6 = draw_mover(6,rm6,-1)

def draw_last():
   global last
   for g in last:
      sense.set_pixel(7,g,[0,125,0])

def detect():
   global lm1,rm2,lm3,rm4,lm5,rm6, frog_pos
   color = [210,255,30] if frog_pos[0]%2==1 else [30,255,210]
   if frog_pos[0] == 1 and frog_pos[1] in lm1:
      sense.set_pixel(frog_pos[0],frog_pos[1],color)
      return True;
   if frog_pos[0] == 2 and frog_pos[1] in rm2:
      sense.set_pixel(frog_pos[0],frog_pos[1],color)
      return True;
   if frog_pos[0] == 3 and frog_pos[1] in lm3:
      sense.set_pixel(frog_pos[0],frog_pos[1],color)
      return True;
   if frog_pos[0] == 4 and frog_pos[1] in rm4:
      sense.set_pixel(frog_pos[0],frog_pos[1],color)
      return True;
   if frog_pos[0] == 5 and frog_pos[1] in lm5:
      sense.set_pixel(frog_pos[0],frog_pos[1],color)
      return True;
   if frog_pos[0] == 6 and frog_pos[1] in rm6:
      sense.set_pixel(frog_pos[0],frog_pos[1],color)
      return True;
   return False;

def show(message):
   sense.set_rotation(270)
   sense.show_message(message)
   sense.set_rotation(180)
   
sense.stick.direction_up = move_left
sense.stick.direction_down = move_right
sense.stick.direction_left = move_up
sense.stick.direction_right = move_down

for i in range(10000):
   draw_frog()
   if(i%8==0):
      sense.clear()
      draw_movers()
   if(i%4 == 0):
      colision = detect()
   
   draw_last()
      
   if(frog_pos[0] == 7):
      last.append(frog_pos[1])
      frog_pos = [0,4]
      frog_dir = 0
      
   if colision:
      sleep(3)
      show("Score : " + str(score))
      frog_pos = [0,4]
      frog_dir = 0
      score = 0
      colision = False
      last=[]

   if(len(last) == 8):
      sleep(3)
      show("You win")
      frog_pos = [0,4]
      frog_dir = 0
      score = 0
      last=[]
      
   sleep(0.1)
