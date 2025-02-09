import math
import random
import pygame

# constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_x = 370
PLAUER_START_Y  = 380
ENEMY_START_Y_MIN = 50
ENEMY_START_Y_MAX = 150
ENEMY_SPEED_X = 4
ENEMY_SPEED_Y = 40
BULLET_SPEED_ = 30
COLLISION_DISTANCE = 27

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

background = pygame.image.load('space background.avif')

pygame.display.set_caption("space Invader")
icon = pygame. image.load('space_rocket.png')
pygame.display.set_icon(icon)

playerImg = pygame. image. load('space_rocket.png')
playerx = PLAYER_START_x
playery = PLAYER_START_Y
playerx_change = 0

enemyImg = []
enemyx = []
enemyy = []
enemyX_change = []
enemyy_change = []
num_of_enemies = 6

for _i in range(num_of_enemies):
    enemyImg.append(pygame. image. load(''))
    enemyx.append(random.randint(0, SCREEN_WIDTH - 64)) 

    enemyy.append(random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX))
    enemyX_change.append(ENEMY_SPEED_X)
    enemyy_change.append(ENEMY_SPEED_Y)

    bulletingImg = pygame.image.load('')
    bulletx =0
    bullety = PLAYER_START_Y
    bulletx_ = 0
    bullety_change = BULLET_SPEED_Y
    bullet_stste = "ready" 
    # score
    score_value = 0
    font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):

    score = font.render("score :" + str(score_value), True,(255, 255,255))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))

def player(x, y):
    screen.blit(playerImg, (x,y))
def fire_bulet(x,y):
    # Fire a bulet from the player'position
    global bullet_state
    bullet_state = "fire"
    screen.bilt(bulletImg, (x + 16, y + 10))
def isCollision((enemyX, enemyY, bulletX, bulletY)**2)

distance = math.sqrt((enemyX- bulletX)**2 +(enemyY - bulletY)** 2) return distance < COLLISION_DISTANCE

running = True
while running:
    screen.fill((0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
        running = False
    if event.type == pygame.KEYDOWN:
     if event.key == pygame.K_LEFT:
         playerX_change = -5
     if event.key == pygame.K_RIGHT:
        playerX_change = 5
    if event.key == pygame.KEYUP and event.key in [pygame.K_LEFT, pygame.K_RIGHT]: 
       playerX_change = 0 

    playerX +=playerX_change
    playerX = max(0, min(playerX, SCREEN_WIDTH - 64)) # 64 is the size of the player

for i in range(num_of_enemies):
    if enemyY[i] > 340: #Game Over condition
        for j in range(num_of_enemies):
          enemyY[j] = 2000
        game_over_text()
        break
    enemyX[i] += enemyX_change[i]
    if enemyX[i] <= 0 or enemyX[i] >= SCREEN_WIDTH - 64:
        enemyX_change[i] *= -1
        enemyY[i] += enemyY_change[i]

    if iscollision(enemyX[i], enemyY[i], bulletX, bulletY):
      bulletY = PLAYER_START_Y
      bullet_start = "ready"
      score_value +=1
      enemyX[i] = random.randint(0, SCREEN_WIDTH - 64)
      enemyY[i] = random.randint(ENEMY_START_Y_MIN, ENEMY_START_Y_MAX)
    enemy(enemyX[i], enemyY[i],i) 

    if bulletY <= 0:
        bullet = PLAYER_START_Y
        bullet_start = "ready"
    elif bullet_start == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY = bulletY_change
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
