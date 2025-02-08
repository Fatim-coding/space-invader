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

background = pygame.image.load('background.png')

pygame.display.set_caption("space Invader")
icon = pygame. image.load('')
pygame.display.set_icon(icon)

playerImg = pygame. image. load('player.png')
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
    bullety = PLAYER_START_y
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

