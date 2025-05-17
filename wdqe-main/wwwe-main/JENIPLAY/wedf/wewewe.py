
import pygame
pygame.init()
window = pygame.display.set_mode((1300 , 600))
clock = pygame.time.Clock()

with open("sjjsww.txt", "r") as fille:
    a = fille.read()

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
    
    for index , char in enumerate(a):
        if char == "#":
            pygame.draw.rect(window,(100,100,100), (index*100,500,50, 60))
    
    pygame.display.update()
    clock.tick(60)