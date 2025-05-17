
import pygame
pygame.init()
window = pygame.display.set_mode((1300 , 600))
clock = pygame.time.Clock()

with open("sjjsww.txt", "r") as fille:
    f = fille.readlines()
    
class Block():
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.rec = pygame.Rect(x,y,width,height)
    def risofka(self):
        pygame.draw.rect(window, self.color, self.rec)
        

class Ball():
    def __init__(self , x , y , color , radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.speed_x = 10
        self.speed_y = 10
    def risofka(self):
        pygame.draw.circle(window, self.color, (self.x,self.y), self.radius)
        
    def go(self):
        self.x += self.speed_x 
        self.y += self.speed_y 
        if self.y > 600:
            self.speed_y *= -1
        if self.x > 1300:
            self.speed_x *= -1
        if self.y < 0:
            self.speed_y *= -1
        if self.x < 0:
            self.speed_x *= -1
            
            
            

            
        
ball = Ball(100,100,(255,255,255), 9)
ball2 = Ball(800,600,(200,200,200), 10)


a=[]

for row , line in enumerate(f):
    for index, char in enumerate(line):


        if char == "#":
            dlok1 = Block(index*100, row*100,50,10,(255,255,255))
            a.append(dlok1)
        
        

game = 1
while game:
    window.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = 0
    
    ball.risofka()
    ball.go()
    ball2.risofka()
    ball2.go()
    
    for i in a:
        i.risofka()
    
    pygame.display.update()
    clock.tick(60)