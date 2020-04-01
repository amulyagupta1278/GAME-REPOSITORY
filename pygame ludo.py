import pygame
import random
pygame.init()
win=pygame.display.set_mode((600,600),0,32)
pygame.display.set_caption("LUDO")
bground1=(255, 215, 150)
white=(255,255,255)
pygame.draw.rect(win,bground1,(0,0,600,600))
pygame.draw.rect(win,white,(50,50,500,500))

def colorsquare(value,x,y,z,w):
    pygame.draw.rect(win,value,(x,y,z,w))

colorsquare((255,0,0),50,50,200,220)    
colorsquare((0,255,0),50,350,200,200)    
colorsquare((0,0,255),350,50,200,220)
colorsquare((255,255,0),350,350,200,200)
#red
colorsquare((255,255,255),90,90,40,40)
colorsquare((255,255,255),90,170,40,40)
colorsquare((255,255,255),170,90,40,40)
colorsquare((255,255,255),170,170,40,40)
#blue
colorsquare((255,255,255),475,90,40,40)
colorsquare((255,255,255),475,170,40,40)
colorsquare((255,255,255),400,90,40,40)
colorsquare((255,255,255),400,170,40,40)
#GREEN

colorsquare((255,255,255),90,475,40,40)
colorsquare((255,255,255),170,475,40,40)
colorsquare((255,255,255),90,400,40,40)
colorsquare((255,255,255),170,400,40,40)
#YELLOW
colorsquare((255,255,255),475,475,40,40)
colorsquare((255,255,255),475,400,40,40)
colorsquare((255,255,255),400,475,40,40)
colorsquare((255,255,255),400,400,40,40)

#LINES
pygame.draw.line(win,(0,0,0),(400,400),(40,40),3)










pygame.display.update()
"""# dice input
def Dice():
    dice=[1,2,3,4,5,6]
    Dice=random.choice(dice)
    print(Dice)
    
root = tk.Tk()
canvas = tk.Canvas( width = 50, height = 5)
canvas.pack()
tk.Button(text = "Click to Roll the Dice", command = Dice).pack(side = tk.TOP)
canvas.mainloop()
"""
