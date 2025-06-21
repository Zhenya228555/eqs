#подключення модулей
import pygame
from random import randint
import socket
#созданя вікна
pygame.init()
window = pygame.display.set_mode((1300 , 600))
clock = pygame.time.Clock()
#пидключеня до сервера
desol=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
desol.connect(("localhost",1337))
sms = desol.recv(1024).decode()
w=sms.split()
w[0]
my_id = int(w[0])
my_x = int(w[1])
my_y = int(w[2])
my_radius = int(w[3])
print(sms)
print(w)
#создавання мячив
class Ball():
    def __init__(self , x , y , color , radius):
        self.x=x
        self.y=y
        self.radius=radius
        self.color=color
        self.rect = pygame.Rect(self.x,self.y,self.radius*2,self.radius*2)
#видрісовка мяча
    def risofka(self):
        pygame.draw.circle(window, self.color, (self.rect.x+self.radius,self.rect.y+self.radius), self.radius) 
    def risofka2(self):
        font = pygame.font.Font(None,10)
        pygame.draw.circle(window, self.color, (self.rect.x+self.radius,self.rect.y+self.radius), self.radius) 
        aajsjsassakskmjsa =font.render("jena",10000000,(0,0,0))
        window.blit(aajsjsassakskmjsa,(self.rect.x+self.radius,self.rect.y+self.radius))
#пустий список   
a = []
for _ in range(6000):
    q = Ball (randint(-1000, 1000),randint(-1000,1000), 
              (randint(0,255),randint(0,255),randint(0,255)) , randint(-10,20))
    a.append(q)
    

game = 1
#видрисофка мячя
ball = Ball(600,300,(255,255,255), my_radius)
#БЕЗКИНЕЧНИЙ ЦИКЕЛ
while game:
    #управлиння
    window.fill((0,0,0))
    for element in a:
        element.risofka()
    for ev in pygame.event.get():
        if ev.type == pygame.QUIT:
             game= 0

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
            for eda in a:
                eda.rect.x += 5
            my_x -= 5
    if keys[pygame.K_d]:
            for eda in a:
                eda.rect.x +=-5
            my_x += 5
    if keys[pygame.K_w]:
            for eda in a:
                eda.rect.y += 5
            my_y += 5
    if keys[pygame.K_s]:
            for eda in a:
                eda.rect.y -= 5
            my -= 5

                    
    # game = 0
#відрисофка
    ball.risofka2()
#частата кадриф
    try:
        msg=(f"{my_id,my_x,my_y,my_radius,my_Name}")
        client.send(msg.encode())
    except:
            pass
    pygame.display.update()
    clock.tick(100)
