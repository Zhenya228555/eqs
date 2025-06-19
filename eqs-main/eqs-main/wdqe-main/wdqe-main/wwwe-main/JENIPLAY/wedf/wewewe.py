
import pygame
pygame.init()
window = pygame.display.set_mode((1300 , 600))
clock = pygame.time.Clock()

with open("sjjsww.txt", "r") as fille:
    f = fille.readlines()
    
pmm = pygame.mixer.music.load("byte-blast-8-bit-arcade-music-background-music-for-video-208780.mp3")
pmm = pygame.mixer.music.play(-1)
pum = pygame.mixer.Sound("sword-demo-310496.mp3")
pom = pygame.mixer.Sound("game-over-38511.mp3")
pam = pygame.mixer.Sound("game-win-36082.mp3")
lose = pygame.image.load("360_F_1179443158_9eZz9fiUrbh8TvR5PXtGJ1Rzh1PY9Ayq.jpg")
lose = pygame.transform.scale(lose,(500,500))#падрезать
loses = pygame.image.load("inline_image_preview.jpg")
loses = pygame.transform.scale(loses,(500,500))
class Block():
    def __init__(self,x,y,width,height,color):
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.rect = pygame.Rect(x,y,width,height)
    def risofka(self):
        pygame.draw.rect(window, self.color, self.rect)
        

class Ball():
    def __init__(self , x , y , color , radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.speed_x = 5
        self.speed_y = 5
        self.rect = pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)
    def risofka(self):
        pygame.draw.circle(window, self.color, (self.rect.x+self.radius,self.rect.y+self.radius), self.radius)    
        
    def go(self):

        self.rect.x =  self.x
        self.rect.y = self.y

        self.x += self.speed_x 
        self.y += self.speed_y 

        if self.y > 600:
            window.blit(lose,(100,100))
            pom.play()
            pygame.display.update()
            
        if self.x > 1300:
            self.speed_x *= -1
        if self.y < 0:
            self.speed_y *= -1
        if self.x < 0:
            self.speed_x *= -1
            
            
            
            

            
        
ball = Ball(400,400,(255,255,255), 9)
parti = Block(400, 500,100,10,(255,255,0))

a=[]

for row , line in enumerate(f):
    for index, char in enumerate(line):


        if char == "#":
            dlok1 = Block(index*100, row*100,50,10,(255,255,255))
            a.append(dlok1)
        
A = False
D = False
game = 1
while game:
    window.fill((0,0,0))
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
            game = 0

            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_d:
                
                    D = True
                if  ev.key == pygame.K_a:
                
                    A=True
            if ev.type == pygame.KEYUP:
                if ev.key == pygame.K_d:
                    
                    D=False
                if  ev.key == pygame.K_a:
                    A=False

        if A == True:
            parti.x += -10
            parti.rect.x += -10
        if D == True:
            parti.x += 10
            parti.rect.x += 10
    
    ball.risofka()
    ball.go()
    parti.risofka()

    for i in a:
        if i.rect.colliderect(ball ):
            pum.play()
            a.remove(i)
            ball.speed_y  *= -1
        else:
            i.risofka()

    if len(a) == 0:
        window.blit(loses,(100,100))
        pam.play()
        pygame.display.update()


    if parti.rect.colliderect(ball):
        pum.play()
        ball.speed_y  *= -1

    
    pygame.display.update()
    clock.tick(100)