import turtle  
import random                 
from random import choice, randint  
                                    
def valiRandomVarv():
    yellow = random.random()
    green = random.random()
    blue = random.random()
    return yellow, green, blue
   
aken = turtle.Screen()
aken.title("PING-PONG")
aken.setup(width=1.0, height=1.0)        
aken.bgcolor("black")
aken.tracer(1.9)                          #palli kiirus             

border = turtle.Turtle()                  #väljaku joonistamine
border.speed(0)                   
border.color(valiRandomVarv())
border.begin_fill()               
border.goto(-700,300)             
border.goto(700,300)              
border.goto(700,-300)             
border.goto(-700,-300)            
border.goto(-700,300)             
border.end_fill()                

border.goto(0,300)                    #väljaku keskel olevad katkendlikud jooned     
border.color('white')
border.setheading(270)            
for i in range(25):               
    if i%2 ==0:
        border.forward(24)
    else:
        border.up()
        border.forward(24)
        border.down()
border.hideturtle()               

ristkylikVasak = turtle.Turtle()                 #ristkülikud
ristkylikVasak.color ('white')    
ristkylikVasak.shape('square')    
ristkylikVasak.shapesize(stretch_len=1, stretch_wid=5) 
ristkylikVasak.penup()            
ristkylikVasak.goto(-600,0)       

ristkylikParem = turtle.Turtle()                
ristkylikParem.color ('white')
ristkylikParem.shape('square')
ristkylikParem.shapesize(stretch_len=1, stretch_wid=5)
ristkylikParem.penup()
ristkylikParem.goto(600,0)

FONT = ('Arial', 38)                             #skoorikastid
score_vasak = 0
skooriKast = turtle.Turtle(visible=False) 
skooriKast.color ('white')
skooriKast.penup()
skooriKast.setposition(-200, 300) 
skooriKast.write(score_vasak, font=FONT)

score_parem = 0
skooriKast2 = turtle.Turtle(visible=False) 
skooriKast2.color ('white')
skooriKast2.penup()
skooriKast2.setposition(200, 300) 
skooriKast2.write(score_parem, font= FONT)

def liigu_yles_vasak(): 
    y = ristkylikVasak.ycor() + 10        
    if y > 250:                 
        y = 250            
    ristkylikVasak.sety(y)     

def liigu_yles_parem():
    y = ristkylikParem.ycor() + 10
    if y >250:
        y = 250
    ristkylikParem.sety(y)

def liigu_alla_vasak():
    y = ristkylikVasak.ycor() -10
    if y < -250:
        y = -250
    ristkylikVasak.sety(y)     

def liigu_alla_parem():
    y = ristkylikParem.ycor() -10
    if y < -250:
        y = -250
    ristkylikParem.sety(y)

pall = turtle.Turtle()                                 #pall
pall.shape('circle')
pall.speed (0)
pall.color('black')
pall.dx = 3                       
pall.dy = -3
pall.penup()                      

aken.listen()                      #ristküliku liigutamise klahvid
aken.onkeypress(liigu_yles_vasak, "w")  
aken.onkeypress(liigu_alla_vasak, "s")
aken.onkeypress(liigu_yles_parem, "p")
aken.onkeypress(liigu_alla_parem, "l")

while True:                             #palli liikumise koordinaadid
    aken.update()
    pall.setx(pall.xcor() + pall.dx)    
    pall.sety(pall.ycor() + pall.dy) 

    if pall.ycor() >= 290:            
        pall.dy = -pall.dy            

    if pall.ycor() <= -290:           
        pall.dy = -pall.dy

    if pall.xcor() >= 690: 
        score_parem += 1 
        skooriKast2.clear()
        skooriKast2.write(score_parem, font= FONT)
        pall.goto(0, randint(-150, 150)) 
        pall.dx = choice ([-4, -3, -2, 2, 3, 4])                
        pall.dy = choice ([-4, -3, -2, 2, 3, 4]) 
    
    if pall.xcor() <= -690:
        score_vasak += 1
        skooriKast.clear()
        skooriKast.write(score_vasak, font=FONT)
        pall.goto(0,randint(-150, 150)) 
        pall.dx = choice ([-4, -3, -2, 2, 3, 4])                
        pall.dy = choice ([-4, -3, -2, 2, 3, 4]) 

    if pall.ycor ()>= ristkylikParem.ycor ()-50 and pall.ycor () <= ristkylikParem.ycor () +50 \
    and pall.xcor () >= ristkylikParem.xcor () -5 and pall.xcor () <=ristkylikParem.xcor () +5:
        pall.dx = -pall.dx  

    if pall.ycor ()>= ristkylikVasak.ycor ()-50 and pall.ycor () <= ristkylikVasak.ycor () +50 \
    and pall.xcor () >= ristkylikVasak.xcor () -5 and pall.xcor () <=ristkylikVasak.xcor () +5:
        pall.dx = -pall.dx  

aken.mainloop()  
