import pygame
import random
import math
pygame.init()

#create screen
screen=pygame.display.set_mode((800,600))

#background
background=pygame.image.load('back.jpg')

#title
pygame.display.set_caption("Gamiry")
icon=pygame.image.load('sci-fi.png')
pygame.display.set_icon(icon)
#player
playerimg=pygame.image.load('player.png')
playerx=370
playery=480
playerx_change=0

#enemy
enemy_img=pygame.image.load('summer.png')
en_x=random.randint(0,735)
en_y=random.randint(50,150)
en_xchange=1
en_ychange=40

#bullets
bullet_img=pygame.image.load('bullets.png')
bullet_x=0
bullet_y=480
bullet_xchange=0
bullet_ychange=4
#ready - can't see bullets
#fire - currently moving
bullet_state="ready"

score=0
def player(x,y):
    screen.blit(playerimg,(x,y))

def enemy(x,y):
    screen.blit(enemy_img,(en_x,en_y))

def bullet_fire(x,y):
    global bullet_state
    bullet_state="fire"
    screen.blit(bullet_img,(x + 16, y + 10))


def is_collision(en_x,en_y,bullet_x,bullet_y):
    distance=math.sqrt((math.pow(en_x-bullet_x,2))+(math.pow(en_y-bullet_y,2)))
    if distance<25:
        return True
    else:
        return False


#game loop
running=True
while running:
    screen.fill((0,0,0))
    #backgroundimage
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                playerx_change=-5
            if event.key==pygame.K_RIGHT:
                playerx_change=5
            if event.key==pygame.K_SPACE:
                if bullet_state is "ready":
                    blt=playerx
                    bullet_fire(playerx,bullet_y)
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerx_change=0
    playerx+=playerx_change
    #boundaries for player
    if playerx<=0:
        playerx=0
    elif playerx>=736:
        playerx=736


    #checking boundaries for enemy
    en_x+=en_xchange
    if en_x<=0:
       en_xchange=2
       en_y+=en_ychange
    elif en_x>=736:
        en_xchange=-2
        en_y+=en_ychange

    #bullet movement

    if bullet_y<=0:
        bullet_y=480
        bullet_state="ready"
    
    if bullet_state is "fire":
        bullet_fire(blt,bullet_y)
        bullet_y -=bullet_ychange
    

    #collision
    collision=is_collision(en_x,en_y,bullet_x,bullet_y)
    if collision:
        bullet_y=480
        bullet_state="ready"
        score+=1
        print(score)
        en_x=random.randint(0,800)
        en_y=random.randint(50,150)

    
    #function calling
    player(playerx,playery)
    enemy(en_x,en_y)

    
    #close
    pygame.display.update()
