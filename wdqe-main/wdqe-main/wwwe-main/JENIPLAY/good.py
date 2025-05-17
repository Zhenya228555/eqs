import pygame#-----пыдключеня модуля-------
pygame.init()

Class Player(GameSpirite):
    def __init__(self,player_image,player_x,playr_y,size_x,size_y,player_x_speed)
#------цвіта------
BLACK = (0, 0, 0)
window = pygame.display.set_mode((1500 , 900))
window.fill(BLACK)
hit = pygame.Rect(100, 100, 250, 250)
#--------картинки------
garga1 = pygame.image.load("asset_level/bush_1.png")
g= pygame.image.load("asset_level/full_g_block.png")
c= pygame.image.load("asset_level/big_prickly_bush.png")
v = pygame.image.load("asset_level/big_rock.png")
r = pygame.image.load("asset_level/big_rock.png")
f = pygame.image.load("asset_level/sprout_1.png")
e = pygame.image.load("asset_level/little_bush.png")
y = pygame.image.load("asset_level/little_bush.png")
u = pygame.image.load("asset_level/little_bush.png")
t = pygame.image.load("asset_level/little_bush.png")
b = pygame.image.load("asset_level/little_bush.png")
be = pygame.image.load("asset_level/little_bush.png")
g = pygame.image.load("asset_level/little_bush.png")
er= pygame.image.load("asset_level/little_bush.png")
eg= pygame.image.load("asset_level/stalker.png")
#--------розмир--------
garga1 = pygame.transform.scale(garga1, (50,50))
g = pygame.transform.scale(g, (50,110))
c = pygame.transform.scale(c, (50,50))
v = pygame.transform.scale(v, (50,50))
r = pygame.transform.scale(r, (50,50))
f = pygame.transform.scale(f, (50,50))
y = pygame.transform.scale(y, (50,50))
u = pygame.transform.scale(u, (50,50))
t = pygame.transform.scale(t, (50,50))
e = pygame.transform.scale(e, (50,50))
b = pygame.transform.scale(b, (50,50))
be = pygame.transform.scale(be, (50,50))
g= pygame.transform.scale(g, (50,50))
er = pygame.transform.scale(er, (50,50))
eg = pygame.transform.scale(eg, (100,100))
#------кардинати-------
while True :
    pygame.draw.rect(window, (255, 255, 255) ,hit)
    window.blit(garga1 , (400,800))
    window.blit(g , (100,800))
    window.blit(c , (300,800))
    window.blit(v , (200,800))
    window.blit(r , (350,800))
    window.blit(f , (250,800))
    window.blit(e,  (150,800))
    window.blit(t , (400,800))
    window.blit(u , (550,800))
    window.blit(y , (450,800))
    window.blit(b , (460,800))
    window.blit(be , (160,800))
    window.blit(g , (560,800))
    window.blit(er , (360,800))
    window.blit(eg , (150,750))
    
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == k_LEFT:
                stalker_x_seed = -8


    pygame.display.update()