#ludo rocks
import tkinter as tk
import random
import pygame
from turtle import *
bgcolor("black")
title("ludo rocks")
speed(0)
pu()
color("#ffd796")
begin_fill()
setposition(-300,-300)
pensize(3)
for side in range(4):
    forward(600)
    left(90)
end_fill()
begin_fill()
color('white')

setposition(-280,-280)
pensize(3)
for side in range(4):
    forward(560)
    left(90)
end_fill()
#def for boxes
def colorsquare(value,x,y,z,w,m):
    begin_fill()
    color(value)
    setposition(x,y)
    pensize(3)
    for side in range(4):
        w(m)
        z(90)
    end_fill()
#use of def-
colorsquare('yellow',-280,-280,left,forward,230)
colorsquare('red',280,-280,right,backward,230)
colorsquare('blue',280,280,left,backward,230)
colorsquare('green',-280,280,right,forward,230)
colorsquare('white',-250,-250,left,forward,170)
colorsquare('white',250,-250,right,backward,170)
colorsquare('white',-250,250,right,forward,170)
colorsquare('white',250,250,left,backward,170)

pu()
#def for circles
def colorcircle(value,x,y,z,w):
    color(value)
    setposition(x,y)
    pensize(3)
    
    
    for side in range(2):
        begin_fill()
        z(20)
        end_fill()
        w(80)
   
#use of def
colorcircle('blue',200,200,circle,backward)
colorcircle('blue',200,120,circle,backward)
colorcircle('red',200,-220,circle,backward)
colorcircle('red',200,-140,circle,backward)
colorcircle('green',-200,200,circle,forward)
colorcircle('green',-200,120,circle,forward)
colorcircle('yellow',-200,-220,circle,forward)
colorcircle('yellow',-200,-140,circle,forward)

def line(x,y,x1,y1,m,n):
    point1 = (x,y)
    point2 = (x1,y1)
    pensize(1)
    color(m,n)
    pu()
    goto(point1)
    pd()
    goto(point2)
def colorfilling(value,x,y,z,w,m,n,o,p,q,r):
    color(value,value)
    pu()
    setposition(x,y)
    pd()
    begin_fill()
    for sides in range(2):
        z (w)
        m(n)
        o(p)
        q(r)
    end_fill()

colorfilling("blue",15,279,right,90,forward,232,right,90,forward,28)
colorfilling("yellow",15,-278,right,90,backward,232,right,90,forward,28)
colorfilling("green",-279,-15,forward,232,left,90,forward,28,left,90)
colorfilling("red",279,-15,backward,232,left,90,forward,28,left,90)

colorfilling("green",-239,50,forward,37,right,90,forward,34,right,90)
colorfilling("red",239,-50,backward,37,right,90,backward,33,right,90)
colorfilling("yellow",-50,-239,left,90,forward,37,left,90,backward,34)
colorfilling("blue",50,239,right,90,forward,37,right,90,forward,34)

#horizontal line1
line(15,280,15,50,'black','black')
line(15,-50,15,-280,'black','black')
#horizontal line 2,'black','black'
line(-15,280,-15,50,'black','black')
line(-15,-50,-15,-280,'black','black')
#vertical line 1
line(280,15,50,15,'black','black')
line(-50,15,-280,15,'black','black')
#vertical line 2
line(280,-15,50,-15,'black','black')
line(-50,-15,-280,-15,'black','black')
#short vertical lines
line(50,241,-50,241,'black','black')
line(50,202,-50,202,'black','black')
line(50,163,-50,163,'black','black')
line(50,124,-50,124,'black','black')
line(50,85,-50,85,'black','black')

line(50,-241,-50,-241,'black','black')
line(50,-202,-50,-202,'black','black')
line(50,-163,-50,-163,'black','black')
line(50,-124,-50,-124,'black','black')
line(50,-85,-50,-85,'black','black')

#the middle rectangle
pu()
setposition(50,50)
pd()
begin_fill()
pu()
setposition(50,50)
pd()
line(50,50,0,0,'blue','blue')

pu()
setposition(0,0)
pd()
line(0,0,-50,50,'blue','blue')
end_fill()





pu()
setposition(-50,50)
pd()
begin_fill()
pu()
setposition(-50,50)
pd()
line(0,0,-50,50,'green','green')

pu()
setposition(0,0)
pd()
line(0,0,-50,-50,'green','green')
end_fill()

pu()
setposition(-50,-50)
pd()
begin_fill()
pu()
setposition(-50,-50)
pd()
line(0,0,-50,-50,'yellow','yellow')

pu()
setposition(0,0)
pd()
line(0,0,50,-50,'yellow','yellow')
end_fill()


pu()
setposition(50,-50)
pd()
begin_fill()
pu()
setposition(50,-50)
pd()
line(0,0,50,-50,'red','red')

pu()
setposition(0,0)
pd()
line(0,0,50,50,'red','red')
end_fill()


pu()
setposition(50,-241)
pd()

#short horizontal lines
def line1(y,x,y1,x1):
    point1 = (x,y)
    point2 = (x1,y1)
    pensize(1)
    color('black','black')
    pu()
    goto(point1)
    pd()
    goto(point2)
line1(50,-241,-50,-241)
line1(50,-202,-50,-202)
line1(50,-163,-50,-163)
line1(50,-124,-50,-124)
line1(50,-85,-50,-85)

color('blue','blue')
pu()
setposition(50,241)
pd()
line1(50,241,-50,241)
line1(50,202,-50,202)
line1(50,163,-50,163)
line1(50,124,-50,124)
line1(50,85,-50,85)
hideturtle()
"""
# dice input
def Dice():
    dice=[1,2,3,4,5,6]
    Dice=random.choice(dice)
    print(Dice)
    
root = tk.Tk()
canvas = tk.Canvas( width = 50, height = 5)
canvas.pack()
tk.Button(text = "Click to Roll the Dice", command = Dice).pack(side = tk.TOP)
canvas.mainloop()

pygame.init()
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x=50
y=50
rad = 20
vel = 5

run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run= False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel

    win.fill((0,0,0))

    pygame.draw.circle(win, (255,0,0), (x,y),rad)
    pygame.display.update()


pygame.quit()
"""
