from turtle import *
from random import randint

#speed ("fast")

step = 30
step2 = 20
mount = [0, 25, 40, 45, 60, 100, 200, 150, 55,20]

forward(800)
goto(-10,0)

def bieda_gora():
    
    for i in range(len(mount)):         
        goto(i * step, mount[i] + randint(0, 40))
        
      
def bieda_gora2():
    
    for i in range(len(mount)):
           
        goto(i * step + 500, mount[i] + randint(0, 20))

  
         

for _ in range(1):
     bieda_gora()
     bieda_gora2()
goto(800,0)     
exitonclick()
