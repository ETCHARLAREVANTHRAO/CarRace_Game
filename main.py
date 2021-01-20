# required modules
import pygame
import sys
import random
import time as t
# Start game
pygame.init()
screen_width = 840
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Car game by Revanth')
time = pygame.time.Clock()

road = pygame.image.load('images/background.png')
roadx = 0
roady = 0
velocity_road= 4

car = pygame.image.load('images/car.png')
carx, cary = screen_width//2-30, screen_height-100
car_velx, car_vely = 0, 0
enemy1 = pygame.image.load('images/image1.png')
enemy2 = pygame.image.load('images/image2.jpg')
enemy3 = pygame.image.load('images/image3.png')
x_pos1 = random.randint(120, int(screen_width/3))
x_pos2 = random.randint(int(screen_width/3), int(2*screen_width/3))
x_pos3 = random.randint(int(2*screen_width/3), screen_width-100)
y_pos1, y_pos2, y_pos3 = 100, 100, 100
i = 0
score = 0
def crash():
    screen.fill((0, 255, 0))
    font = pygame.font.SysFont("comicsansms", 41)
    label = font.render("You hav Crased,Your Score is " + str(score), True, (255, 0, 0))
    screen.blit(label, (screen_width // 2- 300, screen_height // 2))
    t.sleep(0.1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                car_vely += 5
            if event.key == pygame.K_UP:
                car_vely -=5
            if event.key == pygame.K_LEFT:
                car_velx -= 5
            if event.key ==pygame.K_RIGHT:
                car_velx += 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                car_vely -= 5
            if event.key == pygame.K_UP:
                car_vely +=5
            if event.key == pygame.K_LEFT:
                car_velx += 5
            if event.key ==pygame.K_RIGHT:
                car_velx -= 5
    cary += car_vely
    carx += car_velx
    roady = roady +velocity_road
    if roady ==600:
        roady =0
    if cary <= 0:
        cary =0
    if cary >= screen_height -100:
        cary = screen_height -100
    if carx <= 0:
        carx =0
    if carx >= screen_width-50:
        carx = screen_width-50
    i += 0.01
    y_pos1 += 6+i
    y_pos2 += 8+i
    y_pos3 += 10+i
    screen.fill(pygame.Color('white'))
    screen.blit(road, [roadx, roady-600])
    screen.blit(road, [roadx, roady])
    screen.blit(car, (carx, cary))
    screen.blit(enemy1, (x_pos1, y_pos1))
    if y_pos1 >= screen_height:
        y_pos1 = 0 - y_pos1
        x_pos1 = random.randint(120, int(screen_width/3))
        score += 1
    screen.blit(enemy2, (x_pos2, y_pos2))
    if y_pos2 >= screen_height :
        y_pos2 = 0- y_pos2
        x_pos2 = random.randint(int(screen_width / 3), int(2 * screen_width / 3))
        score += 1
    screen.blit(enemy3, (x_pos3, y_pos3))
    if y_pos3 >= screen_height:
        y_pos3 = 0- y_pos3
        x_pos3 = random.randint(int(2 * screen_width / 3), screen_width - 100)
        score += 1
    if cary < y_pos1+ 100 :
        if (carx > x_pos1 and carx < x_pos1+ 50) or (carx + 50 > x_pos1 and carx+ 50 < x_pos1+ 50):
            crash()
    if cary < y_pos2+ 100 :
        if (carx > x_pos2 and carx < x_pos2+ 50) or (carx + 50 > x_pos2 and carx+ 50 < x_pos2+ 50):
            crash()
    if cary < y_pos3+ 100 :
        if (carx > x_pos3 and carx < x_pos3+ 50) or (carx + 50 > x_pos3 and carx+ 50 < x_pos3+ 50):
            crash()
    font1 = pygame.font.SysFont("comicsansms", 41)
    label1 = font1.render("Score " + str(score), True, (255, 0, 0))
    screen.blit(label1, (50, 20))
    pygame.display.flip()
    time.tick(60)