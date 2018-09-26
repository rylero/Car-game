import pygame, sys, random, time
from pygame.locals import *


pygame.init()

display = pygame.display.set_mode((800, 800),HWSURFACE|DOUBLEBUF)
display.fill((0,0,0))

running = True

clock = pygame.time.Clock()

enemy = 1

player = 1


class Color:
    black = (0,0,0)
    white = (255,255,255)
    gray = (50,50,50)

    red = (255,0,0)
    blue = (0,0,255)
    green = (0,255,120)

class Player:
    x,y = 350, 550; width,height = 100,150; lives = 3

    rect = pygame.Rect(x,y,width,height)

    def move_player(d):
        if d == "left":
            d = -4
        elif d == "right":
            d = 4
        Player.x += d

    def d_l():
        lives-=1

def quitGame():
    pygame.quit()
    sys.exit()
    quit()



class Enemy:
    x,y = random.choice((Player.x,random.randint(10, 690))),10; width,height = 100,150

    rect = pygame.Rect(x,y,width,height)

    def move():
        Enemy.y+=random.randint(6,7)
        Enemy.x+=random.randint(int(-0.5),int(0.5))


lose = False

music = pygame.mixer.music.load('house_lo.mp3')
Car = pygame.image.load("Car.bmp").convert()
Enemy_pic = pygame.image.load("Enemy.bmp").convert()
pygame.key.set_repeat(1, 10)

display.fill(Color.black)
font = pygame.font.Font(None, 80)
text = 'Ready'
ren = font.render(text, 0, Color.white, Color.black)
display.blit(ren, (200, 400))
pygame.display.flip()
pygame.event.get()

time.sleep(1)
display.fill(Color.black)
text = '3'
ren = font.render(text, 0, Color.white, Color.black)
display.blit(ren, (200, 400))
pygame.display.flip()
pygame.event.get()


time.sleep(1)
display.fill(Color.black)
text = '2'
ren = font.render(text, 0, Color.white, Color.black)
display.blit(ren, (200, 400))
pygame.display.flip()
pygame.event.get()

time.sleep(1)
display.fill(Color.black)
text = '1'
ren = font.render(text, 0, Color.white, Color.black)
display.blit(ren, (200, 400))
pygame.display.flip()
pygame.event.get()
time.sleep(1)

pygame.mixer.music.play(-1)

score = 0

while running:

    display.fill(Color.black)
#    display.blit(Car, (200,200))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Player.move_player("left")
            if event.key == pygame.K_RIGHT:
                Player.move_player("right")

    if Player.rect.colliderect(Enemy.rect):
        if lose == False:
            print(score)
            display.fill((0,0,0))
        text = 'You lose'
        ren = font.render(text, 0, Color.white, Color.black)
        display.blit(ren, (200, 400))
        pygame.display.flip()
        pygame.mixer.music.stop()
        lose = True
        enemy = 0
        player = 0

    if Player.x >= 690:
        Player.x = 690
    if Player.x <= 10:
        Player.x = 10

    Player.rect = pygame.Rect(Player.x,Player.y,Player.width,Player.height)
    Enemy.rect = pygame.Rect(Enemy.x,Enemy.y,Enemy.width,Enemy.height)

    Enemy.move()
    if player == 1 and enemy == 1:
        display.blit(Car, Player.rect)
        display.blit(Enemy_pic, Enemy.rect)
        #pygame.draw.rect(display, Color.red, Player.rect, 1)
        #pygame.draw.rect(display, Color.red, Enemy.rect, 1)
    else:
        display.fill((0,0,0))

    if Enemy.y >= 801:
        Enemy.x,Enemy.y = random.randint(110, 690),10;
        score += 1

    pygame.display.update()

    clock.tick(100)


quitGame()